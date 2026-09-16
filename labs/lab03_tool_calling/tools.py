"""Local tool boundary: validated calls, scoped approval and durable deduplication."""

from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class BoundaryError(ValueError):
    pass


class ApprovalRequired(BoundaryError):
    pass


class Call(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    tool: Literal["search_docs", "create_issue"]
    arguments: dict
    operation_id: str = Field(min_length=1)


class SearchArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    query: str = Field(min_length=1, max_length=500)


class IssueArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    title: str = Field(min_length=1, max_length=120)
    body: str = Field(min_length=1, max_length=2000)


def fingerprint(call: Call) -> str:
    payload = json.dumps(call.model_dump(), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


class ToolRegistry:
    """Single-user local simulator; database and trusted caller are the trust boundary.

    Approval is never a field in a model-produced call. A trusted UI/CLI calls
    approve() separately. Approvals are process-local and expire on restart.
    """

    def __init__(self, database: Path):
        self.database = database
        self._approvals: set[str] = set()
        with self.connect() as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS issues (id INTEGER PRIMARY KEY, "
                "title TEXT NOT NULL, body TEXT NOT NULL)"
            )
            db.execute(
                "CREATE TABLE IF NOT EXISTS operations (operation_id TEXT PRIMARY KEY, "
                "fingerprint TEXT NOT NULL, result TEXT NOT NULL)"
            )

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.database)

    def validate(self, payload: dict) -> Call:
        call = Call.model_validate(payload)
        schema = SearchArgs if call.tool == "search_docs" else IssueArgs
        schema.model_validate(call.arguments)
        return call

    def approve(self, payload: dict) -> None:
        """Trusted human-controller entrypoint, deliberately absent from the tool registry."""
        self._approvals.add(fingerprint(self.validate(payload)))

    def execute(self, payload: dict) -> dict:
        call = self.validate(payload)
        if call.tool == "search_docs":
            return {
                "documents": [
                    {
                        "id": "support-policy",
                        "text": (
                            "Billing disputes need human review. "
                            "This demo cannot issue refunds."
                        ),
                    }
                ]
            }
        signature = fingerprint(call)
        with self.connect() as db:
            # Serializes local writers. The side effect and receipt commit together.
            db.execute("BEGIN IMMEDIATE")
            receipt = db.execute(
                "SELECT fingerprint, result FROM operations WHERE operation_id = ?",
                (call.operation_id,),
            ).fetchone()
            if receipt:
                if receipt[0] != signature:
                    raise BoundaryError("Operation ID reused with a different payload")
                return json.loads(receipt[1])
            if signature not in self._approvals:
                raise ApprovalRequired("Approve the exact tool, arguments and operation ID")
            issue = db.execute(
                "INSERT INTO issues(title, body) VALUES (?, ?)",
                (call.arguments["title"], call.arguments["body"]),
            )
            result = {"issue_id": issue.lastrowid, "status": "created_locally"}
            db.execute(
                "INSERT INTO operations VALUES (?, ?, ?)",
                (call.operation_id, signature, json.dumps(result)),
            )
        self._approvals.discard(signature)
        return result

    def issue_count(self) -> int:
        with self.connect() as db:
            return db.execute("SELECT COUNT(*) FROM issues").fetchone()[0]
