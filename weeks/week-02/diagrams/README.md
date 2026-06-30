# Week 02 — Architecture Diagrams

## 1. .NET Hosting Architecture

```mermaid
flowchart TB
    subgraph Internet
        Client[Clients]
    end

    subgraph Azure
        AG[Application Gateway / Front Door]
        subgraph AppService["App Service / Container Apps"]
            Kestrel[Kestrel]
            Pipeline[Middleware Pipeline]
            API[Minimal API / Controllers / gRPC]
        end
        KV[Key Vault]
        AI[App Insights]
    end

    Client -->|HTTPS| AG
    AG --> Kestrel
    Kestrel --> Pipeline
    Pipeline --> API
    API --> KV
    API --> AI
```

## 2. DI Lifetime Scopes

```mermaid
flowchart TD
    subgraph Singleton["Singleton Scope (App Lifetime)"]
        S1[CacheService]
        S2[HttpClientFactory]
    end

    subgraph Request1["Request 1 Scope"]
        R1A[OrderService]
        R1B[DbContext Instance 1]
        R1A --> R1B
    end

    subgraph Request2["Request 2 Scope"]
        R2A[OrderService]
        R2B[DbContext Instance 2]
        R2A --> R2B
    end

    S1 -.->|OK inject| R1A
    S1 -.->|OK inject| R2A
    R1B -.->|NEVER inject into| S1
```

## 3. BFF + gRPC Internal Architecture

```mermaid
flowchart LR
    Mobile[Mobile App] -->|REST| MobileBFF[Mobile BFF]
    Web[Web App] -->|REST| WebBFF[Web BFF]
    Partner[Partner] -->|REST| APIM[API Management]

    MobileBFF -->|gRPC| OrderSvc[Order Service]
    WebBFF -->|gRPC| OrderSvc
    APIM -->|REST| WebBFF

    OrderSvc -->|gRPC| PaymentSvc[Payment Service]
    OrderSvc -->|gRPC| InventorySvc[Inventory Service]
    OrderSvc --> DB[(SQL Database)]
```

## 4. Configuration Flow

```mermaid
flowchart TD
    A[appsettings.json] --> E[IConfiguration]
    B[appsettings.Production.json] --> E
    C[Environment Variables] --> E
    D[Azure Key Vault] --> E
    E --> F[Options Pattern]
    F --> G[IOptions T - startup snapshot]
    F --> H[IOptionsMonitor T - hot reload]
    F --> I[IOptionsSnapshot T - per request]
```

## 5. Middleware Pipeline Order

```mermaid
flowchart LR
    A[Request] --> B[Exception Handler]
    B --> C[HSTS / HTTPS]
    C --> D[Static Files]
    D --> E[Routing]
    E --> F[CORS]
    F --> G[Authentication]
    G --> H[Authorization]
    H --> I[Endpoints]
    I --> J[Response]
```

## Practice

Redraw diagrams 2 and 3 from memory. Explain DI lifetime rules while drawing diagram 2 aloud.

---

[← Back to Week 02](../README.md)
