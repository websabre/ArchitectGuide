# Week 02 — Common Mistakes

## 1. Captive Dependencies

**Mistake:** Injecting scoped `DbContext` into singleton services.

**Impact:** Memory leaks, stale data, thread-safety violations.

**Fix:** Match lifetimes; use `IServiceScopeFactory` in singleton background services.

---

## 2. `new HttpClient()` Per Request

**Mistake:** Creating `HttpClient` in methods or transients without factory.

**Impact:** Socket exhaustion — `SocketException` under load.

**Fix:** Always `AddHttpClient<T>()` with Polly policies.

---

## 3. Wrong Middleware Order

**Mistake:** `UseAuthorization()` before `UseAuthentication()`.

**Impact:** 401/403 errors, security bypass in edge cases.

**Fix:** Document standard pipeline order in team wiki.

---

## 4. Reading Secrets from appsettings.json

**Mistake:** API keys committed to git in `appsettings.Development.json` that leak to prod.

**Fix:** Key Vault, user secrets (dev only), environment variables in CI/CD.

---

## 5. gRPC for Public APIs Without gRPC-Web

**Mistake:** Exposing gRPC directly to browser clients.

**Impact:** Browser cannot call gRPC natively.

**Fix:** REST at edge (BFF/APIM); gRPC internal only, or grpc-web proxy.

---

## 6. Monolithic Program.cs

**Mistake:** 500-line `Program.cs` with all endpoints and DI registrations.

**Impact:** Untestable, unmaintainable as service grows.

**Fix:** Extension methods: `AddApplicationServices()`, `MapOrderEndpoints()`.

---

## 7. No Health Checks

**Mistake:** Deploying to K8s/App Service without `/health` endpoints.

**Impact:** Load balancer sends traffic to unhealthy instances.

**Fix:** Liveness + readiness probes from day one.

---

## Architecture Review Checklist — Week 02

- [ ] DI lifetimes correct (no captive dependencies)?
- [ ] IHttpClientFactory for all HTTP clients?
- [ ] Options pattern for configuration?
- [ ] API style documented in ADR?
- [ ] Health checks configured?
- [ ] Middleware order correct?
- [ ] Secrets externalized?
