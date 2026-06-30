# Week 38 — Common Mistakes

## RAG & Vector Search

| Mistake | Why It's Wrong | Better Approach |
|---------|----------------|---------------|
| Tool-first thinking | Naming Azure/AWS services without requirements | Start from NFRs, then map services |
| Ignoring operational cost | Design that works in demo but not at scale | Estimate QPS, storage, monthly cost |
| No failure modes | Happy-path only architecture | Document 3 failure scenarios + mitigations |
| Over-engineering | Microservices for 5-user internal app | Match complexity to actual scale |
| Skipping stakeholder context | Pure tech answer in interview | Tie every decision to business outcome |

## Interview Anti-Patterns
- Memorizing service names without trade-offs
- Cannot estimate scale (users, QPS, storage)
- No experience stories — only theory
