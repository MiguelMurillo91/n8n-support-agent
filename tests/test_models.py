import pytest
from pydantic import ValidationError

from n8n_support_agent.models import Category, Priority, Ticket, Triage


def valid_triage_data() -> dict[str, object]:
    return {
        "category": "nodes",
        "priority": "high",
        "escalate": False,
        "confidence": 0.8,
        "reason": "HTTP Request node returns 401",
    }


def test_ticket_keeps_values():
    ticket = Ticket(subject="Webhook not firing", body="My webhook stopped working.")

    assert ticket.subject == "Webhook not firing"
    assert ticket.body == "My webhook stopped working."


def test_ticket_strips_whitespace_from_subject():
    ticket = Ticket(
        subject="  Webhook not working     ", body="My webhook stopped working"
    )
    assert ticket.subject == "Webhook not working"


def test_triage_keeps_values():
    triage = Triage(
        category=Category.NODES,
        priority=Priority.HIGH,
        escalate=True,
        confidence=0.8,
        reason="HTTP Request node returns 401",
    )

    assert triage.category == Category.NODES
    assert triage.priority == Priority.HIGH
    assert triage.escalate is True
    assert triage.confidence == 0.8
    assert triage.reason == "HTTP Request node returns 401"


def test_category_values_match_taxonomy():
    assert {c.value for c in Category} == {
        "triggers",
        "credentials",
        "data",
        "nodes",
        "hosting",
        "account",
        "other",
    }


def test_priority_values_match_taxonomy():
    assert {p.value for p in Priority} == {"urgent", "high", "normal", "low"}


@pytest.mark.parametrize("subject", ["", "   "])
def test_rejects_empty_subject(subject: str):
    with pytest.raises(ValidationError):
        Ticket(subject=subject, body="My webhook stopped working.")


@pytest.mark.parametrize("body", ["", "   "])
def test_rejects_empty_body(body: str):
    with pytest.raises(ValidationError):
        Ticket(subject="Webhook not firing", body=body)


def test_rejects_unknown_category():
    data = valid_triage_data() | {"category": "billing"}
    with pytest.raises(ValidationError):
        Triage.model_validate(data)


def test_rejects_unknown_priority():
    data = valid_triage_data() | {"priority": "critical"}
    with pytest.raises(ValidationError):
        Triage.model_validate(data)


def test_rejects_confidence_less_zero():
    data = valid_triage_data() | {"confidence": -0.1}
    with pytest.raises(ValidationError, match="greater_than_equal"):
        Triage.model_validate(data)


def test_rejects_confidence_greater_one():
    data = valid_triage_data() | {"confidence": 1.1}
    with pytest.raises(ValidationError, match="less_than_equal"):
        Triage.model_validate(data)


@pytest.mark.parametrize("confidence", [0.0, 1.0])
def test_accepts_confidence_bounds(confidence: float):
    data = valid_triage_data() | {"confidence": confidence}
    assert Triage.model_validate(data).confidence == confidence


@pytest.mark.parametrize("reason", ["", "   "])
def test_rejects_empty_reason(reason: str):
    data = valid_triage_data() | {"reason": reason}
    with pytest.raises(ValidationError, match="string_too_short"):
        Triage.model_validate(data)


def test_rejects_reason_over_300_chars():
    data = valid_triage_data() | {"reason": "x" * 301}
    with pytest.raises(ValidationError, match="string_too_long"):
        Triage.model_validate(data)


def test_accepts_reason_of_300_chars():
    data = valid_triage_data() | {"reason": "x" * 300}
    assert Triage.model_validate(data).reason == "x" * 300
