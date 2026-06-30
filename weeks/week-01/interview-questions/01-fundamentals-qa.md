# Week 01 — Fundamentals Interview Q&A

> **30 questions** — Q001–Q005 & Q011–Q030: Premium format. Q006–Q010: Quick Fire.  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---

## Q001: Value Type vs Reference Type

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Type System |
| **Frequency** | Common |

### Question

What is the difference between value types and reference types in C#? When would you choose each in a system design?

### Short Answer (30 seconds)

Value types are stored on the stack (or inline), copied by value, and include structs and primitives. Reference types live on the heap, are copied by reference, and include classes. Use value types for small immutable data with no identity; use classes for entities with identity and lifecycle.

### Detailed Answer (3–5 minutes)

In C#, the type system divides into value types and reference types. Value types (`struct`, `int`, `decimal`, etc.) are typically allocated on the stack or inline within other objects. When you assign or pass them, a copy is made. Reference types (`class`, `string`, arrays) are allocated on the managed heap and garbage collected. Variables hold a reference (pointer) to the heap object.

**Architect decisions:**

- **Value types (especially `record struct`)** for: money amounts, coordinates, small DTOs in high-throughput paths where reducing GC pressure matters.
- **Reference types (`class`)** for: domain entities with identity (Order, Customer), services, large objects, anything needing polymorphism or inheritance.

**Trade-offs:**
- Value types: less GC pressure, but copying large structs is expensive
- Reference types: efficient passing by reference, but each instance adds GC pressure

In a payment API processing 10K RPS, I'd use `readonly record struct Money(decimal Amount, string Currency)` to avoid heap allocations for transient calculations, but `class Order` for the persisted entity with an `Id`.

### Architecture Perspective

This isn't a trivia question — interviewers want to see if you connect language choices to system behavior: GC pauses, memory footprint, API serialization, and thread safety.

### Follow-up Questions

1. **Can structs be on the heap?**
   - Yes — when boxed, as fields of a class, or in arrays. Structs aren't *always* on the stack.
2. **What about `string`?**
   - `string` is a reference type but immutable. It's a special case — behaves like a value semantically but has reference semantics.

### Common Mistakes in Interviews

- Saying "structs are always on the stack" (incorrect — boxing, class fields)
- Not connecting the answer to GC or performance
- Recommending structs for everything without considering size/copy cost

---

## Q002: Nullable Reference Types

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Type System |
| **Frequency** | Common |

### Question

What are Nullable Reference Types in C# and should they be enabled in enterprise projects?

### Short Answer

NRT is a C# 8+ feature that treats reference types as non-nullable by default when enabled. The compiler warns on potential null dereferences. Yes — enable on all new enterprise projects and enforce warnings as errors in CI.

### Detailed Answer

With `<Nullable>enable</Nullable>`, the compiler tracks nullability:
- `string` = non-nullable (compiler expects never null)
- `string?` = nullable (may be null)
- Warnings on dereferencing potentially null values without checks

For enterprise projects with 50+ developers and millions of lines, null reference exceptions are a top crash cause. NRT catches these at compile time.

**Implementation approach:**
1. Enable on new projects immediately
2. For legacy: enable incrementally per project/assembly
3. Set `TreatWarningsAsErrors` for nullable warnings in CI
4. Use `ArgumentNullException.ThrowIfNull()` at API boundaries

### Architecture Perspective

NRT is a **quality gate** — architects should mandate it in coding standards. The cost is annotation effort; the benefit is fewer production null-reference crashes and clearer API contracts.

---

## Q003: record vs class

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Modern Features |
| **Frequency** | Common |

### Question

When would you use `record` instead of `class` in a .NET architecture?

### Short Answer

Use `record` for immutable data carriers — DTOs, API responses, domain events, message payloads. Use `class` for entities with mutable state, EF Core models, and objects with complex behavior/lifecycle.

### Detailed Answer

`record` provides:
- Value-based equality (by properties, not reference)
- `with` expressions for non-destructive mutation
- Concise syntax with primary constructors (C# 12)
- Immutability by default with `init` accessors

| Use Case | Type | Why |
|----------|------|-----|
| API response model | `record` | Immutable, equality for caching |
| Domain event | `record` | Events are immutable facts |
| EF Core entity | `class` | Change tracking requires mutation |
| Service class | `class` | Has behavior, DI lifetime |
| Value object (Money) | `record struct` | Small, no identity, no GC |

### Follow-up Questions

1. **Can records have methods?** Yes — records can have methods, but keep them focused on the data they represent.
2. **Are records always immutable?** No — you can have mutable `set` properties, but it defeats the purpose.

---

## Q004: What is Boxing?

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Memory & GC |
| **Frequency** | Occasional |

### Question

Explain boxing and unboxing. Why should architects care?

### Short Answer

Boxing converts a value type to `object` (heap allocation). Unboxing converts back. Architects care because accidental boxing in hot paths causes GC pressure and performance degradation.

### Detailed Answer

```csharp
int i = 42;
object o = i;    // Boxing — allocates on heap, copies value
int j = (int)o;  // Unboxing — copies back to stack
```

**Hidden boxing scenarios:**
- `ArrayList` (non-generic collections)
- `string.Format` with value types (older patterns)
- LINQ over non-generic `IEnumerable`
- Calling `ToString()` on structs through `object` reference

In a high-throughput service, even small boxing operations multiplied by millions of requests cause Gen 0 GC pressure.

**Architect action:** Code review guidelines banning non-generic collections; static analysis rules for boxing detection.

---

## Q005: async vs sync — When to Use Async

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Async/Await |
| **Frequency** | Very Common |

### Question

When should you use async/await in a .NET web API? Is it always better than synchronous code?

### Short Answer

Use async for I/O-bound operations (database, HTTP, file system). It frees threads during waits, improving scalability. Don't use async for CPU-bound work — use `Task.Run` to offload to thread pool instead. Async isn't "faster" — it enables better thread utilization.

### Detailed Answer

**I/O-bound (use async):**
```csharp
public async Task<Order> GetOrderAsync(Guid id)
    => await _db.Orders.FindAsync(id);
```

**CPU-bound (don't make the action async):**
```csharp
public IActionResult Compute()
{
    var result = HeavyCalculation(); // synchronous or Task.Run
    return Ok(result);
}
```

**Why async helps scalability:**
- ASP.NET Core thread pool has limited threads (~few hundred)
- Sync I/O blocks a thread for the entire wait (50ms DB call = thread blocked 50ms)
- Async I/O releases the thread during wait; it handles other requests
- At 1000 concurrent requests with 50ms DB latency: sync needs ~1000 threads; async needs far fewer

**When sync is fine:** Console apps, background workers with low concurrency, code that does no I/O.

### Architecture Perspective

Mandate async for all I/O in web APIs. This is a non-negotiable standard in modern .NET architecture — not a performance optimization but a scalability requirement.

---

## Q006–Q010: Quick Fire (Short Answers)

### Q006: What is the difference between `const` and `readonly`?
- `const`: compile-time constant, must be initialized at declaration, implicitly static
- `readonly`: runtime constant, can be set in constructor, instance or static
- **Architect:** Use `const` for true constants (PI, max retry count). Use `readonly` for configuration values set at startup.

### Q007: What is LINQ and when would you avoid it?
- Language Integrated Query — declarative data operations on collections, DB, XML
- **Avoid in:** Hot paths with large collections, real-time systems with strict latency, when profiling shows allocation issues
- **Use in:** Business logic, data transformation, readability-critical code

### Q008: Explain `IDisposable` and when to implement it.
- Releases unmanaged resources (file handles, network connections, unmanaged memory)
- **Architect:** Mandate `using` statements; use `IAsyncDisposable` for async cleanup; DI container handles scoped disposal

### Q009: What is the difference between `IEnumerable` and `IQueryable`?
- `IEnumerable`: in-memory enumeration, executes in .NET
- `IQueryable`: expression trees, executes on provider (EF translates to SQL)
- **Architect:** Never call `IQueryable` methods after materializing to memory; beware of N+1 queries

### Q010: What are extension methods?
- Static methods in static class, first parameter prefixed with `this`
- **Architect:** Useful for cross-cutting concerns (logging, validation); avoid polluting IntelliSense with too many extensions

---

# Part 2: Questions Q011–Q030

> Premium format — full architecture depth.

---

## Q011: is vs as vs Pattern Matching

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Type System |
| **Frequency** | Common |

### Question

Compare `is`, `as`, and pattern matching. When use each?

### Short Answer (30 seconds)

`is` checks type; modern `is` with pattern declares variable. `as` safe cast returns null. Pattern matching (`is Order o`) preferred for clarity and exhaustiveness.

### Detailed Answer (3–5 minutes)

**Modern style:**
```csharp
if (payment is CardPayment card) { ... }
```

**`as`:** legacy nullable cast — `var o = obj as Order; if (o != null)` — more verbose.

**Switch expressions:** exhaustiveness checking with compiler warnings on missing cases — architect mandates for status/state machines in domain.

**Architect:** Prefer pattern matching in code review standards — reduces null reference bugs and improves readability in complex business rules.

### Architecture Perspective

Language feature choice affects maintainability at scale.

### Follow-up Questions

1. **Can pattern matching replace Visitor? — Simple hierarchies yes; double-dispatch Visitor still valid for complex open hierarchies.**
2. **Switch expression exhaustiveness? — Compiler warns on missing enum cases — enable warnings as errors.**

### Common Mistakes in Interviews

- Using `as` when `is` pattern is clearer
- No exhaustiveness on business state switches
- Cast without null check after `as`

---

## Q012: Covariance and Contravariance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Generics |
| **Frequency** | Common |

### Question

Explain covariance and contravariance with examples.

### Short Answer (30 seconds)

Covariance (`out`): return more derived — `IEnumerable<string>` → `IEnumerable<object>`. Contravariance (`in`): accept more base — `Action<object>` → `Action<string>`.

### Detailed Answer (3–5 minutes)

**Design interfaces:** `IProducer<out T>`, `IConsumer<in T>`. Critical when designing shared libraries and LINQ-style APIs.

**IEnumerable<T> covariant** — enables passing `List<string>` where `IEnumerable<object>` expected (read-only producer).

**Action/Func contravariance** — callback parameters.

**Architect:** Misuse causes compile errors in generic APIs — document variance on shared abstractions.

### Architecture Perspective

Generics variance matters for framework design.

### Follow-up Questions

1. **Why not covariant List<T>? — List allows Add — would break type safety.**
2. **Immutable collections variance? — IReadOnlyList covariant for reads.**

### Common Mistakes in Interviews

- Mutable covariant interfaces
- Confusing in/out keywords meaning
- Variance bugs in public SDK design

---

## Q013: delegate vs Func vs Action

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Delegates |
| **Frequency** | Common |

### Question

Difference between delegate, Func, and Action?

### Short Answer (30 seconds)

Delegate is the type concept. `Func<T, TResult>` returns value. `Action<T>` returns void. Both are built-in generic delegate types.

### Detailed Answer (3–5 minutes)

**When custom delegate:** semantic name matters (`EventHandler`, domain-specific).

**Architect preference:** inject interfaces (`IPaymentProcessor`) not `Func<Payment, bool>` in public APIs — clearer contracts, easier testing, stable surface.

**Func acceptable:** internal LINQ-style utilities, local lambdas, fluent configuration.

### Architecture Perspective

API design clarity over delegate brevity.

### Follow-up Questions

1. **Multicast delegates? — `+=` combines — events use this — know removal with `-=`.**
2. **Expression trees vs delegates? — LINQ to SQL uses expressions — different runtime.**

### Common Mistakes in Interviews

- Public API exposes Func everywhere
- Custom delegate for every one-liner
- Confuse delegate with interface role

---

## Q014: Properties vs Fields

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# OOP |
| **Frequency** | Common |

### Question

When use auto-properties vs fields?

### Short Answer (30 seconds)

Public API: always properties — fields should be private. Auto-properties for simple data; full properties when validation/side effects needed.

### Detailed Answer (3–5 minutes)

**Encapsulation:** fields don't version well — adding logic later breaks binary compatibility if public field.

**Performance:** properties compile to methods — negligible; don't use public fields for micro-optimization.

**Architect:** `init` accessors for immutable DTOs; private set for controlled mutation on entities.

### Architecture Perspective

Encapsulation standard enforced in coding guidelines.

### Follow-up Questions

1. **Field-like properties C#? — `{ get; field; }` — rare explicit backing field access.**
2. **Required properties C# 11? — Constructor must set — API contract enforcement.**

### Common Mistakes in Interviews

- Public fields on domain entities
- Property logic in getter with DB call
- Mutable static public fields

---

## Q015: static Classes and Members

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# OOP |
| **Frequency** | Common |

### Question

When are static members appropriate in enterprise .NET?

### Short Answer (30 seconds)

Stateless utilities (`Guid.NewGuid` wrappers), extension method containers, factory registries, well-known singletons (careful).

### Detailed Answer (3–5 minutes)

**Avoid:** static mutable state — untestable, hidden dependencies, thread-safety bugs.

**Architect red flag:** `static HttpClient` or `static DbContext` — use DI singleton lifetime correctly instead.

**Good:** `static` extension methods in `Microsoft.Extensions` style.

### Architecture Perspective

Static state is hidden coupling architects eliminate.

### Follow-up Questions

1. **Static local functions? — Encapsulate helper in method — good practice.**
2. **Generic static classes? — `static class Cache<T>` — per-T static state — thread-safe?**

### Common Mistakes in Interviews

- Static mutable Dictionary cache unbounded
- Static service locator anti-pattern
- Test impossible due to static state

---

## Q016: GC Generations Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | GC |
| **Frequency** | Very Common |

### Question

Explain Gen 0, 1, 2, and LOH. Architect impact?

### Short Answer (30 seconds)

Gen 0: short-lived (temp objects). Gen 1: buffer. Gen 2: long-lived. LOH: ≥85KB objects, collected with Gen 2, compaction limited historically.

### Detailed Answer (3–5 minutes)

**Architect monitors:** `% Time in GC`, Gen 2 collection frequency, LOH size.

**High RPS APIs:** reduce allocations in hot path — pooling, structs, `ArrayPool<byte>`, avoid string concat in loops.

**Server GC:** default for ASP.NET — throughput optimized.

### Architecture Perspective

GC behavior drives latency SLOs.

### Follow-up Questions

1. **POH pinned heap? — Long-lived pinned objects — separate heap .NET 5+.**
2. **GC.TryStartNoGCRegion? — Ultra-low latency short windows — expert use.**

### Common Mistakes in Interviews

- Ignore GC metrics in production
- LOH allocations per request in hot path
- Assume workstation GC for server API

---

## Q017: Finalizers and Why to Avoid

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | GC |
| **Frequency** | Common |

### Question

Why avoid finalizers in .NET application code?

### Short Answer (30 seconds)

Finalizers run on finalizer thread unpredictably, delay GC, promote objects to Gen 2, non-deterministic cleanup.

### Detailed Answer (3–5 minutes)

**Use `IDisposable`/`IAsyncDisposable`/`using`** explicitly.

**SafeDisposable pattern** with `GC.SuppressFinalize` if finalizer exists for native handle safety net.

**Architect:** Code analyzers flag finalizers — ban in application code except interop wrappers.

### Architecture Perspective

Deterministic disposal is architect standard.

### Follow-up Questions

1. **SafeHandle? — Preferred for native resources — finalizer on SafeHandle only.**
2. **Using statement async? — `await using` for IAsyncDisposable.**

### Common Mistakes in Interviews

- Rely on finalizer for SqlConnection cleanup
- Empty finalizer adding GC pressure
- No Dispose pattern on unmanaged wrapper

---

## Q018: Weak References

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Memory |
| **Frequency** | Occasional |

### Question

Use case for WeakReference in application architecture?

### Short Answer (30 seconds)

Large object caches where GC can reclaim under memory pressure — image cache, metadata cache. `ConditionalWeakTable` for attaching data without preventing collection.

### Detailed Answer (3–5 minutes)

**Not** for primary business logic storage — unpredictable disappearance.

**Architect:** prefer explicit cache eviction (LRU, TTL) over weak refs unless memory-sensitive client app.

### Architecture Perspective

Weak refs are specialized — know when not to use.

### Follow-up Questions

1. **WeakReference<T> vs GCHandle? — GCHandle pinned — different purpose.**
2. **MemoryCache with size limit vs weak ref? — Prefer MemoryCache with policies in server apps.**

### Common Mistakes in Interviews

- Business data only in weak reference
- Expect weak ref object always available
- No fallback when weak ref collected

---

## Q019: stackalloc and When to Use

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Common |

### Question

When is `stackalloc` appropriate?

### Short Answer (30 seconds)

Small buffers on stack avoiding heap allocation — parsing, crypto, short-lived span operations. Keep size small (typically <1KB) to avoid stack overflow.

### Detailed Answer (3–5 minutes)

```csharp
Span<byte> buffer = stackalloc byte[256];
```

**With `Span<T>`:** safe scoped lifetime.

**Architect:** profile before micro-optimizing — clarity first unless hot path proven.

### Architecture Perspective

stackalloc is performance tool with bounds.

### Follow-up Questions

1. **stackalloc in loop? — Dangerous — large total stack — allocate outside loop.**
2. **ArrayPool vs stackalloc? — Larger buffers — ArrayPool shared heap.**

### Common Mistakes in Interviews

- Large stackalloc per request
- stackalloc without Span safety
- Premature stackalloc without profiling

---

## Q020: Memory<T> vs Span<T>

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Difference between Memory<T> and Span<T>?

### Short Answer (30 seconds)

`Span<T>` stack-only ref struct — cannot be field on async class. `Memory<T>` heap-friendly — use in async methods and instance fields.

### Detailed Answer (3–5 minutes)

**Rule:** `Span` in synchronous hot path; `Memory` when stored or crossed `await`.

**Architect:** enable `Span` usage in parsing libraries; team training required — ref struct constraints.

### Architecture Perspective

Memory/Span literacy for high-performance .NET.

### Follow-up Questions

1. **ReadOnlySpan<char> for strings? — Zero-copy slicing without Substring allocation.**
2. **MemoryMarshal? — Advanced interop — architect review required.**

### Common Mistakes in Interviews

- Span as class field
- async method using Span parameter incorrectly
- Substring in tight loop instead of span slice

---

## Q021: ConfigureAwait(false) — Still Needed?

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Async |
| **Frequency** | Common |

### Question

Is ConfigureAwait(false) still needed in ASP.NET Core?

### Short Answer (30 seconds)

ASP.NET Core has no `SynchronizationContext` capture issue — `ConfigureAwait(false)` rarely needed in app code. Still recommended in library code for reuse outside ASP.NET.

### Detailed Answer (3–5 minutes)

**Library authors:** use `ConfigureAwait(false)` always.

**Application code:** optional in ASP.NET Core; still valid in UI (WPF/WinForms) and legacy ASP.NET.

**Architect:** coding standard per project type — document in guidelines.

### Architecture Perspective

Async context knowledge shows .NET depth.

### Follow-up Questions

1. **SynchronizationContext what? — Posts continuation to UI thread — ASP.NET Core removed this.**
2. **Library used in UI and ASP.NET? — ConfigureAwait(false) in library mandatory.**

### Common Mistakes in Interviews

- ConfigureAwait(false) everywhere blindly in ASP.NET
- Missing ConfigureAwait in shared library
- async void event handlers without care

---

## Q022: Task vs ValueTask

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Async |
| **Frequency** | Common |

### Question

When use ValueTask instead of Task?

### Short Answer (30 seconds)

ValueTask when operation often completes synchronously — cache hit, buffered read. Reduces Task allocation on hot paths.

### Detailed Answer (3–5 minutes)

**Caution:** ValueTask can only be awaited once — don't cache and reuse multiple times unless converted to Task.

**Architect:** EF Core and ASP.NET internals use ValueTask — application code only after profiling shows Task allocation cost.

### Architecture Perspective

ValueTask is optimization — not default.

### Follow-up Questions

1. **ValueTask.FromResult? — Sync completion path.**
2. **IValueTaskSource? — Advanced pooling — framework level.**

### Common Mistakes in Interviews

- ValueTask everywhere by default
- Double-await ValueTask
- ValueTask without understanding constraints

---

## Q023: CancellationToken Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Async |
| **Frequency** | Common |

### Question

How propagate and honor cancellation in ASP.NET APIs?

### Short Answer (30 seconds)

Accept `CancellationToken` on all async endpoints — ASP.NET passes aborted request token. Pass to EF, HttpClient, `Task.Delay`.

### Detailed Answer (3–5 minutes)

**Cooperative cancellation** — check `token.ThrowIfCancellationRequested()` in long loops.

**Architect:** global timeout policies via middleware; linked tokens for shutdown + request cancel.

**Graceful shutdown:** `IHostApplicationLifetime` linked token stops background work.

### Architecture Perspective

Cancellation is production reliability requirement.

### Follow-up Questions

1. **CancellationToken.None? — Explicit when intentionally ignoring — document why.**
2. **LinkedTokenSource? — Combine shutdown + user cancel.**

### Common Mistakes in Interviews

- Ignore CancellationToken parameter
- Long loop without cancellation check
- Kill thread instead of cooperative cancel

---

## Q024: IAsyncEnumerable Use Cases

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Async |
| **Frequency** | Common |

### Question

When use IAsyncEnumerable<T>?

### Short Answer (30 seconds)

Stream large datasets without loading all into memory — CSV export, DB forward-only read, SignalR streaming, gRPC streaming.

### Detailed Answer (3–5 minutes)

```csharp
await foreach (var row in QueryAsync(token)) { ... }
```

**Architect:** API returns `IAsyncEnumerable` for million-row exports instead of `List<T>`.

### Architecture Perspective

Streaming patterns prevent OOM on large data.

### Follow-up Questions

1. **EF Core AsAsyncEnumerable? — Stream query results.**
2. **Channel vs IAsyncEnumerable? — Producer-consumer — different patterns.**

### Common Mistakes in Interviews

- ToListAsync on million rows
- No cancellation in async enumeration
- Buffer entire export in memory

---

## Q025: Deadlock Scenarios in Async

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Async |
| **Frequency** | Very Common |

### Question

Classic async deadlock in .NET — cause and fix?

### Short Answer (30 seconds)

`.Result` or `.Wait()` on async method blocks thread while async continuation needs same thread (UI/legacy ASP.NET context). Fix: async all the way.

### Detailed Answer (3–5 minutes)

**ASP.NET Core:** less common but thread pool starvation similar symptom from sync-over-async.

**Architect:** analyzers ban `.Result`/`.Wait()` in web projects. Code review gate.

### Architecture Perspective

Deadlock prevention is architect coding standard.

### Follow-up Questions

1. **GetAwaiter().GetResult()? — Same problem — don't.**
2. **Task.Run wrap sync-over-async? — Extra thread — band-aid not fix.**

### Common Mistakes in Interviews

- .Result in controller action
- Blocking async database call
- sync-over-async in library consumed by web app

---

## Q026: Source Generators

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Modern C# |
| **Frequency** | Occasional |

### Question

When adopt source generators in enterprise?

### Short Answer (30 seconds)

Repeatable boilerplate: mapping, DI registration, regex, serialization context. Worth at platform scale with team to maintain generators.

### Detailed Answer (3–5 minutes)

**Examples:** Mapperly, System.Text.Json source gen, compile-time DI scanners.

**Trade-off:** build time, debugging complexity.

**Architect:** approve generator use in platform templates — not one-off per developer.

### Architecture Perspective

Generators are platform decision.

### Follow-up Questions

1. **Incremental generators? — Faster builds large solutions.**
2. **Analyzer vs generator? — Analyzer reports; generator emits code.**

### Common Mistakes in Interviews

- Generator for one mapping class
- No team knowledge to maintain generator
- Build time regression ignored

---

## Q027: required Members (C# 11)

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Modern C# |
| **Frequency** | Common |

### Question

What do `required` properties provide?

### Short Answer (30 seconds)

Compiler enforces object initializer or constructor sets required members — compile-time guarantee non-null initialization.

### Detailed Answer (3–5 minutes)

```csharp
public required string OrderId { get; init; }
```

**With NRT:** stronger API contracts without runtime validation only.

**Architect:** adopt on DTOs and commands in new projects.

### Architecture Perspective

Compile-time contracts reduce runtime validation gaps.

### Follow-up Questions

1. **required vs constructor? — required works with init and object initializers.**
2. **JSON deserialization required? — System.Text.Json respects required.**

### Common Mistakes in Interviews

- Constructor validation only without required
- required on optional fields incorrectly
- Mixing required with nullable confusion

---

## Q028: Primary Constructors Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Modern C# |
| **Frequency** | Common |

### Question

C# 12 primary constructors — benefits and risks?

### Short Answer (30 seconds)

Less boilerplate capturing constructor parameters as fields. Good for small services, records, DI-injected dependencies.

### Detailed Answer (3–5 minutes)

**Risk:** too much logic in primary constructor; entity classes become unclear.

**Architect:** allow for services/DTOs; discourage for rich domain entities with behavior.

### Architecture Perspective

Modern syntax with discipline.

### Follow-up Questions

1. **Primary constructors on records? — Natural fit.**
2. **Validation in primary constructor? — Keep minimal — use factory or validator.**

### Common Mistakes in Interviews

- God constructor logic
- Primary constructor on EF entity with complex rules
- Every class uses primary constructor without review

---

## Q029: Global Usings

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Modern C# |
| **Frequency** | Common |

### Question

Project-wide global usings — architect guidance?

### Short Answer (30 seconds)

`GlobalUsings.cs` for common namespaces (`System`, `Microsoft.Extensions.Logging`) — reduces noise. Don't global-using domain-specific namespaces — hides dependencies.

### Detailed Answer (3–5 minutes)

**Architect:** shared `Directory.Build.props` global usings for org-wide consistency.

**Review:** implicit usings enabled on new SDK projects — understand what's imported.

### Architecture Perspective

Usings affect code clarity and dependency visibility.

### Follow-up Questions

1. **Implicit usings disable? — Explicit control legacy migration.**
2. **Global using alias? — Rare — document if used.**

### Common Mistakes in Interviews

- Global using hides ambiguous types
- Every namespace global — unclear file dependencies
- Conflict between global usings unresolved

---

## Q030: File-Scoped Namespaces

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Modern C# |
| **Frequency** | Common |

### Question

Benefit of file-scoped namespaces?

### Short Answer (30 seconds)

One less indentation level — entire file in namespace. C# 10+ standard for new code.

### Detailed Answer (3–5 minutes)

```csharp
namespace MyApp.Orders;

public class Order { }
```

**Architect:** mandate in `.editorconfig` for new files — consistent style across 50 developers.

### Architecture Perspective

Small syntax improvement compounds at scale.

### Follow-up Questions

1. **Block namespace migration? — Mechanical find-replace safe.**
2. **File-scoped and top-level statements? — Program.cs patterns.**

### Common Mistakes in Interviews

- Mixed styles in same solution
- Block namespace in new files only
- Nested namespace file-scoped incorrectly

---
