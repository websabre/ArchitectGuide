# Week 23 — DDD Diagrams

## Bounded Context Map

```mermaid
flowchart TB
    subgraph Sales["Sales Context"]
        S[Order]
    end
    subgraph Shipping["Shipping Context"]
        SH[Shipment]
    end
    subgraph Billing["Billing Context"]
        B[Invoice]
    end
    Sales -->|Customer-Supplier| Shipping
    Sales -->|ACL| Billing
```

## Aggregate Boundary

```mermaid
flowchart TB
    subgraph OrderAggregate["Order Aggregate"]
        OR[Order - ROOT]
        L1[OrderLine]
        L2[OrderLine]
        ADDR[Address - VO]
    end
    OR --> L1
    OR --> L2
    OR --> ADDR
    CustomerRef[CustomerId reference only]
    OR -.-> CustomerRef
```

## Event Storming Legend

| Color | Element |
|-------|---------|
| Orange | Domain Event |
| Blue | Command |
| Yellow | Aggregate |
| Pink | Policy |
| Green | Read Model |

---

[← Back to Week 23](../README.md)
