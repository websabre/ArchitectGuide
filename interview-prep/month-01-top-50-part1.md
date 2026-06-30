# Month 1 Top 50 — Part 1 (Q001–Q008)

> **C# Fundamentals** | Weeks 1–2 | [Part 2](month-01-top-50-part2.md) | [Index](month-01-top-50-index.md)

---

## Q001: Value Types vs Reference Types

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Type System |
| **Week** | 01 |

### Question

What is the difference between value types and reference types? When would you choose each in system design?

### Short Answer (30 seconds)

Value types are copied by value (structs, primitives); reference types hold a reference to heap objects (classes). Use value types for small immutable data without identity; classes for entities with lifecycle and polymorphism.

### Detailed Answer (3–5 minutes)

Value types (`struct`, `int`, `decimal`) are typically stack-allocated or inline. Assignment copies the entire value. Reference types (`class`) allocate on the heap; variables hold references.

**Architect decisions:**
- `readonly record struct Money(decimal Amount, string Currency)` — high-throughput payment calculations, less GC
- `class Order` — entity with `Id`, persistence, business rules
- Large structs (>16 bytes rule of thumb) — copying cost may exceed GC benefit

**Boxing:** Value types on heap when boxed, in arrays of `object`, or as class fields — "structs are always on stack" is false.

### Architecture Perspective

Interviewers connect this to GC pressure, API design, and serialization — not trivia.

### Follow-up Questions

1. **`string`?** Reference type, immutable, special-cased behavior.
2. **`record class` vs `record struct`?** Reference vs value semantics with value-based equality.

### Common Mistakes in Interviews

- "Structs always on stack"
- Recommending structs everywhere without size/copy analysis

---

## Q002: async/await and ConfigureAwait

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C# Async |
| **Week** | 01 |

### Question

Explain async/await. When does `ConfigureAwait(false)` matter for library vs application code?

### Short Answer (30 seconds)

`async/await` frees threads during I/O by returning a Task and resuming on completion. In ASP.NET Core app code, `ConfigureAwait(false)` is usually unnecessary (no sync context). In shared libraries, use it to avoid deadlocks in UI/legacy ASP.NET contexts.

### Detailed Answer (3–5 minutes)

Async methods compile to state machines. `await` yields the thread; continuation runs when I/O completes.

**ASP.NET Core:** No `SynchronizationContext` — continuations use thread pool. `ConfigureAwait(false)` optional.

**Library code:** `return await Foo().ConfigureAwait(false)` prevents capturing caller context — safe default for reusable libraries.

**Anti-patterns:**
- `async void` except event handlers
- `.Result` / `.Wait()` — deadlock risk with sync context
- Fake async (`Task.Run` wrapping CPU work that's already sync)

**Architect:** Async all the way through I/O boundaries — DB, HTTP, messaging. Measure thread pool starvation under load.

### Follow-up Questions

1. **ValueTask?** When hot path often completes synchronously — reduces allocation.
2. **Thread pool starvation?** Too many blocked sync-over-async calls — fix code, don't just raise min threads.

### Common Mistakes in Interviews

- Saying ConfigureAwait is always required in .NET Core APIs
- Blocking on async with `.Result` in controllers

---

## Q003: Garbage Collection and Architect Impact

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | .NET Runtime |
| **Week** | 01, 02 |

### Question

How does the .NET GC work? What architectural decisions reduce GC pressure?

### Short Answer (30 seconds)

Generational GC: Gen0 (short-lived), Gen1, Gen2 (long-lived), LOH for large objects. Reduce pressure with pooling (`ArrayPool`), structs for transient data, avoiding unnecessary allocations in hot paths, and right-sizing memory limits in containers.

### Detailed Answer (3–5 minutes)

**Generations:** Most objects die young — Gen0 collections are cheap. Promoted objects reach Gen2 — expensive full collections cause pause spikes.

**LOH:** Objects ≥85KB — collected with Gen2, not compacted by default (fragmentation risk).

**Architect tactics:**
- `ArrayPool<byte>.Shared` for buffers
- Object pooling for `HttpClient` era mistakes (now use `IHttpClientFactory`)
- Struct records for value-heavy DTOs in hot loops
- Monitor `% Time in GC` and Gen2 frequency in production

**Container/K8s:** Set memory limits; GC adapts heap — OOMKill if limit too tight.

### Follow-up Questions

1. **GC modes?** Server GC for throughput (multi-core); Workstation for client apps.
2. **LOH compaction?** `GCSettings.LargeObjectHeapCompactionMode` — use carefully.

### Common Mistakes in Interviews

- Ignoring GC when designing high-RPS APIs
- Creating new `JsonSerializerOptions` per request

---

## Q004: Nullable Reference Types in Enterprise

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Type System |
| **Week** | 01 |

### Question

Should nullable reference types be enabled on enterprise .NET projects? Why?

### Short Answer (30 seconds)

Yes — enable `<Nullable>enable</Nullable>` on all new projects and treat warnings as errors in CI. Catches null dereferences at compile time across large teams.

### Detailed Answer (3–5 minutes)

With NRT: `string` is non-nullable by default; `string?` may be null. Compiler warns on unsafe dereference.

**Enterprise rollout:**
1. Enable on new projects immediately
2. Existing code: enable gradually per project with warning baseline
3. CI: `/p:TreatWarningsAsErrors=true` for nullability warnings in new code

**Architect benefit:** NullReferenceException is a top production crash — NRT is cheap insurance at scale.

### Follow-up Questions

1. **`!` null-forgiving operator?** Escape hatch — document why, don't abuse.
2. **API contracts?** `[NotNull]` attributes on public API boundaries.

### Common Mistakes in Interviews

- "We disable nullable because too many warnings" — fix incrementally instead

---

## Q005: records vs classes vs structs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C# Type System |
| **Week** | 01 |

### Question

When do you use `record class`, `record struct`, `class`, and `struct`?

### Short Answer (30 seconds)

`record class` for immutable DTOs and domain events with value equality. `class` for entities with identity and mutable state. `record struct` for small immutable value data. `struct` rarely — prefer `record struct` in modern C#.

### Detailed Answer (3–5 minutes)

| Type | Use Case |
|------|----------|
| `record class OrderCreatedEvent` | Domain events, message contracts |
| `record struct Money` | Small immutable values in hot paths |
| `class Order` | Aggregate root with `Id`, behavior |
| `class` service | DI services, repositories |

**Immutability:** Records encourage `init` — thread-safe, easier reasoning.

**Architect:** Event contracts as records version well; entities stay classes with controlled mutation.

### Follow-up Questions

1. **with expressions?** Non-destructive mutation for records.
2. **EF Core entities as records?** Possible but uncommon — identity and change tracking favor classes.

### Common Mistakes in Interviews

- Using records for everything including mutable domain entities

---

## Q006: LINQ and IEnumerable Architect Considerations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C# / Performance |
| **Week** | 01 |

### Question

What are the performance implications of LINQ in high-throughput APIs?

### Short Answer (30 seconds)

LINQ deferred execution can cause multiple enumeration, hidden allocations, and client-side evaluation if provider is IEnumerable not IQueryable. In hot paths, prefer explicit loops or compiled queries; always materialize once.

### Detailed Answer (3–5 minutes)

**Deferred execution:** `Where().Select()` builds expression tree — executes on enumerate.

**Pitfalls:**
- Multiple enumeration of same IEnumerable — DB hit twice
- `Count()` after `Where()` — may re-scan
- `.ToList()` once at boundary — then operate in memory

**IQueryable (EF):** Translates to SQL — architect ensures queries filter at database, not in memory after `AsEnumerable()`.

**When to avoid LINQ:** Microsecond-critical paths, tight loops — `for` loop clearer and faster.

### Follow-up Questions

1. **IAsyncEnumerable?** Streaming large datasets without loading all to memory.
2. **N+1 queries?** LINQ eager loading with `.Include()` — architect reviews EF queries.

### Common Mistakes in Interviews

- "LINQ is always fine" in 10K RPS endpoints without measurement

---

## Q007: Span, Memory, and stackalloc

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | C# Performance |
| **Week** | 01 |

### Question

When would an architect recommend `Span<T>`, `Memory<T>`, or `stackalloc`?

### Short Answer (30 seconds)

For parsing protocols, crypto, or serialization hot paths where heap allocation per request is measurable. `Span<T>` is stack-only ref struct; `Memory<T>` for async scenarios. Use when profiling proves allocation is a bottleneck — not by default.

### Detailed Answer (3–5 minutes)

`Span<T>` — slice into arrays/strings without copying. `stackalloc` — small buffers on stack.

**Example:** Parsing fixed-width headers, Base64 decoding buffers, custom JSON tokenizer.

**Architect guardrail:** Team must understand lifetime rules — Spans can't escape async methods easily. Prefer `Memory<T>` for async buffer work.

**Don't:** Rewrite entire codebase with Span — measure first.

### Follow-up Questions

1. **ref struct restrictions?** Can't box, can't be class field, can't use in async.
2. **System.IO.Pipelines?** Built on these primitives for high-perf I/O.

### Common Mistakes in Interviews

- Recommending Span without profiling evidence
- Using stackalloc for large buffers — stack overflow risk

---

## Q008: Pattern Matching for Domain Logic

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C# Modern Features |
| **Week** | 01 |

### Question

How does pattern matching improve domain modeling in C# 11+?

### Short Answer (30 seconds)

Switch expressions, relational patterns, and list patterns replace nested if/switch with exhaustive, readable domain rules — compiler warns on non-exhaustive switches when using discriminated unions.

### Detailed Answer (3–5 minutes)

```csharp
public decimal CalculateShipping(Order order) => order switch
{
    { Total: > 100, Customer.IsPrime: true } => 0,
    { Items.Count: > 10 } => 9.99m,
    _ => 4.99m
};
```

**Architect value:** Business rules visible in one place; easier code review than scattered conditionals.

**Combine with:** Discriminated unions via abstract record hierarchy for payment results, validation outcomes.

### Follow-up Questions

1. **Exhaustiveness?** Enable analyzers; use `_` or `default` arm carefully.
2. **vs Strategy pattern?** Pattern matching for simple branching; Strategy when behavior varies by pluggable types.

### Common Mistakes in Interviews

- Giant switch without default handling unknown cases

---

**Navigation:** [Part 2 — .NET & SOLID](month-01-top-50-part2.md) →
