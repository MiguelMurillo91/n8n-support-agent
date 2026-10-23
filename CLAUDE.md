# n8n-support-agent

## What this is
A support agent for N8N

## Tools
- Python 3.14, managed with uv. Never use pip.

## Checks (the "done" check for every task)
- uv run ruff check .
- uv run ruff format --check .
- uv run pyright
- uv run pytest

## Loop rules
- After each change, run all checks. If one fails, read the error, fix, run again.
- Stop when all checks pass.
- If the same check fails 5 times in a row, STOP and tell me what's failing. Don't keep trying.
- Never change, delete, or skip a test to make it pass. If a test looks wrong, stop and ask me.

## Rules
- Tests never call the real API. Use FakeLLM.
- Never commit .env or secrets.
- Never edit evals/tickets.jsonl. Those labels are written by hand.

## Layout
- src/n8n_support_agent/  code
- tests/                  tests
- specs/                  one file per task, written by me
- docs/                   taxonomy and failure log
- evals/                  eval tickets