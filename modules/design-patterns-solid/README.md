# Design Patterns & SOLID Module

| **Module ID** | `design-patterns-solid` | **Weeks** | 3–4 | **Q&A Target** | 250+

## Overview
SOLID principles and design patterns form the vocabulary architects use in code reviews, ADRs, and technical interviews. This module bridges "I know patterns" to "I know when patterns solve real problems."

## Topic Map
| Topic | Week |
|-------|------|
| SOLID principles | 3 |
| Clean/Onion/Hexagonal Architecture | 3 |
| CQRS, MediatR, Vertical Slice | 3 |
| GoF Creational/Structural/Behavioral | 4 |
| Enterprise patterns (Repository, Saga, Outbox) | 4 |
| Anti-patterns | 4 |

## Week Content
- [Week 03](../../weeks/week-03/README.md) — SOLID & Clean Architecture
- [Week 04](../../weeks/week-04/README.md) — Design Patterns

## Interview Q&A
| File | Count |
|------|-------|
| Week 03 Q&A | 120 |
| Week 04 Q&A | 120 |
| **Total** | **240** |

## Key Trade-offs
| Decision | When Pattern | When Skip |
|----------|-------------|-----------|
| Repository | Multiple stores, testing needs | Simple EF-only app |
| CQRS | Read/write scale differs | CRUD with 100 users |
| Saga | Distributed transactions | Single database |
| MediatR | Pipeline behaviors needed | 3 simple endpoints |
