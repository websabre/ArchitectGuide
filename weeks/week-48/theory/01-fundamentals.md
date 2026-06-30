# Whiteboard Mock Sessions — Week 48

> **Week 48** | Timed 45-minute design sessions

## Session 1: Design a Real-Time Notification System

**Prompt:** Push notifications to 10M mobile users. Support email, SMS, push. Priority queues. At-least-once delivery.

**Rubric:**
| Area | Points |
|------|--------|
| Requirements clarification | 15 |
| Component diagram | 20 |
| Queue/topic design | 20 |
| Scale estimates | 15 |
| Failure modes | 15 |
| Monitoring | 15 |

**Time checkpoints:** 5 min requirements, 15 min design, 15 min deep dive, 10 min Q&A.

---

## Session 2: Design an E-Commerce Cart

**Prompt:** Amazon-scale cart. Guest + logged-in. Inventory reservation. Price changes during checkout.

**Key decisions:**
- Cart storage (Redis vs DB)
- Inventory hold TTL
- Optimistic concurrency on checkout
- Event-driven order creation

---

## Self-Review Template

After each session, score yourself 1–5:
- [ ] Asked clarifying questions before designing
- [ ] Stated assumptions explicitly
- [ ] Drew diagram while explaining
- [ ] Addressed scale with numbers
- [ ] Identified single points of failure
- [ ] Left time for trade-off discussion

**Peer review:** Swap diagrams with study partner; critique using rubric.
