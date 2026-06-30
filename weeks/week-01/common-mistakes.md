# Week 01 — Common Mistakes

## Developer Mistakes → Architect Anti-Patterns

### 1. Treating C# as "Just Syntax"

**Mistake:** Focusing only on language features without understanding runtime implications.

**Impact:** Architecture decisions based on "C# can do it" rather than "C# should do it at this scale."

**Fix:** Always connect language choices to GC, threading, serialization, and deployment model.

---

### 2. Async All the Way — Except Where It Matters

**Mistake:** Making CPU-bound methods `async` without `await`, or using `Task.Run` in request handlers to "make it async."

**Impact:** Thread pool starvation, disguised sync code, harder debugging.

**Fix:** Async for I/O only. CPU-bound work: background service, message queue, or `Task.Run` at the edge — not in controllers.

---

### 3. Premature Performance Optimization

**Mistake:** Using `Span<T>`, object pools, and Native AOT on a CRUD API with 100 users.

**Impact:** Complexity without measurable benefit. Team maintains hard-to-read code.

**Fix:** Set performance budgets. Profile first. Optimize hot paths only when metrics justify it.

---

### 4. Ignoring Nullable Reference Types

**Mistake:** Leaving `<Nullable>disable</Nullable>` on new projects "because it's annoying."

**Impact:** NullReferenceExceptions in production. Unclear API contracts.

**Fix:** Mandate NRT in architecture standards. Enable warnings as errors in CI.

---

### 5. Over-Using Records for EF Core Entities

**Mistake:** Using `record` for database entities because "immutable is better."

**Impact:** EF Core change tracking breaks. Developers add mutable workarounds.

**Fix:** `record` for DTOs and events. `class` for persistence entities. Document in coding standards.

---

### 6. LINQ in Hot Paths Without Profiling

**Mistake:** Assuming LINQ is "fast enough" because it works in development.

**Impact:** Allocation storms under production load. p99 latency spikes.

**Fix:** Profile under realistic load. Replace LINQ in identified hot paths. Keep LINQ elsewhere for readability.

---

### 7. Boxing Hidden in APIs

**Mistake:** Non-generic collections, `object` parameters, legacy APIs.

**Impact:** Invisible GC pressure. Hard to diagnose without profiling.

**Fix:** Ban non-generic collections in coding standards. Use generics everywhere.

---

## Interview Red Flags

When candidates say these, dig deeper:

| Statement | Probe With |
|-----------|-----------|
| "Async is always faster" | "Faster for whom — the request or the server?" |
| "Structs are always on the stack" | "What about a struct field in a class?" |
| "We should rewrite in Go for performance" | "What did profiling show was the bottleneck?" |
| "Records are better than classes" | "For what use case — EF entity or API DTO?" |

---

## Architecture Review Checklist — C# Week

When reviewing a .NET codebase, check:

- [ ] NRT enabled?
- [ ] Async for all I/O paths?
- [ ] CancellationToken propagated?
- [ ] No sync-over-async (`.Result`, `.Wait()`)?
- [ ] Appropriate type choices (struct vs class) documented?
- [ ] Performance budgets defined for critical paths?
- [ ] Source-generated serializers for high-throughput APIs?
