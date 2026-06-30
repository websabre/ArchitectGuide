# Lab 36: System Design Capstone — E-Commerce Platform

| **Week** | 36 | **Duration** | 6–8 hours |

## Brief

Whiteboard + document a high-traffic e-commerce platform: catalog, cart, checkout, payments, notifications.

## Scale

- 5K orders/minute peak
- 10M products
- 99.9% availability target

## Required Diagrams

1. High-level components
2. Checkout sequence (sync + async)
3. Data stores per bounded context

## Required ADRs (minimum 3)

- SQL vs NoSQL per service
- Saga orchestration vs choreography
- Cache strategy

## Failure Scenarios

Document mitigations for:
- Payment timeout after inventory reserved
- Double-click on Pay button
- Hot product crashing cache

## Self-Assessment

| Mock | Score | Pass? |
|------|-------|-------|
| [Checkout mock](../../../interview-prep/mock-interviews/mock-05-system-design-checkout.md) | /100 | |

← [Month 9 capstone](../../../program/phase-09-month-09/capstone.md)
