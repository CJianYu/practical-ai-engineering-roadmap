from enum import Enum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class SupportTicket(BaseModel):
    """A validated boundary object for a model-produced support classification."""

    model_config = ConfigDict(extra="forbid")

    category: Literal["billing", "bug", "feature_request", "account", "other"]
    priority: Priority
    summary: str = Field(min_length=5, max_length=160)
    requires_human: bool
    confidence: float = Field(ge=0.0, le=1.0)
