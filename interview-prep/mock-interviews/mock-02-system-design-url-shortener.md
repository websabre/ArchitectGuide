# Mock Interview 02 — System Design (45 min)

> **Duration:** 45 minutes | **Framework:** [RESHADED](../whiteboard/README.md) | **Weeks 48–49 prep

## Prompt

**Design a URL shortener** (like bit.ly) for 100M URLs, 10K writes/sec, 100K reads/sec.

## Interviewer Script

### Minute 0–5: Requirements
Ask candidate to clarify. Expected questions:
- Custom aliases? (yes, optional)
- Expiration? (yes, optional TTL)
- Analytics? (click counts — yes)

**Write assumptions on board if virtual.**

### Minute 5–10: Estimation
Expect:
- Storage: 100M × ~500 bytes ≈ 50GB + growth
- Read: 100K QPS — cache critical
- Write: 10K QPS — async OK with redirect cache

### Minute 10–20: High-Level Design
Look for:
- API service (create, redirect)
- ID generation (base62, snowflake, or hash)
- SQL or NoSQL for persistence
- Redis cache for hot URLs
- CDN for redirect edge (optional advanced)

### Minute 20–35: Deep Dive
Pick 2:
1. **Cache strategy** — cache-aside, TTL, thundering herd
2. **ID collision** — unique constraint, retry
3. **Redirect flow** — 301 vs 302, analytics async

### Minute 35–45: Failure & Scale
- DB down — cache serves reads, writes queue?
- Hot URL — single key saturation in Redis
- 10x growth — shard by hash prefix

## Scoring Rubric

| Criteria | Weight |
|----------|--------|
| Requirements | 15% |
| Estimation | 10% |
| High-level design | 25% |
| Deep dive | 25% |
| Failure/scale | 15% |
| Communication | 10% |

**Pass:** ≥ 75/100

## Reference Solution Sketch

```
Client → API Gateway → Shortener API → SQL (authoritative)
                      ↓
                    Redis (cache)
Redirect: Client → CDN/Edge → Redis → SQL fallback
Analytics: async queue → worker → analytics DB
```

## Candidate Prep

- [ ] Practice RESHADED framework timed
- [ ] Review [Week 33 theory](../../weeks/week-33/theory/)
- [ ] Draw diagram from memory before mock
