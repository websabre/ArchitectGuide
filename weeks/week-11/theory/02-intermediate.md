# Azure Data Platform — Intermediate

> **Week 11** | **Level:** Intermediate

## SQL vs Cosmos — Decision Matrix

| Factor | Azure SQL | Cosmos DB |
|--------|-----------|-----------|
| Data model | Relational, ACID | Document / multi-model |
| Scale pattern | Vertical + read replicas | Horizontal partition key |
| Consistency | Strong default | Tunable (5 levels) |
| Cost at low scale | Often cheaper | RU minimums add up |

## Partition Key Design (Cosmos)

- High cardinality (userId, tenantId) — avoid hot partitions
- Include in queries — cross-partition scans are expensive
- Synthetic keys for even distribution when natural key skews

## Blob Lifecycle Policies

```
Hot (30 days) → Cool (90 days) → Archive
```

Architect: align tier to access pattern; archive for compliance retention.



## Architect Deep Dive: Polyglot Persistence

### Typical microservice data map
| Service | Store | Why |
|---------|-------|-----|
| Orders | Azure SQL | ACID, reporting |
| Product catalog | PostgreSQL + JSONB | Flexible attributes |
| Sessions / cart | Redis | TTL, speed |
| Product search | AI Search | Full-text, facets |
| Analytics events | Event Hubs → ADLS | Append-only lake |

### EF Core + Azure SQL operations
- Connection retry enabled (`EnableRetryOnFailure`)
- Read replicas via `ApplicationIntent=ReadOnly` for reporting queries
- Query Store enabled in production for regression detection

**Next:** [03-advanced.md](03-advanced.md)
