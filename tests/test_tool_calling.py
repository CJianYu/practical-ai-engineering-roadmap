from copy import deepcopy

import pytest
from pydantic import ValidationError

from labs.lab03_tool_calling.tools import ApprovalRequired, BoundaryError, ToolRegistry


def issue_call():
    return {
        "tool": "create_issue",
        "arguments": {"title": "Billing", "body": "Review"},
        "operation_id": "issue-1",
    }


def test_unapproved_write_is_blocked(tmp_path):
    tools = ToolRegistry(tmp_path / "tools.sqlite")
    with pytest.raises(ApprovalRequired):
        tools.execute(issue_call())
    assert tools.issue_count() == 0


@pytest.mark.parametrize("change", ["body", "operation_id"])
def test_approval_does_not_cover_changed_payload(tmp_path, change):
    tools = ToolRegistry(tmp_path / "tools.sqlite")
    call = issue_call()
    tools.approve(call)
    altered = deepcopy(call)
    if change == "body":
        altered["arguments"]["body"] = "Different operation"
    else:
        altered["operation_id"] = "other-operation"
    with pytest.raises(ApprovalRequired):
        tools.execute(altered)
    assert tools.issue_count() == 0


def test_retry_after_restart_reuses_committed_receipt(tmp_path):
    path = tmp_path / "tools.sqlite"
    tools = ToolRegistry(path)
    tools.approve(issue_call())
    first = tools.execute(issue_call())
    restarted = ToolRegistry(path)
    assert restarted.execute(issue_call()) == first
    assert restarted.issue_count() == 1


def test_reused_operation_id_with_new_arguments_is_rejected(tmp_path):
    tools = ToolRegistry(tmp_path / "tools.sqlite")
    call = issue_call()
    tools.approve(call)
    tools.execute(call)
    call["arguments"]["body"] = "Changed body"
    tools.approve(call)
    with pytest.raises(BoundaryError, match="reused"):
        tools.execute(call)
    assert tools.issue_count() == 1


@pytest.mark.parametrize(
    "payload",
    [
        {**issue_call(), "approved": True},
        {**issue_call(), "tool": "approve"},
        {**issue_call(), "arguments": {"title": 123, "body": "test"}},
        {**issue_call(), "arguments": {"title": "test", "body": "test", "admin": True}},
    ],
)
def test_untrusted_payload_cannot_expand_schema(tmp_path, payload):
    tools = ToolRegistry(tmp_path / "tools.sqlite")
    with pytest.raises(ValidationError):
        tools.execute(payload)
    assert tools.issue_count() == 0


def test_approval_is_not_persisted_as_model_state(tmp_path):
    path = tmp_path / "tools.sqlite"
    tools = ToolRegistry(path)
    tools.approve(issue_call())
    with pytest.raises(ApprovalRequired):
        ToolRegistry(path).execute(issue_call())


def test_read_requires_no_approval(tmp_path):
    tools = ToolRegistry(tmp_path / "tools.sqlite")
    result = tools.execute(
        {"tool": "search_docs", "arguments": {"query": "refund"}, "operation_id": "read"}
    )
    assert result["documents"][0]["id"] == "support-policy"
    assert tools.issue_count() == 0


def test_receipt_failure_rolls_back_issue_creation(tmp_path):
    import sqlite3

    tools = ToolRegistry(tmp_path / "tools.sqlite")
    tools.approve(issue_call())
    with tools.connect() as db:
        db.execute(
            "CREATE TRIGGER fail_receipt BEFORE INSERT ON operations "
            "BEGIN SELECT RAISE(ABORT, 'receipt unavailable'); END"
        )
    with pytest.raises(sqlite3.IntegrityError):
        tools.execute(issue_call())
    assert tools.issue_count() == 0
    with tools.connect() as db:
        db.execute("DROP TRIGGER fail_receipt")
    tools.execute(issue_call())
    assert tools.issue_count() == 1
