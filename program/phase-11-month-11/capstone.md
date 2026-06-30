# Month 11 Capstone — Enterprise Case Study Marathon

> **Phase 11** | Complete after weeks in this month.

## Brief

4 case studies with full architecture reviews.

## Scenario

You are interviewing for **principal architect** roles where loops include **90-minute architecture reviews** of messy real-world scenarios. Over two weeks you will complete **four enterprise case studies** (CS44-A through CS44-D from Week 44), each simulating a different industry and constraint set — legacy modernization, merger integration, regulatory deadline, and cost-out mandate. Constraints: each review must produce ADRs, risk register, and phased roadmap; you cannot propose "big bang" rewrites. Stakeholders vary per case (CIO, regulator, acquired company's CTO, CFO). This marathon proves you can lead reviews, not just draw greenfield diagrams.

## Architecture Expectations

A passing solution must demonstrate architecture review board readiness:

- **Four completed case studies** — CS44-A, B, C, D from [Week 44](../../weeks/week-44/README.md)
- **Architecture review template** — current state, target state, gap analysis, risks, roadmap per case
- **2 ADRs minimum per case** — documenting the highest-stakes decisions
- **C4 or equivalent diagrams** — current vs target for each case
- **Risk register** — likelihood, impact, mitigation, owner per case
- **Phased roadmap** — 90-day, 6-month, 12-month horizons with dependencies
- **Stakeholder communication** — executive summary (1 page) per case for non-technical audience
- **Cross-case retrospective** — recurring patterns, anti-patterns you caught, personal checklist

## Deliverables

- [ ] **CS44-A architecture review** — full template + 2 ADRs + diagrams
- [ ] **CS44-B architecture review** — full template + 2 ADRs + diagrams
- [ ] **CS44-C architecture review** — full template + 2 ADRs + diagrams
- [ ] **CS44-D architecture review** — full template + 2 ADRs + diagrams
- [ ] **Risk register** (consolidated) — top 10 risks across all four cases
- [ ] **ADR index** — 8+ ADRs with status and cross-links
- [ ] **Executive summaries** — 1 page each, four cases
- [ ] **Marathon retrospective** — patterns, anti-patterns, personal review checklist
- [ ] **Peer review** — one case reviewed by study partner with written feedback

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Each case's business drivers and constraints restated accurately
- Scope of review bounded (in/out of architecture remit)
- Success criteria defined per case

**Architecture quality (30 pts)**

- Current and target states are internally consistent
- Roadmaps are phased with realistic dependencies
- Integration and data concerns addressed where relevant

**Trade-off documentation (20 pts)**

- 2+ ADRs per case follow Nygard format
- Alternatives and rejected options documented
- Technical debt explicitly called out with paydown plan

**Production realism (15 pts)**

- Risk registers are actionable (not generic)
- Cost, timeline, and organizational change considered
- No unrealistic big-bang proposals

**Presentation / ADRs (15 pts)**

- Executive summaries understandable by CIO/CFO
- Diagrams support 90-minute review format
- Retrospective shows growth across four cases

**Pass:** ≥ 70 points (average across four case studies)

## Timeline

Suggested **2-week sprint** at end of Month 11:

| Day | Focus |
|-----|-------|
| **Mon W1** | CS44-A — read case, current state diagram, gap analysis |
| **Tue W1** | CS44-A — target state, 2 ADRs, roadmap, executive summary |
| **Wed W1** | CS44-B — full architecture review |
| **Thu W1** | CS44-C — full architecture review |
| **Fri W1** | CS44-D — full architecture review |
| **Mon W2** | Consolidated risk register + ADR index |
| **Tue W2** | Peer review — swap CS44-B or C |
| **Wed W2** | Revise weakest case from feedback |
| **Thu W2** | Marathon retrospective + personal checklist |
| **Fri W2** | Submit package; self-score all four cases |

## References

- [Week 41 — Architecture Reviews & ADRs](../../weeks/week-41/README.md)
- [Week 42 — FinOps, DR & Performance Engineering](../../weeks/week-42/README.md)
- [Week 43 — Frontend Architecture (React & Angular)](../../weeks/week-43/README.md)
- [Week 44 — Enterprise Case Study Marathon](../../weeks/week-44/README.md)
- [Case study template](../../templates/case-study-template.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
