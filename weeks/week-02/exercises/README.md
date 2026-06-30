# Week 02 — Exercises

## Exercise 1: DI Lifetime Audit (45 min)

Given this registration code, identify all lifetime violations:

```csharp
builder.Services.AddSingleton<AppDbContext>();
builder.Services.AddScoped<OrderService>();
builder.Services.AddSingleton<CacheService>();
builder.Services.AddScoped<ICacheService>(sp => sp.GetRequiredService<CacheService>());
builder.Services.AddTransient<EmailService>();
builder.Services.AddSingleton<ReportJob>();
```

Fix violations and explain each fix.

---

## Exercise 2: Minimal API Design (60 min)

Build a Minimal API for a `Product` resource with:
- GET /api/v1/products/{id}
- GET /api/v1/products?category={cat}
- POST /api/v1/products
- Options pattern for `ProductOptions`
- Health check endpoint
- OpenAPI annotations

---

## Exercise 3: API Style ADR (30 min)

Write an ADR choosing REST vs gRPC for:
- Customer-facing order status API
- Internal inventory check between Order and Inventory services

Two ADRs using [adr-template.md](../../../templates/adr-template.md).

---

## Exercise 4: Middleware Ordering (20 min)

List correct order for: CORS, Authentication, Authorization, Exception Handler, HTTPS Redirection, Routing, Static Files.

Explain what breaks if Authorization comes before Authentication.

---

## Exercise 5: Interview Drill (30 min)

Practice aloud from [interview-questions/](../interview-questions/) — Q001, Q005, Q010.

---

[← Back to Week 02](../README.md)
