# Mock Interview 01 — Technical Deep Dive (.NET & Architecture)

> **Duration:** 60 minutes | **Level:** Solution Architect | **Weeks 45–47 prep

## Format

| Block | Time | Activity |
|-------|------|----------|
| Warm-up | 5 min | Introductions, interviewer explains format |
| C# / .NET | 20 min | Q009, Q001, Q013 from [Month 1 Top 50](../month-01-top-50-index.md) |
| SOLID scenario | 15 min | Payment provider extension (Q014, Q039) |
| Architecture | 15 min | Clean Architecture vs Vertical Slice (Q018) |
| Your questions | 5 min | Candidate asks interviewer |

## Interviewer Script

### Opening
"We'll cover C#, .NET, SOLID, and a short architecture discussion. Think aloud — I'm evaluating how you communicate trade-offs, not perfect answers."

### C# Block (pick 2–3)
1. "Walk me through value vs reference types and when you'd choose each at scale."
2. "Explain async/await — what happens to threads during `await database.QueryAsync()`?"
3. "How does GC affect your API design decisions?"

**Probe:** "What if this API does 15K RPS?" "Where would you use `record struct`?"

### SOLID Block
"We're adding cryptocurrency payments to an existing Stripe integration. How do you design it without modifying existing payment code every time?"

**Look for:** Strategy/OCP, DI registration, interface segregation, tests.

**Red flags:** Giant switch statement, modifying `PaymentService` only.

### Architecture Block
"Team debates Clean Architecture layers vs Vertical Slice for a new order service. What do you recommend and why?"

**Look for:** Team size, feature velocity, domain complexity, hybrid mention.

## Scoring Rubric

| Score | Description |
|-------|-------------|
| 5 | Clear trade-offs, production examples, probes handled well |
| 3 | Correct but shallow, needs prompting |
| 1 | Incorrect or cannot communicate reasoning |

**Pass:** Average ≥ 3.5 across sections.

## Candidate Prep

- [ ] Practice [Month 1 Top 50](../month-01-top-50-index.md) Q001, Q009, Q013, Q014, Q018 aloud
- [ ] Prepare 1 real project example for payment/integration story
- [ ] Review [Week 03 theory](../../weeks/week-03/theory/)

## After Action

Record weak areas in [progress tracker](../../templates/progress-tracker.md).
