# Month 9 Capstone — System Design Whiteboard Marathon

> **Phase 9** | Complete after weeks in this month.

## Brief

5 designs: URL shortener, chat, payments, feed, notifications — 45 min each.

## Scenario

You have completed eight months of architecture study and are entering **loop-interview season** at tier-1 tech companies. Recruiters schedule back-to-back **45-minute system design** rounds covering diverse domains. You must prove you can clarify requirements, estimate scale, draw architecture, and discuss trade-offs under time pressure — without referencing slides. Constraints: each session is timed (45 min design + 15 min self-review), designs must use the **RESHADED** framework, and you record or write up each session for retrospective. Stakeholders are imaginary interviewers probing depth on consistency, caching, sharding, and failure modes.

## Architecture Expectations

A passing solution must show repeatable interview performance across five domains:

- **RESHADED framework** applied every session — Requirements, Estimation, Storage, High-level design, APIs, Deep dives, Evaluation, Distinctive insight
- **Five complete designs** — URL shortener, real-time chat, payment system, news feed, notification system
- **Scale estimates** — users, QPS, storage growth with back-of-envelope math shown
- **Diagrams per design** — high-level boxes + one deep-dive (e.g., sharding, fan-out, idempotency)
- **Consistency model** — stated per design (strong, eventual, causal)
- **Bottleneck analysis** — single biggest risk and mitigation per design
- **Self-score ≥75/100** on at least 3 of 5 designs using the rubric below
- **Retrospective doc** — patterns that repeated, weak areas, improvement plan

## Deliverables

- [ ] **5 design write-ups** — one per system (45-min session notes + final diagram)
- [ ] **RESHADED checklist** — completed template for each session
- [ ] **Scale estimation worksheet** — shared template with all five workloads
- [ ] **Mermaid architecture diagram** per design (high-level + one deep-dive each)
- [ ] **API sketch** per design — 5–10 key endpoints or events
- [ ] **Self-assessment scores** — rubric applied; 3+ designs ≥75/100
- [ ] **Marathon retrospective** — strengths, gaps, next 10 practice topics
- [ ] **Peer review** — swap one design with study partner for feedback

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Functional and non-functional requirements stated upfront
- Scope explicitly bounded (MVP vs future)
- Clarifying questions documented as if to interviewer

**Architecture quality (30 pts)**

- High-level design matches scale estimates
- Deep dive shows real expertise (not generic boxes)
- Data model and API design are coherent

**Trade-off documentation (20 pts)**

- At least two alternatives considered per major decision
- Consistency vs availability trade-off explicit
- Bottleneck and mitigation identified

**Production realism (15 pts)**

- Failure modes addressed (single points of failure, retries)
- Monitoring and alerting mentioned
- Cost or operational burden acknowledged

**Presentation / ADRs (15 pts)**

- Diagram readable in 30 seconds
- Narrative fits 45-minute interview pacing
- Retrospective shows measurable improvement across 5 sessions

**Pass:** ≥ 70 points (average across five designs; at least three individual designs ≥75)

## Timeline

Suggested **2-week sprint** at end of Month 9:

| Day | Focus |
|-----|-------|
| **Mon W1** | Design 1 — URL shortener (45 min timed + 15 min review) |
| **Tue W1** | Design 2 — Real-time chat |
| **Wed W1** | Design 3 — Payment system |
| **Thu W1** | Design 4 — News feed |
| **Fri W1** | Design 5 — Notification system |
| **Mon W2** | Compile scale estimation worksheet across all five |
| **Tue W2** | Self-score each design; identify weakest two |
| **Wed W2** | Redo weakest design under timed conditions |
| **Thu W2** | Peer review swap + retrospective doc |
| **Fri W2** | Submit marathon package; confirm 3+ designs ≥75 |

## References

- [Week 33 — High-Level System Design Methodology](../../weeks/week-33/README.md)
- [Week 34 — Scalability, Caching & CDN](../../weeks/week-34/README.md)
- [Week 35 — Messaging & Event-Driven Architecture](../../weeks/week-35/README.md)
- [Week 36 — System Design Capstone](../../weeks/week-36/README.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
