# Week 43 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: React Concurrent Rendering Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | React Patterns |
| **Frequency** | Common |

### Question

When adopt React concurrent features and what operational risks follow?

### Short Answer (30 seconds)

Concurrent rendering enables interruptible updates, transitions, and Suspense — improves INP but adds debugging complexity and requires compatible libraries.

### Detailed Answer (3–5 minutes)

**Adopt when:**
- Large lists with filtering causing jank
- Heavy dashboard re-renders on real-time data
- Willing to upgrade ecosystem (Router, Query)

**Risks:**
- Third-party libs not concurrent-safe
- Harder repro race bugs
- SSR streaming coordination

**Architect:** Pilot on internal admin before customer checkout — measure INP delta.

### Architecture Perspective

Concurrent mode is performance architecture with ecosystem dependency cost.

### Follow-up Questions

1. **startTransition vs debounce? — Transition marks low-priority — keeps input responsive.**
2. **Strict Mode double render? — Surfaces side effects — fix before concurrent prod.**

### Common Mistakes in Interviews

- Enable concurrent without profiling baseline
- Legacy class components with unsafe lifecycles
- Assume all hooks libraries concurrent-ready

---

## Q072: Angular Signals Migration Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Angular Patterns |
| **Frequency** | Common |

### Question

Plan incremental migration from RxJS-heavy state to Angular signals.

### Short Answer (30 seconds)

Introduce signals in leaf components; `computed` for derived state; `toSignal` bridge observables; keep RxJS at HTTP boundary; avoid big-bang rewrite.

### Detailed Answer (3–5 minutes)

**Phases:**
1. New components signal-first
2. `input()`/`output()` instead of decorators
3. Facades expose signals + observables during transition
4. Remove redundant BehaviorSubjects

**Architect:** Migration ADR with team training — signals change mental model.

### Architecture Perspective

Signals simplify Angular change detection — migration is multi-quarter program.

### Follow-up Questions

1. **signal vs computed? — computed pure derivation — no side effects.**
2. **Zoneless preview? — Signals prepare for zone.js optional future.**

### Common Mistakes in Interviews

- Rewrite entire NgRx to signals in one sprint
- Mix signals and mutateOn push inputs
- Drop RxJS before HTTP layer migrated

---

## Q073: Redux Toolkit vs React Query Split

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | State Management |
| **Frequency** | Common |

### Question

Define ownership boundary between Redux Toolkit and TanStack Query.

### Short Answer (30 seconds)

React Query owns server cache; RTK slices own UI session, wizard, optimistic cart draft; RTK Query only if consolidating on Redux stack.

### Detailed Answer (3–5 minutes)

**Decision matrix:**
| Data type | Owner |
|-----------|-------|
| API entities | React Query |
| Auth session UI | Context or RTK |
| Multi-step form | RTK or Zustand |
| URL filters | Router search params |

**Architect:** One-page state ownership diagram in repo — prevents duplicate caches.

### Architecture Perspective

Dual state libraries OK with clear boundaries — chaos without documentation.

### Follow-up Questions

1. **Normalize across both? — Don't duplicate same entity in Redux and Query.**
2. **DevTools? — Both enabled in dev — correlate action vs query invalidation.**

### Common Mistakes in Interviews

- Same order list in Redux and Query
- Invalidate Query from every Redux action
- No documented ownership rules

---

## Q074: BFF Saga Orchestration Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | BFF |
| **Frequency** | Common |

### Question

Implement long-running multi-step orchestration in BFF without distributed transactions.

### Short Answer (30 seconds)

Saga pattern: choreographed events or BFF orchestrator with compensating actions; idempotent steps; state machine persisted for resume.

### Detailed Answer (3–5 minutes)

**Checkout saga:**
1. Reserve inventory
2. Authorize payment
3. Confirm order
4. On failure: release inventory, void auth

**Storage:** saga instance id in Redis/DB.

**Architect:** Never 2PC across microservices — saga with explicit compensations.

### Architecture Perspective

BFF orchestration is frontend-facing saga — architects own failure semantics.

### Follow-up Questions

1. **Temporal in BFF? — Durable workflows — heavy but reliable for complex flows.**
2. **Sync HTTP chain? — Timeout cascade — async saga preferred >3 steps.**

### Common Mistakes in Interviews

- Distributed two-phase commit from BFF
- No compensation on payment failure after inventory hold
- Saga state only in memory — lost on restart

---

## Q075: BFF Stale Aggregate Caching

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | BFF |
| **Frequency** | Common |

### Question

Cache aggregated BFF responses without serving stale critical data.

### Short Answer (30 seconds)

TTL by data sensitivity; cache key includes user/tenant; event-driven invalidation for inventory/price; `stale-while-revalidate` for homepage aggregates only.

### Detailed Answer (3–5 minutes)

**Tiers:**
- Product catalog: 60s TTL + event invalidation
- User profile: no cache or 10s private
- Cart: never shared cache

**Architect:** Cache tier matrix in BFF ADR — auditors ask about stale price risk.

### Architecture Perspective

BFF cache improves p99 — wrong TTL on prices is revenue/legal risk.

### Follow-up Questions

1. **Redis vs in-memory? — Redis for multi-instance BFF; local for dev only.**
2. **Stampede? — Single-flight lock on cache miss rebuild.**

### Common Mistakes in Interviews

- Cache checkout totals cross-user
- Infinite TTL on volatile prices
- No invalidation on promotion start event

---

## Q076: MFE Independent Deploy Pipelines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Micro-Frontends |
| **Frequency** | Common |

### Question

Design CI/CD so micro-frontends deploy without shell redeploy.

### Short Answer (30 seconds)

Each remote has own pipeline publishing `remoteEntry.js` to versioned storage; shell loads URL from config; contract tests gate breaking changes.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```
MFE PR → build → deploy remoteEntry → integration test vs prod shell stub → promote
```

**Architect:** Deploy decoupling is MFE ROI — without it, MFE complexity unjustified.

### Architecture Perspective

Independent deploy requires contract discipline — not cowboy releases.

### Follow-up Questions

1. **Blue/green remote? — Two URLs — config switch — instant rollback.**
2. **Feature flag in remote? — Remote reads flag service — gradual UI rollout.**

### Common Mistakes in Interviews

- Shell must redeploy for every remote change
- remoteEntry overwritten without version path
- No contract test on shared dependency bump

---

## Q077: MFE Cross-Team Contract Tests

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Micro-Frontends |
| **Frequency** | Common |

### Question

Implement contract testing between shell and micro-frontend remotes.

### Short Answer (30 seconds)

Consumer-driven contracts: shell declares expected remote exports; Pact or custom integration test loads remote in CI; fail build on export mismatch.

### Detailed Answer (3–5 minutes)

**Test matrix:**
- Shell v2.3 + Checkout MFE v1.8 ✓
- Shell v2.3 + Checkout MFE v2.0 ✗ breaking export

**Architect:** Compatibility matrix published — ops knows valid combinations.

### Architecture Perspective

Contract tests prevent Friday remote deploy breaking Monday shell.

### Follow-up Questions

1. **Pact for JS modules? — Less common than API Pact — integration tests often suffice.**
2. **Visual contract? — Storybook compose — shell renders remote stories in CI.**

### Common Mistakes in Interviews

- Integration discovered only in production
- Remote removes export without semver major
- No documented compatibility matrix

---

## Q078: OIDC BFF Token Exchange

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | OIDC Auth |
| **Frequency** | Common |

### Question

Implement OAuth token exchange at BFF for downstream service calls.

### Short Answer (30 seconds)

BFF holds user session; exchanges for service-specific token via OBO (on-behalf-of) or client credentials with user context propagation — never forward browser access token to all microservices.

### Detailed Answer (3–5 minutes)

**Azure:** `acquireTokenOnBehalfOf` with user assertion.
**Pattern:** BFF is only confidential client microservices trust.

**Architect:** Token flow diagram in security review — scopes minimized per downstream.

### Architecture Perspective

Token exchange centralizes trust — browser token is insufficient for service mesh.

### Follow-up Questions

1. **Pass-through JWT? — Anti-pattern — broad scopes in browser — use BFF exchange.**
2. **Token caching BFF? — Cache downstream tokens in memory with expiry buffer.**

### Common Mistakes in Interviews

- Browser access token attached to every microservice call
- Refresh token exposed to SPA for exchange
- No scope restriction per downstream

---

## Q079: CSRF Defense with WebSockets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CSRF |
| **Frequency** | Common |

### Question

Extend CSRF protections when SPA uses cookie auth and WebSockets.

### Short Answer (30 seconds)

Validate Origin on WebSocket upgrade; use CSRF token in upgrade request header; same-site cookies; per-connection auth after upgrade not just cookie presence.

### Detailed Answer (3–5 minutes)

**Checklist:**
- `Origin` header matches allowlist
- CSRF token in `Sec-WebSocket-Protocol` or first message
- Revalidate session on sensitive subscribe

**Architect:** WebSocket CSRF often forgotten — include in threat model.

### Architecture Perspective

Cookies sent on WS upgrade — CSRF subscription attack possible without Origin check.

### Follow-up Questions

1. **CORS vs WS Origin? — WS uses Origin header — not CORS preflight.**
2. **SignalR antiforgery? — Built-in token for negotiate endpoint.**

### Common Mistakes in Interviews

- Accept WS from any Origin
- Auth cookie alone on upgrade without validation
- Assume Bearer-only when using cookies

---

## Q080: SSR Edge Middleware Auth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SSR/CSR |
| **Frequency** | Common |

### Question

Enforce authentication at edge middleware before SSR render.

### Short Answer (30 seconds)

Edge middleware (Vercel, Cloudflare Workers, Front Door rules) validates session cookie; redirect unauthenticated before origin SSR compute — saves cost and prevents data leak in HTML.

### Detailed Answer (3–5 minutes)

**Flow:**
```
Request → Edge validate JWT/session → pass headers to origin OR redirect /login
```

**Architect:** Edge auth reduces attack surface — origin never renders protected HTML for anonymous.

### Architecture Perspective

Edge auth is performance and security — fewer wasted SSR cycles.

### Follow-up Questions

1. **Middleware vs BFF? — Edge for coarse gate; BFF for fine permissions.**
2. **Geo routing? — Edge can route EU users to EU origin — GDPR.**

### Common Mistakes in Interviews

- SSR renders user PII before auth check
- Auth only client-side after hydration
- Edge and origin session validation inconsistent

---

## Q081: ISR Product Catalog Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SSR/CSR |
| **Frequency** | Common |

### Question

Use Incremental Static Regeneration for large product catalogs.

### Short Answer (30 seconds)

Pre-render top SKUs at build; on-demand ISR for long tail; revalidate interval 300s; stale-while-revalidate serves CDN cached page while regenerating.

### Detailed Answer (3–5 minutes)

**Next.js:** `revalidate: 300` on product page.
**Invalidation:** webhook from PIM on price change purges path.

**Architect:** ISR balances SEO, cost, and freshness — ADR defines revalidate per category sensitivity.

### Architecture Perspective

ISR is hybrid SSR/SSG — architects pick revalidate per merchandise type.

### Follow-up Questions

1. **On-demand revalidate API? — Secret-protected purge — instant price update.**
2. **Millions of SKUs? — Build top 10K; ISR on first request long tail.**

### Common Mistakes in Interviews

- SSR every product page every request — cost explosion
- Static only — prices stale days
- No webhook invalidation on flash sale

---

## Q082: Core Web Vitals CI Gates

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Core Web Vitals |
| **Frequency** | Common |

### Question

Enforce Core Web Vitals budgets in CI/CD pipeline.

### Short Answer (30 seconds)

Lighthouse CI on representative URLs; fail PR if LCP/INP/CLS regression >10%; RUM synthetic baseline; performance budget on bundle size correlated.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```
PR → deploy preview → Lighthouse CI → comment scores → block if regression
```

**Architect:** Vitals gates connect frontend arch to release policy — not optional nice-to-have.

### Architecture Perspective

CI vitals catch regressions before prod — complements RUM.

### Follow-up Questions

1. **Lab vs field? — Lab consistent; field noisy — both tracked.**
2. **Representative URLs? — Test worst pages — category with heavy images.**

### Common Mistakes in Interviews

- Lighthouse only on empty homepage
- No mobile emulation in CI
- Ignore 15% regression as noise always

---

## Q083: Bundle Budget Enforcement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Bundle Optimization |
| **Frequency** | Common |

### Question

Implement bundle size budgets with analyzer in CI.

### Short Answer (30 seconds)

size-limit or bundlesize on main + route chunks; webpack-bundle-analyzer artifact on failure; PR comment with diff table.

### Detailed Answer (3–5 minutes)

**Budget example:**
- main: 200KB gzip
- route-checkout: 80KB gzip
- total: 500KB gzip

**Architect:** Budget ADR signed by EM — exceptions need waiver.

### Architecture Perspective

Bundle budget is architectural governance — prevents death by dependency.

### Follow-up Questions

1. **Analyze trend? — Track main bundle over releases — graph in dashboard.**
2. **Who approves waiver? — Architect + EM — documented in PR.**

### Common Mistakes in Interviews

- Budget only on main not route chunks
- No PR diff comment — surprise growth
- Waiver becomes permanent

---

## Q084: Design System Contribution Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Design Systems |
| **Frequency** | Common |

### Question

Operate contribution model for enterprise design system.

### Short Answer (30 seconds)

RFC for new primitives; core team triages; consumers submit PRs with stories; office hours; governance council quarterly.

### Detailed Answer (3–5 minutes)

**Tiers:**
- **Core team** — merges primitives
- **Contributors** — patterns and recipes
- **Consumers** — issues and feedback

**Architect:** Design system without contribution model becomes bottleneck.

### Architecture Perspective

Contribution scales design system beyond central team.

### Follow-up Questions

1. **Fork vs upstream? — Teams fork buttons — merge back via contribution RFC.**
2. **Deprecation council? — Quarterly remove unused components.**

### Common Mistakes in Interviews

- Only design team can commit
- No RFC for breaking API change
- 50 duplicate PR buttons

---

## Q085: GraphQL Federation Frontend Impact

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | GraphQL |
| **Frequency** | Uncommon |

### Question

How does GraphQL federation affect frontend architecture?

### Short Answer (30 seconds)

Single graph endpoint; Apollo Router aggregates subgraphs; frontend unaware of service split but affected by query cost and partial errors.

### Detailed Answer (3–5 minutes)

**Frontend concerns:**
- Partial data errors in multi-subgraph query
- Increased latency variance
- Schema registry drives codegen client

**Architect:** Frontend codegen tied to schema CI — breaking schema fails client build.

### Architecture Perspective

Federation hides backend split — doesn't hide performance coupling.

### Follow-up Questions

1. **Entity keys? — Frontend benefits unified types — `@key` backend concern.**
2. **Error policy? — `errorPolicy: 'all'` show partial UI with banners.**

### Common Mistakes in Interviews

- Assume federation fixes N+1 automatically
- Client bypasses router to subgraph
- No handling partial GraphQL errors

---

## Q086: WebSocket Horizontal Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | WebSockets |
| **Frequency** | Common |

### Question

Scale WebSocket layer horizontally across multiple nodes.

### Short Answer (30 seconds)

Sticky sessions OR Redis/Azure Web PubSub backplane; partition connections; avoid in-memory-only pub/sub on multi-node.

### Detailed Answer (3–5 minutes)

**Azure Web PubSub:** managed scale — app server sends messages via service.
**Self-hosted:** Redis backplane for SignalR.

**Architect:** Capacity plan connections per node — load test 10K concurrent.

### Architecture Perspective

Stateful WebSocket requires backplane architecture — not just add pods.

### Follow-up Questions

1. **Sticky vs backplane? — Backplane preferred — even connection distribution.**
2. **Connection drain on deploy? — Graceful shutdown — clients reconnect.**

### Common Mistakes in Interviews

- Scale pods without backplane — split rooms
- Memory leak per connection unbounded
- No load test on connection count

---

## Q087: PWA Push Notification Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | PWA |
| **Frequency** | Common |

### Question

Design push notification architecture for enterprise PWA.

### Short Answer (30 seconds)

Service worker `push` event; VAPID keys; notification permission UX; backend notification service; user preference store; GDPR consent.

### Detailed Answer (3–5 minutes)

**Flow:**
Server → FCM/Web Push → SW → showNotification → click opens URL.

**Architect:** Push is opt-in architecture — respect quiet hours and unsubscribe.

### Architecture Perspective

Push extends PWA engagement — platform limits especially iOS.

### Follow-up Questions

1. **VAPID rotation? — Key rollover plan — dual keys during transition.**
2. **Payload size? — Minimal — fetch details on click — avoid PII in push body.**

### Common Mistakes in Interviews

- Push without user consent
- PII in notification text lock screen
- No handling permission denied gracefully

---

## Q088: Frontend SLO Dashboards

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Frontend Observability |
| **Frequency** | Common |

### Question

Define SLOs and dashboards for frontend reliability.

### Short Answer (30 seconds)

SLIs: JS error rate, LCP p75, API success from browser, checkout completion. SLO 99.5% error-free sessions; error budget drives release freeze.

### Detailed Answer (3–5 minutes)

**Dashboard panels:**
- Error rate by release version
- Vitals by geo
- BFF correlation failures

**Architect:** Frontend SLO on equal footing with API SLO — joint incident response.

### Architecture Perspective

Frontend SLO makes client quality measurable — not subjective.

### Follow-up Questions

1. **Error budget policy? — Exhausted budget → freeze features fix reliability.**
2. **Synthetic + RUM SLI? — Combine — synthetic for availability RUM for vitals.**

### Common Mistakes in Interviews

- Only backend SLOs defined
- No release version dimension
- SLO without error budget policy

---

## Q089: CDN Geo Failover Routing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CDN |
| **Frequency** | Common |

### Question

Architect CDN geo-routing with failover for global SPA users.

### Short Answer (30 seconds)

Anycast CDN primary; health probe origin; failover to secondary region origin; geo rules route EU traffic EU origin; TTL low on DNS failover layer.

### Detailed Answer (3–5 minutes)

**Retail peak:** pre-warm all edges; origin shield; tiered cache.

**Architect:** Failover drill quarterly — DNS TTL reality check.

### Architecture Perspective

CDN geo architecture affects GDPR residency and latency.

### Follow-up Questions

1. **Origin shield? — Collapse CDN hits to single mid-tier — protect origin.**
2. **Multi-CDN? — Active-passive — complex — retail sometimes justified.**

### Common Mistakes in Interviews

- Single origin US-only for EU customers
- Failover never tested
- DNS TTL 24h — slow failover

---

## Q090: HSTS Preload Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security Headers |
| **Frequency** | Uncommon |

### Question

Evaluate HSTS preload submission for public SPA domain.

### Short Answer (30 seconds)

HSTS preload lists domain in browsers — HTTPS only forever. Submit only after full HTTPS migration, includeSubDomains validated, no mixed content.

### Detailed Answer (3–5 minutes)

**Checklist:**
- All subdomains HTTPS
- Redirect HTTP→HTTPS
- max-age ≥31536000
- preload token header

**Architect:** Irreversible — legal and ops sign-off before preload.

### Architecture Perspective

HSTS preload is strong commitment — architects verify entire domain estate.

### Follow-up Questions

1. **Remove from preload? — Very difficult — plan before submit.**
2. **Dev subdomains? — Ensure HTTPS or exclude from includeSubDomains.**

### Common Mistakes in Interviews

- Submit preload with HTTP marketing subdomain
- Mixed content on CDN
- No rollback plan documented

---

## Q091: Module Federation Runtime Plugins

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Module Federation |
| **Frequency** | Uncommon |

### Question

Use module federation runtime plugins for advanced MFE integration.

### Short Answer (30 seconds)

Runtime plugins intercept remote loading, shared init, error handling — customize retry, logging, version negotiation.

### Detailed Answer (3–5 minutes)

**Use cases:**
- Retry remoteEntry load 3 times
- Telemetry on remote load latency
- Override shared module resolution

**Architect:** Plugins are power tool — document centrally — avoid per-team hacks.

### Architecture Perspective

Runtime plugins extend federation — operational maturity feature.

### Follow-up Questions

1. **@module-federation/enhanced? — Runtime APIs evolve — pin versions.**
2. **Error boundary per remote load? — Plugin + React boundary combo.**

### Common Mistakes in Interviews

- Unhandled remote load failure white screen
- Plugin logic diverges per MFE team
- No telemetry on remote load failures

---

## Q092: Accessibility CI Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Accessibility |
| **Frequency** | Common |

### Question

Integrate accessibility testing into frontend CI pipeline.

### Short Answer (30 seconds)

axe-core in Playwright e2e; Storybook a11y addon; eslint-plugin-jsx-a11y; block PR on critical violations; manual checklist for releases.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```
PR → unit → Storybook build → axe scan → e2e keyboard smoke
```

**Architect:** a11y CI gate required for public sector contracts.

### Architecture Perspective

Automated a11y CI catches regressions — manual still required.

### Follow-up Questions

1. **False positives? — Triage rules — allowlist with ticket for exceptions.**
2. **VPAT evidence? — Export axe reports per release for compliance folder.**

### Common Mistakes in Interviews

- a11y only manual before launch once
- axe not run on modal dialogs
- Ignore contrast failures as cosmetic

---

## Q093: Third-Party Script Governance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Core Web Vitals |
| **Frequency** | Common |

### Question

Govern third-party scripts impacting Core Web Vitals.

### Short Answer (30 seconds)

Tag manager inventory; load analytics after `load` event; SRI on external scripts; performance budget per vendor; block new scripts without architect approval.

### Detailed Answer (3–5 minutes)

**Process:**
Marketing requests script → perf review → staged load → RUM measure INP delta.

**Architect:** Third-party council approves tags — INP regressions are incidents.

### Architecture Perspective

Tag sprawl kills INP — governance is architecture.

### Follow-up Questions

1. **Partytown? — Web worker offload for analytics scripts.**
2. **Google Tag Manager? — Container audit monthly — remove unused tags.**

### Common Mistakes in Interviews

- Unlimited marketing pixels
- Sync script in head blocking render
- No owner for tag inventory

---

## Q094: Vite vs Webpack Bundler ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Bundle Optimization |
| **Frequency** | Common |

### Question

Choose Vite vs Webpack for enterprise SPA bundler.

### Short Answer (30 seconds)

Vite: fast dev ESM, Rollup prod — greenfield default. Webpack: mature Module Federation, complex legacy loaders — MFE or legacy often Webpack.

### Detailed Answer (3–5 minutes)

**Decision factors:**
- MFE federation maturity
- Existing webpack config investment
- Dev experience priority
- Plugin ecosystem needs

**Architect:** Bundler ADR — migration cost quantified — not trend-driven.

### Architecture Perspective

Bundler choice affects MFE, CI time, and hiring — ADR warranted.

### Follow-up Questions

1. **Rspack? — Webpack-compatible faster — migration middle path.**
2. **esbuild? — Vite uses esbuild dev — prod Rollup.**

### Common Mistakes in Interviews

- Webpack solely because 'always used it'
- Mix Vite app with Webpack MFE without plan
- No perf comparison dev build times

---

## Q095: API Client Codegen Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | BFF |
| **Frequency** | Common |

### Question

Generate TypeScript API client from BFF OpenAPI spec.

### Short Answer (30 seconds)

CI generates `api-client` package from OpenAPI on BFF merge; consumers import typed functions; breaking change fails client build.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```
BFF OpenAPI → openapi-generator → packages/api-client → npm workspace
```

**Architect:** Contract-first — BFF publishes schema before frontend implements.

### Architecture Perspective

Codegen eliminates hand-written fetch typos — architecture for API evolution.

### Follow-up Questions

1. **openapi-fetch vs axios codegen? — Lighter runtime — team preference.**
2. **Version pinning? — Client major matches BFF API version.**

### Common Mistakes in Interviews

- Hand-written fetch URLs diverge from BFF
- OpenAPI not updated in CI
- Breaking API change undetected until runtime

---

## Q096: Feature Flag Taxonomy Frontend

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Frontend |
| **Frequency** | Common |

### Question

Define feature flag taxonomy for frontend architecture.

### Short Answer (30 seconds)

Release flags (short-lived), experiment flags (A/B), ops kill switches (permanent), permission flags (entitlement). Server evaluation for security; client for UI-only.

### Detailed Answer (3–5 minutes)

**Naming:** `release.checkout-v2`, `ops.disable-recommendations`, `exp.hero-banner-b`.

**Architect:** Flag registry with owner and expiry — quarterly cleanup sprint.

### Architecture Perspective

Flag taxonomy prevents security flags client-tamperable.

### Follow-up Questions

1. **Kill switch drill? — Quarterly verify ops can disable feature in 60s.**
2. **Same flag service backend+frontend? — Unified Azure App Config.**

### Common Mistakes in Interviews

- Permanent flags become undeletable debt
- Security gate only client flag
- No expiry on release flags

---

## Q097: Micro-Frontend Shared Router State

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Micro-Frontends |
| **Frequency** | Uncommon |

### Question

Share routing state between shell and micro-frontends.

### Short Answer (30 seconds)

Shell owns browser history; remotes receive basename; custom events or shared router library for cross-MFE navigation; avoid multiple History API listeners.

### Detailed Answer (3–5 minutes)

**Pattern:**
```
shell.navigate('/checkout/shipping') → loads checkout MFE route
```

**Architect:** Navigation contract documented — query param namespaced per MFE.

### Architecture Perspective

Shared router state is MFE integration pain point — explicit contract needed.

### Follow-up Questions

1. **single-spa? — Framework orchestrates mount/unmount lifecycle.**
2. **Deep link across MFE? — Shell parses URL delegates to remote.**

### Common Mistakes in Interviews

- Two routers fight popstate
- Query params collision between MFEs
- Remote changes URL outside its prefix

---

## Q098: NgRx Effects vs React Query

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | State Management |
| **Frequency** | Uncommon |

### Question

Compare NgRx effects orchestrating API vs TanStack Query in Angular/React.

### Short Answer (30 seconds)

Effects for complex multi-action orchestration; Query for fetch/cache/invalidation — prefer Query for CRUD; effects for saga-like workflows.

### Detailed Answer (3–5 minutes)

**Angular modern:** `@ngrx/signals` + `@tanstack/angular-query-experimental` emerging split.

**Architect:** Pick one HTTP cache strategy per app — dual cache bugs.

### Architecture Perspective

Effects excel at orchestration not caching — architects separate concerns.

### Follow-up Questions

1. **Effect infinite loop? — Wrong `switchMap` — architectural code review.**
2. **RTK Query Angular equivalent? — TanStack Query adoption growing.**

### Common Mistakes in Interviews

- Effect fetches and caches without invalidation strategy
- Duplicate HTTP cache Effect and Query
- Every GET through heavy effect chain

---

## Q099: CSP Report-Only Rollout

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security Headers |
| **Frequency** | Common |

### Question

Roll out Content Security Policy using Report-Only mode.

### Short Answer (30 seconds)

Deploy `Content-Security-Policy-Report-Only` collecting violations; fix inline scripts and rogue tags; switch to enforcing after clean week; monitor report-uri endpoint.

### Detailed Answer (3–5 minutes)

**Violations common:**
- Legacy inline onclick
- Marketing tag not nonce'd
- Dev hot reload scripts

**Architect:** CSP rollout is change program — coordinate marketing and platform.

### Architecture Perspective

Report-Only de-risks CSP enforcement breaking prod checkout.

### Follow-up Questions

1. **report-to Reporting API? — Modern replacement report-uri.**
2. **Nonce injection? — BFF renders per-request nonce in HTML template.**

### Common Mistakes in Interviews

- Enforce strict CSP day one — break checkout
- Ignore violation reports
- Different CSP dev vs prod undocumented

---

## Q100: GraphQL APQ Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | GraphQL |
| **Frequency** | Common |

### Question

Deploy Automatic Persisted Queries in production GraphQL frontend.

### Short Answer (30 seconds)

Client sends query hash; server allowlist only persisted queries; blocks arbitrary query strings; reduces payload and attack surface.

### Detailed Answer (3–5 minutes)

**Apollo APQ:**
`extensions.persistedQuery.sha256Hash` on POST.

**Architect:** APQ is production security baseline for public GraphQL.

### Architecture Perspective

APQ combines performance and security — architects mandate for prod.

### Follow-up Questions

1. **Query registry CI? — Register hashes on deploy — reject unknown.**
2. **GET for persisted query? — CDN cache safe queries only.**

### Common Mistakes in Interviews

- Arbitrary GraphQL strings in prod
- APQ without hash allowlist
- Persisted query not updated on schema change

---
