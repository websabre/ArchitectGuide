# Week 03 — Exercises

> Theory: [theory/](../theory/README.md) · Lab: [lab-03-clean-architecture](../labs/lab-03-clean-architecture.md) · Interview: [interview-questions/](../interview-questions/README.md)

## Exercise 1: Dependency Rule Violation Audit (45 min)

Review this snippet from a legacy Order service:

```csharp
// Domain/Order.cs
public class Order
{
    public void Submit()
    {
        using var conn = new SqlConnection(ConfigurationManager.ConnectionStrings["Orders"].Value);
        conn.Open();
        // ... persist directly
        EmailService.SendConfirmation(this.CustomerEmail);
    }
}
```

**Tasks:**
1. List every dependency rule violation (inner → outer, framework leakage, etc.)
2. Map each violation to a SOLID principle it breaks
3. Sketch the corrected dependency direction

**Deliverable:** Annotated diagram + bullet list of at least 6 violations with fixes.

---

## Exercise 2: Layer Boundary Design (45 min)

Design project boundaries for a new **Subscription Billing** bounded context:

- Domain: plans, invoices, payment attempts
- Application: use cases (subscribe, cancel, retry payment)
- Infrastructure: Stripe adapter, SQL persistence
- API: Minimal API host

**Tasks:**
1. Draw the 4-layer onion with allowed dependency arrows
2. List which types live in each project (interfaces vs implementations)
3. Identify one place MediatR fits and one place it does not

**Deliverable:** C4 container diagram or Excalidraw sketch. Compare with [diagrams/](../diagrams/README.md).

---

## Exercise 3: Ports & Adapters Exercise (60 min)

Implement a **notification port** without referencing SMTP or SendGrid in Domain/Application:

```csharp
public interface INotificationPort
{
    Task SendAsync(NotificationMessage message, CancellationToken ct);
}
```

Wire two adapters: `SmtpNotificationAdapter` and `SendGridNotificationAdapter`. Register via DI with a config flag.

**Deliverable:** Interface in Application layer, adapters in Infrastructure, unit test using a fake port.

---

## Exercise 4: ADR — Clean Architecture Adoption (30 min)

Write an ADR for:

> "Should the new Inventory microservice adopt full Clean Architecture (4 projects) or a simplified 2-layer approach?"

Team context: 3 devs, 6-month deadline, heavy CRUD, one complex pricing rule.

Use [templates/adr-template.md](../../../templates/adr-template.md). Reference [theory/](../theory/README.md) trade-offs.

---

## Exercise 5: Interview Drill (30 min)

Answer aloud from [01-fundamentals-qa.md](../interview-questions/01-fundamentals-qa.md):

1. Q001 (Single Responsibility)
2. Q005 (Dependency Inversion)
3. Q010 (Anemic vs Rich Domain Model)

Score: clarity / accuracy / trade-offs (1–5 each). Target: 12+/15.

---

[← Back to Week 03](../README.md)
