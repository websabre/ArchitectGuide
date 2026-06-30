# Week 03 — Diagrams

## Clean Architecture Layers

```mermaid
flowchart TB
    subgraph Outer["Frameworks & Drivers"]
        API[ASP.NET Core API]
        EF[EF Core]
        MQ[Message Bus]
    end

    subgraph Adapters["Interface Adapters"]
        Controllers[Endpoints]
        Repo[Repositories]
        DTOs[DTOs / Mappers]
    end

    subgraph App["Application"]
        Commands[Commands / Queries]
        Handlers[Handlers]
    end

    subgraph Domain["Domain"]
        Entities[Entities]
        VO[Value Objects]
        Events[Domain Events]
    end

    API --> Controllers
    Controllers --> Handlers
    Handlers --> Entities
    Handlers --> Repo
    Repo --> EF
    Handlers --> MQ
    Entities --> Events
```

## Hexagonal (Ports & Adapters)

```mermaid
flowchart LR
    REST[REST Adapter] --> Port1[IOrderService Port]
    gRPC[gRPC Adapter] --> Port1
    Port1 --> Domain[Domain Core]
    Domain --> Port2[IOrderRepository Port]
    Port2 --> EF[EF Adapter]
    Port2 --> Memory[In-Memory Adapter]
```

## Vertical Slice vs Layered

```mermaid
flowchart TB
    subgraph Layered["Horizontal Layers"]
        L1[API Layer]
        L2[Business Layer]
        L3[Data Layer]
        L1 --> L2 --> L3
    end

    subgraph Vertical["Vertical Slices"]
        F1[Create Order Feature]
        F2[Get Order Feature]
        F3[Cancel Order Feature]
    end
```

## CQRS Read/Write Separation

```mermaid
flowchart LR
    Client --> API[API]
    API -->|Command| Write[Write Model / EF]
    API -->|Query| Read[Read Model / Dapper / Cache]
    Write -->|Events| Projector[Projection Handler]
    Projector --> Read
```

## Modular Monolith

```mermaid
flowchart TB
    subgraph Monolith
        O[Orders Module]
        P[Payments Module]
        S[Shipping Module]
        O -.->|Events| P
        P -.->|Events| S
    end
    O --> ODB[(Orders Schema)]
    P --> PDB[(Payments Schema)]
    S --> SDB[(Shipping Schema)]
```

---

[← Back to Week 03](../README.md)
