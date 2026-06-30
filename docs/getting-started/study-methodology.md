# Study Methodology — Learning Architecture, Not Just Topics

## The Feynman Technique for Architects

After each theory section:

1. **Explain it** as if teaching a junior developer
2. **Identify gaps** where your explanation breaks down
3. **Go back** to the source material
4. **Simplify** using analogies and diagrams

If you can't explain the trade-off between two approaches in 2 minutes, you haven't learned it yet.

---

## The ADR Habit

Starting Week 3, write one **Architecture Decision Record** per week for a decision you made (even in labs).

Template: [templates/adr-template.md](../../templates/adr-template.md)

By Week 52, you'll have 50 ADRs — a portfolio that demonstrates architect thinking.

---

## Spaced Repetition Schedule

| Review | When | What |
|--------|------|------|
| Daily | 15 min | Previous day's interview Q&A (5 questions) |
| Weekly | Sunday | Full week review + assessment |
| Monthly | End of month | Month assessment + previous month Q&A drill |
| Quarterly | Weeks 13, 26, 39 | Cross-module mock interview |

Use flashcards (Anki or physical) for:
- Acronyms (CAP, PACELC, WAF pillars, OWASP)
- Service comparisons (App Service vs AKS vs Functions)
- Complexity classes (O(n log n) for common operations)

---

## Active vs Passive Learning

| Passive (insufficient alone) | Active (required) |
|------------------------------|-------------------|
| Reading theory | Drawing diagrams from memory |
| Watching architecture videos | Timed whiteboard designs |
| Reading interview answers | Speaking answers aloud |
| Copying lab steps | Breaking lab intentionally, then fixing |
| Reading case studies | Writing your own solution first |

**Target ratio:** 30% passive / 70% active

---

## The Trade-off Journal

Keep a running journal (personal, not in repo):

```markdown
## Week 03 — Trade-off: Repository vs Direct DbContext

**Context:** Order service data access
**Option A:** Generic Repository + UoW
**Option B:** DbContext directly in handlers
**Chose:** B for this bounded context
**Because:** EF Core already implements repository; extra layer adds complexity
**Risk:** Harder to swap persistence later
**Mitigation:** Interface on DbContext for testability
```

This journal becomes interview gold — real decisions with reasoning.

---

## Mock Interview Cadence

| Phase | Mock Frequency | Format |
|-------|----------------|--------|
| Months 1–6 | 1 per month | 30-min technical Q&A |
| Months 7–9 | 2 per month | 45-min system design |
| Months 10–11 | 2 per month | Full 60-min architect interview |
| Month 12 | 2 per week | Panel mock (3 rounds) |

Record yourself. Architects are judged on **clarity**, not just correctness.

---

## Study Groups (Optional)

If learning with peers:

- **Weekend design sessions:** One person presents a system design, others challenge
- **ADR review:** Peer-review each other's ADRs
- **Case study debates:** Defend different architecture choices

---

## When You're Stuck

1. Re-read the **Trade-offs** section of the current week
2. Check [decision-frameworks.md](../reference/decision-frameworks.md)
3. Draw the system — if you can't draw it, you don't understand it
4. Write down the specific question you're stuck on
5. Move to the lab — hands-on often clarifies theory

---

## Measuring Readiness

You're ready to move to the next week when:

- [ ] Assessment score ≥ 70%
- [ ] Can explain week's core concepts in 5 minutes aloud
- [ ] Completed lab without following steps verbatim
- [ ] Answered 20 interview questions at "good enough for interview" level

You're ready for architect interviews (Week 52) when:

- [ ] 45-minute system design feels natural, not rushed
- [ ] Can compare Azure vs AWS for any given workload
- [ ] Have 10+ STAR stories with metrics
- [ ] Portfolio of 5+ architecture diagrams you've created
- [ ] Mock panel score ≥ 80%

---

Next: [Week 01](../../weeks/week-01/README.md)
