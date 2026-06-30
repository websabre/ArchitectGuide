# Week 02 Assessment — .NET Runtime & API Architecture

| **Time Limit** | 60 min | **Pass** | 70% |

## Section A: Conceptual (30 pts)

### A1. DI Lifetimes (10 pts)

A `ReportGeneratorService` runs as a **singleton** background hosted service. It needs `AppDbContext` to query data every hour.

**Question:** How do you design this correctly? What's wrong with injecting `AppDbContext` directly?

**Model Answer:** DbContext is scoped. Inject `IServiceScopeFactory`, create scope per hourly run, resolve DbContext within scope, dispose scope after. Direct injection causes captive dependency — single DbContext for app lifetime, stale connections, not thread-safe.

### A2. Minimal APIs vs MVC (10 pts)

Team building a new inventory microservice with 15 endpoints, 4 developers, needs OpenAPI docs.

**Question:** Minimal APIs or MVC Controllers? Justify.

**Model Answer:** Minimal APIs — 15 endpoints is manageable, low ceremony, good OpenAPI support, fits microservice size. MVC if team has heavy filter conventions or plans 50+ endpoints with shared base controller logic. Document choice in ADR.

### A3. gRPC vs REST (10 pts)

When would you choose gRPC over REST for a new internal service?

**Model Answer:** Internal service-to-service, high throughput, low latency, strict contracts, streaming needed. Binary protobuf smaller than JSON. Not for browser clients or public third-party APIs without grpc-web gateway.

## Section B: Diagram (20 pts)

Draw BFF + gRPC internal architecture for mobile and web clients.

## Section C: Trade-off (25 pts)

**Scenario:** Startup with 3 developers, 1 API, 500 users. CTO wants gRPC everywhere "for performance."

**Model Answer:** Over-engineering. 500 users don't need gRPC performance. REST Minimal API ships faster, easier debugging, broader tooling. Revisit gRPC when internal service count > 5 or latency SLA breached. Architect's job: right-size technology to context.

## Section D: Production (15 pts)

**Scenario:** After deployment, `SocketException: Only one usage of each socket address` errors appear.

**Model Answer:** Classic `new HttpClient()` anti-pattern. Fix with `IHttpClientFactory`. May need to restart pods to clear exhausted sockets. Add coding standard banning direct HttpClient instantiation.

## Section E: Communication (10 pts)

Explain DI to a junior developer in 2 minutes.

**Model Answer:** Framework creates objects for you. Register interfaces with implementations. Specify lifetime: singleton (one instance), scoped (per request), transient (every time). Like a restaurant: singleton is the building, scoped is your table setting per customer, transient is a new napkin each time.

## Self-Score

| Section | Score | Max |
|---------|-------|-----|
| A | | 30 |
| B | | 20 |
| C | | 25 |
| D | | 15 |
| E | | 10 |
