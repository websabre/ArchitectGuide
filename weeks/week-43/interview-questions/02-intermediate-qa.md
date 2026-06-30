# Week 43 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: React Container Presentational Split

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | React Patterns |
| **Frequency** | Very Common |

### Question

When should you split React components into container and presentational layers?

### Short Answer (30 seconds)

Containers own data fetching and side effects; presentational components receive props and render UI. Split when reuse, testing, or team boundaries benefit.

### Detailed Answer (3–5 minutes)

**Container (smart):** uses hooks, React Query, dispatches actions — passes data/callbacks down.
**Presentational (dumb):** pure render from props; Storybook-friendly; no direct API calls.

**When to split:**
- Same UI appears with different data sources
- Design system team owns presentational; feature team owns containers
- Unit test UI without MSW mocking

**When not to split:** trivial forms — over-abstraction.

**Architect:** Document pattern in frontend standards — prevents 400-line mixed components.

### Architecture Perspective

Interviewers test separation of concerns — not dogmatic layer count.

### Follow-up Questions

1. **Hooks replace HOC containers? — Yes — custom hooks often replace container components.**
2. **Testing strategy? — Presentational snapshot; container integration with MSW.**

### Common Mistakes in Interviews

- Every component forced into two files regardless of size
- Presentational component calling fetch directly
- Container passing 40 props — needs composition or context slice

---

## Q032: React Composition Over Inheritance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | React Patterns |
| **Frequency** | Common |

### Question

Why does React favor composition over class inheritance for UI reuse?

### Short Answer (30 seconds)

Compose behavior via children, render props, and hooks instead of deep class hierarchies. Composition keeps trees flexible and avoids fragile base class problems.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Children:** `<Card>{content}</Card>`
- **Slots:** named props `header`, `footer`
- **Hooks:** `usePagination()` shared logic

**Anti-pattern:** `BaseList extends BaseComponent extends...` — breaks when requirements diverge.

**Enterprise:** Compound components (`<Tabs><Tabs.List/><Tabs.Panel/></Tabs>`) scale in design systems.

**Architect:** Enforce composition in lint rules — discourage class components in new code.

### Architecture Perspective

Composition is React idiomatic architecture for shared UI behavior.

### Follow-up Questions

1. **HOC vs hooks? — Hooks preferred — avoids wrapper hell and ref forwarding pain.**
2. **Render props still? — Rare — hooks cover most cases; render props for inversion control libraries.**

### Common Mistakes in Interviews

- Deep inheritance tree for UI variants
- Copy-paste components instead of composable primitives
- God hook with 15 unrelated concerns

---

## Q033: React Suspense Error Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | React Patterns |
| **Frequency** | Common |

### Question

How do Suspense and error boundaries fit enterprise React architecture?

### Short Answer (30 seconds)

Suspense defers rendering until async data ready; error boundaries catch render errors and show fallback UI. Together they structure loading/error states without scattered try/catch in every component.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
<ErrorBoundary fallback={<ErrorPage/>}>
  <Suspense fallback={<Skeleton/>}>
    <OrderDetail/>
  </Suspense>
</ErrorBoundary>
```

**Route-level:** lazy `React.lazy` + Suspense per route chunk.
**Data:** React Query `useSuspenseQuery` or Relay.

**Limitations:** Error boundaries don't catch event handlers or async — use try/catch there.

**Architect:** Standardize boundary placement — layout vs feature — in frontend ADR.

### Architecture Perspective

Suspense enables declarative loading architecture — reduces spinner spaghetti.

### Follow-up Questions

1. **Server Components + Suspense? — RSC streams HTML — boundaries at server/client split.**
2. **Monitoring? — Log boundary errors to RUM with component stack metadata.**

### Common Mistakes in Interviews

- try/catch around every child instead of boundary
- No fallback — blank screen during lazy load
- Error boundary only at app root — loses context

---

## Q034: TanStack Query Server State

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | State Management |
| **Frequency** | Very Common |

### Question

Architect server state management with TanStack Query instead of Redux.

### Short Answer (30 seconds)

TanStack Query caches API responses, handles stale-while-revalidate, deduplication, and background refetch. Redux reserved for true client-only global state.

### Detailed Answer (3–5 minutes)

**Query architecture:**
- Query keys hierarchical: `['orders', tenantId, filters]`
- `staleTime` / `gcTime` per domain sensitivity
- Mutations invalidate related queries
- Prefetch on hover for perceived speed

**BFF integration:** queries hit BFF endpoints; correlation id in meta.

**Architect:** Document query key conventions — prevents cache bugs across teams.

### Architecture Perspective

Server state in Redux is 2018 pattern — Query is default for API data.

### Follow-up Questions

1. **Optimistic updates? — `onMutate` rollback pattern for cart lines.**
2. **SSR hydration? — dehydrate query cache on server — rehydrate client.**

### Common Mistakes in Interviews

- Redux storing entire API responses with manual sync
- staleTime 0 on all queries — thundering herd
- No mutation invalidation strategy

---

## Q035: Angular Core Shared Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Angular Patterns |
| **Frequency** | Very Common |

### Question

Explain Angular core and shared module boundaries in large apps.

### Short Answer (30 seconds)

Core module: singleton services imported once in AppModule — auth, HTTP interceptors, global error handler. Shared module: reusable UI imported by feature modules — never provides singletons.

### Detailed Answer (3–5 minutes)

**Rules:**
- `CoreModule.forRoot()` guard — throw if imported twice
- Shared exports CommonModule, Material subset, dumb components
- Features lazy-load; import SharedModule

**Standalone era:** `provideHttpClient(withInterceptors())` in bootstrap replaces some CoreModule patterns.

**Architect:** Nx enforce-module-boundaries — core cannot import features.

### Architecture Perspective

Angular module boundaries prevent duplicate service instances and circular imports.

### Follow-up Questions

1. **providedIn root vs CoreModule? — `providedIn: 'root'` common — Core for interceptors bundle.**
2. **SharedModule growing forever? — Split into SharedUi and SharedForms packages.**

### Common Mistakes in Interviews

- HttpClient provided in every feature module
- CoreModule imported in lazy feature — duplicate interceptors
- Business logic services in SharedModule

---

## Q036: Angular OnPush Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Angular Patterns |
| **Frequency** | Common |

### Question

When mandate OnPush change detection strategy in Angular architecture?

### Short Answer (30 seconds)

OnPush checks component only on input reference change, events, or async pipe emissions — reduces change detection cycles in large templates.

### Detailed Answer (3–5 minutes)

**Use OnPush when:**
- Lists with 100+ rows
- Dashboard with many child components
- Design system primitives

**Requirements:**
- Immutable input updates or signals
- Async pipe for observables — not manual subscribe in component

**Architect:** ESLint rule default OnPush for new components; measure with Angular DevTools profiler.

### Architecture Perspective

OnPush is performance architecture — mandatory at enterprise list scale.

### Follow-up Questions

1. **Signals Angular 17+? — Fine-grained reactivity reduces need for manual OnPush in some cases.**
2. **Zone.js future? — Experimental zoneless — OnPush/signals prepare migration.**

### Common Mistakes in Interviews

- Default change detection on data grid with 500 rows
- Mutate input object in place — OnPush stale UI
- subscribe in component without async pipe

---

## Q037: Angular RxJS Facade Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Angular Patterns |
| **Frequency** | Common |

### Question

Design component state with RxJS observables in Angular without store overload.

### Short Answer (30 seconds)

Use BehaviorSubject or signals for local state; facade service exposing readonly observables; async pipe in template — avoid manual subscribe/unsubscribe.

### Detailed Answer (3–5 minutes)

**Facade pattern:**
```typescript
readonly vm$ = combineLatest([items$, filter$]).pipe(map(...));
```

**NgRx only when:** time-travel, complex cross-feature client state, audit requirements.

**Architect:** RxJS marble test facades — document hot vs cold observables in team guide.

### Architecture Perspective

Not every Angular app needs NgRx — facades + Query-like services suffice.

### Follow-up Questions

1. **shareReplay vs publishReplay? — shareReplay for HTTP cache in service — watch refCount.**
2. **Unsubscribe? — takeUntilDestroyed() in Angular 16+.**

### Common Mistakes in Interviews

- NgRx for simple form toggle state
- Memory leak from forgotten subscriptions
- Nested subscribe callbacks — callback hell

---

## Q038: Zustand Lightweight Global State

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | State Management |
| **Frequency** | Common |

### Question

When choose Zustand over Redux Toolkit in React architecture?

### Short Answer (30 seconds)

Zustand suits medium client state without boilerplate — cart, UI prefs, wizard progress. Redux when middleware ecosystem, devtools time-travel, or large team conventions mandate RTK.

### Detailed Answer (3–5 minutes)

**Zustand strengths:** minimal API, no Provider wrapper, slice pattern with middleware.
**Redux strengths:** RTK Query integration, established enterprise patterns, strict action traceability.

**Architect:** ADR picks one global client store per product — avoid Zustand + Redux coexistence without boundaries.

### Architecture Perspective

Store choice is team velocity vs governance trade-off.

### Follow-up Questions

1. **Zustand persist middleware? — localStorage UI prefs — never persist tokens.**
2. **Immer in Zustand? — immer middleware for immutable updates simply.**

### Common Mistakes in Interviews

- Three global state libraries in one SPA
- Zustand store as API cache duplicating React Query
- No devtools in prod debugging plan

---

## Q039: BFF Bootstrap Endpoint

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | BFF |
| **Frequency** | Very Common |

### Question

Design a BFF bootstrap endpoint that initializes SPA shell state.

### Short Answer (30 seconds)

Single `/api/bootstrap` returns user profile, feature flags, tenant config, and CSRF token — reduces waterfall on app load.

### Detailed Answer (3–5 minutes)

**Payload:**
```json
{ user, permissions, features, csrfToken, locale }
```

**Security:** HttpOnly session established before bootstrap; short cache `private, max-age=0`.

**Performance:** parallel with static asset load; SSR can embed bootstrap JSON in HTML nonce script.

**Architect:** Version bootstrap contract — breaking changes require coordinated deploy.

### Architecture Perspective

Bootstrap endpoint is SPA architecture seam between auth and UI.

### Follow-up Questions

1. **GraphQL bootstrap? — single query `viewer { ... }` equivalent.**
2. **CDN cache bootstrap? — Never — personalized — edge per-user only with caution.**

### Common Mistakes in Interviews

- SPA fires 8 API calls before first paint
- Feature flags only client SDK — flash of wrong UI
- Bootstrap includes secrets or refresh tokens

---

## Q040: BFF Error Mapping to UI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | BFF |
| **Frequency** | Common |

### Question

How should a BFF map downstream errors to SPA-friendly responses?

### Short Answer (30 seconds)

BFF translates microservice error codes to stable UI contract — user-safe messages, retry hints, correlation id — never leak stack traces or internal service names.

### Detailed Answer (3–5 minutes)

**Pattern:**
```json
{ "error": "INVENTORY_UNAVAILABLE", "message": "Item temporarily unavailable", "retryable": true, "traceId": "abc" }
```

**Map 404/409/422** to domain-specific codes; **502/503** to generic outage with retry.

**Architect:** OpenAPI documents error schema — frontend handles finite set.

### Architecture Perspective

BFF is translation layer — downstream chaos should not reach UI raw.

### Follow-up Questions

1. **Problem Details RFC 7807? — Standard error body — good for BFF consistency.**
2. **Partial failure aggregation? — 207-style multi-status or degrade sections.**

### Common Mistakes in Interviews

- Pass through raw microservice 500 text to user
- Different error shapes per downstream service
- No correlation id in error response

---

## Q041: BFF Rate Limiting Per Client

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | BFF |
| **Frequency** | Common |

### Question

Implement per-client rate limiting at the BFF for SPA protection.

### Short Answer (30 seconds)

Rate limit by session, API key, or IP at BFF — protects downstream microservices from UI-driven traffic spikes and abuse.

### Detailed Answer (3–5 minutes)

**Implementation:**
- Token bucket per userId in Redis
- 429 with `Retry-After` header
- Stricter limits on expensive aggregate endpoints
- Whitelist internal batch jobs

**SPA handling:** intercept 429 — show friendly message; exponential backoff on auto-retry.

**Architect:** Rate limits documented in API contract — product knows UX under throttle.

### Architecture Perspective

BFF rate limiting is edge defense — not only API gateway concern.

### Follow-up Questions

1. **Gateway vs BFF limit? — Gateway global; BFF per-endpoint business limits.**
2. **Burst allowance? — Allow short burst for human click patterns — block sustained abuse.**

### Common Mistakes in Interviews

- No rate limit on search autocomplete — DB melt
- 429 without Retry-After — client hammers
- Same limit for read and write endpoints

---

## Q042: Micro-Frontend Shell Routing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Micro-Frontends |
| **Frequency** | Very Common |

### Question

How does the shell application route between micro-frontends?

### Short Answer (30 seconds)

Shell owns top-level router — maps paths to remote MFE entry points. Each MFE registers routes under prefix; shell loads remote module federation bundle on navigation.

### Detailed Answer (3–5 minutes)

**Pattern:**
```
/shop/*     → catalog MFE
/checkout/* → checkout MFE
/account/*  → account MFE
```

**Shell responsibilities:** auth guard, layout chrome, design system provider, error boundary per MFE.

**Architect:** Route ownership matrix in integration ADR — prevents duplicate `/checkout` mounts.

### Architecture Perspective

Shell routing is integration contract — breaking changes need coordinated release.

### Follow-up Questions

1. **Hash vs history routing? — History preferred — hash ugly but simpler cross-MFE in iframe legacy.**
2. **Deep linking? — Shell must bootstrap correct remote before render — test bookmark URLs.**

### Common Mistakes in Interviews

- Each MFE owns full URL space independently
- No loading boundary between remote transitions
- Shell and remote both import router — conflict

---

## Q043: Module Federation Shared Dependencies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Module Federation |
| **Frequency** | Very Common |

### Question

Configure Webpack Module Federation shared dependency singletons.

### Short Answer (30 seconds)

Share React, React-DOM, design system as singletons — one copy in browser — version range in federation config prevents duplicate hook errors.

### Detailed Answer (3–5 minutes)

**Config concept:**
```js
shared: { react: { singleton: true, requiredVersion: '^18.0.0' } }
```

**Mismatch:** remote loads React 17 + shell React 18 — runtime crash.

**Architect:** Shared dependency matrix in CI — compatibility test shell + all remotes before deploy.

### Architecture Perspective

Duplicate React is top MFE production incident — federation config is architecture.

### Follow-up Questions

1. **eager vs lazy shared? — eager in shell for core; lazy for optional libs.**
2. **Version negotiation? — Federation runtime picks highest compatible — document limits.**

### Common Mistakes in Interviews

- No requiredVersion — silent duplicate bundles
- Shared lodash entire package — bloat
- Remote bundles own React — hooks invalid

---

## Q044: OIDC Authorization Code PKCE

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | OIDC Auth |
| **Frequency** | Very Common |

### Question

Walk through Authorization Code + PKCE flow for public SPA clients.

### Short Answer (30 seconds)

SPA generates code_verifier/challenge, redirects to IdP, receives code on callback, exchanges code for tokens via backend/BFF with client authentication — no implicit flow.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Generate PKCE verifier + S256 challenge
2. Redirect `/authorize?code_challenge=...`
3. Callback `?code=...`
4. BFF POST `/token` with verifier + secret
5. Session cookie to browser

**Architect:** PKCE mandatory for all public clients — OAuth 2.1 direction.

### Architecture Perspective

PKCE prevents authorization code interception — baseline SPA auth architecture.

### Follow-up Questions

1. **Public client no secret? — Pure SPA token exchange discouraged — use BFF confidential client.**
2. **Refresh token rotation? — Enable in IdP — detect token replay theft.**

### Common Mistakes in Interviews

- Implicit flow for new application
- code_verifier stored in predictable location
- Token exchange from browser with client secret embedded

---

## Q045: OIDC Silent Session Renewal

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | OIDC Auth |
| **Frequency** | Common |

### Question

Design silent token/session renewal without disrupting SPA UX.

### Short Answer (30 seconds)

Hidden iframe or BFF refresh endpoint renews session before expiry; prompt=none for IdP silent auth; fallback to interactive login on failure.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **BFF session refresh** — sliding cookie server-side — SPA unaware
- **MSAL silent acquire** — iframe to IdP — breaks with third-party cookie blocking
- **Proactive refresh** — renew at 75% lifetime

**Architect:** Monitor silent renew failure rate — Safari ITP drives BFF cookie pattern.

### Architecture Perspective

Session continuity is UX architecture — expiry surprises cause cart abandonment.

### Follow-up Questions

1. **Third-party cookie blocking? — Prefer same-site BFF session over iframe renew.**
2. **Concurrent tabs? — BroadcastChannel sync logout and renew across tabs.**

### Common Mistakes in Interviews

- Wait until 401 on API call to renew
- Refresh token in localStorage
- No logout on silent renew failure — zombie session

---

## Q046: CSRF SameSite Cookie Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | CSRF |
| **Frequency** | Very Common |

### Question

Explain SameSite cookie attributes for SPA session security.

### Short Answer (30 seconds)

SameSite=Lax blocks most cross-site POST CSRF; Strict blocks all cross-site cookies; None requires Secure and needs extra CSRF defenses for cross-site embeds.

### Detailed Answer (3–5 minutes)

**Guidance:**
- **Lax** — default for session cookies — good balance
- **Strict** — high security — breaks external link deep-login flows
- **None+Secure** — only if iframe/embed required — pair with CSRF token

**Architect:** Document cookie policy in security ADR — align BFF and CDN cookie domains.

### Architecture Perspective

SameSite is first-line CSRF defense with cookie-based SPA sessions.

### Follow-up Questions

1. **Cross-subdomain SPA? — Set cookie Domain carefully — sibling subdomain attacks.**
2. **CHIPS partitioned cookies? — Emerging — third-party context isolation.**

### Common Mistakes in Interviews

- SameSite=None without Secure
- Session cookie on parent domain shared with untrusted subdomain
- Ignore CSRF because SameSite exists — defense in depth

---

## Q047: CSRF Anti-Forgery Token Header

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | CSRF |
| **Frequency** | Common |

### Question

Implement double-submit or synchronizer CSRF token pattern for SPA mutations.

### Short Answer (30 seconds)

Server issues CSRF token in cookie or bootstrap; SPA reads token and sends `X-XSRF-TOKEN` header on POST/PUT/DELETE; server validates match.

### Detailed Answer (3–5 minutes)

**Flow:**
1. Bootstrap returns `csrfToken` or sets readable `XSRF-TOKEN` cookie
2. Axios interceptor adds header from cookie
3. BFF validates header vs server-side session store

**Architect:** CSRF required for cookie auth mutations — not needed for Bearer-only APIs.

### Architecture Perspective

CSRF token pattern pairs with HttpOnly session cookies in BFF architecture.

### Follow-up Questions

1. **Angular HttpClient XSRF? — Built-in `XsrfInterceptor` — enable cookie name config.**
2. **GET with side effects? — Forbidden — CSRF via img tag vector.**

### Common Mistakes in Interviews

- CSRF token in localStorage only — XSS steals it
- Validate CSRF on GET requests breaking caching
- Token never rotated on privilege escalation

---

## Q048: SSR Hydration Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SSR/CSR |
| **Frequency** | Very Common |

### Question

What is hydration in SSR architecture and what problems does it cause?

### Short Answer (30 seconds)

Hydration attaches event listeners to server-rendered HTML so React/Angular becomes interactive. Mismatch between server HTML and client render causes bugs and performance cost.

### Detailed Answer (3–5 minutes)

**Issues:**
- **Mismatch** — server/client date/time, random IDs, browser-only APIs
- **Double data fetch** — server fetched, client refetches
- **Bundle cost** — hydration JS still downloaded

**Mitigation:** consistent render, `suppressHydrationWarning` sparingly, pass serialized state.

**Architect:** Hydration test in CI — visual diff server vs client render.

### Architecture Perspective

Hydration is SSR tax — architects minimize mismatch and duplicate fetch.

### Follow-up Questions

1. **Selective hydration? — React 18+ prioritize interactive regions.**
2. **Streaming hydration? — Progressive — improve TTFB to interactive gap.**

### Common Mistakes in Interviews

- Date.now() in SSR render — mismatch guaranteed
- No serialized state — client refetch waterfall
- Ignore hydration warnings in console

---

## Q049: CSR SPA When Appropriate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SSR/CSR |
| **Frequency** | Common |

### Question

When is pure CSR the right frontend architecture choice?

### Short Answer (30 seconds)

CSR fits authenticated internal apps, dashboards behind login, heavy interactivity with no SEO need — simpler deploy as static assets on CDN.

### Detailed Answer (3–5 minutes)

**CSR wins when:**
- No public SEO pages
- Complex client-only interactions (editors, dashboards)
- Team expertise Vite/React SPA
- Compliance prefers static hosting

**Trade-off:** slower first contentful paint — acceptable on VPN internal tools.

**Architect:** Document SEO/NFR justification in ADR — revisit if marketing pages added.

### Architecture Perspective

CSR is valid enterprise choice — not legacy by default.

### Follow-up Questions

1. **Prerender marketing only? — Hybrid — prerender.io or separate Next marketing site.**
2. **SEO for SPA? — meta management limited — prerender or SSR for public pages.**

### Common Mistakes in Interviews

- CSR for public product catalog needing Google index
- No loading skeleton — white screen perception
- Choose CSR only because team avoids Node hosting

---

## Q050: LCP Largest Contentful Paint

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Core Web Vitals |
| **Frequency** | Very Common |

### Question

Architect frontend changes to improve Largest Contentful Paint.

### Short Answer (30 seconds)

LCP measures largest visible element paint — usually hero image or H1 block. Optimize via CDN, preload, SSR critical HTML, compress images, eliminate render-blocking CSS/JS.

### Detailed Answer (3–5 minutes)

**Tactics:**
- `fetchpriority=high` on LCP image
- WebP/AVIF responsive `srcset`
- Inline critical CSS for above-fold
- Remove blocking third-party scripts from head

**Target:** LCP <2.5s at p75 mobile.

**Architect:** RUM identifies actual LCP element per template — not guessed.

### Architecture Perspective

LCP drives SEO ranking and conversion — architecture not only CSS tweak.

### Follow-up Questions

1. **LCP vs FCP? — FCP first paint any content; LCP main content — optimize LCP element.**
2. **Client-side render LCP? — Delayed until JS — SSR/SSG for public LCP pages.**

### Common Mistakes in Interviews

- Huge unoptimized hero PNG
- LCP element lazy-loaded — paradoxically slower
- Measure desktop lab only — mobile LCP fails

---

## Q051: INP Interaction to Next Paint

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Core Web Vitals |
| **Frequency** | Common |

### Question

Reduce Interaction to Next Paint in complex SPAs.

### Short Answer (30 seconds)

INP measures responsiveness across all interactions — long main-thread tasks delay feedback. Split JS, defer work, use web workers, virtualize lists.

### Detailed Answer (3–5 minutes)

**Techniques:**
- Break tasks <50ms — `scheduler.yield()`
- Debounce expensive handlers
- Virtual scroll for tables
- Offload parsing to worker

**Target:** INP <200ms p75.

**Architect:** INP regression gates in CI RUM synthetic — block releases on spike.

### Architecture Perspective

INP replaced FID — holistic interactivity metric — SPA-heavy sites must architect for it.

### Follow-up Questions

1. **React concurrent features? — `startTransition` deprioritize non-urgent updates.**
2. **Third-party impact? — Tag manager scripts — measure INP with/without.**

### Common Mistakes in Interviews

- Synchronous JSON parse of 5MB on click
- Re-render entire tree on keystroke
- No performance profiling before launch

---

## Q052: CLS Cumulative Layout Shift

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Core Web Vitals |
| **Frequency** | Common |

### Question

Prevent Cumulative Layout Shift in SPA and SSR applications.

### Short Answer (30 seconds)

Reserve space for images, ads, fonts, and async content — width/height attributes, aspect-ratio CSS, skeleton placeholders, font-display swap.

### Detailed Answer (3–5 minutes)

**Common CLS causes:**
- Images without dimensions
- Web fonts FOIT/FOUT
- Dynamic banners injected above content
- Client-rendered charts replacing placeholder

**Target:** CLS <0.1 p75.

**Architect:** Design system components embed dimension contracts — Card always min-height.

### Architecture Perspective

CLS is trust metric — jumping buttons cause mis-clicks and frustration.

### Follow-up Questions

1. **Skeleton loaders? — Fixed height skeletons — not collapsing spinners.**
2. **A/B test banners? — Reserve slot — inject without push.**

### Common Mistakes in Interviews

- Ads load without reserved slot
- Icon font without fallback metrics
- Modal opens without scroll lock causing shift

---

## Q053: Tree Shaking and Side Effects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Bundle Optimization |
| **Frequency** | Very Common |

### Question

Configure packages for effective tree shaking in production bundles.

### Short Answer (30 seconds)

Use ES modules, `sideEffects: false` in package.json when safe, import specific functions not barrel files, verify with bundle analyzer.

### Detailed Answer (3–5 minutes)

**Example:**
```js
import debounce from 'lodash-es/debounce'; // not import _ from 'lodash'
```

**Library audit:** moment → dayjs; full icon pack → per-icon import.

**Architect:** Dependency weight review in ADR for any lib >20KB gzip.

### Architecture Perspective

Tree shaking is architecture decision at import and dependency choice.

### Follow-up Questions

1. **Barrel files? — Re-export can defeat shaking — import from deep path.**
2. **sideEffects false incorrectly? — CSS imports dropped — test thoroughly.**

### Common Mistakes in Interviews

- Import entire lodash
- CommonJS-only library in ESM app — no shake
- No bundle analyzer in CI

---

## Q054: Route Level Code Splitting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Bundle Optimization |
| **Frequency** | Very Common |

### Question

Implement route-level code splitting in enterprise SPA.

### Short Answer (30 seconds)

Each route lazy-loaded via dynamic import — separate chunk per feature — reduces initial JS to login shell + home only.

### Detailed Answer (3–5 minutes)

**React:** `const Admin = lazy(() => import('./Admin'))`
**Angular:** `loadChildren` or `loadComponent`

**Prefetch:** hover or `requestIdleCallback` prefetch likely next route.

**Architect:** Initial bundle budget ADR — e.g. 200KB gzip — CI enforces.

### Architecture Perspective

Route splitting is default — monolithic bundle is anti-pattern at scale.

### Follow-up Questions

1. **Named chunks? — webpack magic comment `/* webpackChunkName: "checkout" */`.**
2. **Shared chunk strategy? — splitChunks vendor — balance cache vs parallel load.**

### Common Mistakes in Interviews

- Admin routes in main bundle
- Lazy route without Suspense/loading UI
- Duplicate dependencies across chunks unoptimized

---

## Q055: Design Token Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Systems |
| **Frequency** | Very Common |

### Question

Structure design tokens for multi-brand enterprise design system.

### Short Answer (30 seconds)

Tokens as JSON — primitive (color.blue.500), semantic (color.text.primary), component (button.primary.bg) — compiled to CSS variables, Tailwind preset, iOS plist.

### Detailed Answer (3–5 minutes)

**Pipeline:**
Figma Tokens → JSON repo → Style Dictionary build → `@corp/tokens` npm package

**Theming:** brand A/B override semantic layer only.

**Architect:** Token breaking change = major semver — consumers pin consciously.

### Architecture Perspective

Tokens are API between design and engineering — version like code.

### Follow-up Questions

1. **Dark mode? — Semantic tokens flip — not hardcoded hex in components.**
2. **Spacing scale? — 4px base grid — document exceptions.**

### Common Mistakes in Interviews

- Hex colors hardcoded in 400 components
- Tokens only in Figma — not in code pipeline
- No deprecation path for renamed tokens

---

## Q056: Storybook Contract Testing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Systems |
| **Frequency** | Common |

### Question

Use Storybook as component contract layer in design system architecture.

### Short Answer (30 seconds)

Each primitive has stories for states (default, disabled, error, loading); visual regression via Chromatic; a11y addon axe scan — consumers trust stable props API.

### Detailed Answer (3–5 minutes)

**CI gates:**
- Storybook build on PR
- Visual diff approval
- a11y violations block merge

**Architect:** Design system is product — Storybook is living documentation and test harness.

### Architecture Perspective

Storybook prevents design system drift — architectural quality gate.

### Follow-up Questions

1. **Composition stories? — Document slot patterns — not only isolated button.**
2. **MDX docs? — Usage guidelines alongside stories — architects onboard teams.**

### Common Mistakes in Interviews

- Storybook only local — never CI
- Stories outdated vs component API
- No accessibility addon scans

---

## Q057: GraphQL Client Cache Normalization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | GraphQL |
| **Frequency** | Common |

### Question

Explain Apollo Client normalized cache architecture.

### Short Answer (30 seconds)

Apollo stores objects by `__typename + id` — updates propagate to all queries referencing entity — reduces redundant network fetches.

### Detailed Answer (3–5 minutes)

**Patterns:**
- `cache.modify` after mutation
- `fetchPolicy: cache-and-network` for fresh + fast
- Type policies for merge behavior on paginated lists

**Architect:** Cache policy ADR — stale data bugs are cross-team incidents.

### Architecture Perspective

Normalized cache is GraphQL frontend superpower — also complexity source.

### Follow-up Questions

1. **Evict vs garbage collect? — `cache.evict` on logout — clear PII.**
2. **Partial data? — `possibleTypes` for fragments — union/interface config.**

### Common Mistakes in Interviews

- fetchPolicy network-only everywhere — no cache benefit
- Paginated list merge wrong — duplicate rows
- PII remains in cache after logout

---

## Q058: GraphQL Query Cost Limits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | GraphQL |
| **Frequency** | Common |

### Question

Protect GraphQL gateway from expensive client queries.

### Short Answer (30 seconds)

Enforce depth/complexity limits, persisted queries in production, rate limit per client, cost analysis before execution.

### Detailed Answer (3–5 minutes)

**Production:**
- APQ allowlist only
- Max depth 10, complexity score 1000
- Reject introspection publicly

**Architect:** GraphQL DoS is real — gateway limits are architecture not optional.

### Architecture Perspective

GraphQL flexibility requires server-side cost governance.

### Follow-up Questions

1. **DataLoader? — Batch N+1 resolvers — BFF/gateway pattern.**
2. **Federation cost? — Sum subgraph costs — federated gateway enforces.**

### Common Mistakes in Interviews

- Arbitrary client queries in production
- No depth limit — stack overflow / DB melt
- Introspection enabled on public endpoint

---

## Q059: WebSocket Heartbeat Reconnect

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | WebSockets |
| **Frequency** | Very Common |

### Question

Design heartbeat and reconnection for SPA WebSocket clients.

### Short Answer (30 seconds)

Client sends ping or responds to server heartbeat; on disconnect exponential backoff reconnect with jitter; resubscribe channels; replay missed events from last sequence id.

### Detailed Answer (3–5 minutes)

**Client state machine:**
```
Connected → Disconnected → Backoff → Reconnecting → Resync
```

**Server:** idle timeout 60s; graceful drain on deploy.

**Architect:** Real-time SLI includes reconnect success rate — not only message latency.

### Architecture Perspective

Reconnect architecture prevents silent stale dashboards.

### Follow-up Questions

1. **Sticky sessions? — Prefer Redis backplane over sticky for scale.**
2. **Token expiry on connection? — Force reconnect with fresh token before drop.**

### Common Mistakes in Interviews

- No reconnect — user sees frozen prices
- Immediate reconnect storm after outage
- Missed messages never backfilled

---

## Q060: WebSocket Auth on Connect

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | WebSockets |
| **Frequency** | Common |

### Question

Authenticate WebSocket connections in enterprise SPA architecture.

### Short Answer (30 seconds)

Validate JWT or session on HTTP upgrade request; short-lived connection token; re-auth on reconnect; authorize per-channel subscription server-side.

### Detailed Answer (3–5 minutes)

**Patterns:**
- `Sec-WebSocket-Protocol` carries token — or query param with caution
- BFF issues one-time `wss_ticket` after session valid
- SignalR `[Authorize]` on hub methods

**Architect:** Never trust client channel join without server ACL check.

### Architecture Perspective

WebSocket auth is connection + per-message authorization.

### Follow-up Questions

1. **Query string token? — Logs leak — prefer post-connect auth message over TLS.**
2. **Azure Web PubSub? — Server validates upstream — built-in token service.**

### Common Mistakes in Interviews

- Subscribe to admin channel without server check
- Long-lived JWT in connection never refreshed
- Auth only on HTTP page not WS upgrade

---

## Q061: PWA Service Worker Caching

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PWA |
| **Frequency** | Common |

### Question

Choose service worker caching strategies for enterprise PWA.

### Short Answer (30 seconds)

Cache-first for hashed static assets; network-first for API; stale-while-revalidate for images; never cache authenticated API responses with PII.

### Detailed Answer (3–5 minutes)

**Workbox recipes:**
- `precacheAndRoute` build assets
- `NetworkFirst` for `/api/bootstrap`
- Offline fallback HTML page

**Architect:** SW update strategy documented — `skipWaiting` vs user prompt for refresh.

### Architecture Perspective

Service worker cache is offline architecture — wrong strategy leaks stale or private data.

### Follow-up Questions

1. **Cache versioning? — Hash in precache manifest — auto bump on build.**
2. **iOS PWA limits? — Test install and storage quotas separately.**

### Common Mistakes in Interviews

- Cache-first on personalized API
- SW never updates — users on week-old app
- No offline fallback UX

---

## Q062: PWA Offline Write Queue

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PWA |
| **Frequency** | Common |

### Question

Queue offline form submissions in PWA architecture.

### Short Answer (30 seconds)

Store pending mutations in IndexedDB; background sync or online event replays queue; idempotency keys prevent duplicate server writes.

### Detailed Answer (3–5 minutes)

**Flow:**
1. User submits offline → persist `{ idempotencyKey, payload, timestamp }`
2. `navigator.onLine` → replay FIFO
3. UI shows pending/synced/failed states

**Architect:** Idempotency mandatory — replay is not edge case on mobile field apps.

### Architecture Perspective

Offline write queue is distributed systems problem on client.

### Follow-up Questions

1. **Conflict resolution? — Last-write-wins or server merge — document per entity.**
2. **Quota exceeded? — IndexedDB cleanup policy for old synced items.**

### Common Mistakes in Interviews

- Duplicate submissions on replay without idempotency
- Queue not cleared after successful sync
- Sensitive PII in IndexedDB unencrypted

---

## Q063: RUM Correlation to Backend

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Frontend Observability |
| **Frequency** | Very Common |

### Question

Correlate frontend RUM traces with backend distributed tracing.

### Short Answer (30 seconds)

Inject `traceparent` header from RUM SDK on fetch; BFF propagates to microservices; single trace id in support tooling across browser span and DB query.

### Detailed Answer (3–5 minutes)

**Stack:**
- App Insights / Datadog RUM + APM
- W3C Trace Context standard
- Custom attributes: `userId` hashed, `tenantId`, `release`

**Architect:** End-to-end traces cut MTTR — frontend team owns propagation initiation.

### Architecture Perspective

Without correlation, backend green while users hit client timeout.

### Follow-up Questions

1. **CORS expose trace headers? — `Access-Control-Expose-Headers: traceparent`.**
2. **Sampling? — 100% on errors; head-based sample on happy path.**

### Common Mistakes in Interviews

- No trace header from SPA
- Different trace format per service
- PII in trace attributes

---

## Q064: Frontend Error Tracking Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Frontend Observability |
| **Frequency** | Common |

### Question

Design frontend error tracking and alerting architecture.

### Short Answer (30 seconds)

Capture unhandled errors and promise rejections; source maps in secure vault; fingerprint dedupe; alert on new error spike or checkout error rate SLO breach.

### Detailed Answer (3–5 minutes)

**Tiers:**
- P0: payment/checkout JS error → page
- P1: feature module error rate >1%
- P2: deprecated browser quirks

**Architect:** Error budget for client-side — tie to release rollback policy.

### Architecture Perspective

Client errors are production incidents — architecture includes RUM alerting.

### Follow-up Questions

1. **Source maps public? — Never — upload to Sentry/App Insights private.**
2. **Session replay? — Sampled; mask PII fields — GDPR consent.**

### Common Mistakes in Interviews

- No client error monitoring
- Alert on every single JS error — noise
- Source maps exposed on CDN

---

## Q065: CDN Immutable Asset Hashing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | CDN |
| **Frequency** | Very Common |

### Question

Configure CDN caching with content-hashed static assets.

### Short Answer (30 seconds)

Filenames include content hash — `app.a1b2c3.js` — `Cache-Control: immutable, max-age=31536000` — only `index.html` short cache.

### Detailed Answer (3–5 minutes)

**Deploy:**
```
upload dist/* → blob
index.html: no-cache
*.[hash].js: immutable
```

**Rollback:** deploy previous hash set — instant.

**Architect:** Hash strategy prevents stale JS after deploy — users never hard-refresh.

### Architecture Perspective

Immutable hashed assets are SPA CDN foundation.

### Follow-up Questions

1. **Purging? — Purge index.html only — not every JS file.**
2. **Far future expires? — Pair immutable with hash — safe long TTL.**

### Common Mistakes in Interviews

- Overwrite app.js in place — users cached old bundle
- index.html cached 1 year
- No cache bust on deploy

---

## Q066: CDN API Origin Separation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | CDN |
| **Frequency** | Common |

### Question

Separate CDN origins for static assets vs API traffic.

### Short Answer (30 seconds)

Static on `cdn.corp.com` blob; API on `api.corp.com` BFF; different cache policies, WAF rules, and TLS certs — prevents API cookies on static domain.

### Detailed Answer (3–5 minutes)

**Benefits:**
- Static max cache; API no cache
- DDoS profile differs — rate limit API only
- CSP `connect-src` explicit

**Architect:** Domain architecture diagram shows static/API split — security review standard.

### Architecture Perspective

Origin separation reduces blast radius and clarifies cache policy.

### Follow-up Questions

1. **Same domain path split? — `/static` vs `/api` on one host — viable but cookie scope careful.**
2. **Azure Front Door? — Multi-origin routing rules — single entry hostname possible.**

### Common Mistakes in Interviews

- API and static share cookie domain unnecessarily
- CDN caches 401 API responses
- CORS complexity because origins tangled

---

## Q067: Content Security Policy Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security Headers |
| **Frequency** | Very Common |

### Question

Draft a Content Security Policy for enterprise React SPA.

### Short Answer (30 seconds)

Restrict script-src to self + nonce; connect-src to BFF and analytics; frame-ancestors none; default-src self; report-uri for violation monitoring.

### Detailed Answer (3–5 minutes)

**Starter CSP:**
```
default-src 'self';
script-src 'self' 'nonce-{random}';
connect-src 'self' https://api.corp.com;
img-src 'self' data: https:;
frame-ancestors 'none';
```

**Rollout:** Report-Only mode first — collect violations — then enforce.

**Architect:** CSP template per environment — stricter prod than dev.

### Architecture Perspective

CSP is XSS mitigation architecture — nonce per HTML response.

### Follow-up Questions

1. **unsafe-inline? — Avoid in prod — breaks XSS protection.**
2. **Third-party analytics? — Specific script-src host — not blanket allow.**

### Common Mistakes in Interviews

- CSP unsafe-inline everywhere
- No report-uri — blind to violations
- CSP only on API not HTML shell

---

## Q068: HSTS and Security Header Bundle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security Headers |
| **Frequency** | Common |

### Question

Which security headers should BFF set on SPA HTML shell responses?

### Short Answer (30 seconds)

HSTS, CSP, X-Content-Type-Options nosniff, Referrer-Policy strict-origin-when-cross-origin, Permissions-Policy limiting geolocation/camera, X-Frame-Options or CSP frame-ancestors.

### Detailed Answer (3–5 minutes)

**BFF middleware** applies headers to `index.html` and API responses consistently.

**HSTS:** `max-age=31536000; includeSubDomains` after HTTPS verified.

**Architect:** Header bundle in IaC/CDN rule template — drift detection in security scan.

### Architecture Perspective

Security headers are cheap baseline — architect standardizes via platform.

### Follow-up Questions

1. **HSTS preload? — Only when committed to HTTPS everywhere — irreversible.**
2. **Permissions-Policy? — Disable unused APIs — reduce attack surface.**

### Common Mistakes in Interviews

- Missing nosniff — MIME sniff attacks
- Allow framing — clickjacking risk
- Different headers CDN vs origin — inconsistent protection

---

## Q069: Module Federation Remote Versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Module Federation |
| **Frequency** | Common |

### Question

Version and deploy module federation remotes independently.

### Short Answer (30 seconds)

Semver remote entries; shell declares compatible range; integration tests on shell+remote matrix; feature flags gate new remote versions.

### Detailed Answer (3–5 minutes)

**Deploy:**
- Remote builds `remoteEntry.js` to versioned path
- Shell config points to prod remote URL
- Canary remote for subset of users

**Architect:** MFE release train doc — shell team not bottleneck for remote deploys.

### Architecture Perspective

Independent deploy is MFE value — versioning prevents runtime incompatibility.

### Follow-up Questions

1. **Runtime plugin? — Dynamic remote URL from config service.**
2. **Rollback remote? — Repoint URL to previous remoteEntry — fast revert.**

### Common Mistakes in Interviews

- Breaking remote API without shell update
- No integration test matrix
- remoteEntry cached immutable incorrectly

---

## Q070: WCAG Keyboard Navigation SPA

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Accessibility |
| **Frequency** | Very Common |

### Question

Ensure keyboard navigation works in client-side routed SPAs.

### Short Answer (30 seconds)

Focus management on route change, skip links, logical tab order, visible focus rings, trap focus in modals, announce route changes via aria-live.

### Detailed Answer (3–5 minutes)

**Checklist:**
- Move focus to `h1` on navigate
- `aria-current='page'` on nav
- Escape closes modal restoring focus
- No `tabindex=-1` on interactive elements

**Architect:** a11y acceptance criteria per epic — same priority as functional AC.

### Architecture Perspective

SPA routing breaks accessibility if focus not managed — lawsuit and compliance risk.

### Follow-up Questions

1. **WCAG 2.1 AA? — Enterprise standard — keyboard operable is Level A minimum.**
2. **Automated axe? — Catches ~30% — manual keyboard test required.**

### Common Mistakes in Interviews

- Click-only interactions no keyboard equivalent
- Focus lost on route change — user disoriented
- Custom div buttons without role/tabindex

---
