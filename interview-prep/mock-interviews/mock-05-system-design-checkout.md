# Mock Interview 05 — System Design (E-Commerce Checkout)

> **Duration:** 45 minutes | **Week 49 prep

## Prompt

Design checkout for high-traffic e-commerce: cart, inventory hold, payment, order creation. 5K orders/minute at peak.

## Key Evaluation Points

| Area | Must Cover |
|------|------------|
| Inventory | Reservation TTL, oversell prevention |
| Payment | Idempotency keys, saga vs 2PC |
| Consistency | At-least-once events, outbox pattern |
| Failure | Payment timeout, inventory release |

## Deep Dive Probes

- "Customer double-clicks Pay — what happens?"
- "Payment succeeds, order service down — how recover?"
- "How long hold inventory?"

## Reference Patterns

- Saga orchestration or choreography
- `Idempotency-Key` header
- Redis for cart, SQL for orders
- Message bus for `PaymentCompleted` event

## Rubric

Same as [mock-02](mock-02-system-design-url-shortener.md) — pass ≥ 75/100.

## Prep

- [Week 35 messaging theory](../../weeks/week-35/theory/)
- [Week 21 distributed systems](../../weeks/week-21/theory/)
