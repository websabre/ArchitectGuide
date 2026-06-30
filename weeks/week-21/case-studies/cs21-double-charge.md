# Case Study: Payment Double-Charge Incident

| **Week** | 21 | **Difficulty** | Expert |

## Context
FinTech company. Customers charged twice for same order during Black Friday. Root cause: client retry + message queue redelivery + non-idempotent payment handler.

## Timeline
1. Payment gateway timeout (30s)
2. Mobile app retries POST /payments
3. Service Bus redelivers same message (handler crashed after charge, before ack)
4. No idempotency key — second charge succeeds

## Your Task
1. Root cause analysis
2. Fix architecture (not just bug fix)
3. Prevent recurrence

## Reference Solution

**Immediate:**
- Idempotency-Key on all payment commands (client + message)
- `ProcessedPayments` table with unique constraint on `(orderId, operation)`
- Payment gateway idempotency key passthrough (Stripe supports this)

**Architecture:**
- Outbox pattern for order → payment flow
- Saga with compensating refund on duplicate detection
- Circuit breaker on payment gateway — fail fast, don't retry non-idempotent without key

**Monitoring:**
- Alert on duplicate idempotency key attempts
- Dashboard: payment success rate, retry rate, DLQ depth

## Interview STAR
Situation: double-charge incident. Action: idempotency + outbox + monitoring. Result: zero duplicates in 12 months post-fix.
