# Technical Interview Intensive — .NET & Design Patterns

> **Week 45** | Review Months 1–2

## Objectives
- Reinforce C#, .NET 8, SOLID, design patterns
- Practice 30-second and 5-minute answer formats
- Identify weak areas for final review

---

## Daily Schedule

| Day | Focus | Q&A Target |
|-----|-------|------------|
| Mon | C# type system, async, memory | 40 questions |
| Tue | ASP.NET Core, middleware, DI | 40 questions |
| Wed | SOLID, patterns (factory, strategy, observer) | 40 questions |
| Thu | EF Core, SQL, data access patterns | 40 questions |
| Fri | Mock interview (60 min) + self-assessment | — |

---

## Answer Framework

1. **Direct answer** (10 sec)
2. **How it works** (60 sec)
3. **Architect trade-off** (30 sec)
4. **Real example** from your experience (30 sec)

---

## High-Frequency Topics

| Topic | Must Know |
|-------|-----------|
| `async/await` | ConfigureAwait, deadlock, ValueTask |
| DI lifetimes | Singleton vs Scoped vs Transient |
| GC generations | LOH, Gen2 pauses, pooling |
| CQRS | When to split read/write |
| Repository pattern | When it's overkill |

---

## Mock Interview Script

**Interviewer:** "Design a rate limiter for a public API."

**You cover:**
- Token bucket vs sliding window
- Redis vs in-memory per instance
- Response headers (429, Retry-After)
- Per-tenant vs per-IP limits

**Resources:** [Week 1–4 interview-questions/](../../week-01/interview-questions/), [Month 2 Top 50](../../../interview-prep/month-02-top-50-index.md)
