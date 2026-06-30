# System Design Top 50 — Part 1 (Q001–Q008)

> [Part 2](system-design-top-50-qa-part2.md) | [Part 3](system-design-top-50-qa-part3.md) | [Index](system-design-top-50-index.md)

---

## Q001: RESHADED Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Methodology |
| **Week** | 33 |

### Question

Walk through your system design interview framework.

### Short Answer (30 seconds)

**R**equirements (functional + NFR), **E**stimation (QPS, storage), **S**torage schema, **H**igh-level design, **A**PI, **D**eep dive (2 components), **E**dge cases, **D**eployment/monitoring. Never jump to boxes before requirements.

### Detailed Answer (3–5 minutes)

Spend first 5 minutes clarifying: read/write ratio, latency SLA, consistency, durability, geographic distribution, auth.

Estimation: DAU × actions = QPS; storage = records × size × retention.

High-level: clients → LB → API → cache → DB → async workers.

Deep dive: interviewer picks 2 — usually cache + database or messaging.

Close with failure modes and how you'd monitor.

### Common Mistakes

- Drawing microservices without scale justification
- No numbers in estimation

---

## Q002: Back-of-Envelope Estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Estimation |
| **Week** | 33 |

### Question

100M users, 10% DAU post daily — estimate QPS for social feed.

### Short Answer

10M DAU × 10 reads/day = 100M reads/day ≈ 1,200 read QPS average; peak 3× ≈ 3,600 QPS. Writes lower — estimate separately.

### Detailed Answer

Always state assumptions. Round numbers: 100M × 0.1 = 10M active. 10M × 10 / 86400 ≈ 1,157 QPS. Peak factor 2–5× for evening hours.

Storage: 10M posts/day × 1KB = 10GB/day before replication.

---

## Q003: Functional vs Non-Functional Requirements

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Requirements |
| **Week** | 33 |

### Question

What NFRs must you clarify before designing Twitter/X?

### Short Answer

Read latency (<200ms), write availability, fan-out on read vs write, consistency (eventual OK for timeline?), retention, geo distribution.

### Detailed Answer

Fan-out on write vs read is THE architectural fork — celebrity users break naive fan-out-on-write.

---

## Q004: Load Balancer Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Week** | 34 |

### Question

L4 vs L7 load balancing — when each?

### Short Answer

L4: TCP routing, extreme throughput, non-HTTP. L7: HTTP path routing, TLS termination, WAF, sticky sessions.

---

## Q005: Caching Strategies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Week** | 34 |

### Question

Compare cache-aside, write-through, write-behind.

### Short Answer

Cache-aside: app manages cache (most common). Write-through: write cache + DB sync. Write-behind: write cache, async DB — fast but risk data loss.

---

## Q006: Database Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Week** | 34 |

### Question

SQL vs NoSQL for session store vs analytics?

### Short Answer

Sessions: Redis (speed, TTL). Analytics: column store / data warehouse (BigQuery, Synapse). Transactions: SQL.

---

## Q007: Horizontal vs Vertical Scaling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Scalability |
| **Week** | 34 |

### Question

When does vertical scaling stop working?

### Short Answer

Single-machine limits, no redundancy, cost curve nonlinear. Beyond ~32 cores or need 99.99% — go horizontal with stateless app tier.

---

## Q008: CDN Use Cases

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Edge |
| **Week** | 34 |

### Question

What should and shouldn't go through CDN?

### Short Answer

Should: static assets, video, public images. Shouldn't: personalized API JSON (unless edge compute); auth-sensitive without careful cache keys.

**Next:** [Part 2](system-design-top-50-qa-part2.md) →
