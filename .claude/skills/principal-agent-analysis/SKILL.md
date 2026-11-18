---
name: principal-agent-analysis
description: Map and interpret principal-agent relations between governments, public organizations, citizens, communities, and other actors in social media data. Use when analyzing accountability, responsiveness, representation, public service communication, citizen mentions, institutional replies, or online government-society engagement.
---

# Principal-Agent Analysis in Social Media

## Conceptual model
Specify who is the principal and who is the agent for the particular institutional relationship. Do not assume citizens are always principals or government always agent; describe delegation, mandate, information asymmetry, monitoring, discretion, and accountability in the case at hand.

Potential dimensions:
- Principal: constituency, citizen group, legislature, funder, regulator, or authorizing body.
- Agent: public agency, elected official, contractor, service provider, or delegated implementer.
- Delegation: formal mandate, policy, service obligation, or public expectation.
- Information asymmetry: unequal access to information, expertise, or implementation data.
- Monitoring: questions, complaints, mentions, public records, oversight, and performance indicators.
- Responsiveness: acknowledgement, substantive answer, resolution, explanation, or non-response.
- Accountability: answerability, justification, correction, remedy, and sanction mechanisms.

## Workflow
1. Draw the institutional relationship before analyzing posts. Record legal/formal mandates and informal expectations separately.
2. Identify actors and accounts using transparent rules; distinguish official institutional accounts from personal accounts, fan accounts, media, and unaffiliated users.
3. Define interaction events: post, mention, reply, quote, repost, complaint, question, answer, commitment, referral, and resolution.
4. Build a directed interaction table with source actor, target actor, timestamp, interaction type, issue, and evidence link/ID.
5. Create descriptive metrics: inbound mentions, outbound replies, reply rate, median response time, issue-level response rate, unresolved questions, and interaction concentration. State denominators and missing-data rules.
6. Code substantive responsiveness. A reply is not necessarily an answer; separate acknowledgement, generic response, relevant information, action/commitment, and verified resolution.
7. Map networks and identify brokers or highly central accounts cautiously. Centrality measures describe graph structure, not influence or legitimacy by themselves.
8. Compare communication with institutional documents, service standards, and follow-up evidence. Verify any claim that a case was resolved.
9. Interpret principal-agent implications: monitoring capacity, agency discretion, incentive alignment, information gaps, accountability channels, and risks of symbolic responsiveness.

## Metrics definitions
- Reply rate = eligible inbound interactions receiving an attributable institutional reply / all eligible inbound interactions. Define eligibility and time-to-reply cutoff.
- Median response time = median elapsed time between eligible inbound post and first attributable institutional reply, excluding or separately reporting right-censored cases.
- Resolution rate = cases with independently verifiable resolution / cases with a trackable issue outcome. Do not equate a response with resolution.
- Interaction concentration = share of eligible interactions accounted for by top actors, with the chosen concentration measure stated.

## Safeguards
- Never infer an official mandate from a verified badge alone; corroborate with official sources.
- Do not classify criticism as misinformation without checking factual claims.
- Avoid exposing citizen handles or sensitive case details in published outputs.
- Do not infer personal identities, political affiliation, or other sensitive attributes.
- State that social media users are a self-selected subset of affected people.

## Output
Provide: relationship map; actor/role definitions; interaction taxonomy; metric table with denominators; selected anonymized case traces; findings on responsiveness and accountability; corroboration; limitations; recommendations.
