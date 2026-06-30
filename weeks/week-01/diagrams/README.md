# Week 01 — Architecture Diagrams

## 1. .NET Request Processing Pipeline

```mermaid
sequenceDiagram
    participant Client
    participant Kestrel
    participant Middleware
    participant Controller
    participant Service
    participant DB

    Client->>Kestrel: HTTP Request
    Kestrel->>Middleware: Pipeline (auth, logging, etc.)
    Middleware->>Controller: Route matched
    Controller->>Service: async call
    Service->>DB: async query
    DB-->>Service: result
    Service-->>Controller: OrderDto
    Controller-->>Client: JSON Response
```

## 2. Memory Allocation in Request Lifecycle

```mermaid
flowchart TD
    A[HTTP Request] --> B[Kestrel Buffer Pool]
    B --> C[Middleware Allocations]
    C --> D[Deserialization - JSON to DTO]
    D --> E{Hot path?}
    E -->|Yes| F[Span/Pooled Objects]
    E -->|No| G[Standard LINQ/Classes]
    F --> H[Business Logic]
    G --> H
    H --> I[Serialization - DTO to JSON]
    I --> J[Response]
    
    D -.->|Allocates| K[Gen 0 Heap]
    G -.->|Allocates| K
    I -.->|Allocates| K
    K --> L{GC Trigger?}
    L -->|Yes| M[GC Pause - Latency Spike]
```

## 3. Async Request Thread Model

```mermaid
flowchart LR
    subgraph ThreadPool["Thread Pool"]
        T1[Thread 1]
        T2[Thread 2]
        T3[Thread 3]
    end

    T1 -->|handles request| A[await DB call]
    A -->|thread released| TP[Thread Pool]
    TP -->|I/O completes| T2
    T2 -->|continuation| B[await HTTP call]
    B -->|thread released| TP
    TP -->|I/O completes| T3
    T3 -->|complete response| C[Return to client]
```

## 4. C4 Container — Typical .NET API (Context Level)

```mermaid
C4Context
    title System Context - Order Management API

    Person(customer, "Customer", "Places orders via web/mobile")
    System(api, "Order API", ".NET 8 ASP.NET Core API")
    System_Ext(payment, "Payment Gateway", "Stripe/PayPal")
    System_Ext(email, "Email Service", "SendGrid")
    SystemDb(db, "SQL Database", "Order persistence")

    Rel(customer, api, "Places orders", "HTTPS/JSON")
    Rel(api, payment, "Process payments", "HTTPS")
    Rel(api, email, "Send confirmations", "HTTPS")
    Rel(api, db, "Read/write orders", "TDS/SQL")
```

> **Note:** C4 diagrams render on tools supporting C4 Mermaid syntax. For GitHub, use the sequence/flowchart diagrams above.

## 5. Type Selection Decision Tree

```mermaid
flowchart TD
    A[Need a new type?] --> B{Has identity?}
    B -->|Yes| C{class - Entity}
    B -->|No| D{Size < 16 bytes?}
    D -->|Yes| E{Immutable?}
    D -->|No| F{Immutable?}
    E -->|Yes| G[record struct]
    E -->|No| H[struct with care]
    F -->|Yes| I[record class]
    F -->|No| J{class - mutable DTO}
    
    C --> K[EF Core entity, domain aggregate]
    G --> L[Value object in hot path]
    I --> M[API response, event payload]
```

## Practice Exercise

Redraw diagrams 1, 2, and 5 from memory. Time yourself — aim for under 5 minutes each.

---

[← Back to Week 01](../README.md)
