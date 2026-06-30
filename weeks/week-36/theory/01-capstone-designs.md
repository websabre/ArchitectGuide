# System Design Capstone — 5 Whiteboard Sessions

> **Week 36** | **Level:** Expert

## Timed Designs (45 min each)

### Design 1: URL Shortener (bit.ly)

**Requirements:** 100M URLs, 10K QPS read, 100 QPS write, custom aliases optional.

**Key components:**
- `base62(id)` → short code
- Redis cache hot URLs
- SQL/NoSQL for persistence
- 301 redirect (cacheable) vs 302 (analytics)

**Deep dive:** ID generation (counter vs random), collision handling.

---

### Design 2: Real-Time Chat (WhatsApp-lite)

**Requirements:** 50M users, 1:1 and group chat, online presence, message history.

**Key components:**
- WebSocket connections (million concurrent — connection servers)
- Message queue for delivery
- Cassandra/DynamoDB for message storage (time-series by conversation)
- Redis for presence and recent messages

**Deep dive:** WebSocket scaling with sticky sessions vs pub/sub backplane.

---

### Design 3: Payment System (Stripe-lite)

**Requirements:** Process payments, idempotent, PCI scope minimized, 99.99% availability.

**Key components:**
- Tokenization (no card storage)
- Idempotency keys
- Saga: authorize → capture → settle
- Audit log (append-only)
- Double-entry ledger

**Deep dive:** Exactly-once illusion via idempotency.

---

### Design 4: News Feed (Twitter/Instagram)

**Requirements:** 300M users, fan-out on write vs read trade-off.

**Approaches:**
| Approach | Pros | Cons |
|----------|------|------|
| Fan-out on write | Fast reads | Slow for celebrities (millions followers) |
| Fan-out on read | Simple writes | Slow reads for active users |
| Hybrid | Best of both | Complexity |

**Deep dive:** Celebrity user handling (hybrid approach).

---

### Design 5: Rate Limiter

**Requirements:** 1000 RPS per API key, distributed across 10 API servers.

**Algorithms:**
| Algorithm | Description |
|-----------|-------------|
| Token bucket | Burst allowed, refill rate |
| Sliding window | Precise rate over window |
| Fixed window | Simple, boundary spike issue |

**Implementation:** Redis `INCR` + `EXPIRE` or Redis Cell module.

---

## Self-Assessment Rubric

| Score | Criteria |
|-------|----------|
| 5/5 | Clarified requirements, estimated scale, clean diagram, deep dive, trade-offs |
| 3/5 | Good diagram but missed scale estimation or failure modes |
| 1/5 | Jumped to solution without questions |

**Target:** 4/5 average across 5 designs before Week 45 interview intensive.

## Recordings

Record each session. Review within 24 hours. Note: pacing, clarity, missed requirements.
