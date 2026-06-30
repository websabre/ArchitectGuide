# Lab 02: DI, Minimal APIs, and gRPC Side-by-Side

| Attribute | Value |
|-----------|-------|
| **Week** | 02 |
| **Duration** | 120 minutes |
| **Prerequisites** | .NET 8 SDK, Week 01 lab |

## Objectives

- [ ] Build a service with proper DI lifetimes
- [ ] Expose REST via Minimal APIs
- [ ] Expose gRPC for internal consumers
- [ ] Configure health checks and Options pattern

## Step 1: Create Solution

```bash
dotnet new webapi -n OrderGateway -o order-gateway --use-minimal-apis
cd order-gateway
dotnet new grpc -n OrderGrpc -o order-grpc
dotnet new sln -n OrderLab
dotnet sln add order-gateway order-grpc
```

## Step 2: Options Pattern

Add to `appsettings.json`:

```json
{
  "OrderService": {
    "BaseUrl": "https://localhost:5001",
    "TimeoutSeconds": 10
  }
}
```

```csharp
public class OrderServiceOptions
{
    public const string SectionName = "OrderService";
    public string BaseUrl { get; set; } = "";
    public int TimeoutSeconds { get; set; } = 30;
}

builder.Services.Configure<OrderServiceOptions>(
    builder.Configuration.GetSection(OrderServiceOptions.SectionName));
```

## Step 3: DI Registration

```csharp
builder.Services.AddScoped<IOrderRepository, InMemoryOrderRepository>();
builder.Services.AddSingleton<IClock, SystemClock>();
builder.Services.AddHttpClient<IOrderClient, OrderClient>();
builder.Services.AddHealthChecks().AddCheck("self", () => HealthCheckResult.Healthy());
```

**Architect note:** Repository is Scoped (per-request state). Clock is Singleton (stateless).

## Step 4: Minimal API Endpoints

```csharp
var orders = app.MapGroup("/api/v1/orders").WithTags("Orders");

orders.MapGet("/{id:guid}", async (Guid id, IOrderRepository repo) =>
{
    var order = await repo.GetByIdAsync(id);
    return order is not null ? Results.Ok(order) : Results.NotFound();
});

orders.MapPost("/", async (CreateOrderRequest req, IOrderRepository repo) =>
{
    var order = await repo.CreateAsync(req);
    return Results.Created($"/api/v1/orders/{order.Id}", order);
});
```

## Step 5: Add gRPC Service (order-grpc project)

Define `Protos/order.proto` and implement `OrderService`. Configure Kestrel for HTTP/2.

## Step 6: Health Checks

```csharp
app.MapHealthChecks("/health/live");
app.MapHealthChecks("/health/ready");
```

Test: `curl http://localhost:5000/health/ready`

## Step 7: Verify DI Lifetimes

Intentionally inject `IOrderRepository` (scoped) into a singleton service. Observe runtime exception or stale data. Fix with `IServiceScopeFactory`.

## Lab Report

1. When would you expose both REST and gRPC from the same service vs separate services?
2. Document your DI lifetime choices in a mini-ADR.
3. What would change for Azure App Service deployment?

## Cleanup

```bash
cd .. && rm -rf order-gateway order-grpc OrderLab.sln
```
