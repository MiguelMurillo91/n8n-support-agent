# Tickets taxonomy

the following 2 tables show the Categories and priorities the ticketing system is going to use.

| Category    | Covers                                                        |
|-------------|---------------------------------------------------------------|
| triggers    | webhooks, schedules, workflows that don't start               |
| credentials | logins to other apps, OAuth, API keys                         |
| data        | expressions, mapping items, the Code node                     |
| nodes       | a specific node misbehaving (HTTP Request, Gmail, Airtable…)  |
| hosting     | self-hosting, Docker, env variables, proxies, upgrades        |
| account     | n8n Cloud plan, billing, workspace access                     |
| other       | feature requests, general questions                           |

| Priority | Rule                                                             |
|----------|------------------------------------------------------------------|
| urgent   | production is down, data is being lost, or n8n won't start       |
| high     | a workflow is blocked with no workaround                         |
| normal   | a real problem, but there's a workaround or it's only in testing |
| low      | how-to questions, feature requests                               |

## Tie-break rules
- “HTTP Request returns 401”:  nodes
- “Webhook stopped working after I moved n8n behind Nginx”: hosting
- “Gmail node fails since my Google token expired”: credentials

## Escalation rules
A ticket must be escalated to a human when:
- The ticket is related to the account, billing, cancelations and related topics
- The certanty in the answer is below 90%

## Eval set rules
A ticket goes in the eval set only if its answer is confirmed by a docs page or a solved forum thread, or I reproduced it myself. Escalation tickets are the exception: their correct answer is “a human handles this.”


## Ideas for the agent (to test later)
- The certainty in the answer is above 90%

## Open questions
No questions yet