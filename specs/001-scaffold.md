# 001 — Project scaffold

## Goal
Set up the n8n-support-agent project with the same foundations as
intent-parser, plus the data models that every later step depends on.

## What to build
- Copy from ../intent-parser, unchanged (check first if the file already exist):
  - .gitignore rules (.DS_Store, .env)
  - .dockerignore
  - .env.example
  - .github/workflows/ci.yml
  - tests/conftest.py
  - llm.py and anthropic_client.py, into src/n8n_support_agent/
  - the [tool.*] sections of pyproject.toml
- src/n8n_support_agent/models.py with:
  - Category and Priority as StrEnums, values exactly as in docs/taxonomy.md
  - Ticket: subject and body, both required, neither can be empty
  - Triage: category, priority, escalate (true/false),
    confidence (0 to 1), reason (1 to 300 characters)
- tests/test_models.py
- docs/failure-log.md: an empty table with columns
  date | ticket id | what went wrong | type | fixed?

## Done when
- [ ] A valid Ticket and a valid Triage build and keep their values
- [ ] Tests show each invalid case is rejected:
      empty subject, empty body, unknown category, unknown priority,
      confidence below 0 or above 1, empty reason, reason over 300 characters
- [ ] uv run pytest passes
- [ ] uv run pyright is clean
- [ ] uv run ruff check and ruff format --check pass
- [ ] CI is green on GitHub

## Not in scope
- No calls to the Anthropic API, and no prompts.
- No FastAPI app or any HTTP endpoint.
- No eval runner or scoring code.
- Do not create or edit evals/tickets.jsonl.
- No new dependencies beyond pydantic, anthropic, python-dotenv,
  and the dev tools (pytest, pyright, ruff).

## Loop
- Done check: everything in "Done when" passes.
- Order: write tests/test_models.py first and stop, so I can approve the tests.
  Only after my approval, build the code in a loop until all checks pass.
- Limit: stop after 5 failed attempts on the same check, and report.
- Tests are locked after my approval. Ask before changing any test.