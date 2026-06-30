# Whiteboard System Design — Framework

## The RESHADED Framework

Use this 45-minute structure in every system design interview:

| Step | Time | Letter | Action |
|------|------|--------|--------|
| 1 | 5 min | **R**equirements | Functional + non-functional; ask clarifying questions |
| 2 | 5 min | **E**stimation | Back-of-envelope: users, QPS, storage, bandwidth |
| 3 | 10 min | **S**ystem design | High-level boxes and arrows; APIs; data model |
| 4 | 15 min | **H**ighlights | Deep dive 2 critical components |
| 5 | 5 min | **A**vailability | Failure modes, redundancy, DR |
| 6 | 3 min | **D**eployment | How it gets built, deployed, monitored |
| 7 | 2 min | **E**volution | How it scales 10x; what changes |
| 8 | — | **D**iscussion | Trade-offs, alternatives, open questions |

---

## Clarifying Questions Cheat Sheet

Always ask before designing:

```
Users & Scale:
- How many daily/monthly active users?
- Read vs write ratio?
- Geographic distribution?

Performance:
- Latency requirements (p50, p99)?
- Availability SLA (99.9%, 99.99%)?
- Consistency requirements (strong vs eventual)?

Constraints:
- Budget sensitivity?
- Team size and expertise?
- Existing systems to integrate with?
- Compliance (GDPR, HIPAA, PCI)?
- Timeline?
```

---

## Estimation Quick Reference

| Metric | Calculation |
|--------|-------------|
| QPS | DAU × actions/day ÷ 86400 |
| Peak QPS | Average QPS × 3–5 |
| Storage/year | Records/day × record size × 365 |
| Bandwidth | QPS × response size |
| Servers (rough) | Peak QPS ÷ RPS per server |

**Assume:** 1 server ≈ 500–2000 RPS for simple CRUD (varies widely)

---

## Common Design Problems (Week 36 Capstone)

| # | Problem | Key Challenges |
|---|---------|---------------|
| 1 | URL Shortener | Hashing, collision, redirect latency |
| 2 | Real-time Chat | WebSockets, presence, message ordering |
| 3 | Payment System | Idempotency, consistency, PCI |
| 4 | News Feed | Fan-out on write vs read, ranking |
| 5 | Rate Limiter | Token bucket, distributed counters |
| 6 | Notification System | Multi-channel, delivery guarantees |
| 7 | E-commerce Platform | Inventory, cart, search, checkout |
| 8 | Video Streaming | CDN, transcoding, adaptive bitrate |
| 9 | Ride Sharing | Geospatial, matching, real-time |
| 10 | Distributed Cache | Eviction, consistency, partitioning |

---

## Scoring Rubric (Self / Peer Review)

| Criteria | Weight | 1 (Poor) | 3 (Good) | 5 (Excellent) |
|----------|--------|----------|----------|---------------|
| Requirements | 15% | Jumps to design | Asks some questions | Thorough clarification |
| Estimation | 10% | No numbers | Rough estimates | Structured calculations |
| High-level design | 25% | Missing components | Core components present | Clean, complete diagram |
| Deep dive | 20% | Surface level | One component detailed | Two components, trade-offs |
| Scale & failure | 15% | Not addressed | Basic redundancy | DR, monitoring, failure modes |
| Communication | 15% | Confusing | Clear structure | Engaging, checks understanding |

---

## Practice Schedule

| Week | Designs | Time Each |
|------|---------|-----------|
| 33 | 1 (with framework learning) | 60 min |
| 34–35 | 1 per week | 45 min |
| 36 | 5 capstone | 45 min each |
| 48–49 | 6 mocks | 45 min each |

Record every session. Review within 24 hours.
