# Week 43 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Scenario Black Friday SPA Outage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Frontend Architecture |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Black Friday 09:00 ET: your SPA checkout shows infinite spinner. CDN healthy, BFF p99 2s, payment microservice green. RUM shows 40% JS error spike on `chunk-checkout-v4.js` failed to load. CEO on bridge. What do you diagnose and fix in order?

### Short Answer (30 seconds)

Suspect botched deploy — hashed chunk missing or `index.html` pointing to deleted bundle. Roll back `index.html` to previous deploy, verify chunk 404s in CDN logs, implement deploy atomicity and synthetic checkout monitor.

### Detailed Answer

**Triage order (first 15 min):**
1. Confirm CDN 404 on `chunk-checkout-*.js` — RUM `Script error` + network tab pattern
2. Compare deployed `index.html` asset manifest vs blob storage — orphan reference
3. Roll back `index.html` only — immutable chunks mean previous hashes still exist
4. Validate synthetic checkout passes
5. Communicate ETA — not root cause essay

**Root cause classes:**
- Partial deploy (index new, chunks old deleted)
- CDN purge too aggressive
- Module federation remote version mismatch post-deploy

**Permanent fixes:**
- Atomic deploy manifest swap
- CI verifies all referenced chunks exist post-upload
- Canary 5% before full index promotion
- RUM alert on JS load failure rate

**Stakeholders:** Keep CEO on business metrics — conversion recovering — technical detail offline.

### Architecture Perspective

Expert scenarios test incident command under frontend-specific deploy failures — not generic 'check logs'.

### Follow-up Questions

1. **Module federation angle? — If error on `remoteEntry.js` — roll back remote URL config not only shell.**
2. **Why payment green but checkout broken? — Client never reached payment — failure earlier in browser bundle load.**

### Common Mistakes in Interviews

- Blame payment microservice because checkout broken
- Purge entire CDN cache as first action
- Redeploy without verifying chunk manifest integrity

---

## Q102: Scenario MFE Version Mismatch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Micro-Frontends |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Monday deploy: Account MFE v3.2 ships breaking export removed from shell contract. Shell still v2.1. Production white screen for `/account/*`. How prevent recurrence and recover?

### Short Answer (30 seconds)

Immediate: roll back Account MFE `remoteEntry` URL to v3.1. Long-term: contract tests block breaking export without shell major bump; compatibility matrix; blue/green remote URLs.

### Detailed Answer

**Recovery:**
1. Repoint config service `accountMfeUrl` → last known good v3.1 path
2. Purge CDN cache on `remoteEntry.js` if needed
3. Verify shell error boundary shows degraded message not white screen

**Prevention architecture:**
- Pact or integration test: shell imports `mountAccount` — fails CI on v3.2 PR
- Semver: removing export = major bump requiring shell update
- Feature flag wraps new account module — off until shell ready
- Runtime plugin retries remote load with fallback UI

**Governance:** MFE council approves breaking remote changes — joint release train.

### Architecture Perspective

MFE incidents are contract failures — expert answer addresses deploy decoupling paradox.

### Follow-up Questions

1. **Shared dependency mismatch too? — Check React duplicate if white screen with hook error instead.**
2. **Error boundary? — Should isolate MFE failure — shell nav still works — architect reviews boundary placement.**

### Common Mistakes in Interviews

- Force shell emergency deploy without testing matrix
- Disable contract tests to unblock Friday deploy
- iframe MFE without version strategy

---

## Q103: Scenario OIDC Token in localStorage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | OIDC Auth |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Security audit flags SPA storing refresh token in localStorage. Product resists BFF refactor citing 6-month roadmap. Architect stance and phased remediation?

### Short Answer (30 seconds)

Accept risk short-term with compensating controls; phased migration to BFF + HttpOnly session; never store refresh in localStorage in new code; document waiver with expiry.

### Detailed Answer

**Immediate compensating controls (0–30 days):**
- Short access token TTL 5–15 min
- CSP strict script-src
- Aggressive XSS scanning
- No refresh token rotation reuse detection off

**Phase 1 (30–90 days):**
- BFF token exchange for new features only
- Dual auth path behind flag

**Phase 2 (90–180 days):**
- Migrate all flows to Authorization Code + BFF cookie
- Remove tokens from browser storage

**Executive message:** XSS + localStorage refresh = session theft — regulatory and fraud exposure quantified.

**Waiver:** CISO sign-off 90-day expiry — tracked in risk register.

### Architecture Perspective

Expert tests security pragmatism — not dogmatic 'rewrite tomorrow' without migration plan.

### Follow-up Questions

1. **PKCE alone enough? — No — PKCE protects code interception not XSS token theft.**
2. **Mobile apps? — Separate threat model — attestation and secure enclave.**

### Common Mistakes in Interviews

- Encrypt token in localStorage — still XSS extractable
- Ignore audit finding because OAuth 'standard'
- Big-bang auth rewrite without phased rollout

---

## Q104: Scenario CSR SEO Traffic Collapse

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | SSR/CSR |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Marketing reports 60% organic traffic drop after replatforming product catalog to pure CSR React. Leadership blames 'SEO bug'. Architect diagnosis and recovery plan?

### Short Answer (30 seconds)

CSR eliminated crawlable HTML — Google sees empty shell. Recovery: SSR/SSG/ISR for catalog, prerender, or dynamic rendering for bots; fix meta/canonical; Search Console validation.

### Detailed Answer

**Diagnosis:**
- View-source on product URL — empty div#root
- Google Search Console — soft 404 / crawled not indexed spike
- Lighthouse SEO audit fails

**Recovery options (ranked):**
1. **Next.js ISR/SSR** for catalog routes — ADR hybrid
2. **Prerender.io** bot detection — faster tactical
3. **SSG** nightly build for top 50K SKUs

**Parallel:**
- Server-render title/meta at minimum even if hybrid
- XML sitemap update
- Structured data JSON-LD

**Timeline:** Tactical prerender week 1; strategic SSR quarter 1.

**Lesson:** SEO is NFR — should have been gate in replatform ADR.

### Architecture Perspective

Expert scenario connects frontend architecture choice to revenue impact.

### Follow-up Questions

1. **hreflang international? — CSR broke href tags — fix in SSR template.**
2. **Core Web Vitals improved but traffic died? — SEO and vitals both matter — explain trade-off.**

### Common Mistakes in Interviews

- Buy more Google Ads instead of fix crawlability
- SPA with client-only document.title
- Block bots from site — worsens problem

---

## Q105: Scenario INP Regression Release

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Core Web Vitals |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

RUM shows INP p75 jumped 180ms → 480ms after release. Release adds personalization SDK and larger Redux selector recompute. VP demands hotfix today. Approach?

### Short Answer (30 seconds)

Identify INP regression via RUM slice by release version; defer personalization SDK load; memoize selectors; `startTransition` for non-urgent updates; canary rollback if needed.

### Detailed Answer

**Hour 0–2:**
- Confirm correlation release `v4.2.0` + INP in Chrome mobile US
- Long task profiling — personalization SDK main thread 200ms blocks

**Hotfix options:**
1. Feature flag off personalization — immediate INP recovery
2. Load SDK after `requestIdleCallback`
3. Move selector derive to worker or server
4. Rollback release if flag insufficient

**Validation:** RUM INP p75 <250ms within 2h of flag off.

**Follow-up:** INP budget in CI; SDK performance review gate; Redux selector audit with reselect.

**VP comms:** 'Disabled non-critical personalization restoring responsiveness — reintroduce with performance guardrails.'

### Architecture Perspective

Expert INP scenario requires RUM-driven triage and business-aware hotfix not only code optimize.

### Follow-up Questions

1. **Personalization server-side? — Edge compute personalization — remove client SDK entirely long-term.**
2. **startTransition scope? — Mark filter UI updates transition — keep add-to-cart urgent.**

### Common Mistakes in Interviews

- Week-long perf rewrite before any mitigation
- Ignore mobile RUM — desktop lab fine
- Add more analytics to debug INP — worsens INP

---

## Q106: Scenario GraphQL Query Storm

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | GraphQL |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Public GraphQL endpoint suffers 10x traffic spike — expensive nested queries melt DB. Frontend team built rich dashboard. Incident response and architectural fix?

### Short Answer (30 seconds)

Emergency: enable query depth/complexity limits, block introspection, APQ allowlist only, rate limit per API key. Long-term: persisted queries, DataLoader, BFF for dashboard aggregate, cost analysis.

### Detailed Answer

**Immediate (incident):**
1. WAF rate limit + complexity reject
2. Identify top costly query from gateway logs
3. Temporary disable dashboard feature flag
4. Scale read replicas — tactical

**Architectural fixes:**
- APQ production mandatory
- Query cost calculator — reject >1000 cost
- Dashboard moves to BFF REST aggregate or single approved persisted query
- DataLoader batch N+1 resolvers
- CDN only for GET persisted queries safe

**Governance:** Frontend cannot ship arbitrary GraphQL strings to prod — schema registry + allowlist CI.

### Architecture Perspective

GraphQL incidents are often missing server governance — expert covers ops and design.

### Follow-up Questions

1. **Federation blame? — Subgraph N+1 still possible — gateway limits essential.**
2. **Client cache storm? — refetchQueries on interval — separate from server storm.**

### Common Mistakes in Interviews

- Scale DB infinitely without query limits
- Disable entire API instead of costly queries only
- Allow introspection during attack reconnaissance

---

## Q107: Scenario WebSocket Stale Prices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | WebSockets |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Trading dashboard SPA shows stale prices after network blip — users make decisions on old data. WebSocket reconnects but gaps not backfilled. Design fix?

### Short Answer (30 seconds)

On reconnect fetch snapshot REST + resume WS with sequence; gap detection triggers resync; UI shows data freshness timestamp; stale threshold warning banner.

### Detailed Answer

**Architecture:**
```
Disconnect → Banner 'Reconnecting'
Reconnect → GET /prices/snapshot?since=lastSeq
WS subscribe with lastSeq+1
Gap detected → full resync
```

**Client state:**
- `lastSequenceId` per channel
- `lastUpdatedAt` displayed per panel
- Disable trade button if data >5s stale

**Server:**
- Retain 60s event buffer per symbol for gap fill
- Kafka partition ordering per symbol

**Testing:** Chaos disconnect tests in CI.

### Architecture Perspective

Real-time UX requires explicit staleness architecture — reconnect ≠ consistent.

### Follow-up Questions

1. **Snapshot API load on mass reconnect? — Rate limit + incremental catch-up protocol.**
2. **SSE fallback? — One-way price feed — simpler reconnect semantics.**

### Common Mistakes in Interviews

- Assume reconnect sufficient without resync
- No UI indication of stale data
- Unbounded event buffer server memory

---

## Q108: Scenario PWA Offline PHI Leak

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | PWA |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Field clinician PWA caches patient schedule offline. Security finds PHI in service worker cache on shared tablet. Remediation architecture?

### Short Answer (30 seconds)

Remove PHI from SW cache; encrypt IndexedDB at rest; device MDM; auto logout; cache only non-PHI shell; server session short TTL; remote wipe.

### Detailed Answer

**Immediate:**
1. Deploy SW update `skipWaiting` clearing PHI caches
2. Force re-login all field devices
3. MDM remote wipe shared tablets policy

**Architecture fix:**
- **Never** cache `/api/patients` in SW
- Offline: queue action ids only — fetch PHI on demand online
- Encrypted storage Android/iOS WebView where applicable
- Session 15 min idle logout
- Device attestation for PWA install

**Compliance:** HIPAA minimum necessary — offline PHI requires risk assessment and often prohibited.

**ADR:** PWA offline scope explicitly excludes PHI storage.

### Architecture Perspective

Expert scenario blends PWA architecture with HIPAA — hot topic for healthcare frontend.

### Follow-up Questions

1. **BAA for CDN? — PHI must not sit on non-BAA edge cache.**
2. **Shared tablet? — User profile switch must clear all client storage.**

### Common Mistakes in Interviews

- Encrypt PHI in IndexedDB with key in JS — XSS still wins
- Cache-first on all API routes
- Offline mode without security review

---

## Q109: Scenario CSP Breaks Checkout

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Security Headers |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Enforcing strict CSP breaks checkout — payment iframe blocked. Security insists no unsafe-inline. Resolve architecture?

### Short Answer (30 seconds)

CSP `frame-src` allow payment PSP domain; `script-src` nonce for bootstrap; hash for small inline config; report-only validated first; document payment domains in CSP template.

### Detailed Answer

**Fix CSP entries:**
```
frame-src https://js.stripe.com;
script-src 'self' 'nonce-{n}';
connect-src 'self' https://api.corp.com https://api.stripe.com;
```

**Process:**
1. Report-Only identified `frame-src` violation
2. Add PSP domains per environment
3. Nonce injection via BFF HTML render
4. Regression test checkout in CI with CSP enforced

**Security alignment:** Strict CSP compatible with iframe payments — no unsafe-inline required.

**Architect:** Payment CSP allowlist maintained by platform team — PSP change triggers CSP update PR.

### Architecture Perspective

CSP + payments is common production breakage — expert knows frame-src and nonce patterns.

### Follow-up Questions

1. **PCI iframe? — PAN stays PSP domain — CSP must allow frame not script from PSP.**
2. **Third-party GTM? — Often conflicts — move tags server-side or strict nonce.**

### Common Mistakes in Interviews

- unsafe-inline to quickly fix prod
- CSP not tested in CI checkout flow
- Omit frame-src — defaults block iframe

---

## Q110: Scenario Design System Breaking Release

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Design Systems |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design system v5 removes Button `variant` prop breaking 40 apps. CI didn't catch — production deploy Friday. Contain and fix process?

### Short Answer (30 seconds)

Roll back design system major or pin consumers; codemod `variant` → `appearance`; semver enforcement; consumer integration tests in DS pipeline; canary publish.

### Detailed Answer

**Containment:**
1. Republish `@corp/ui@4.x` as `latest` dist-tag
2. Apps pin `4.9.2` in emergency PR
3. Identify broken apps via error tracking `undefined variant`

**Process fix:**
- DS major requires codemod + migration guide
- **Consumer test suite** runs against DS beta in DS CI before publish
- Breaking change RFC 30-day notice
- Dist-tag `next` for early adopters — `latest` only stable

**Architect:** Design system is platform — its outage equals multi-app outage.

### Architecture Perspective

DS breakage is multi-tenant incident — rollback and consumer testing architecture.

### Follow-up Questions

1. **Visual regression? — Chromatic on DS — catches style not API breaks — need type tests.**
2. **Semver automation? — semantic-release based on commit types.**

### Common Mistakes in Interviews

- Publish major Friday without beta period
- No consumer contract tests in DS CI
- Apps use caret range on DS — auto-breaking

---

## Q111: Scenario Multi-Region CDN Stale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CDN |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

EU users see US product prices after emergency USD sale ended — CDN cached JSON aggregate at edge 24h TTL. Architect prevention?

### Short Answer (30 seconds)

Never cache personalized or price JSON at CDN; short TTL + event purge; `Cache-Control: private` for user-specific; price version in URL; CDN purge webhook on promo end.

### Detailed Answer

**Root cause:** BFF `/api/catalog` cached at CDN with aggressive TTL — sale flag in response stale.

**Fix architecture:**
- Price-sensitive: `Cache-Control: private, no-store` or max-age 60 + purge
- Separate static product content (cacheable) from price fragment (dynamic client fetch)
- **Composite pattern:** SSR shell + client fetch `/api/prices?ids=` short TTL
- Event-driven purge: promo service fires Front Door purge

**Governance:** Cache tier matrix — Tier-0 price data never immutable CDN.

**Incident comms:** Legal/pricing team notification — incorrect price display risk.

### Architecture Perspective

CDN caching wrong tier causes revenue and compliance incidents — architect separates static from volatile.

### Follow-up Questions

1. **Edge Side Includes? — Rare — fragment assembly for prices.**
2. **Vary header? — `Vary: Cookie` often breaks CDN cache predictably — prefer private no-store.**

### Common Mistakes in Interviews

- Cache all BFF GETs 24h for performance
- Manual purge forgotten after promo ends
- Same cache policy catalog and prices

---

## Q112: Scenario Accessibility Lawsuit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Accessibility |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Retailer receives ADA demand letter — checkout keyboard trap and missing labels. Legal wants 30-day remediation plan. Architect response?

### Short Answer (30 seconds)

Immediate hotfix keyboard trap and labels; CI a11y gates; VPAT update; design system audit; third-party audit; training — phased plan with Week 1 critical path fixes.

### Detailed Answer

**Week 1 critical:**
- Fix modal focus trap checkout payment step
- Label all form fields `aria-describedby` errors
- Deploy axe-tested patch

**30-day plan:**
- WCAG 2.1 AA audit all flows
- Storybook a11y CI mandatory
- Design system component a11y certification
- External audit firm validation
- VPAT/ACR published for legal

**Architecture:**
- a11y definition of done per epic
- Keyboard test checklist QA gate
- `$lib/a11y` shared focus utilities

**Legal interface:** Document remediation timeline — good faith effort reduces exposure.

### Architecture Perspective

Expert a11y scenario is legal + engineering program — not only alt tags.

### Follow-up Questions

1. **Overlay widgets? — Avoid accessibility overlay lawsuits — fix root code.**
2. **Mobile app scope? — Letter may include iOS — coordinate native team.**

### Common Mistakes in Interviews

- Promise full WCAG AAA in 30 days unrealistic
- Fix only homepage — checkout still broken
- No CI prevention — repeat violations

---

## Q113: Scenario BFF Becomes Monolith

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | BFF |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Checkout BFF grew to 80 endpoints, 200K LOC, 12 developers — deploy bottleneck and defect rate up. Architect evolution options?

### Short Answer (30 seconds)

Split BFF by subdomain (checkout BFF, account BFF); extract orchestration to workflow service; keep BFF thin aggregation; strangle by route prefix to new services.

### Detailed Answer

**Assessment metrics:**
- Deploy frequency dropped
- Lead time up
- Change failure rate up

**Options:**
1. **Split BFFs** — align to MFE boundaries — checkout vs catalog
2. **Workflow engine** — move saga out of BFF
3. **GraphQL federation** — if clients need flexible queries
4. **Anti-corruption** — domain modules inside monolith first then extract

**Not:** micro-BFF per developer — wrong granularity.

**Migration:** Strangler route `/api/checkout/v2` → new slim BFF; old BFF read-only deprecate.

### Architecture Perspective

BFF monolith is common failure mode — expert proposes bounded split aligned to domains.

### Follow-up Questions

1. **Shared library extract? — Common DTO/auth middleware npm package — reduce duplication without one BFF.**
2. **Team topology? — Team per BFF — Conway alignment.**

### Common Mistakes in Interviews

- Add more endpoints to same BFF for speed
- Rewrite entire BFF big-bang
- No metrics justify split timing

---

## Q114: Scenario Angular Zoneless Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Angular Patterns |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Angular 18 zoneless preview: team wants migration for performance. Existing code relies on zone.js patch. Architect migration plan?

### Short Answer (30 seconds)

Audit zone dependencies; enable zoneless dev branch; signals + OnPush everywhere; `provideExperimentalZonelessChangeDetection`; fix broken third-party libs; incremental module migration.

### Detailed Answer

**Phases:**
1. Inventory `NgZone.run` usage and async patterns
2. OnPush + signals default new code
3. Enable zoneless in staging — test lib compatibility (charts, maps)
4. Replace zone-dependent hacks with `markForCheck`/`detectChanges` intentionally
5. Production flag per app module

**Risks:**
- Third-party date pickers not updating
- Tests assuming zone auto-flush

**Architect:** Zoneless ADR ties to Angular LTS roadmap — training budget.

### Architecture Perspective

Zoneless is emerging Angular architecture — expert plans ecosystem compatibility.

### Follow-up Questions

1. **RxJS async pipe zoneless? — Works with signals bridge — test thoroughly.**
2. **Hybrid zone? — Temporary `ngZone: 'noop'` experiments — not prod mixed.**

### Common Mistakes in Interviews

- Enable zoneless prod without staging lib audit
- Default change detection remains
- Ignore failing third-party widgets

---

## Q115: Scenario Federation React Duplicate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Module Federation |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Production error 'Invalid hook call' after MFE deploy. Shell React 18.2, Catalog remote bundles React 18.1 separately. Diagnose and fix?

### Short Answer (30 seconds)

Module federation shared config failed — duplicate React. Fix shared singleton requiredVersion, eager load React in shell, rebuild remote with externals, verify bundle analyzer single React.

### Detailed Answer

**Diagnosis:**
- `npm ls react` in remote shows nested copy
- Webpack bundle analyzer two React instances
- Hooks error on catalog route only

**Fix:**
```js
shared: { react: { singleton: true, strictVersion: true, requiredVersion: '18.2.0' } }
```
- Remote `react` as external via federation shared
- CI integration test imports remote in shell — no hook error

**Prevention:**
- Shared dependency matrix in MFE council
- Renovate bot coordinated React bumps
- Block remote deploy if shared version mismatch

### Architecture Perspective

Duplicate React is #1 MFE production issue — expert answer is federation config not 'restart pods'.

### Follow-up Questions

1. **strictVersion true? — Fails fast at load — better than runtime hook error.**
2. **pnpm hoisting? — Monorepo package manager affects duplicate detection.**

### Common Mistakes in Interviews

- Downgrade shell React to match remote
- Ignore shared config — bundle React in remote for autonomy
- No integration test after React version bump

---

## Q116: Scenario RUM Shows Backend Green

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Frontend Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Support tickets spike 'site broken' but API dashboards 99.99% success. RUM reveals 25% users on IE11 and old Safari get blank screen after babel config dropped polyfills. Response?

### Short Answer (30 seconds)

Restore critical polyfills or transpile to support agreed browser matrix; RUM browser dimension alert; document supported browsers; graceful degradation message for unsupported.

### Detailed Answer

**Analysis:**
- RUM `browser.name` slice — errors on IE11/Safari 12
- Missing `core-js` polyfills for `Promise.allSettled`
- Build target ES2020 broke legacy

**Fix:**
1. Hotfix rebuild with browserslist `>0.5%, not dead`
2. Unsupported browser interstitial instead of blank
3. RUM alert error rate by browser >5%

**Policy:**
- Supported browser matrix in ADR — enterprise may require IE11 extra quarter
- `@babel/preset-env` useBuiltIns usage

**Comms:** Not API outage — client compatibility — set expectations.

### Architecture Perspective

Expert observability scenario — frontend failures invisible to backend APM.

### Follow-up Questions

1. **ESM only build? — Legacy browsers need transpilation — architect approves browserslist.**
2. **Feature detection? — Partial — polyfills still needed for syntax.**

### Common Mistakes in Interviews

- Tell users upgrade browser only — no hotfix
- Backend team scales API unnecessarily
- Drop browserslist without stakeholder sign-off

---

## Q117: Scenario Supply Chain Script Attack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Security Headers |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

npm dependency compromise serves malicious script. CSP nonce-based blocked it but staging used unsafe-inline. Architect supply chain + CSP defense layers?

### Short Answer (30 seconds)

SRI on third-party scripts; lockfile integrity; CSP enforce nonce prod; dependency scanning; private npm proxy; subresource monitoring; incident revoke lockfile.

### Detailed Answer

**Defense layers:**
1. **CSP nonce** prod — inline attack blocked (this incident)
2. **SRI** `integrity=` on CDN scripts
3. **npm** — `npm audit`, Renovate, provenance attestations
4. **Artifactory** proxy with vulnerability gate
5. **RUM** detect unexpected script load hash

**Incident:**
- Pin known-good package version
- Rotate secrets assuming exfil attempt
- Forensic npm publish timeline

**Architect:** Supply chain threat model includes build pipeline and runtime CSP.

### Architecture Perspective

Expert connects CSP value to real supply chain incident — layered defense narrative.

### Follow-up Questions

1. **SBOM? — CycloneDX in CI — audit trail for compromised package scope.**
2. **Typosquatting? — npm org scope policy `@corp/*` only.**

### Common Mistakes in Interviews

- Rely only on npm audit weekly
- unsafe-inline prod to avoid CSP maintenance
- No SRI on third-party marketing scripts

---

## Q118: Scenario Tenant Theme XSS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Micro-Frontends |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Multi-tenant SaaS allows custom CSS per tenant. Tenant injects `background:url(javascript:...)` — XSS in shared domain app. Architect tenant customization sandbox?

### Short Answer (30 seconds)

Sanitize tenant CSS; disallow `javascript:` and `expression`; CSP blocks inline; isolate tenant admin custom CSS via Shadow DOM or iframe; separate subdomain per enterprise tenant optional.

### Detailed Answer

**Architecture options (ranked):**
1. **CSS sanitizer** — allowlist properties — strip `url()` except https CDN allowlist
2. **Design tokens only** — tenants pick from presets not raw CSS
3. **Shadow DOM** — tenant widget isolated
4. **Dedicated subdomain** — `tenant.app.com` — cookie isolation

**CSP:** strict `style-src` — no tenant inline style attributes.

**Governance:** Enterprise tier gets subdomain silo; SMB gets token-only theming.

**Incident:** Disable custom CSS feature flag globally — audit tenant configs.

### Architecture Perspective

Tenant customization is XSS surface — expert architects sandbox not full CSS freedom.

### Follow-up Questions

1. **CSP style-src unsafe-inline? — Incompatible with tenant CSS — sanitizer required.**
2. **DOMPurify for CSS? — Use dedicated CSS sanitizer library.**

### Common Mistakes in Interviews

- Allow arbitrary tenant `<style>` injection
- Shared cookie domain all tenants
- No security review for customization feature

---

## Q119: Scenario Executive Demands Micro-Frontend

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Micro-Frontends |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

CTO mandates micro-frontends for 8-person single-product team citing Netflix. Architect pushback and alternative?

### Short Answer (30 seconds)

Recommend feature-folder monolith SPA + design system; MFE justified at team/org scale not 8 devs; document cost: federation, CI matrix, UX consistency; propose triggers for future MFE split.

### Detailed Answer

**Pushback data:**
- 8 devs = release coupling manageable with trunk-based dev
- MFE adds 30–40% integration overhead industry average
- Netflix scale ≠ your scale

**Alternative architecture:**
- Monorepo Nx — apps/packages clear boundaries
- Module boundaries lint — prepare extract later
- Independent deploy via feature flags not remotes

**MFE triggers (document):**
- >4 teams own UI with separate release cadence
- Acquisition integrates separate SPA
- Regulatory isolation requires separate deploy

**Executive framing:** 'Invest integration tax now or speed feature delivery — recommend revisit at 4-team split.'

### Architecture Perspective

Expert scenario tests organizational architecture judgment — when NOT to adopt hype.

### Follow-up Questions

1. **Conway's Law? — MFE aligns to teams — without teams MFE solves nothing.**
2. **Partial MFE? — Shell + one remote — worst of both — avoid half measure.**

### Common Mistakes in Interviews

- Agree to MFE to please CTO without ADR
- iframe micro-frontend as 'quick MFE'
- No exit criteria if MFE fails

---

## Q120: Scenario WCAG vs Release Deadline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Accessibility |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Accessibility audit fails WCAG AA on new checkout 2 days before mandated go-live (contract penalty). PM wants ship anyway. Architect position?

### Short Answer (30 seconds)

Ship blocker list only if legal accepts risk; minimum viable a11y fixes mandatory (keyboard, labels, contrast); document remedation waiver; never ship payment inaccessible to keyboard — contractual and ethical line.

### Detailed Answer

**Non-negotiable (2-day fix):**
- Keyboard complete checkout path
- Form labels + error announcements
- Focus visible
- Color contrast payment buttons

**Can defer 30 days with waiver:**
- Enhanced screen reader announcements polish
- AAA contrast optional text

**Process:**
- Legal reviews ADA exposure vs contract penalty
- Customer comms if partial remediation
- CI axe gate post-launch prevent regression

**Architect role:** Quantify lawsuit risk vs delay cost — not blanket block or blanket ship.

### Architecture Perspective

Expert tests ethics and program management — balanced architect stance under deadline.

### Follow-up Questions

1. **Post-launch overlay? — Reject as sole fix — legal increasingly rejects overlays.**
2. **Manual test sign-off? — Named owner signs keyboard path tested.**

### Common Mistakes in Interviews

- Ship knowing keyboard trap exists
- Delay launch indefinitely for minor AAA issues
- No written waiver or remediation date

---
