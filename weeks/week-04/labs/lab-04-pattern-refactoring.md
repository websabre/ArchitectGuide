# Lab 04: Refactor with Strategy and Factory Patterns

| **Week** | 04 | **Duration** | 120 min |

## Objectives

- [ ] Refactor switch-based shipping calculator to Strategy pattern
- [ ] Add new shipping method without modifying existing code (OCP)
- [ ] Write unit tests per strategy
- [ ] Document pattern choice in ADR

## Setup

```bash
dotnet new sln -n ShippingPatterns
dotnet new classlib -n Shipping.Domain -o src/Domain
dotnet new classlib -n Shipping.Application -o src/Application
dotnet new xunit -n Shipping.Tests -o tests/Tests
dotnet sln add src/* tests/Tests
dotnet add src/Application reference src/Domain
dotnet add tests/Tests reference src/Application
```

## Step 1: Legacy Code (Intentional Violation)

```csharp
public decimal Calculate(string method, Order order) => method switch
{
    "standard" => order.Weight * 0.5m,
    "express" => order.Weight * 1.2m + 10m,
    "overnight" => order.Weight * 2.0m + 25m,
    _ => throw new ArgumentException("Unknown method")
};
```

## Step 2: Strategy Interface

```csharp
public interface IShippingStrategy
{
    string Name { get; }
    decimal Calculate(Order order);
}
```

Implement `StandardShipping`, `ExpressShipping`, `OvernightShipping`.

## Step 3: Factory / DI Registration

```csharp
services.AddKeyed<IShippingStrategy>("standard", (sp, _) => new StandardShipping());
services.AddKeyed<IShippingStrategy>("express", (sp, _) => new ExpressShipping());
```

## Step 4: Add `InternationalShipping` Without Editing Switch

New class + DI registration only — proves OCP.

## Verification

- [ ] 4+ unit tests (one per strategy + factory resolution)
- [ ] No `switch` on shipping type in application layer
- [ ] ADR: Strategy vs Chain of Responsibility

## Lab Report

1. What would break if you added crypto payments to a switch-based payment service?
2. When is Strategy overkill?
3. Link to [Month 1 Top 50 Q031](../../../interview-prep/month-01-top-50-part3.md)

## Cleanup

Remove solution or archive in `~/labs/week-04/`.
