# Week 01 — Advanced Interview Q&A (Q071–Q100)

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Native AOT vs JIT for .NET APIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

When recommend Native AOT compilation for .NET 8 services?

### Short Answer (30 seconds)

Native AOT for cold-start sensitive (Functions, edge), constrained memory, or security (no JIT). JIT default for most ASP.NET APIs with reflection-heavy frameworks.

### Detailed Answer (3–5 minutes)

**Native AOT:** faster startup, smaller footprint, no dynamic codegen — limitations: reflection, some EF features, longer compile.

**JIT:** full runtime flexibility, tiered compilation optimizes hot paths.

**Architect:** Profile first — team wanted Go rewrite at 500 RPS — Native AOT + optimization often sufficient without language change.

### Architecture Perspective

Technology choice requires workload-specific evidence.

### Follow-up Questions

1. **Trimming vs AOT? — Trimming reduces size; AOT eliminates JIT — different trade-offs.**
2. **EF Core AOT? — Improving but verify — may need Dapper for hot path.**

### Common Mistakes in Interviews

- AOT everywhere mandate
- Ignore reflection dependency break
- Rewrite language before profiling

---

## Q072: LOH Fragmentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | GC |
| **Frequency** | Common |

### Question

Large Object Heap issues in .NET service — diagnosis and fix?

### Short Answer (30 seconds)

Objects ≥85KB go to LOH, collected with Gen2, not compacted by default (pre-.NET 4.5.1 limitations improved). Large byte arrays, JSON strings cause LOH pressure and fragmentation.

### Detailed Answer (3–5 minutes)

**Diagnose:** `% Time in GC`, LOH size in dotMemory, Gen2 frequency.

**Fix:** pool large buffers (`ArrayPool<byte>`), stream JSON instead of materialize, `POH` pinned object heap for specific scenarios, upgrade runtime for compaction settings.

Payment API serializing 500KB JSON per request — switch to streaming or chunk.

### Architecture Perspective

LOH is common production GC issue architects recognize.

### Follow-up Questions

1. **ArrayPool return? — Don't return arrays still in use — clear sensitive data.**
2. **Gen2 full blocking? — Indicates LOH or long-lived object pressure.**

### Common Mistakes in Interviews

- ToString on huge collections in logs
- Deserialize entire blob to string
- Ignore Gen2 GC alerts

---

## Q073: ConfigureAwait and Library Code

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |
| **Frequency** | Occasional |

### Question

Should library authors use ConfigureAwait(false)?

### Short Answer (30 seconds)

Library code: yes — avoid capturing caller sync context unnecessarily. Application code (ASP.NET): generally no — needs HttpContext on continuation after await.

### Detailed Answer (3–5 minutes)

ASP.NET Core doesn't have legacy sync context capture issue like old ASP.NET — but library code still benefits from `ConfigureAwait(false)` for reuse in UI, legacy contexts.

Architect coding standard: analyzers enforce in shared libraries.

### Architecture Perspective

Async context rules differ library vs app — architects document standards.

### Follow-up Questions

1. **Task.Run to offload CPU? — Extra thread pool hop — only for CPU-bound blocking code.**
2. **async void? — Only event handlers — never in services.**

### Common Mistakes in Interviews

- ConfigureAwait(false) in every ASP.NET line blindly
- async void service methods
- Blocking .Result in library

---

## Q074: Assembly Load Context and Plugins

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Runtime |
| **Frequency** | Rare |

### Question

Design plugin architecture in .NET without memory leaks?

### Short Answer (30 seconds)

`AssemblyLoadContext` collectible contexts unload plugin assemblies. Default ALC loads permanently — plugin reload leaks.

### Detailed Answer (3–5 minutes)

Create collectible `PluginLoadContext`, load plugin DLL, execute, unload context when done.

**Architect:** Plugin systems need isolation — also security sandbox — run untrusted plugins out-of-process.

### Architecture Perspective

Plugin architecture is advanced .NET architect topic.

### Follow-up Questions

1. **Unload limitations? — References from default context prevent unload — strict boundary.**
2. **Roslyn scripting? — Separate ALC per script execution.**

### Common Mistakes in Interviews

- Load plugins in default context
- No isolation for third-party code
- Assume unload always works

---

## Q075: Distributed Caching Stampede

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Common |

### Question

Cache expires on hot product — 10K requests miss simultaneously?

### Short Answer (30 seconds)

Cache stampede — use lock per key (mutex), early probabilistic refresh, request coalescing (`HybridCache` in .NET 9), never expire all keys same second.

### Detailed Answer (3–5 minutes)

**Pattern:** first miss acquires lock, others wait or serve stale briefly (`stale-while-revalidate`).

**Redis:** `SETNX` lock key, single flight rebuild.

### Architecture Perspective

Stampede prevention is architect-level caching knowledge.

### Follow-up Questions

1. **Thundering herd vs stampede? — Same problem — coordinated miss.**
2. **Negative caching? — Cache 'not found' briefly — prevent DB hammer.**

### Common Mistakes in Interviews

- Identical TTL on all keys
- No lock on cache miss
- Cache bypass floods DB

---

## Q076: Source Generator Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Modern C# |
| **Frequency** | Occasional |

### Question

When adopt C# source generators in enterprise platform?

### Short Answer (30 seconds)

Boilerplate reduction: mapping, DI registration, API clients, validators. Worth when pattern repeats 50+ times and team can maintain generator.

### Detailed Answer (3–5 minutes)

Examples: Mapperly for DTO mapping, compile-time regex, System.Text.Json source context.

**Risk:** debugging harder, build time increase, team skill requirement.

Architect approves generator use in platform template — not ad-hoc per project.

### Architecture Perspective

Generators are platform decision — consistency vs complexity.

### Follow-up Questions

1. **Analyzer vs generator? — Analyzer flags issues; generator emits code.**
2. **Incremental generator? — Faster builds in large solutions.**

### Common Mistakes in Interviews

- Generator for one-off mapping
- No documentation for generated code consumers
- Build time regression ignored

---

## Q077: Microservices vs Modular Monolith ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Write ADR: stay modular monolith or split to microservices?

### Short Answer (30 seconds)

Document context: team size 8, 2 deploys/week pain, no K8s ops. Recommendation: modular monolith + strangler for one hot module. Revisit when team >15 or deploy daily required.

### Detailed Answer (3–5 minutes)

**ADR sections:** Status, context, decision, consequences, alternatives rejected.

Rejected: full microservices — ops cost exceeds benefit at current scale.

### Architecture Perspective

ADR articulation is architect core skill.

### Follow-up Questions

1. **When revisit ADR? — Quarterly or on trigger metrics.**
2. **Who approves? — Architecture review board or tech lead + EM.**

### Common Mistakes in Interviews

- ADR without rejected alternatives
- Decision without measurable triggers
- ADRs never updated

---

## Q078: Performance Culture and Budgets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Establish performance culture in .NET organization?

### Short Answer (30 seconds)

Performance budgets in CI (k6/Gatling gate), mandatory profiling for P0 features, `% Time in GC` and p99 dashboards, blameless postmortems on regressions.

### Detailed Answer (3–5 minutes)

Architect defines non-negotiables: no PR merging if critical path +20% latency in benchmark.

Budget example: search API p99 < 200ms at 1K RPS.

### Architecture Perspective

Performance is ongoing architecture governance.

### Follow-up Questions

1. **Regression test data? — Record baseline on main branch.**
2. **Production profiling? — dotTrace continuous profiler sampling — low overhead.**

### Common Mistakes in Interviews

- Optimize without measurement
- Performance testing only before release
- No production latency SLO

---

## Q079: Security in .NET API Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Architect security checklist for new ASP.NET Core API?

### Short Answer (30 seconds)

AuthN at edge, authZ policies, input validation, rate limiting, secrets in Key Vault, HTTPS only, security headers, dependency scanning, audit logs.

### Detailed Answer (3–5 minutes)

OWASP API Top 10 mapped to controls. Pen test before public launch.

Never expose internal exception details — ProblemDetails with trace ID only.

### Architecture Perspective

Security architecture is part of API design — not separate phase.

### Follow-up Questions

1. **BOLA/IDOR? — Authorize every resource access by owner — `{userId}/orders/{id}`.**
2. **CORS misconfiguration? — Explicit origins — not `*` with credentials.**

### Common Mistakes in Interviews

- JWT in localStorage
- Missing authZ on object access
- Secrets in appsettings.json

---

## Q080: Technical Debt Prioritization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Common |

### Question

Prioritize technical debt vs features — framework?

### Short Answer (30 seconds)

Classify debt: interest rate (cost of delay), principal (fix cost), blast radius. High interest + small principal → next sprint. Low interest → backlog.

### Detailed Answer (3–5 minutes)

Quantify: 'missing index costs $4K/month compute' beats 'code smells.'

20% capacity rule for platform/debt — negotiate with product.

### Architecture Perspective

Architects quantify debt in business terms.

### Follow-up Questions

1. **Strangler reduces debt incrementally? — Preferred over rewrite.**
2. **Debt register? — Visible to leadership — not hidden shame.**

### Common Mistakes in Interviews

- All debt equal priority
- Rewrite without business case
- No metrics on debt impact

---

## Q081: Reflection Cost and Alternatives

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Runtime |
| **Frequency** | Common |

### Question

When is reflection acceptable in production .NET, and what alternatives should architects mandate?

### Short Answer (30 seconds)

Reflection is fine at startup (DI registration, mapping config) but costly in hot paths — metadata lookup, Activator.CreateInstance, and property iteration allocate and bypass JIT inlining. Prefer compile-time solutions: source generators, delegates, or expression trees compiled once.

### Detailed Answer (3–5 minutes)

**Cost profile:**
- `typeof(T).GetProperties()` — cache results statically
- `Activator.CreateInstance` — 10–100× slower than `new T()`
- JSON serializers using reflection — switch to `System.Text.Json` source generators

**Alternatives:**
| Pattern | Use Case |
|---------|----------|
| Source generators | DTO mapping, serializers, DI registration |
| Compiled delegates | Dynamic property access after one-time compile |
| `IServiceProvider` keyed services | Plugin resolution without reflection scan |
| Interface + factory registry | Known types at compile time |

**Architect rule:** Reflection allowed in composition root and one-time startup; banned in request path without benchmark proof.

**Native AOT note:** Reflection trimmed — plan alternatives before AOT migration.

### Architecture Perspective

Reflection is a platform tax — architects distinguish bootstrap vs hot-path usage.

### Follow-up Questions

1. **Reflection.Emit vs expression trees? — Emit for dynamic assemblies; expressions for single-delegate compile.**
2. **HybridCache reflection? — .NET 9 caches reflection metadata internally — still avoid per-request.**

### Common Mistakes in Interviews

- GetProperties() in every request handler
- Reflection-based ORM mapping in microsecond SLA path
- No static cache for reflection metadata

---

## Q082: Expression Trees Use Cases

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Advanced C# |
| **Frequency** | Occasional |

### Question

What are expression trees in .NET and when should architects use them?

### Short Answer (30 seconds)

Expression trees represent code as data (`Expression<Func<T,bool>>`) — compiled once to delegates or translated to SQL (EF Core), OData filters, or dynamic rules engines. Use when you need inspectable, composable predicates — not for simple lambdas.

### Detailed Answer (3–5 minutes)

**Use cases:**
1. **EF Core** — `Where(x => x.Age > 18)` translated to SQL via expression visitor
2. **Dynamic filtering** — API `?sort=name&filter=status eq active` → composable `IQueryable`
3. **Rule engines** — business rules stored as expressions, compiled at load
4. **Specification pattern** — `ISpecification<T>.Criteria` as expression

```csharp
Expression<Func<Order, bool>> pred = o => o.Total > 100;
var compiled = pred.Compile(); // once
```

**Avoid:** Compiling same expression per request — cache `Func<T,bool>`. Don't build expression trees manually unless framework requires it — use `PredicateBuilder` libraries.

**Architect:** Expression trees bridge type-safe C# and external DSLs — document who owns translation (EF vs custom).

### Architecture Perspective

Expression trees power IQueryable — architects know when compile-once pays off.

### Follow-up Questions

1. **Expression vs delegate? — Delegate executes; expression describes — EF needs description.**
2. **Visitor pattern complexity? — Custom translators need test suite — EF does heavy lifting.**

### Common Mistakes in Interviews

- Compile() inside request loop
- Manual expression building for simple if/else
- Expression tree for logging only

---

## Q083: Channels vs BlockingCollection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

Compare `System.Threading.Channels` and `BlockingCollection<T>` for producer-consumer in .NET.

### Short Answer (30 seconds)

`Channels` (async-first, backpressure, bounded/unbounded, `IAsyncEnumerable`) is the modern choice. `BlockingCollection` blocks thread pool threads — legacy, avoid in ASP.NET request paths.

### Detailed Answer (3–5 minutes)

| Feature | Channels | BlockingCollection |
|---------|----------|-------------------|
| Async | `await reader.ReadAsync()` | Blocking `Take()` |
| Backpressure | Bounded capacity + `Wait`/`Drop` | Bounded with locks |
| Thread use | Non-blocking async | Blocks threads |
| Integration | `BackgroundService`, pipelines | TPL Dataflow predecessor |

**Architect pattern:**
```csharp
var channel = Channel.CreateBounded<WorkItem>(100);
// Producer: await channel.Writer.WriteAsync(item)
// Consumer: await foreach (var item in channel.Reader.ReadAllAsync(ct))
```

**Use BlockingCollection only:** Legacy integration, existing TPL code not yet migrated.

**Production:** Bounded channel with `FullMode.Wait` prevents OOM when consumer slower than producer. Multiple readers via `Channel.CreateUnbounded` + single consumer `BackgroundService`.

### Architecture Perspective

Channels align with async ASP.NET — BlockingCollection starves thread pool under load.

### Follow-up Questions

1. **Channel vs ConcurrentQueue? — Channel adds backpressure and async wait — queue alone spins.**
2. **System.Threading.Channels unbounded risk? — Memory growth if consumer dies — prefer bounded.**

### Common Mistakes in Interviews

- BlockingCollection.Take() in async API
- Unbounded channel without monitoring
- Multiple writers without TryWrite handling

---

## Q084: Immutable Collections Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Collections |
| **Frequency** | Occasional |

### Question

When architect `System.Collections.Immutable` in enterprise .NET services?

### Short Answer (30 seconds)

Immutable collections (`ImmutableList<T>`, `ImmutableDictionary<K,V>`) provide thread-safe snapshots without locks — ideal for shared config, lookup tables, and functional pipelines. Mutations return new instances — pay copy cost.

### Detailed Answer (3–5 minutes)

**Architect use cases:**
- **Cached reference data** — product catalog snapshot refreshed hourly — readers never see partial update
- **Options/config snapshots** — `IOptionsMonitor` callback builds new immutable graph
- **Domain value objects** — internal immutable state, exposed as `IReadOnlyList`
- **Concurrent read-heavy maps** — `ImmutableDictionary` + atomic `Interlocked.Exchange` reference swap

**Pattern:**
```csharp
private volatile ImmutableDictionary<string, Sku> _catalog = ImmutableDictionary<string, Sku>.Empty;
void Refresh(IEnumerable<Sku> skus) =>
    Interlocked.Exchange(ref _catalog, skus.ToImmutableDictionary(s => s.Code));
```

**Avoid:** Per-request mutations — use mutable collections in local scope. Large frequent updates — copy cost dominates.

**NuGet:** `System.Collections.Immutable` — also used by Roslyn, MSBuild.

### Architecture Perspective

Immutable snapshots eliminate reader locks — architects use for shared read-mostly state.

### Follow-up Questions

1. **Frozen collections .NET 8? — `FrozenDictionary` faster read — immutable after build.**
2. **Persistent immutable vs deep copy? — Structural sharing — not full copy on every Add.**

### Common Mistakes in Interviews

- ImmutableList per-request Add in loop
- Mutable static dictionary without sync
- Immutable for write-heavy cache

---

## Q085: ConcurrentDictionary Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

Production patterns for `ConcurrentDictionary` beyond basic Get/Add?

### Short Answer (30 seconds)

`GetOrAdd`, `AddOrUpdate`, and `GetOrAdd` with lazy factory prevent duplicate expensive initialization. Avoid locking entire dictionary — use per-key patterns and `ConcurrentDictionary` for cache, not primary data store.

### Detailed Answer (3–5 minutes)

**Patterns:**
1. **Lazy singleton per key** — `GetOrAdd(key, _ => ExpensiveCreate(key))` — factory may run twice rarely; OK for idempotent
2. **Atomic counter** — `AddOrUpdate(key, 1, (_, count) => count + 1)`
3. **Striped locking** — combine with `SemaphoreSlim` per key for non-atomic multi-step updates
4. **Cache with TTL** — store `(Value, Expiry)` tuple; background sweep or lazy expiry check

**Anti-patterns:**
- `TryGetValue` then `TryAdd` race — use `GetOrAdd` atomic
- Holding lock while awaiting — blocks other keys
- Million keys unbounded — memory leak; use IMemoryCache with size limits

**Architect:** In-memory `ConcurrentDictionary` cache is process-local — document cache invalidation across instances (Redis pub/sub, message).

### Architecture Perspective

ConcurrentDictionary is in-process concurrent map — not distributed cache.

### Follow-up Questions

1. **GetOrAdd factory runs twice? — Documented race — use Lazy<T> inside value if costly.**
2. **ConcurrentDictionary vs IMemoryCache? — IMemoryCache adds eviction, size limits, DI integration.**

### Common Mistakes in Interviews

- TryGetValue + TryAdd race condition
- Unbounded cache keys in long-running service
- Async work inside GetOrAdd factory blocking threads

---

## Q086: Thread Safety and Lock-Free Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Concurrency |
| **Frequency** | Occasional |

### Question

Explain lock-free patterns available in .NET and when architects choose them over locks?

### Short Answer (30 seconds)

Lock-free uses atomic operations (`Interlocked`, `Volatile`, `MemoryBarrier`) to avoid mutex contention. Use for simple counters, reference swaps, and lock-free queues at high contention — not replacement for all synchronization.

### Detailed Answer (3–5 minutes)

**Building blocks:**
- `Interlocked.Increment`, `CompareExchange` — atomic counter, CAS loops
- `volatile` / `Volatile.Read/Write` — visibility guarantees
- `ImmutableInterlocked` — atomic immutable collection swap
- `System.Threading.Channels` — internally efficient queues

**When lock-free:**
- Metrics counters at millions ops/sec
- Single-writer reference swap (config reload)
- `ConcurrentQueue` / Channels for producer-consumer

**When locks (`lock`, `SemaphoreSlim`):**
- Multi-step invariants across fields
- Complex business rules
- Async code — `SemaphoreSlim`, not `lock` with await

**Architect caution:** Lock-free CAS retry loops can starve under extreme contention — benchmark. Prefer `ConcurrentDictionary` and BCL abstractions over hand-rolled lock-free.

### Architecture Perspective

Lock-free trades complexity for latency — architects default to BCL concurrent types first.

### Follow-up Questions

1. **SpinLock vs lock? — SpinLock for micro-short critical sections only — can waste CPU.**
2. **Memory model on ARM? — Volatile/Interlocked required — don't rely on accidental ordering.**

### Common Mistakes in Interviews

- Hand-rolled lock-free linked list
- lock {} around await
- False sharing on hot counters — pad cache lines in extreme HPC

---

## Q087: Parallel.For Pitfalls

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Parallelism |
| **Frequency** | Common |

### Question

What are production pitfalls of `Parallel.For` and `Parallel.ForEach` in .NET?

### Short Answer (30 seconds)

Parallel.For uses thread pool threads — wrong for I/O-bound work, dangerous with thread-affine APIs (DbContext, HttpContext), and can cause oversubscription when combined with async. Use for CPU-bound, partitionable, thread-safe workloads only.

### Detailed Answer (3–5 minutes)

**Pitfalls:**
1. **I/O inside loop** — blocks thread pool → starvation — use `Task.WhenAll` + async
2. **Non-thread-safe collections** — `List<T>.Add` races — use `ConcurrentBag` or lock
3. **DbContext per iteration** — not thread-safe — one context per thread via `Parallel.For` local init
4. **ASP.NET request** — Parallel.For in controller doubles thread pressure with Kestrel
5. **Small collections** — parallel overhead exceeds benefit — threshold ~1000+ CPU-heavy items
6. **Exception handling** — `AggregateException` — handle `LoopResult`

**Better alternatives:**
- CPU batch: `Parallel.For` with `MaxDegreeOfParallelism`
- I/O batch: `await Task.WhenAll(items.Select(ProcessAsync))`
- Data pipeline: `Channel` + `BackgroundService`

**Architect:** Ban Parallel.For in web request path by analyzer; restrict to batch jobs, image processing, compute workers.

### Architecture Perspective

Parallel.For is for CPU parallelism — not async I/O replacement.

### Follow-up Questions

1. **Partitioner.Create? — Custom chunk sizing for uneven work per item.**
2. **PLINQ vs Parallel.For? — PLINQ declarative; similar thread pool — same pitfalls.**

### Common Mistakes in Interviews

- Parallel.For with async lambda — doesn't exist — common mistake with .Result
- Shared DbContext across parallel iterations
- Parallel.For on 10-item collection

---

## Q088: PLINQ When to Use

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Parallelism |
| **Frequency** | Occasional |

### Question

When should architects recommend PLINQ (`AsParallel()`) in production .NET?

### Short Answer (30 seconds)

PLINQ parallelizes LINQ to Objects in-memory queries — use for CPU-bound filtering/aggregation on large in-memory collections, offline batch processing. Avoid on IQueryable (not EF-translatable), small collections, or order-dependent operations without `AsOrdered()`.

### Detailed Answer (3–5 minutes)

**Good fits:**
- In-memory analytics on 100K+ records loaded once
- Image/file batch transformation
- Complex CPU aggregation where `Parallel.For` less readable

**Bad fits:**
- `dbContext.Orders.AsParallel()` — doesn't parallelize SQL — pulls all to memory
- Latency-sensitive API request path
- Side-effecting `Select` (DB writes per item)
- Collections < few thousand simple ops

```csharp
var result = records.AsParallel()
    .WithDegreeOfParallelism(Environment.ProcessorCount)
    .Where(r => ExpensiveCpuCheck(r))
    .ToList();
```

**Architect:** PLINQ is batch/offline tool — document in platform guidance. Prefer explicit `Parallel.For` when degree of parallelism must be tightly controlled.

### Architecture Perspective

PLINQ parallelizes in-memory LINQ — architects block EF + AsParallel anti-pattern.

### Follow-up Questions

1. **AsOrdered cost? — Preserves order with coordination overhead — only when required.**
2. **WithExecutionMode ForceParallelism? — Debug only — not production.**

### Common Mistakes in Interviews

- AsParallel on IQueryable EF query
- PLINQ with non-thread-safe side effects
- Default parallelism on machine with 64 cores — cap for shared hosts

---

## Q089: MemoryPool and ArrayPool

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Architect guidance for `MemoryPool<T>` and `ArrayPool<T>` in high-throughput .NET APIs?

### Short Answer (30 seconds)

ArrayPool rents/returns byte buffers — eliminates LOH allocation for transient buffers. MemoryPool rents `IMemoryOwner<T>` — structured memory for pipelines (Kestrel, Pipelines). Always return buffers; clear sensitive data; never return buffer still in use.

### Detailed Answer (3–5 minutes)

**ArrayPool<byte>.Shared:**
```csharp
var buffer = ArrayPool<byte>.Shared.Rent(minSize);
try { /* use buffer.AsSpan(0, actualLength) */ }
finally { ArrayPool<byte>.Shared.Return(buffer, clearArray: true); }
```

**MemoryPool:** Used internally by `PipeReader`/`PipeWriter` — custom protocol parsers rent from `MemoryPool<byte>.Shared`.

**Architect rules:**
- Pool buffers >1KB used frequently in hot path
- `clearArray: true` for security-sensitive data
- Don't pool tiny arrays — overhead exceeds benefit
- Document max rent size — unbounded rent breaks pool buckets

**LOH connection:** Arrays >85KB go to LOH — pooling prevents Gen2 pressure.

**System.Text.Json:** `JsonSerializer.SerializeToUtf8Bytes` allocates — use `IBufferWriter<byte>` + ArrayPool for zero-copy paths.

### Architecture Perspective

Pooling is architect-level GC strategy — mandatory review for serialization-heavy APIs.

### Follow-up Questions

1. **ArrayPool vs stackalloc? — stackalloc for small fixed spans <1KB sync-only.**
2. **LOH threshold 85KB? — Rent size may exceed needed — use exact length slice.**

### Common Mistakes in Interviews

- Forget Return() — pool exhaustion
- Return buffer while async IO still reading
- Pool every 32-byte allocation

---

## Q090: Utf8JsonReader Streaming

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Serialization |
| **Frequency** | Common |

### Question

How architect high-performance JSON parsing with `Utf8JsonReader`?

### Short Answer (30 seconds)

`Utf8JsonReader` is forward-only, low-allocation UTF-8 JSON reader — parse streams without deserializing entire document to `JsonDocument` or string. Use for large payloads, selective field extraction, and hot paths.

### Detailed Answer (3–5 minutes)

**Patterns:**
```csharp
var reader = new Utf8JsonReader(utf8Bytes);
while (reader.Read())
{
    if (reader.TokenType == JsonTokenType.PropertyName &&
        reader.ValueTextEquals("orderId"))
    {
        reader.Read();
        var id = reader.GetInt64();
    }
}
```

**Architect use cases:**
- Webhook ingestion — extract 3 fields from 5MB JSON
- Log/event pipeline — stream from `PipeReader`
- API gateway — validate structure without full model bind

**vs alternatives:**
| Approach | When |
|----------|------|
| `JsonSerializer.Deserialize<T>` | Full object mapping, moderate size |
| `JsonDocument` | Random access, moderate memory |
| `Utf8JsonReader` | Streaming, selective, max perf |
| Source generator | Known schema, compile-time |

**Caveat:** Manual parsing brittle — wrap in tested extractor class; use source generator for known DTOs when possible.

### Architecture Perspective

Utf8JsonReader is architect tool for allocation-sensitive JSON pipelines.

### Follow-up Questions

1. **JsonReaderException handling? — Partial reads from stream — buffer incomplete JSON.**
2. **PipeReader integration? — Kestrel request body — avoid ToArray() materialize.**

### Common Mistakes in Interviews

- ReadAsStringAsync entire 50MB body
- Hand-rolled parser without tests per schema version
- Utf8JsonReader on UTF-16 string — convert allocates

---

## Q091: HttpContext Accessor Anti-Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ASP.NET Core |
| **Frequency** | Very Common |

### Question

Why is `IHttpContextAccessor` considered an anti-pattern in domain and application layers?

### Short Answer (30 seconds)

`IHttpContextAccessor` hides implicit dependency on HTTP request — untestable domain logic, service locator smell, breaks in background workers, and thread-unsafe if cached in singleton. Pass `UserId`, `CorrelationId`, `CancellationToken` explicitly.

### Detailed Answer (3–5 minutes)

**Problems:**
- Domain service calls `httpContextAccessor.HttpContext.User` — can't unit test without mock HTTP
- Singleton caching accessor — stale/wrong context
- MediatR handler uses accessor — obscures real dependencies in signature

**Architect-approved pattern:**
```csharp
// Middleware extracts context → scoped IRequestContext
public interface IRequestContext
{
    string UserId { get; }
    string CorrelationId { get; }
}
// Handler: CreateOrderHandler(IRequestContext ctx) — explicit
```

**Legitimate accessor use:** Infrastructure only — logging enrichers, legacy library bridge, framework middleware.

**Enforcement:** ArchUnitNet test — domain project must not reference `Microsoft.AspNetCore.Http`.

### Architecture Perspective

Explicit context injection preserves clean architecture boundaries.

### Follow-up Questions

1. **AsyncLocal for context? — Same hidden dependency problem — prefer explicit scoped service.**
2. **Minimal APIs access HttpContext param? — OK at edge — map to command before domain.**

### Common Mistakes in Interviews

- IHttpContextAccessor in domain entity
- Singleton service storing HttpContext field
- Accessor in MediatR behavior without interface abstraction

---

## Q092: Options Validation IValidateOptions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Configuration |
| **Frequency** | Common |

### Question

How implement robust options validation with `IValidateOptions<T>` and `ValidateOnStart`?

### Short Answer (30 seconds)

Bind configuration to `IOptions<T>`, validate with `IValidateOptions<T>` or data annotations, call `ValidateOnStart()` so misconfiguration fails at boot — not first request.

### Detailed Answer (3–5 minutes)

**Implementation:**
```csharp
services.AddOptions<PaymentOptions>()
    .BindConfiguration("Payment")
    .ValidateDataAnnotations()
    .Validate(o => o.TimeoutSeconds > 0, "Timeout must be positive")
    .ValidateOnStart();

public class PaymentOptionsValidator : IValidateOptions<PaymentOptions>
{
    public ValidateOptionsResult Validate(string name, PaymentOptions options)
    {
        if (string.IsNullOrEmpty(options.ApiKey))
            return ValidateOptionsResult.Fail("ApiKey required");
        if (!Uri.TryCreate(options.BaseUrl, UriKind.Absolute, out _))
            return ValidateOptionsResult.Fail("Invalid BaseUrl");
        return ValidateOptionsResult.Success;
    }
}
```

**Architect:**
- Cross-field validation in `IValidateOptions` — URL + API key consistency
- Secrets validated present (not empty) — actual values from Key Vault
- Separate options per bounded context — not one `AppSettings` god object
- Health check can re-validate critical options if using `IOptionsMonitor`

### Architecture Perspective

Fail-fast configuration prevents production runtime exceptions on missing settings.

### Follow-up Questions

1. **IValidateOptions vs ValidateDataAnnotations? — Combine — annotations for simple, custom for cross-field.**
2. **Options in library vs app? — Library registers `AddOptions<T>` extension with validator.**

### Common Mistakes in Interviews

- No ValidateOnStart — first request crashes
- Catch validation errors and use defaults
- 500-line monolithic Options class

---

## Q093: Health Check UI Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Should architects expose Health Checks UI in production ASP.NET Core?

### Short Answer (30 seconds)

Expose `/health/live` and `/health/ready` for orchestrators (K8s probes) — minimal JSON, no dependency details publicly. Health Checks UI (`/health-ui`) is dev/staging only — production leaks dependency topology and aids attackers.

### Detailed Answer (3–5 minutes)

**Production pattern:**
```csharp
app.MapHealthChecks("/health/live", new() { Predicate = _ => false }); // process up
app.MapHealthChecks("/health/ready", new() { Predicate = check => check.Tags.Contains("ready") });
```

**Security:**
- Public ready endpoint returns `Healthy`/`Unhealthy` only — not SQL connection strings in response
- Detailed checks (`/health/detail`) — internal network + auth or metrics backend only
- AspNetCore.HealthChecks.UI — disable in prod or protect with OAuth + IP allowlist

**Architect:** Align probes — liveness (restart pod) vs readiness (remove from LB). Dependency checks (SQL, Redis) on readiness only.

**Azure:** App Service health check path = `/health/ready`. Front Door origin probe same.

### Architecture Perspective

Health endpoints are attack surface — architects separate public minimal vs internal detailed.

### Follow-up Questions

1. **Health check caching? — `Microsoft.Extensions.Diagnostics.HealthChecks` timeout per check — tune.**
2. **Tag-based filtering? — `ready` vs `live` tags — K8s best practice.**

### Common Mistakes in Interviews

- Health Checks UI public on internet
- Return exception stack in health response
- Liveness probe checks SQL — kills pod on DB blip

---

## Q094: API Versioning Header vs URL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Very Common |

### Question

Compare URL path, header, and query string API versioning for enterprise .NET APIs.

### Short Answer (30 seconds)

URL path (`/v2/orders`) — most visible, cache-friendly, easy routing. Header (`api-version: 2.0`) — clean URLs, harder to test in browser. Query (`?api-version=2.0`) — optional versioning, poor caching. Architects pick one standard per platform.

### Detailed Answer (3–5 minutes)

| Strategy | Pros | Cons |
|----------|------|------|
| URL path | Explicit, gateway routing, docs clarity | URL proliferation |
| Header | Clean URLs, REST purist | Proxy config, curl friction |
| Media type | Hypermedia purist | Complex, rare in practice |
| Query string | Easy opt-in | CDN cache key mess |

**ASP.NET Core:** `Asp.Versioning.Http` supports all — configure default version + sunset headers.

**Architect policy:**
- Public mobile/ partner APIs — URL versioning + deprecation `Sunset` header
- Internal east-west — header or no versioning with simultaneous deploy
- Document minimum supported version — 2 major versions max

**Gateway:** APIM/YARP route `/v1/*` vs `/v2/*` to different backends during strangler.

### Architecture Perspective

Versioning strategy is long-term consumer contract — architects document deprecation timeline.

### Follow-up Questions

1. **Sunset header RFC? — Communicate version retirement date to API consumers.**
2. **Default version assume 1.0? — Unversioned calls route to oldest — explicit policy needed.**

### Common Mistakes in Interviews

- Three versioning strategies in same org
- Breaking change without version bump
- Version in body JSON — hardest to route

---

## Q095: ProblemDetails Exception Mapping

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Very Common |

### Question

How architect consistent exception-to-`ProblemDetails` mapping in ASP.NET Core APIs?

### Short Answer (30 seconds)

Use `IExceptionHandler` (.NET 8+) or middleware with typed exception hierarchy — map `NotFoundException` → 404, `ValidationException` → 400, unknown → 500 without leaking internals. Include `traceId`, `type` URI, RFC 7807 fields.

### Detailed Answer (3–5 minutes)

**Architecture:**
```csharp
public class GlobalExceptionHandler : IExceptionHandler
{
    public async ValueTask<bool> TryHandleAsync(
        HttpContext ctx, Exception ex, CancellationToken ct)
    {
        var (status, title) = ex switch
        {
            NotFoundException => (404, "Not Found"),
            FluentValidation.ValidationException => (400, "Validation Error"),
            ConflictException => (409, "Conflict"),
            _ => (500, "Internal Server Error")
        };
        var problem = new ProblemDetails
        {
            Status = status, Title = title,
            Type = $"https://api.example.com/errors/{status}",
            Extensions = { ["traceId"] = Activity.Current?.Id }
        };
        if (ex is ValidationException ve)
            problem.Extensions["errors"] = ve.Errors;
        await Results.Problem(problem).ExecuteAsync(ctx);
        return true;
    }
}
```

**Rules:**
- 500 responses — generic message; log full exception server-side
- Domain exceptions carry error codes — not SQL messages
- Consistent across all services — shared `ProblemDetails` library

### Architecture Perspective

ProblemDetails is enterprise API error contract — architects enforce via shared middleware package.

### Follow-up Questions

1. **ValidationProblemDetails? — ModelState + FluentValidation unified shape.**
2. **Exception middleware order? — Before endpoints — catch handler exceptions too.**

### Common Mistakes in Interviews

- return ex.Message on 500
- Different error JSON shape per service
- Stack trace in ProblemDetails extensions public

---

## Q096: MediatR Pipeline Behaviors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

Design MediatR pipeline behaviors for cross-cutting concerns in Clean Architecture.

### Short Answer (30 seconds)

Pipeline behaviors wrap handlers — order: logging → validation → authorization → transaction → handler. Register open generic `IPipelineBehavior<TRequest,TResponse>` in DI.

### Detailed Answer (3–5 minutes)

**Standard behaviors:**
1. **ValidationBehavior** — FluentValidation all `IValidator<TRequest>`
2. **LoggingBehavior** — request name, duration, user
3. **TransactionBehavior** — `IUnitOfWork.Commit` for commands only
4. **AuthorizationBehavior** — policy check on request attributes
5. **CachingBehavior** — queries with `ICacheableQuery` marker

```csharp
public class ValidationBehavior<TReq, TRes> : IPipelineBehavior<TReq, TRes>
    where TReq : IRequest<TRes>
{
    public async Task<TRes> Handle(TReq req, RequestHandlerDelegate<TRes> next, CancellationToken ct)
    {
        await _validator.ValidateAndThrowAsync(req, ct);
        return await next();
    }
}
```

**Architect:** Behavior order documented in platform README. Avoid 10 behaviors — performance and debuggability suffer. Queries skip transaction behavior via marker interface.

### Architecture Perspective

MediatR pipeline is enterprise cross-cutting backbone — architects standardize behavior set.

### Follow-up Questions

1. **Behavior ordering? — Registration order in DI — first registered outermost.**
2. **MediatR vs decorator? — Behaviors are chain; decorators per handler — choose consistency.**

### Common Mistakes in Interviews

- Transaction on query handler
- Authorization only in controller — bypassed by internal Send()
- Behavior with sync blocking I/O

---

## Q097: EF Core Interceptors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Access |
| **Frequency** | Common |

### Question

When use EF Core interceptors and what cross-cutting concerns do they solve?

### Short Answer (30 seconds)

Interceptors hook `DbCommand`, `SaveChanges`, connection events — implement auditing, soft delete, multi-tenancy filters, slow query logging, and command tagging without repository boilerplate.

### Detailed Answer (3–5 minutes)

**Common interceptors:**
- **Auditing** — `SaveChangesInterceptor` sets `CreatedAt`, `ModifiedBy` on `EntityState.Added/Modified`
- **Soft delete** — rewrite `Delete` to `Update` with `IsDeleted` flag
- **Tenant filter** — `QueryExpressionInterceptor` adds `Where(e => e.TenantId == current)` globally
- **Tagging** — `CommandInterceptor` appends `-- Tag: OrderService.GetById` for SQL insights
- **Retry** — connection resiliency (built-in) + custom for transient detection

```csharp
options.AddInterceptors(new AuditingInterceptor(currentUser));
```

**Architect cautions:**
- Global query filters + multi-tenancy — test bypass for admin reports
- Interceptor order matters — document registration
- Don't hide business rules that belong in domain — auditing OK, pricing rules not

### Architecture Perspective

Interceptors centralize persistence cross-cutting — architects govern tenant and audit policies.

### Follow-up Questions

1. **IDbCommandInterceptor vs SaveChangesInterceptor? — Command for SQL; SaveChanges for entity state.**
2. **EF Plus vs interceptor? — Third-party bulk — evaluate vendor lock-in.**

### Common Mistakes in Interviews

- Soft delete interceptor without unique index on filtered column
- Tenant filter missing on new entity type
- Interceptor throws — opaque transaction failure

---

## Q098: Compiled Queries EF Core

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Access |
| **Frequency** | Occasional |

### Question

When do compiled queries in EF Core justify the complexity?

### Short Answer (30 seconds)

Compiled queries cache query expression translation and delegate — shave microseconds on hot paths executed millions of times. Worth for tight loops; unnecessary for typical CRUD called once per request.

### Detailed Answer (3–5 minutes)

**Syntax:**
```csharp
private static readonly Func<AppDbContext, int, Order?> GetOrderById =
    EF.CompileQuery((AppDbContext ctx, int id) =>
        ctx.Orders.AsNoTracking().FirstOrDefault(o => o.Id == id));

// Usage
var order = GetOrderById(dbContext, orderId);
```

**When to use:**
- High-frequency lookup (product catalog by SKU every request)
- Minimal API hot endpoints after profiling proves EF compile cost significant
- .NET multi-tenant same query shape different context instance

**When to skip:**
- Dynamic LINQ with varying shapes — can't compile one delegate
- Already using `AsNoTracking` projection — optimize N+1 first

**Architect:** Measure with BenchmarkDotNet — compiled query saves ~10–30% EF overhead, not magic fix for bad SQL.

### Architecture Perspective

Compiled queries micro-optimize hot EF paths — architects apply after N+1 and index fixes.

### Follow-up Questions

1. **EF.CompileAsyncQuery? — Async hot paths — same pattern.**
2. **Query splitting interaction? — Compiled query includes AsSplitQuery in expression.**

### Common Mistakes in Interviews

- Compiled query for admin report run once daily
- Dynamic filter breaks compiled query cache
- Skip indexes because compiled query added

---

## Q099: Bulk Insert Strategies EF Core

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Access |
| **Frequency** | Very Common |

### Question

Compare bulk insert strategies for high-volume .NET data ingestion.

### Short Answer (30 seconds)

EF `SaveChanges` row-by-row is too slow for 100K+ rows. Strategies: `AddRange` + batched SaveChanges, `ExecuteSqlRaw` COPY/BULK INSERT, `SqlBulkCopy`, third-party EFExtensions, or bypass EF with Dapper.

### Detailed Answer (3–5 minutes)

| Strategy | Throughput | Trade-off |
|----------|------------|----------|
| AddRange + batch SaveChanges | Moderate | Change tracking overhead |
| ExecuteUpdate/Insert (.NET 7+) | Good | SQL generation limits |
| SqlBulkCopy | Very high | SQL Server specific, no EF tracking |
| PostgreSQL COPY | Very high | Npgsql binary import |
| EF Extensions BulkInsert | High | License, extension dep |

**Architect pattern:**
- **OLTP path** — normal EF for business transactions
- **Ingestion pipeline** — separate worker, `SqlBulkCopy` or CSV `BULK INSERT`, no DbContext
- **Batch size** — 1000–5000 per SaveChanges batch; tune memory

**Pitfalls:** Identity column handling, trigger firing, audit interceptor bypass on raw bulk, transaction log growth — coordinate with DBA.

### Architecture Perspective

Bulk insert is separate architectural path from OLTP EF — don't force SaveChanges at scale.

### Follow-up Questions

1. **Change tracking off? — `context.ChangeTracker.AutoDetectChangesEnabled = false` for large AddRange.**
2. **Outbox pattern bulk? — Insert outbox in same transaction — order matters.**

### Common Mistakes in Interviews

- SaveChanges 1M rows in single request
- Bulk insert without transaction boundary plan
- Ignore audit requirements on bulk path

---

## Q100: Architect Code Review Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Leadership |
| **Frequency** | Very Common |

### Question

What does a .NET architect code review checklist cover beyond syntax?

### Short Answer (30 seconds)

Architect review verifies boundaries, NFRs, operability, and systemic risk — not formatting. Checklist: layering violations, security authZ gaps, data access patterns, async discipline, observability, configuration, API contract, and failure modes.

### Detailed Answer (3–5 minutes)

**Checklist categories:**
1. **Architecture** — Domain doesn't reference Infrastructure; no circular deps; appropriate pattern (not gold-plated CQRS)
2. **Security** — AuthZ on every mutating endpoint; input validation; secrets not in code; IDOR check
3. **Data** — N+1 risk; transaction scope; migration included; index for new filters
4. **Async** — No `.Result`/`.Wait()`; CancellationToken propagated; DbContext not in singleton
5. **Observability** — Structured logging with correlation ID; metrics on critical path; health checks
6. **API** — Versioning; ProblemDetails; breaking change assessment; pagination on lists
7. **Resilience** — Timeouts on HttpClient; retry only idempotent; circuit breaker on externals
8. **Performance** — Allocation in hot path; caching stampede risk; pool usage

**Process:** Automate with analyzers, ArchUnitNet, and CI — human review for trade-offs and ADR alignment.

**Architect role:** Teach via review comments — link to standards doc, not rewrite PR.

### Architecture Perspective

Architect code review gates systemic risk — checklist scales team quality.

### Follow-up Questions

1. **Automate what? — StyleCop, Roslyn analyzers, NetArchTest, EF query count test.**
2. **Review size limit? — 400 LOC PR guideline — architect splits large changes.**

### Common Mistakes in Interviews

- Review only naming conventions
- Approve without running app or tests
- No security review on public endpoints

---
