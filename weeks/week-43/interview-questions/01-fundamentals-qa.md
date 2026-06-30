# Week 43 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: React Architecture for Enterprise

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

How do you structure React architecture for a large enterprise single-page application?

### Short Answer (30 seconds)

Enterprise React = feature-based folders, container/presentational split, shared design system, server state via TanStack Query, client state only where needed, lazy-loaded routes, TypeScript strict mode, and ESLint boundary rules between domains.

### Detailed Answer (3–5 minutes)

**Recommended structure:**
```
src/
  features/orders/     — components, hooks, api, types
  features/checkout/
  shared/ui/           — design system primitives
  shared/hooks/
  app/                 — routing, providers, layout shell
```

**Key patterns:**
- **Container components** — fetch/orchestrate; pass data to **presentational** pure UI
- **Custom hooks** — `useOrderList()` encapsulates React Query + error handling
- **Design system package** — shared Button, Modal, tokens — versioned independently
- **Code splitting** — `React.lazy` per route; monitor bundle with webpack analyzer

**State ownership (frontend ADR):**
| Data type | Tool |
|-----------|------|
| Server/API cache | TanStack Query |
| URL state | React Router search params |
| Complex client-only | Context or Zustand (sparingly) |
| Form transient | React Hook Form local state |

**Architect:** Feature-first structure maps to team boundaries — layer-first (all components together) couples teams at scale.

### Architecture Perspective

Enterprise React architecture is team topology — interviewers probe folder structure and state ownership.

### Follow-up Questions

1. **Server Components? — Next.js App Router shifts data fetch server-side — document boundary in ADR.**
2. **Monorepo vs multirepo? — Nx/Turborepo for shared design system across multiple SPAs.**

### Common Mistakes in Interviews

- God component 2000 lines mixing fetch and UI
- Redux store for all API response caching
- No shared design system — 12 inconsistent button implementations

---

## Q002: Angular Enterprise Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

How should a large enterprise Angular application be structured?

### Short Answer (30 seconds)

Enterprise Angular uses domain feature folders, lazy-loaded routes, core module (singleton services once), shared module (dumb UI), strict import boundaries, and standalone components for new code. Prevents circular dependencies and enables independent team delivery.

### Detailed Answer (3–5 minutes)

**Folder layout:**
```
src/app/
  core/           — auth, interceptors, guards (import once in AppConfig)
  shared/         — pipes, directives, presentational components
  features/
    checkout/     — lazy route, feature-specific services
    account/
```

**Modern Angular (v17+):**
- Standalone components + `provideRouter` with `loadComponent`
- Signals for reactive state where appropriate
- NgModules acceptable for legacy maintenance — new code standalone-first

**Boundary enforcement:**
- ESLint `import/no-restricted-paths` — features cannot import sibling features
- Shared services only via `core/` or explicit public API barrel

**Architect concerns:**
- HttpClient interceptors centralized in core (auth token, correlation ID, error handling)
- One `providedIn: 'root'` singleton per domain service — avoid duplicate providers
- Lazy loading mandatory for features >50KB — initial bundle budget enforcement

### Architecture Perspective

Angular enterprise structure prevents dependency spaghetti — architects enforce boundaries, not just recommend folders.

### Follow-up Questions

1. **NgModule vs standalone migration? — Incremental: new features standalone; migrate legacy on touch.**
2. **Nx monorepo? — Enforces module boundaries with tags (`scope:checkout`, `type:feature`).**

### Common Mistakes in Interviews

- Everything imported in AppModule — no lazy loading
- Feature-to-feature direct imports causing circular deps
- Shared module re-providing HttpClient in every feature

---

## Q003: BFF Pattern Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Explain the Backend-for-Frontend (BFF) pattern and when to use it.

### Short Answer (30 seconds)

BFF is a dedicated API layer per frontend experience (web, mobile) that aggregates microservices, shapes DTOs for UI screens, and handles browser-specific auth. Prevents SPA from calling many microservices directly and coupling UI to internal service topology.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
Web SPA → Web BFF → Order MS, Payment MS, Inventory MS
Mobile  → Mobile BFF → (same or subset of services)
```

**BFF responsibilities:**
- Aggregate parallel downstream calls into one screen payload
- Transform internal domain models to UI-friendly DTOs
- Handle cookie/session auth appropriate for browser
- Apply per-client rate limiting and caching

**BFF vs API Gateway:**
| Concern | API Gateway | BFF |
|---------|-------------|-----|
| Auth, TLS, WAF | ✅ | Delegates to gateway |
| Screen-specific aggregation | ❌ | ✅ |
| Per-client DTO shaping | ❌ | ✅ |

**When to use:** 3+ microservices per screen, different web/mobile needs, or auth token exchange complexity.
**When to skip:** Small team, monolith backend, simple CRUD — BFF adds operational overhead.

**Architect:** One BFF per frontend type — not one BFF per developer.

### Architecture Perspective

BFF is the UI's API contract — architects prevent SPAs from becoming distributed monolith clients.

### Follow-up Questions

1. **GraphQL as BFF? — Possible for flexible queries; adds schema governance and N+1 risk.**
2. **BFF business logic limit? — Orchestration yes; core domain rules stay in microservices.**

### Common Mistakes in Interviews

- SPA calls 15 microservices directly from browser
- Single BFF serving web and mobile with divergent screen needs
- BFF becomes dumping ground for all business logic

---

## Q004: Micro-Frontends Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

What are micro-frontends and when should an enterprise adopt them?

### Short Answer (30 seconds)

Micro-frontends decompose a web UI into independently deployable frontend applications composed at runtime (Module Federation, single-spa) or build time (monorepo packages). Adopt when team autonomy and release cadence pain exceed integration complexity cost — not for small teams.

### Detailed Answer (3–5 minutes)

**Composition models:**
| Model | How | Trade-off |
|-------|-----|----------|
| Build-time | npm packages in monorepo | Simple; coupled deploy |
| Run-time (Module Federation) | Shell loads remote bundles | Independent deploy; version matrix |
| iframe | Isolated embed | Strong isolation; UX limitations |

**Typical architecture:**
- **Shell** — routing, auth, design system, layout
- **Remote MFEs** — checkout, catalog, account — separate repos and pipelines
- **Shared dependencies** — React singleton via federation shared config

**Adopt when:**
- 5+ teams blocked on unified SPA release train
- Clear domain boundaries map to UI slices
- Organization accepts contract testing and version compatibility overhead

**Skip when:**
- <20 frontend developers — feature folders in monolith SPA simpler
- Tight UX consistency requirements without design system discipline

**Architect:** Micro-frontends are organizational architecture — technical cost is real; document decision in ADR.

### Architecture Perspective

Micro-frontends trade integration complexity for team autonomy — architects quantify when the trade is worth it.

### Follow-up Questions

1. **Module Federation vs single-spa? — Federation shares DOM seamlessly; single-spa orchestrates framework-agnostic mounts.**
2. **Shared design system? — Mandatory — without it MFEs look like different products.**

### Common Mistakes in Interviews

- Micro-frontends adopted for 5 developers because it's trendy
- No contract tests between shell and remotes
- Duplicate React versions loaded — bundle bloat and hook errors

---

## Q005: SPA Security Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

What are the essential security considerations for enterprise single-page applications?

### Short Answer (30 seconds)

SPA security: OIDC/OAuth with PKCE (no implicit flow), tokens in memory or HttpOnly cookies (not localStorage for refresh), CSP headers, XSS prevention (sanitize, avoid dangerouslySetInnerHTML), CORS strict origin, BFF for token handling, and security headers on HTML shell.

### Detailed Answer (3–5 minutes)

**Authentication:**
- Authorization Code + PKCE for public SPA clients
- Short-lived access token; refresh via HttpOnly Secure SameSite cookie or BFF session
- Never store refresh tokens in localStorage — XSS exfiltration risk

**XSS defense:**
- Content-Security-Policy: `script-src 'self'`; nonce for inline if required
- Sanitize user HTML (DOMPurify); encode output in templates
- Avoid embedding secrets or API keys in client bundle — use BFF

**API security:**
- CORS: explicit allowed origins — not `*` with credentials
- CSRF: SameSite cookies or anti-CSRF tokens for cookie-based auth
- Rate limiting at gateway/BFF per session/IP

**Supply chain:**
- Lockfile + `npm audit` in CI; Dependabot for CVE patches
- Subresource Integrity (SRI) on CDN scripts

**Architect:** SPA security ADR documents token storage decision and threat model summary — security headers on API alone miss the HTML attack surface.

### Architecture Perspective

SPA security failures are architecture failures — token storage and CSP are interview staples.

### Follow-up Questions

1. **BFF for token exchange? — Keeps client secret and refresh handling server-side.**
2. **Third-party scripts? — Analytics/chat widgets are XSS vectors — load async with strict CSP.**

### Common Mistakes in Interviews

- Refresh token in localStorage
- API keys embedded in React bundle
- Security headers configured on API but not on HTML shell

---

## Q006: React Component Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Design scalable React component architecture for enterprise SPA.

### Short Answer (30 seconds)

Feature folders, smart/container vs presentational components, shared UI library, hooks for logic reuse, lazy routes, strict TypeScript boundaries. Avoid prop drilling via composition or context sparingly.

### Detailed Answer (3–5 minutes)

**Structure:**
```
src/features/orders/components/
src/shared/ui/
src/shared/hooks/
```

**Patterns:**
- **Container** — fetches data, passes props to **Presentational** — pure UI
- **Compound components** — `<Select>` + `<Select.Option>`
- **Custom hooks** — `useOrderList()` encapsulates React Query

**Architect:** Design system components in shared package — apps compose features.

**Performance:** `React.memo` selectively; code-split by route.

### Architecture Perspective

React architecture affects bundle size, testability, and team parallelization.

### Follow-up Questions

1. **Feature vs layer folders? — Feature-first scales with teams — layer-first couples.**
2. **Server Components? — Next.js App Router — shift data fetch to server — architecture split.**

### Common Mistakes in Interviews

- God component 2000 lines
- Global context for all server state
- No shared design system — 12 button styles

---

## Q007: Angular Module Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Organize Angular application structure for large enterprise apps.

### Short Answer (30 seconds)

NgModule or standalone components with domain folders, lazy-loaded feature routes, shared module for UI primitives, core module singleton services, strict dependency rules.

### Detailed Answer (3–5 minutes)

**Recommended layout:**
- `core/` — auth, interceptors, singleton services (import once)
- `shared/` — pipes, directives, dumb components
- `features/checkout/` — lazy route module or standalone route

**Modern Angular:** Standalone components + `provideRouter` with lazy `loadComponent`.

**Architect:** Enforce ESLint boundary rules — features don't import sibling features directly.

### Architecture Perspective

Angular structure prevents circular dependencies at enterprise scale.

### Follow-up Questions

1. **NgModule vs standalone? — New apps standalone-first; modules legacy maintenance.**
2. **Barrel files? — `index.ts` exports — careful of tree-shake breakage.**

### Common Mistakes in Interviews

- Everything in AppModule
- Shared module imports HttpClient 40 times
- Feature-to-feature direct imports

---

## Q008: State Management with Redux

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

When use Redux (or Redux Toolkit) in frontend architecture?

### Short Answer (30 seconds)

Redux when complex shared client state, many components need same data, time-travel debugging valuable, or predictable state transitions across large team. Prefer server state library (React Query) for API data.

### Detailed Answer (3–5 minutes)

**Redux fits:**
- Multi-step wizard state across routes
- Optimistic UI with complex rollback
- Client-only domain (cart, editor canvas)

**Often skip Redux:**
- Server data cache — TanStack Query handles
- Local UI state — useState sufficient

**Redux Toolkit:** Slices, RTK Query for API — reduces boilerplate.

**Architect:** Document state ownership — server vs client — in frontend ADR.

### Architecture Perspective

Redux is not default — interviewers test server vs client state split.

### Follow-up Questions

1. **RTK Query vs React Query? — RTK if already Redux; React Query if not.**
2. **Normalized store? — entities adapter for large lists — O(1) lookup.**

### Common Mistakes in Interviews

- Redux for every API call
- No selector memoization — rerender storm
- Global store as dump for all transient UI

---

## Q009: BFF for SPA

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Why use a Backend-for-Frontend (BFF) for single-page applications?

### Short Answer (30 seconds)

BFF tailors API to UI needs — aggregates microservices, hides internal topology, handles auth token exchange, reduces over-fetching, enables independent SPA/mobile BFFs.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
SPA → BFF (Checkout API) → Order MS, Payment MS, Inventory MS
```

**BFF responsibilities:**
- DTO shaping for screens
- Orchestration and parallel calls
- Session/cookie handling for browser
- Rate limiting per UI client

**Architect:** One BFF per frontend type (web BFF, mobile BFF) — not one BFF per developer preference.

### Architecture Perspective

BFF prevents SPA from becoming distributed monolith client.

### Follow-up Questions

1. **BFF vs API Gateway? — Gateway cross-cutting (auth, throttle); BFF domain-specific aggregation.**
2. **GraphQL as BFF? — Possible — federation adds complexity.**

### Common Mistakes in Interviews

- SPA calls 15 microservices directly
- Same BFF for mobile and web with divergent needs
- BFF becomes business logic dumping ground

---

## Q010: API Aggregation in BFF

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Implement API aggregation patterns in BFF without creating bottlenecks.

### Short Answer (30 seconds)

Parallel async calls, timeout per dependency, partial response strategy, circuit breaker, cache hot aggregates, pagination at BFF boundary.

### Detailed Answer (3–5 minutes)

**Pattern:**
```csharp
var order = orderTask; var payment = paymentTask;
await Task.WhenAll(order, payment);
return MapCheckoutView(order, payment);
```

**Resilience:**
- 2s timeout per downstream
- Fallback UI sections if inventory unavailable
- Bulkhead thread pool per dependency

**Architect:** BFF p99 budget = sum of parallel not serial — design parallel paths.

### Architecture Perspective

BFF aggregation latency is UX latency — architect parallel I/O.

### Follow-up Questions

1. **GraphQL N+1 in BFF? — DataLoader pattern batch fetches.**
2. **Cache aggregated homepage? — CDN edge or Redis 60s TTL — stampede protection.**

### Common Mistakes in Interviews

- Serial 6 downstream calls per screen
- No timeout — hung BFF blocks UI
- BFF transaction across services — distributed txn anti-pattern

---

## Q011: Micro-Frontends and Module Federation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

When adopt micro-frontends with module federation?

### Short Answer (30 seconds)

When independent teams deploy UI slices on different cadences, shared shell hosts remotes (Webpack Module Federation, single-spa). Trade complexity for team autonomy — not for small teams.

### Detailed Answer (3–5 minutes)

**Architecture:**
- **Shell** — routing, auth, design system
- **Remote MFEs** — checkout, account, catalog — independent deploy
- **Shared dependencies** — React singleton via federation config

**When yes:** 5+ teams, release coupling pain, clear domain splits.
**When no:** <20 devs, unified product — monolith SPA + feature folders simpler.

**Architect:** Contract tests between shell and remotes; version compatibility matrix.

### Architecture Perspective

Micro-frontends are organizational architecture — technical cost is real.

### Follow-up Questions

1. **Module Federation vs iframe? — Federation shared DOM; iframe isolation but UX clunky.**
2. **CSS isolation? — Shadow DOM or CSS modules — prevent style bleed.**

### Common Mistakes in Interviews

- MFE for 3-person team
- Duplicate React copies — broken hooks
- No shared design system contract

---

## Q012: SPA Authentication with OIDC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Design OIDC authentication flow for SPA architecture.

### Short Answer (30 seconds)

Authorization Code + PKCE (no implicit flow). SPA redirects to IdP, receives code, exchanges via BFF or secure backend — tokens not long-lived in browser storage if avoidable.

### Detailed Answer (3–5 minutes)

**Recommended flow:**
1. SPA → redirect to Entra ID/Okta
2. Callback with auth code
3. BFF exchanges code for tokens (client secret on server)
4. BFF sets HttpOnly session cookie to SPA

**Avoid:** Implicit flow deprecated; storing refresh token in localStorage.

**Architect:** Token lifetime, silent renew, logout propagates to IdP (front-channel back-channel).

### Architecture Perspective

SPA auth is XSS-sensitive — architects choose BFF cookie pattern for Tier-0.

### Follow-up Questions

1. **MSAL.js? — Microsoft library — handles PKCE and token cache — prefer BFF for confidential client.**
2. **Multiple IdP? — Federated identity — single corporate Entra as broker.**

### Common Mistakes in Interviews

- Implicit flow in new app
- JWT in localStorage for refresh token
- No CSRF protection on cookie session

---

## Q013: CSRF Protection for SPA

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Protect cookie-based SPA sessions against CSRF.

### Short Answer (30 seconds)

SameSite=Strict/Lax cookies, anti-CSRF token on state-changing requests, double-submit cookie, or BFF-only mutations with custom header requirement.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **SameSite=Lax** — Blocks cross-site POST in modern browsers
- **Anti-forgery token** — Server renders token; SPA sends `X-XSRF-TOKEN` header
- **Custom header** — `X-Requested-With` — simple CSRF defense for APIs

**Architect:** CSRF matters when session cookie auth — not when pure Bearer token in Authorization header (still XSS risk).

**BFF:** Validate Origin/Referer on mutations.

### Architecture Perspective

CSRF is revived risk with HttpOnly cookie SPA pattern — design explicitly.

### Follow-up Questions

1. **SameSite=None? — Required cross-site embed — must Secure + CSRF token.**
2. **GET mutations? — Never — CSRF via img tag.**

### Common Mistakes in Interviews

- HttpOnly cookie without CSRF token
- CORS * with credentials true
- State-changing GET endpoints

---

## Q014: CORS and BFF Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Explain CORS in SPA architecture and why BFF reduces CORS pain.

### Short Answer (30 seconds)

Browser enforces CORS on cross-origin XHR. SPA on `app.com` calling `api.com` needs Access-Control-Allow-Origin. BFF same-origin to SPA eliminates browser CORS for main API calls.

### Detailed Answer (3–5 minutes)

**Without BFF:**
- API must allow `app.com` origin
- Preflight on custom headers
- Credentials complicate Allow-Origin (no wildcard)

**With BFF:**
- SPA calls `app.com/api` — same origin — no CORS
- BFF server-side calls microservices — no browser CORS

**Architect:** Public third-party API still needs strict CORS allowlist — not `*`.

### Architecture Perspective

CORS is browser policy — server-to-server unaffected.

### Follow-up Questions

1. **Preflight cache? — Access-Control-Max-Age reduces OPTIONS traffic.**
2. **Multiple SPA origins? — Dynamic allowlist from config — not static *.**

### Common Mistakes in Interviews

- CORS * with credentials
- Fix CORS by disabling browser security
- Expose internal admin API with wide CORS

---

## Q015: SSR vs CSR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Compare SSR and CSR architecture tradeoffs.

### Short Answer (30 seconds)

CSR: browser renders, rich interactivity, slower FCP. SSR: server renders HTML, better SEO and LCP, higher server cost. Choose per page type — marketing SSR, app shell CSR or hybrid.

### Detailed Answer (3–5 minutes)

| Factor | CSR | SSR |
|--------|-----|-----|
| SEO | Poor without prerender | Strong |
| TTFB/LCP | Slower first paint | Faster content |
| Server load | Static CDN | Compute per request |
| Interactivity | Immediate post-hydrate | Hydration cost |

**Hybrid:** SSR product pages, CSR authenticated app behind login.

**Architect:** Core Web Vitals targets drive decision — not framework religion.

### Architecture Perspective

SSR vs CSR is NFR and SEO decision — document in frontend ADR.

### Follow-up Questions

1. **Streaming SSR? — React 18 send HTML chunks — improve TTFB.**
2. **Edge SSR? — Vercel/Front Door — reduce origin distance.**

### Common Mistakes in Interviews

- CSR for public product catalog needing SEO
- SSR every API call — server bottleneck
- Ignore hydration mismatch bugs

---

## Q016: When to Choose Next.js

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

When recommend Next.js for frontend architecture?

### Short Answer (30 seconds)

Next.js when need SSR/SSG, file-based routing, API routes/BFF colocation, image optimization, incremental static regeneration — React team building full-stack web product on Vercel or Node hosting.

### Detailed Answer (3–5 minutes)

**Next.js strengths:**
- App Router + Server Components
- ISR for catalog pages
- Built-in code splitting and image CDN
- Middleware for auth at edge

**Skip when:**
- Pure internal admin SPA behind VPN — Vite CSR simpler
- Heavy Angular enterprise standard
- Non-React stack mandated

**Architect:** Hosting model (Vercel vs self-hosted AKS) affects cost and compliance ADR.

### Architecture Perspective

Next.js is platform choice — justify with SSR/SEO/perf requirements.

### Follow-up Questions

1. **Server Components data fetch? — Direct DB from server — secure credentials off client.**
2. **next export static? — SSG only sites — no server — cheap hosting.**

### Common Mistakes in Interviews

- Next.js chosen because 'it's popular'
- Serverless functions uncapped cost on traffic spike
- Mixing pages and app router without migration plan

---

## Q017: Core Web Vitals Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Architect frontend for Core Web Vitals (LCP, INP, CLS).

### Short Answer (30 seconds)

LCP: optimize hero image, SSR critical content, CDN. INP: reduce JS main thread, code split, web workers. CLS: reserve space for images/ads, font-display swap, avoid DOM injection above fold.

### Detailed Answer (3–5 minutes)

**Targets:** LCP <2.5s, INP <200ms, CLS <0.1 (75th percentile).

**Architecture levers:**
- Critical path CDN
- Critical CSS inline
- Defer third-party scripts (analytics last)
- Skeleton loaders with fixed dimensions

**Measure:** RUM (Application Insights web vitals), Lighthouse CI gates.

**Architect:** Third-party script governance — marketing tags kill INP.

### Architecture Perspective

Core Web Vitals are ranking and conversion metrics — architecture owns baseline.

### Follow-up Questions

1. **INP replaced FID? — INP measures all interactions — stricter.**
2. **LCP element? — Usually hero image — preload `fetchpriority=high`.**

### Common Mistakes in Interviews

- Measure only Lighthouse desktop lab
- No font strategy — FOIT/CLS spike
- Third-party tag manager uncontrolled

---

## Q018: Bundle Size Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Strategies to reduce JavaScript bundle size in SPA architecture.

### Short Answer (30 seconds)

Route-level code splitting, tree shaking, analyze webpack/vite bundle, replace heavy libs, dynamic import charts/maps, server-side heavy logic, shared vendor chunk strategy.

### Detailed Answer (3–5 minutes)

**Tactics:**
- `import()` lazy routes
- `lodash-es` per-function import not full lodash
- Replace moment with date-fns/dayjs
- `sideEffects: false` in package.json
- Module Federation shared singletons

**CI:** `bundlesize` or `size-limit` PR check — fail >5% growth.

**Architect:** Performance budget ADR — max 250KB initial JS gzip.

### Architecture Perspective

Bundle size is latency tax on every first visit.

### Follow-up Questions

1. **Source map explorer? — Visualize what's in bundle — find surprise deps.**
2. **Duplicate packages? — npm dedupe or pnpm strict — two React versions.**

### Common Mistakes in Interviews

- Import entire icon library
- No lazy load on admin-only routes
- Ignore dependency weight in ADR

---

## Q019: Frontend Caching Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Design caching layers for SPA and static assets.

### Short Answer (30 seconds)

Browser cache (hash filenames immutable), CDN edge cache, service worker for offline (PWA), HTTP cache headers, client data cache (React Query staleTime), BFF Redis for API aggregates.

### Detailed Answer (3–5 minutes)

**Cache tiers:**
1. **Static assets** — `Cache-Control: max-age=31536000, immutable`
2. **index.html** — `no-cache` — always revalidate
3. **API GET** — `ETag` + short TTL via BFF
4. **Client** — React Query `staleTime: 60_000`

**Architect:** Cache invalidation on deploy via asset hashing — not manual purge.

### Architecture Perspective

Frontend caching reduces origin load and improves repeat visit LCP.

### Follow-up Questions

1. **Stale-while-revalidate? — CDN serves stale while fetching fresh — smooth spikes.**
2. **Auth API cache? — Never cache personalized responses at CDN.**

### Common Mistakes in Interviews

- Cache-Control no-store on static hashed JS
- React Query staleTime 0 everywhere — refetch storm
- CDN caching Set-Cookie responses

---

## Q020: WebSocket Real-Time Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Design real-time WebSocket architecture for SPA.

### Short Answer (30 seconds)

WebSocket gateway (SignalR, Azure Web PubSub), sticky sessions or backplane (Redis), auth on connect, reconnect with exponential backoff, fallback SSE/long polling.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
SPA ←WSS→ Web PubSub/SignalR Hub → Service Bus → Workers
```

**Concerns:**
- Scale: Azure Web PubSub serverless scale
- Auth: JWT query string or post-connect claim
- Message ordering per channel
- Heartbeat and idle disconnect

**Architect:** Real-time path separate from REST BFF — different SLI (connection count).

### Architecture Perspective

WebSockets add stateful infra — justify vs polling for update frequency.

### Follow-up Questions

1. **SignalR vs raw WebSocket? — SignalR handles fallback and groups — .NET natural fit.**
2. **Backpressure? — Rate limit client publish — prevent flood.**

### Common Mistakes in Interviews

- WebSocket for data that updates daily
- No reconnect logic — silent stale UI
- Broadcast all events to all users

---

## Q021: GraphQL on Frontend

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Common |

### Question

When use GraphQL in frontend architecture vs REST BFF?

### Short Answer (30 seconds)

GraphQL when many clients need flexible field selection, rapid UI iteration, federated subgraphs mature. REST BFF when simple aggregates, team prefers simplicity, caching at CDN easier.

### Detailed Answer (3–5 minutes)

**GraphQL pros:** Single endpoint, typed schema, reduces over-fetch
**Cons:** Query complexity limits, caching harder, N+1 server-side

**Patterns:**
- Apollo Client cache normalized
- Persisted queries for production security
- Federation for domain teams

**Architect:** GraphQL gateway with cost/complexity analysis — prevent expensive queries.

### Architecture Perspective

GraphQL is not REST replacement everywhere — operational cost real.

### Follow-up Questions

1. **APQ? — Automatic persisted queries — allowlist production queries.**
2. **GraphQL subscriptions? — WebSocket — separate scaling concern.**

### Common Mistakes in Interviews

- GraphQL expose entire DB schema
- No query depth limit — DoS vector
- GraphQL for 2 static screens

---

## Q022: Design System Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Architect enterprise design system for multiple web applications.

### Short Answer (30 seconds)

Token layer (color, spacing), component library (Storybook), npm package versioning, accessibility baked in, contribution model, visual regression tests.

### Detailed Answer (3–5 minutes)

**Layers:**
1. **Design tokens** — JSON → CSS variables / Tailwind preset
2. **Primitives** — Button, Input, Modal
3. **Patterns** — Checkout flow components
4. **Documentation** — Storybook + usage guidelines

**Delivery:** `@corp/ui` semver; consuming apps pin major.

**Architect:** Design system is platform product — roadmap, SLA, breaking change policy.

### Architecture Perspective

Design system reduces inconsistency and accessibility debt across apps.

### Follow-up Questions

1. **Monorepo vs separate repo? — Monorepo Nx/Turborepo common for DS + apps.**
2. **Theming? — CSS variables + `[data-theme=dark]`.**

### Common Mistakes in Interviews

- Copy-paste components per project
- Breaking changes without semver
- Accessibility not tested in CI

---

## Q023: Frontend Monorepo

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Structure frontend monorepo for apps, BFF, and design system.

### Short Answer (30 seconds)

Nx or Turborepo: apps/web, apps/mobile-web, packages/ui, packages/api-client, shared eslint/tsconfig. Affected builds in CI — only test what changed.

### Detailed Answer (3–5 minutes)

**Benefits:**
- Atomic cross-package refactor
- Shared types OpenAPI → TypeScript client
- Single PR for feature spanning UI + BFF

**Challenges:**
- CI time — use remote cache (Nx Cloud)
- Ownership boundaries — CODEOWNERS per package

**Architect:** Monorepo ADR documents when to split repo (open source lib, acquirer isolation).

### Architecture Perspective

Monorepo fits full-stack product teams — polyrepo fits independent vendors.

### Follow-up Questions

1. **OpenAPI codegen? — `packages/api-client` generated from BFF swagger on build.**
2. **Deploy independently? — Each app separate pipeline from monorepo — affected only.**

### Common Mistakes in Interviews

- Monorepo without affected CI — 2 hour builds
- Circular package dependencies
- No shared lint/tsconfig — drift

---

## Q024: Feature Flags for UI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Implement feature flags in frontend architecture safely.

### Short Answer (30 seconds)

LaunchDarkly/Azure App Configuration — evaluate flags server-side in BFF when possible; client flags for UI-only toggles; kill switch for bad deploy; avoid long-lived flags.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Server-side evaluation** — BFF includes `features: { newCheckout: true }` in bootstrap
- **Client SDK** — Real-time flag change without redeploy
- **Flag hygiene** — Remove after 90 days — tech debt otherwise

**Architect:** Flag taxonomy — release, experiment, ops kill switch — different owners.

### Architecture Perspective

Feature flags decouple deploy from release — architecture for progressive delivery.

### Follow-up Questions

1. **Same flag backend+frontend? — Coordinate naming convention in config repo.**
2. **A/B test flags? — Analytics correlation id — measure conversion.**

### Common Mistakes in Interviews

- 100 permanent flags — unmaintainable
- Client-only flag for security feature
- No kill switch tested in drill

---

## Q025: Accessibility Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Bake accessibility into frontend architecture (WCAG 2.1 AA).

### Short Answer (30 seconds)

Design system components accessible by default, axe-core in CI, keyboard nav spec, semantic HTML, ARIA only when needed, focus management in SPA route changes, contrast tokens.

### Detailed Answer (3–5 minutes)

**Architecture gates:**
- PR: eslint-plugin-jsx-a11y + axe scan Storybook
- Manual: screen reader test checklist per major flow
- VPAT/ACR for enterprise sales

**SPA specifics:** Announce route change to screen reader (`aria-live`), trap focus in modals.

**Architect:** A11y non-negotiable for public sector and retail — lawsuit risk.

### Architecture Perspective

Accessibility is architecture — retrofit costs 10× build-time inclusion.

### Follow-up Questions

1. **WCAG AA vs AAA? — AA enterprise standard; AAA selective.**
2. **Automated only? — Catches ~30% — manual keyboard required.**

### Common Mistakes in Interviews

- div button everywhere
- Color-only error states
- Skip focus management in client router

---

## Q026: Mobile Web vs Native

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Decide mobile web vs native app architecture.

### Short Answer (30 seconds)

Mobile web: one codebase, instant updates, limited device APIs. Native: performance, offline, push, App Store presence. PWA/hybrid middle ground for some B2B.

### Detailed Answer (3–5 minutes)

**Decision matrix:**
| Need | Mobile web | Native |
|------|------------|--------|
| Biometric, BLE | Limited | Full |
| Offline complex | Weak | Strong |
| SEO/discovery | Good | Store ASO |
| Release speed | Immediate | Store review |

**Architect:** Often both — mobile web for breadth, native for power users — shared BFF.

### Architecture Perspective

Platform choice affects team skills, release, and capability — ADR required.

### Follow-up Questions

1. **Capacitor/Ionic? — Web in native shell — middle path — know limits.**
2. **React Native? — Shared logic with web React — not shared DOM.**

### Common Mistakes in Interviews

- Native app for content brochure site
- Ignore iOS/Android platform guidelines
- Separate backends per mobile web and web

---

## Q027: PWA Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Common |

### Question

Design Progressive Web App architecture.

### Short Answer (30 seconds)

Service worker caching strategies, web app manifest, HTTPS, install prompt, push notifications (where supported), offline fallback page, background sync for forms.

### Detailed Answer (3–5 minutes)

**Components:**
- **Manifest** — icons, theme, display standalone
- **Service worker** — cache-first static, network-first API
- **Workbox** — precache build assets

**Limits:** iOS push/history constraints; not full native replacement.

**Architect:** PWA for field workers low connectivity — not default consumer strategy if native needed.

### Architecture Perspective

PWA extends web reach with installability and offline — know platform gaps.

### Follow-up Questions

1. **Cache versioning? — Service worker activate skipWaiting strategy — avoid stale app.**
2. **Offline write? — IndexedDB queue + background sync when online.**

### Common Mistakes in Interviews

- Service worker caches API with PII
- No update strategy — users stuck old SW
- PWA without HTTPS

---

## Q028: Frontend Observability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Instrument frontend for observability in production.

### Short Answer (30 seconds)

RUM: Application Insights, Datadog RUM, Sentry — capture JS errors, Core Web Vitals, API correlation, session replay sampled, source maps secure upload.

### Detailed Answer (3–5 minutes)

**Key telemetry:**
- `window.onerror` + unhandledrejection
- Fetch/XHR failure with traceparent correlation to BFF
- Custom events: checkout_step_completed
- Vitals: LCP, INP, CLS automatic

**Privacy:** Mask PII in session replay; GDPR consent banner.

**Architect:** Frontend traces link to backend via W3C trace context — end-to-end latency visible.

### Architecture Perspective

Without RUM, backend green while users suffer JS errors.

### Follow-up Questions

1. **Source maps? — Upload to monitoring — hide from public CDN.**
2. **Sampling? — 100% errors; 10% sessions for replay — cost control.**

### Common Mistakes in Interviews

- No client-side error tracking
- Analytics without correlation id to backend
- Session replay records credit card fields

---

## Q029: CDN for Static Assets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Architect CDN delivery for SPA static assets.

### Short Answer (30 seconds)

Build output to blob + Azure Front Door/CDN, fingerprinted filenames, gzip/brotli, HTTP/2, edge locations near users, separate origin for API vs static.

### Detailed Answer (3–5 minutes)

**Deployment:**
```
CI → upload dist/ to $web blob → purge index.html only → CDN edge caches JS/CSS immutable
```

**Security:** CSP headers from CDN rules; Subresource Integrity on third-party scripts.

**Architect:** Global users — CDN non-optional for LCP target.

### Architecture Perspective

CDN is default architecture for public SPA — origin direct is anti-pattern.

### Follow-up Questions

1. **Dual CDN? — Primary + failover DNS — retail peak resilience.**
2. **Private SPA? — CDN still OK with auth at edge or VPN-only origin.**

### Common Mistakes in Interviews

- Deploy overwrites JS without hash — cache poison
- API and static same cookie domain confusion
- No brotli compression

---

## Q030: Frontend Security Headers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Frontend |
| **Frequency** | Very Common |

### Question

Configure security headers for SPA and BFF architecture.

### Short Answer (30 seconds)

CSP restrict script sources, HSTS, X-Frame-Options DENY, X-Content-Type-Options nosniff, Referrer-Policy, Permissions-Policy limit camera/mic.

### Detailed Answer (3–5 minutes)

**Example CSP:**
```
default-src 'self'; script-src 'self' 'nonce-{random}'; connect-src 'self' https://api.corp.com;
```

**BFF sets headers** on HTML shell and API responses.

**Architect:** CSP nonce per request for inline bootstrap — avoid unsafe-inline.

### Architecture Perspective

Security headers are cheap defense — architect standard template per tier.

### Follow-up Questions

1. **CSP report-only first? — Monitor violations before enforce — reduce breakages.**
2. **HSTS preload? — Only when HTTPS mature — irreversible commitment.**

### Common Mistakes in Interviews

- CSP unsafe-inline everywhere
- Missing frame-ancestors — clickjacking
- Security headers only on API not HTML shell

---
