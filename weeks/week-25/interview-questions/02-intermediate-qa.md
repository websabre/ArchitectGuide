# Week 25 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Docker Image Layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

How do Docker image layers work and why do architects care about layer design?

### Short Answer (30 seconds)

Each Dockerfile instruction creates a read-only layer stacked on a base image. Layers are cached and shared across images — smaller, stable lower layers speed builds and reduce registry storage.

### Detailed Answer (3–5 minutes)

**Mechanism:** `FROM`, `RUN`, `COPY` each add layers. Union filesystem presents single view. Changed layer invalidates cache for all layers above it.

**Architect decisions:**
- Put rarely-changing dependencies (`dotnet restore`) before frequently-changing source (`COPY . .`)
- Share base layers across microservices via common `aspnet` runtime image
- Monitor image size — 500MB+ .NET images slow deploy and increase attack surface

**Production:** `docker history myapp:tag` shows layer sizes; `dive` tool inspects waste.

### Architecture Perspective

Layer design directly affects CI time, deploy speed, and security patch velocity.

### Follow-up Questions

1. **Layer deduplication across nodes? — Same layer pulled once per node — shared base reduces bandwidth.**
2. **Squash layers? — `docker build --squash` loses cache benefits — rarely recommended.**

### Common Mistakes in Interviews

- COPY . . before restore — cache bust every commit
- Single RUN apt-get without cleanup — bloated layer
- Ignore layer size in image governance

---

## Q032: Multi-Stage Builds

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Design a multi-stage Dockerfile for a .NET 8 API. What goes in each stage?

### Short Answer (30 seconds)

Build stage: SDK image, restore, publish. Runtime stage: aspnet runtime only, copy published output. Final image excludes SDK, source, and build tools.

### Detailed Answer (3–5 minutes)

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY *.csproj ./
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
COPY --from=build /app/publish .
USER $APP_UID
ENTRYPOINT ["dotnet", "MyApi.dll"]
```

**Architect:** Multi-stage is default for production — never ship SDK in runtime. Separate test stage optional for CI `docker build --target test`.

### Architecture Perspective

Multi-stage separates build-time attack surface from runtime minimalism.

### Follow-up Questions

1. **Distroless final stage? — Even smaller — no shell — harder to debug.**
2. **BuildKit cache mounts? — `RUN --mount=type=cache` speeds NuGet restore.**

### Common Mistakes in Interviews

- Single-stage SDK image in production
- Copy entire repo including secrets into final stage
- No non-root USER in final stage

---

## Q033: Dockerfile Best Practices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

List Dockerfile best practices for enterprise .NET container pipelines.

### Short Answer (30 seconds)

Pin base image digests, multi-stage build, non-root user, .dockerignore, health check, explicit EXPOSE, no secrets in layers, minimal packages.

### Detailed Answer (3–5 minutes)

**Checklist:**
1. `FROM mcr.microsoft.com/dotnet/aspnet:8.0@sha256:...` — reproducible builds
2. `.dockerignore` excludes `bin/`, `obj/`, `.git`
3. `USER app` — never run as root
4. `HEALTHCHECK` or K8s probes — not both conflicting
5. One process per container — PID 1 handles signals
6. Label with `org.opencontainers.image.revision` for traceability

**Architect:** Central template Dockerfile in platform repo; teams extend via ARG not copy-paste.

### Architecture Perspective

Dockerfile standards prevent security drift across dozens of services.

### Follow-up Questions

1. **Hadolint in CI? — Lint Dockerfile on every PR.**
2. **Chiseled images? — Ubuntu chiseled .NET — smaller attack surface.**

### Common Mistakes in Interviews

- `:latest` tag in production Dockerfile
- apt-get update without version pin in same RUN
- Secrets via ENV or ARG persisted in image history

---

## Q034: Container vs VM

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

When containers vs VMs for .NET workloads on Azure?

### Short Answer (30 seconds)

Containers: microservices, fast deploy, density, K8s/Container Apps. VMs: legacy apps, stateful monoliths needing full OS control, licensed software, strong isolation boundary.

### Detailed Answer (3–5 minutes)

**Containers excel:** Homogeneous .NET APIs, horizontal scale, GitOps deploy, 50+ services.

**VMs excel:** SQL Server legacy, Active Directory integration, custom kernel modules, compliance requiring dedicated hypervisor isolation.

**Hybrid:** AKS nodes are VMs running containers — you get both. App Service runs containers on managed VM pools.

**Architect:** Default cloud-native .NET to containers; VM only with documented justification in ADR.

### Architecture Perspective

Container vs VM is isolation and operational model trade-off.

### Follow-up Questions

1. **VMs inside containers? — Nested virt niche — not typical.**
2. **Windows containers vs Linux? — Linux default for .NET 8 — cost and ecosystem.**

### Common Mistakes in Interviews

- VM per microservice at scale
- Containers for everything including stateful DB
- Ignore resource isolation differences

---

## Q035: Docker Networking Bridge

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

Explain Docker bridge networking for local multi-container apps.

### Short Answer (30 seconds)

Default bridge network: containers get private IPs, communicate by container name on user-defined bridge. Published ports map host:container for external access.

### Detailed Answer (3–5 minutes)

**User-defined bridge** (`docker network create app-net`): DNS resolution between containers by name — `http://api:8080` from `web` container.

**vs host network:** Container shares host NIC — performance but no isolation.

**Architect local dev:** Compose creates default network; match service names to production K8s DNS patterns.

**Production note:** Docker bridge is local dev only — K8s CNI handles prod networking.

### Architecture Perspective

Bridge networking models service discovery for local dev parity.

### Follow-up Questions

1. **Overlay network? — Multi-host Swarm/K8s — not default single-host bridge.**
2. **host.docker.internal? — Reach host from container — Mac/Windows dev.**

### Common Mistakes in Interviews

- Link containers via --link deprecated flag
- Published port conflicts on shared dev machine
- Assume bridge behavior equals K8s ClusterIP

---

## Q036: Docker Compose Local Dev

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Design docker-compose.yml for local .NET API + Postgres + Redis dev stack.

### Short Answer (30 seconds)

Define services with build contexts, env files, depends_on, healthchecks, named volumes for DB persistence, and shared network.

### Detailed Answer (3–5 minutes)

```yaml
services:
  api:
    build: .
    ports: ["8080:8080"]
    environment:
      ConnectionStrings__Default: Host=db;Database=app
    depends_on:
      db: { condition: service_healthy }
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
volumes:
  pgdata:
```

**Architect:** `compose.override.yml` for dev-only mounts; never commit prod secrets; document `docker compose up` in README.

### Architecture Perspective

Compose is architect's local parity tool — not production orchestrator.

### Follow-up Questions

1. **Compose Watch? — Auto-rebuild on file change — dev velocity.**
2. **Testcontainers vs Compose? — Testcontainers for CI integration tests; Compose for daily dev.**

### Common Mistakes in Interviews

- Prod secrets in compose.yml committed
- depends_on without healthcheck — race on startup
- Bind mount entire repo over published DLL in container

---

## Q037: Image Scanning Vulnerabilities

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

How integrate container image vulnerability scanning in CI/CD?

### Short Answer (30 seconds)

Scan every image build with Trivy, Microsoft Defender for Containers, or ACR Tasks scan. Fail pipeline on Critical CVE without exception process; quarantine non-compliant images in registry.

### Detailed Answer (3–5 minutes)

**Pipeline gate:**
1. `docker build` → push to staging tag
2. Scan — `trivy image --severity CRITICAL,HIGH`
3. Block deploy if Critical > 0 (or SLA to patch within 7 days)
4. ACR retention policy + continuous scan on push

**Architect:** Base image patching weekly automated PR; SBOM attached for audit. Exception workflow with risk acceptance sign-off.

### Architecture Perspective

Image scanning is supply chain hygiene — non-negotiable in enterprise.

### Follow-up Questions

1. **Distroless reduces CVEs? — Fewer packages — fewer findings — not zero.**
2. **False positives? — Vulnerability without exploit path — triage process.**

### Common Mistakes in Interviews

- Scan only on deploy not on build
- Ignore base image CVEs — only scan app layer
- No policy for stale images in registry

---

## Q038: Non-Root Container User

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Why run containers as non-root and how for .NET on Linux?

### Short Answer (30 seconds)

Root in container escaping to host is catastrophic. Non-root limits blast radius. .NET 8 images include `APP_UID` — set `USER $APP_UID` in Dockerfile.

### Detailed Answer (3–5 minutes)

**Implementation:**
```dockerfile
USER $APP_UID
```

**K8s:** `securityContext.runAsNonRoot: true` + `runAsUser: 1654`.

**File permissions:** Ensure `/app` writable only if needed; read-only root filesystem where possible.

**Architect:** Admission policy deny images running as UID 0; platform base images pre-configured.

### Architecture Perspective

Non-root is CIS Docker benchmark requirement.

### Follow-up Questions

1. **fsGroup for volumes? — K8s sets volume ownership for non-root write.**
2. **OpenShift random UID? — .NET images support arbitrary UID with proper permissions.**

### Common Mistakes in Interviews

- Run as root because 'easier permissions'
- USER directive missing — defaults root
- Writable root filesystem with root user

---

## Q039: Read-Only Root Filesystem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

When enforce read-only root filesystem for containers?

### Short Answer (30 seconds)

When app writes only to explicit volumes/tmp — prevents runtime malware persistence. Enable `readOnlyRootFilesystem: true` in K8s securityContext; mount `emptyDir` for `/tmp` if needed.

### Detailed Answer (3–5 minutes)

**.NET APIs:** Often stateless — ideal for read-only root. Logs to stdout — no file write needed.

**Exceptions:** Apps writing temp uploads — mount writable `emptyDir` at `/tmp` only.

**Architect:** Platform default read-only; services request writable mounts via chart values with justification.

### Architecture Perspective

Read-only root limits container compromise impact.

### Follow-up Questions

1. **writable /tmp emptyDir? — Standard pattern for read-only root.**
2. **Break-glass debug? — Ephemeral debug container with writable FS.**

### Common Mistakes in Interviews

- Read-only but app writes logs to /var/log — crash loop
- Entire FS writable without reason
- No exception process for writable mount requests

---

## Q040: Resource Limits cgroups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

How set CPU and memory limits on Docker containers and why?

### Short Answer (30 seconds)

`docker run --memory=512m --cpus=1.5` maps to cgroup limits. Prevents one container starving host; enables capacity planning.

### Detailed Answer (3–5 minutes)

**Docker Compose:**
```yaml
deploy:
  resources:
    limits: { cpus: '1', memory: 512M }
```

**K8s equivalent:** requests and limits — scheduler uses requests; OOMKill uses limits.

**Architect:** Always set memory limits — .NET GC behaves differently under cgroup cap. Load test at limit before production. No limit = noisy neighbor on shared nodes.

### Architecture Perspective

cgroups enforce fairness — critical on multi-tenant nodes.

### Follow-up Questions

1. **.NET GC under memory limit? — `DOTNET_GCHeapHardLimit` auto from cgroup — verify behavior.**
2. **CPU limits vs throttling? — CFS quota throttles — requests guarantee minimum.**

### Common Mistakes in Interviews

- No memory limit on Java/.NET heap-heavy apps
- Limit below minimum app footprint — OOMKill loop
- Docker local dev with no limits hiding prod issues

---

## Q041: Docker Registry ACR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Design Azure Container Registry strategy for multi-team .NET platform.

### Short Answer (30 seconds)

Premium ACR for geo-replication and private link; one registry per environment or tenant; RBAC scoped to teams; ACR Tasks for build/scan; retention policies.

### Detailed Answer (3–5 minutes)

**Structure:**
- `mycompany.azurecr.io/platform/orders-api:1.2.3`
- Prod: pull from geo-replicated Premium ACR via Private Endpoint
- CI: Managed Identity `AcrPush` — no admin user

**Architect:** Webhook or ARC triggers deploy; image signing with Notation/Cosign optional for zero-trust.

### Architecture Perspective

ACR is private artifact store — treat like production database.

### Follow-up Questions

1. **ACR vs Docker Hub? — ACR integrated RBAC, no rate limits, geo-rep.**
2. **Tasks cache? — ACR Tasks remote cache speeds multi-stage builds.**

### Common Mistakes in Interviews

- ACR admin user enabled in prod
- Single `:latest` tag deploy pipeline
- No geo-replication for multi-region DR

---

## Q042: Image Tagging Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Define image tagging strategy for GitOps .NET microservices.

### Short Answer (30 seconds)

Immutable tags: `{semver}` + `{git-sha}` + `{build-id}`. Never deploy `:latest` to prod. Promote same digest across environments.

### Detailed Answer (3–5 minutes)

**Tags:**
- `orders-api:2.4.1` — release
- `orders-api:2.4.1-abc1234` — traceability
- `orders-api:sha-abc1234` — GitOps pin

**Promotion:** Dev deploys `sha-abc1234`; prod deploys same digest after gate — not rebuilt.

**Architect:** Document in platform ADR; admission controller rejects mutable tags.

### Architecture Perspective

Tag immutability enables rollback and audit.

### Follow-up Questions

1. **Digest vs tag? — Deploy by digest `@sha256:...` for absolute immutability.**
2. **Semantic versioning policy? — Major API break = major tag.**

### Common Mistakes in Interviews

- `:latest` in production Helm values
- Rebuild image per environment — different digests
- Overwrite existing semver tag in registry

---

## Q043: .NET Container Base Images

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Which Microsoft .NET container base images to use and when?

### Short Answer (30 seconds)

`mcr.microsoft.com/dotnet/aspnet:8.0` for runtime; `sdk:8.0` for build only. Alpine/smaller variants for size; chiseled for security-minimal.

### Detailed Answer (3–5 minutes)

**Choices:**
- **aspnet** — production API default
- **sdk** — CI build stage only
- **Alpine** — smaller but musl compatibility testing required
- **Chiseled Ubuntu** — no shell/package manager — hardened

**Architect:** Pin major version (`8.0`); automate patch updates via Renovate; test Alpine in CI if adopted.

### Architecture Perspective

Base image choice affects size, CVE surface, and glibc compatibility.

### Follow-up Questions

1. **Self-contained vs framework-dependent container? — FDD smaller layers with shared runtime base.**
2. **Native AOT container? — Distroless-friendly — smallest — reflection limits.**

### Common Mistakes in Interviews

- SDK image in production runtime
- Unpinned `aspnet:latest`
- Alpine in prod without integration test on musl

---

## Q044: Health Checks Dockerfile

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

HEALTHCHECK in Dockerfile vs Kubernetes probes — how coordinate?

### Short Answer (30 seconds)

Docker HEALTHCHECK for local/single-host; K8s liveness/readiness for orchestration. Prefer K8s probes in production — disable conflicting Dockerfile HEALTHCHECK or align endpoints.

### Detailed Answer (3–5 minutes)

**Dockerfile:**
```dockerfile
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8080/health/live || exit 1
```

**K8s:** Separate `/health/live` and `/health/ready` — readiness excludes external deps from liveness.

**Architect:** Standard health endpoints in all .NET services; platform Helm chart wires probes consistently.

### Architecture Perspective

Health checks drive restart and traffic routing decisions.

### Follow-up Questions

1. **curl in distroless? — Use `/health` TCP probe or minimal wget alternative.**
2. **Startup probe? — Slow .NET cold start — avoid premature liveness kill.**

### Common Mistakes in Interviews

- HTTP check to payment provider in liveness
- No health endpoint — default TCP only
- Docker HEALTHCHECK and K8s probe different paths — confusion

---

## Q045: Volume vs Bind Mount

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

When Docker named volume vs bind mount?

### Short Answer (30 seconds)

Named volumes: portable, Docker-managed storage, prod data (DB). Bind mounts: dev hot-reload source code, config files from host path.

### Detailed Answer (3–5 minutes)

**Dev:** `volumes: [".:/src"]` bind mount for live edit — not for prod.

**Prod DB:** Named volume or cloud disk — `postgres_data:/var/lib/postgresql/data`.

**K8s mapping:** PVC for named volume equivalent; ConfigMap mount for config.

**Architect:** Never bind mount host paths in production K8s — use PVC and secrets.

### Architecture Perspective

Volume type affects portability and performance.

### Follow-up Questions

1. **volume mount performance Mac? — VirtioFS/osxfs slower — use delegated mode.**
2. **ReadOnlyMany PVC? — Shared config across pods.**

### Common Mistakes in Interviews

- Bind mount prod database data directory
- Anonymous volumes without backup plan
- Bind mount secrets from developer laptop path

---

## Q046: Secrets in Containers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

How manage secrets for .NET containers without baking into images?

### Short Answer (30 seconds)

Runtime injection: K8s Secrets + CSI, Azure Key Vault Provider, Docker secrets (Swarm), environment from orchestrator. Never ARG/ENV secrets in Dockerfile.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **AKS:** Secrets Store CSI Driver → Key Vault → mount as files
- **Local dev:** User secrets / `.env` gitignored / Docker Compose secrets
- **.NET:** `AddAzureKeyVault()` or file-based config provider

**Architect:** Secrets rotation without image rebuild; audit access; prefer workload identity over client secrets.

### Architecture Perspective

Secret management separates build artifacts from runtime credentials.

### Follow-up Questions

1. **Sealed Secrets / External Secrets? — GitOps-safe secret delivery.**
2. **Build-time secret in multi-stage? — BuildKit secret mount — not in layer.**

### Common Mistakes in Interviews

- Connection string in Dockerfile ENV
- Secrets in image layers from COPY .env
- Same secret volume world-readable in container

---

## Q047: Docker Security CIS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

Key CIS Docker Benchmark controls for production?

### Short Answer (30 seconds)

Non-root user, read-only root FS, no privileged mode, limit capabilities, scan images, use user namespaces where supported, log to centralized sink, pin versions.

### Detailed Answer (3–5 minutes)

**Top CIS items:**
1. 4.1 — non-root default
2. 4.6 — no new privileges
3. 5.1 — verify image provenance
4. 5.7 — no privileged containers
5. 5.15 — single main process

**Architect:** OPA/Gatekeeper or Azure Policy for AKS enforces CIS-aligned admission; quarterly benchmark audit.

### Architecture Perspective

CIS benchmark translates container security to checklist.

### Follow-up Questions

1. **Pod Security Standards? — K8s restricted profile maps to CIS.**
2. **seccomp/AppArmor profiles? — Limit syscalls — platform-provided defaults.**

### Common Mistakes in Interviews

- Privileged container for 'simple fix'
- CAP_SYS_ADMIN granted broadly
- No image provenance verification

---

## Q048: Container Orchestration When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

When move from Docker Compose to Kubernetes or Container Apps?

### Short Answer (30 seconds)

When you need: multi-host scheduling, rolling updates, autoscaling, service discovery at scale, self-healing, or >3 services in prod with SLA.

### Detailed Answer (3–5 minutes)

**Stay Compose/local:** Developer machines, integration test fixtures.

**Container Apps:** HTTP scale-to-zero, simpler ops, KEDA built-in — sweet spot for many .NET APIs.

**AKS:** Full K8s APIs, service mesh, complex networking, multi-team platform.

**Architect:** Decision matrix in ADR — team K8s skill, scale, compliance drive choice.

### Architecture Perspective

Orchestration choice is operational complexity vs capability.

### Follow-up Questions

1. **Docker Swarm? — Legacy — greenfield choose K8s or managed PaaS.**
2. **Nomad? — Simpler scheduler — niche multi-workload.**

### Common Mistakes in Interviews

- AKS for two static containers
- Compose in production at scale
- Skip orchestration with manual docker run fleet

---

## Q049: Dockerfile Cache Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

Optimize Dockerfile layer caching for fast CI builds?

### Short Answer (30 seconds)

Order instructions least-to-most frequently changing; copy csproj before source; use BuildKit cache mounts for NuGet; parallel stages where independent.

### Detailed Answer (3–5 minutes)

**Pattern:**
```dockerfile
COPY *.csproj ./
RUN --mount=type=cache,target=/root/.nuget/packages \
    dotnet restore
COPY . .
RUN dotnet publish ...
```

**CI:** `--cache-from` previous image; ACR Tasks remote cache.

**Architect:** Target <3 min image build for typical API; monitor build metrics in pipeline dashboard.

### Architecture Perspective

Cache strategy saves CI minutes and developer wait time at scale.

### Follow-up Questions

1. **BuildKit inline cache? — Export cache metadata in image for pull.**
2. **Remote cache backend? — GitHub Actions cache or ACR.**

### Common Mistakes in Interviews

- COPY . . before restore
- Clean dotnet cache every build intentionally
- No cache-from in CI — full rebuild always

---

## Q050: Distroless Images

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

When use distroless or chiseled images for .NET?

### Short Answer (30 seconds)

When security posture prioritizes minimal attack surface over shell debugging convenience. .NET chiseled images from Microsoft — no apt, no bash.

### Detailed Answer (3–5 minutes)

**Pros:** Fewer CVEs, smaller image, compliance friendly.

**Cons:** No `kubectl exec` shell — debug via ephemeral debug containers or logs.

**Architect:** Platform standard for prod; developers use debug variant tag in non-prod. Pair with good observability.

### Architecture Perspective

Distroless trades debug convenience for security minimalism.

### Follow-up Questions

1. **debug distroless variant? — Non-prod images with shell — separate tag.**
2. **Google distroless dotnet? — Community; prefer Microsoft chiseled for .NET.**

### Common Mistakes in Interviews

- Distroless without centralized logging — blind debugging
- Shell-dependent healthcheck in distroless
- Distroless without team training on debug patterns

---

## Q051: Sidecar Pattern Containers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

Explain sidecar pattern — production examples for .NET on K8s.

### Short Answer (30 seconds)

Sidecar: auxiliary container in same pod sharing network/volumes with main app. Examples: Envoy proxy, log shipper, config sync, service mesh dataplane.

### Detailed Answer (3–5 minutes)

**Examples:**
- **Istio sidecar** — mTLS, telemetry
- **Fluent Bit** — log forwarding
- **Dapr sidecar** — state/pubsub abstractions

**Architect:** Sidecar adds resource overhead — justify per pod. Init vs sidecar: init runs to completion before app starts.

### Architecture Perspective

Sidecars extend pod capability without changing app code.

### Follow-up Questions

1. **Sidecar resource limits? — Include in pod quota — sidecars consume CPU/memory.**
2. **Ambient mesh? — Sidecar-less Istio — reduces overhead — emerging.**

### Common Mistakes in Interviews

- Sidecar for every trivial concern
- Ignore sidecar memory in pod sizing
- Two app containers without clear sidecar boundary

---

## Q052: Init Containers Concept

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

When use init containers vs main container startup logic?

### Short Answer (30 seconds)

Init containers run sequentially to completion before app starts — migrations, wait-for dependency, download config, set permissions.

### Detailed Answer (3–5 minutes)

**Use init when:**
- DB schema migrate once per deploy
- Wait for Kafka topic creation
- Fetch secrets from vault before app reads them

**Avoid:** Long-running init — blocks pod ready. Use Job for one-off batch migrate instead if slow.

**Architect:** Standard init chart patterns in platform Helm library.

### Architecture Perspective

Init containers serialize pre-start dependencies cleanly.

### Follow-up Questions

1. **Init container failure? — Pod restarts — ensure idempotent migrations.**
2. **Share volume with app? — `emptyDir` for downloaded artifacts.**

### Common Mistakes in Interviews

- Heavy migration in init blocking scale-out
- Init container with different image tag unvetted
- Duplicate migration in app AND init

---

## Q053: Container Logging Drivers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

How should .NET containers emit logs in production?

### Short Answer (30 seconds)

Write structured logs to stdout/stderr — container runtime collects. Avoid file-based logging inside container. Centralize with Fluent Bit/DaemonSet → Log Analytics/ELK.

### Detailed Answer (3–5 minutes)

**.NET:** Serilog `WriteTo.Console(new JsonFormatter())` — one JSON line per event.

**Docker driver:** `json-file` default locally; prod uses cluster collector not docker logs.

**Architect:** Correlation ID in every log line; no sensitive data in logs; retention policy per compliance.

### Architecture Perspective

Stdout logging is 12-factor container standard.

### Follow-up Questions

1. **Fluent Bit vs Fluentd? — Fluent Bit lighter for DaemonSet.**
2. **Log rotation docker json-file? — Local only — size limits on dev.**

### Common Mistakes in Interviews

- Logs written only to file inside container
- Plain text logs without correlation ID
- Container logs as only observability — no metrics/traces

---

## Q054: Docker on Windows vs Linux

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

Compare Docker on Windows vs Linux for .NET 8 deployments.

### Short Answer (30 seconds)

Linux containers dominate .NET 8 — smaller images, K8s default, lower cost. Windows containers for legacy .NET Framework and Windows-specific dependencies only.

### Detailed Answer (3–5 minutes)

**Linux:** `mcr.microsoft.com/dotnet/aspnet:8.0` on AKS Linux nodes — standard.

**Windows:** Larger images, Windows node pools, higher cost, slower pull — isolate Framework apps.

**Architect:** Migration path Framework → .NET 8 on Linux containers; Windows container only with ADR justification.

### Architecture Perspective

Platform default Linux — Windows is exception path.

### Follow-up Questions

1. **WSL2 Docker Desktop? — Linux containers on Windows dev machine.**
2. **Hyper-V isolation? — Windows container isolation modes — perf impact.**

### Common Mistakes in Interviews

- Windows containers for new .NET 8 APIs
- Mixed OS in same K8s pod — impossible
- Ignore Windows node licensing cost

---

## Q055: BuildKit Features

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

Which BuildKit features matter for enterprise .NET image builds?

### Short Answer (30 seconds)

Cache mounts, secret mounts, SSH mounts, parallel stage execution, provenance attestations, and improved layer export.

### Detailed Answer (3–5 minutes)

**Enable:** `DOCKER_BUILDKIT=1` default in modern Docker.

**Key features:**
```dockerfile
RUN --mount=type=cache,target=/root/.nuget/packages dotnet restore
RUN --mount=type=secret,id=nugetconfig dotnet restore
```

**Architect:** BuildKit in ACR Tasks and GitHub Actions; SBOM/provenance for supply chain.

### Architecture Perspective

BuildKit is modern build engine — enable platform-wide.

### Follow-up Questions

1. **buildx bake? — Multi-image matrix builds monorepo.**
2. **Provenance attestation? — SLSA level — link image to source commit.**

### Common Mistakes in Interviews

- Legacy builder without cache mounts
- Secrets in RUN command line visible
- No build provenance in regulated environment

---

## Q056: OCI Image Spec

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Occasional |

### Question

What is the OCI image spec and why does portability matter?

### Short Answer (30 seconds)

OCI (Open Container Initiative) defines image format and runtime spec — Docker, containerd, CRI-O interoperate. Image = manifest + config + layers.

### Detailed Answer (3–5 minutes)

**Architect relevance:** Images built in CI run on AKS (containerd), local Docker, and other clouds without rebuild. Sign manifests with Notation.

**Components:**
- **Image spec** — layer tarball format
- **Runtime spec** — how to run bundle

Vendor neutrality reduces lock-in.

### Architecture Perspective

OCI standard enables multi-cloud container portability.

### Follow-up Questions

1. **OCI artifacts? — Store SBOM, signatures alongside images in registry.**
2. **Docker vs OCI media types? — Compatible — registries translate.**

### Common Mistakes in Interviews

- Proprietary image format dependency
- Assume Docker-only runtime in design
- Ignore manifest list for multi-arch

---

## Q057: Container Escape Risks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

What is container escape and how mitigate architecturally?

### Short Answer (30 seconds)

Escape: exploit kernel or misconfiguration to access host. Mitigate: patch nodes, non-root, no privileged, seccomp/AppArmor, network policies, minimal images, runtime threat detection.

### Detailed Answer (3–5 minutes)

**Attack vectors:**
- Privileged container → host devices
- Kernel CVE (runc, containerd)
- Mounted docker.sock in container

**Architect:** AKS auto-patches nodes; Defender for Containers; deny privileged in admission; regular pen test.

### Architecture Perspective

Container security assumes hostile workload — defense in depth.

### Follow-up Questions

1. **gVisor/Kata runtime? — VM-isolated containers — higher isolation cost.**
2. **Rootless Docker? — Daemonless rootless — dev security.**

### Common Mistakes in Interviews

- Mount /var/run/docker.sock in app container
- Privileged pods for performance
- Unpatched node images for months

---

## Q058: SBOM for Containers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

Why generate SBOM for container images and how?

### Short Answer (30 seconds)

SBOM (Software Bill of Materials) lists components for CVE matching and compliance. Generate in CI with Syft/Trivy; attach to registry as OCI artifact.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```bash
syft packages myapp:1.0 -o spdx-json > sbom.spdx.json
```

**Architect:** Required for executive order / supply chain compliance in many enterprises. Link SBOM to vulnerability scan results; retain per release.

### Architecture Perspective

SBOM enables precise impact analysis when Log4Shell-style CVEs hit.

### Follow-up Questions

1. **SPDX vs CycloneDX? — Both common — pick one org standard.**
2. **SBOM only at release not per build? — Per immutable image digest.**

### Common Mistakes in Interviews

- No SBOM in regulated industry
- SBOM generated but never stored
- Scan image without SBOM component linkage

---

## Q059: Local Dev vs Prod Parity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

How maximize dev/prod parity without running full AKS locally?

### Short Answer (30 seconds)

Same container image digest, same env var names, Compose mimics service topology, Testcontainers for integration tests, feature flags for external service stubs.

### Detailed Answer (3–5 minutes)

**Practices:**
- Build once, promote digest
- `appsettings.Development.json` mirrors prod structure not values
- Local Aspire or Tilt for K8s-like dev optional
- Contract tests against real Postgres in Testcontainers

**Architect:** Document acceptable dev/prod gaps; minimize 'works on my machine' via CI integration environment.

### Architecture Perspective

Parity reduces deployment surprises — architect defines minimum bar.

### Follow-up Questions

1. **Dev containers? — VS Code devcontainer.json — onboarding standard.**
2. **Kind/minikube local K8s? — For platform team not every developer.**

### Common Mistakes in Interviews

- Different DB engine local vs prod
- Mock everything — no integration tests
- Developers never run container locally

---

## Q060: Docker ADR Template

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Common |

### Question

What belongs in an ADR for adopting containers on Azure?

### Short Answer (30 seconds)

Context, decision (AKS vs Container Apps vs App Service), base image standard, registry choice, security controls, networking, observability, rollback, and team skill plan.

### Detailed Answer (3–5 minutes)

**ADR sections:**
1. **Context** — monolith deploy pain, scale needs
2. **Decision** — AKS + ACR Premium + GitOps
3. **Consequences** — ops overhead, benefits
4. **Standards** — Dockerfile template, tagging, scanning gates
5. **Rejected** — VM-only, serverless-only

**Architect:** ADR is living doc — review quarterly.

### Architecture Perspective

Container ADR aligns platform and product teams.

### Follow-up Questions

1. **When revise ADR? — Major cost or security incident triggers review.**
2. **Link ADR to runbooks? — On-call references ADR decisions.**

### Common Mistakes in Interviews

- ADR written after production firefight only
- No rejected alternatives documented
- ADR ignores team training plan

---

## Q061: Container Image Signing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Container Image Signing — what do you need to know and decide?

### Short Answer (30 seconds)

Container Image Signing requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *Container Image Signing*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Container Image Signing to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Container Image Signing is healthy in production?**
2. **What is the rollback plan if Container Image Signing change fails?**

### Common Mistakes in Interviews

- Treating Container Image Signing as set-and-forget with no monitoring
- No ADR documenting trade-offs for Container Image Signing
- Copying Container Image Signing pattern from blog without context fit

---

## Q062: Docker Content Trust

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Docker Content Trust — what do you need to know and decide?

### Short Answer (30 seconds)

Docker Content Trust requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *Docker Content Trust*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Docker Content Trust to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Docker Content Trust is healthy in production?**
2. **What is the rollback plan if Docker Content Trust change fails?**

### Common Mistakes in Interviews

- Treating Docker Content Trust as set-and-forget with no monitoring
- No ADR documenting trade-offs for Docker Content Trust
- Copying Docker Content Trust pattern from blog without context fit

---

## Q063: OCI Image Spec

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: OCI Image Spec — what do you need to know and decide?

### Short Answer (30 seconds)

OCI Image Spec requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *OCI Image Spec*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect OCI Image Spec to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove OCI Image Spec is healthy in production?**
2. **What is the rollback plan if OCI Image Spec change fails?**

### Common Mistakes in Interviews

- Treating OCI Image Spec as set-and-forget with no monitoring
- No ADR documenting trade-offs for OCI Image Spec
- Copying OCI Image Spec pattern from blog without context fit

---

## Q064: Distroless Images

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Distroless Images — what do you need to know and decide?

### Short Answer (30 seconds)

Distroless Images requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *Distroless Images*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Distroless Images to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Distroless Images is healthy in production?**
2. **What is the rollback plan if Distroless Images change fails?**

### Common Mistakes in Interviews

- Treating Distroless Images as set-and-forget with no monitoring
- No ADR documenting trade-offs for Distroless Images
- Copying Distroless Images pattern from blog without context fit

---

## Q065: Chiseled .NET Images

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Chiseled .NET Images — what do you need to know and decide?

### Short Answer (30 seconds)

Chiseled .NET Images requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *Chiseled .NET Images*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Chiseled .NET Images to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Chiseled .NET Images is healthy in production?**
2. **What is the rollback plan if Chiseled .NET Images change fails?**

### Common Mistakes in Interviews

- Treating Chiseled .NET Images as set-and-forget with no monitoring
- No ADR documenting trade-offs for Chiseled .NET Images
- Copying Chiseled .NET Images pattern from blog without context fit

---

## Q066: BuildKit Cache Mounts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: BuildKit Cache Mounts — what do you need to know and decide?

### Short Answer (30 seconds)

BuildKit Cache Mounts requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *BuildKit Cache Mounts*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect BuildKit Cache Mounts to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove BuildKit Cache Mounts is healthy in production?**
2. **What is the rollback plan if BuildKit Cache Mounts change fails?**

### Common Mistakes in Interviews

- Treating BuildKit Cache Mounts as set-and-forget with no monitoring
- No ADR documenting trade-offs for BuildKit Cache Mounts
- Copying BuildKit Cache Mounts pattern from blog without context fit

---

## Q067: Docker Scout Scanning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Docker Scout Scanning — what do you need to know and decide?

### Short Answer (30 seconds)

Docker Scout Scanning requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *Docker Scout Scanning*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Docker Scout Scanning to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Docker Scout Scanning is healthy in production?**
2. **What is the rollback plan if Docker Scout Scanning change fails?**

### Common Mistakes in Interviews

- Treating Docker Scout Scanning as set-and-forget with no monitoring
- No ADR documenting trade-offs for Docker Scout Scanning
- Copying Docker Scout Scanning pattern from blog without context fit

---

## Q068: ACR Tasks Build

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: ACR Tasks Build — what do you need to know and decide?

### Short Answer (30 seconds)

ACR Tasks Build requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *ACR Tasks Build*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect ACR Tasks Build to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove ACR Tasks Build is healthy in production?**
2. **What is the rollback plan if ACR Tasks Build change fails?**

### Common Mistakes in Interviews

- Treating ACR Tasks Build as set-and-forget with no monitoring
- No ADR documenting trade-offs for ACR Tasks Build
- Copying ACR Tasks Build pattern from blog without context fit

---

## Q069: Container Registry Geo-Replication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Container Registry Geo-Replication — what do you need to know and decide?

### Short Answer (30 seconds)

Container Registry Geo-Replication requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *Container Registry Geo-Replication*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Container Registry Geo-Replication to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Container Registry Geo-Replication is healthy in production?**
2. **What is the rollback plan if Container Registry Geo-Replication change fails?**

### Common Mistakes in Interviews

- Treating Container Registry Geo-Replication as set-and-forget with no monitoring
- No ADR documenting trade-offs for Container Registry Geo-Replication
- Copying Container Registry Geo-Replication pattern from blog without context fit

---

## Q070: Docker Desktop vs Linux Engine

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Docker |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Docker Desktop vs Linux Engine — what do you need to know and decide?

### Short Answer (30 seconds)

Docker Desktop vs Linux Engine requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 25 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 25 — Docker):**
- Scenario: production system at scale needs a decision involving *Docker Desktop vs Linux Engine*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Docker Desktop vs Linux Engine to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Docker Desktop vs Linux Engine is healthy in production?**
2. **What is the rollback plan if Docker Desktop vs Linux Engine change fails?**

### Common Mistakes in Interviews

- Treating Docker Desktop vs Linux Engine as set-and-forget with no monitoring
- No ADR documenting trade-offs for Docker Desktop vs Linux Engine
- Copying Docker Desktop vs Linux Engine pattern from blog without context fit

---
