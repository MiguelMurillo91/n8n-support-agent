from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints

NonEmptyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class Category(StrEnum):
    TRIGGERS = "triggers"
    CREDENTIALS = "credentials"
    DATA = "data"
    NODES = "nodes"
    HOSTING = "hosting"
    ACCOUNT = "account"
    OTHER = "other"


class Priority(StrEnum):
    URGENT = "urgent"
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"


class Ticket(BaseModel):
    subject: NonEmptyStr
    body: NonEmptyStr


class Triage(BaseModel):
    category: Category
    priority: Priority
    escalate: bool
    confidence: float = Field(ge=0.0, le=1.0)
    reason: str = Field(min_length=1, max_length=300)
