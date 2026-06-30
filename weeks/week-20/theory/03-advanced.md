# Multi-Cloud Architecture — Advanced

> **Week 20** | **Level:** Advanced

## FARCS Framework (Interview)

- **F**unctional requirements
- **A**vailability / DR
- **R**eplication / data residency
- **C**ost
- **S**ecurity / compliance

## FinOps Across Clouds

- Unit economics: cost per transaction, per tenant
- Commitment strategies: RIs, Savings Plans, Azure Reservations
- Tagging enforcement via policy (Azure Policy, SCPs)

## Architect Scenario

CTO wants active-active in Azure and AWS for payment API. Design portable core + cloud-specific adapters. Document trade-offs.

**Cross-cutting:** [FinOps](../../../docs/cross-cutting/finops-cost-optimization/README.md)

**Premium Q&A:** [Azure Top 50](../../../interview-prep/azure-top-50-index.md) | [AWS Top 50](../../../interview-prep/aws-top-50-index.md)

## Architect Deep Dive: Exit Strategy

Every managed service choice should note **migration cost** in ADR: "If we leave Azure SQL, we need logical export + downtime window of X hours." Honesty beats faux portability.

