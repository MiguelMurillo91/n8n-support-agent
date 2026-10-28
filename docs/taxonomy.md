# Ticket taxonomy

Labels for routing n8n support tickets. Every ticket gets one category,
one priority, and an escalate flag (true/false).

Agreement v1: (fill in after the agreement check)

## Categories

| Category    | Covers                                                       |
|-------------|--------------------------------------------------------------|
| triggers    | webhooks, schedules, workflows that don't start              |
| credentials | logins to other apps, OAuth, API keys                        |
| data        | expressions, mapping items, the Code node                    |
| nodes       | a specific node misbehaving (HTTP Request, Gmail, Airtable…) |
| hosting     | self-hosting, Docker, env variables, proxies, upgrades       |
| account     | n8n Cloud plan, billing, workspace access                    |
| other       | feature requests, general questions                          |

## Tie-break rules

1. **Root cause wins.** If the problem is the login to another service
   (expired token, wrong API key, 401/403 errors), it's `credentials`,
   even when the error shows up inside a node.
   Why: the fix is in the credential, not the node.
   - "HTTP Request returns 401" → credentials
   - "Gmail node fails since my Google token expired" → credentials

2. **Server setup beats the feature.** If a trigger or node only fails
   because of how n8n is installed (proxy, domain, env variables,
   Docker), it's `hosting`.
   Why: the fix is in the server config, not the workflow.
   - "Webhook stopped working after I moved n8n behind Nginx" → hosting

3. **Wrong output, node ran fine → data.** If the node runs without an
   error but the result is wrong or empty because of an expression or
   mapping, it's `data`, not `nodes`.
   Why: the fix is in the expression, not the node's settings.

## Priorities

| Priority | Rule                                                             |
|----------|------------------------------------------------------------------|
| urgent   | production is down, data is being lost, or n8n won't start       |
| high     | a workflow is blocked with no workaround                         |
| normal   | a real problem, but there's a workaround or it's only in testing |
| low      | how-to questions, feature requests                               |

## Escalation rules

Decide from the ticket text alone. A ticket is `escalate: true` when:

- It's about the account: billing, refunds, cancellations, plan changes,
  workspace access.
- It looks like a bug in n8n itself: it worked before an upgrade, and the
  docs say it should still work.
- Data was lost, or there's a security issue (leaked credentials,
  someone else's data visible).
- The user explicitly asks for a human.

Everything else is `escalate: false`.

## Eval set rules

A ticket goes in the eval set only if its answer is confirmed by a docs
page or a solved forum thread, or I reproduced it myself. Escalation
tickets are the exception: their correct answer is "a human handles this."

## Open questions

- A Cloud user's webhook times out after 100 seconds. Is it `triggers`
  (how webhooks work) or `account` (a limit of their plan)?
  Answer: `triggers`

- The user says "production is down" but describes a workflow that's
  still in testing. Do we trust what they say or what they describe?
  Answer: Trust the description

## Ideas for the agent (to test later)

- Escalate when the agent's confidence is below 90%. Test in Phase 6:
  is the model's confidence actually reliable?
