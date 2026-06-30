# Docker & Container Architecture — Fundamentals

> **Week 25** | **Module:** [docker-kubernetes](../../../modules/docker-kubernetes/README.md)

## Learning Objectives
- Explain container architecture vs VMs
- Build production-grade Dockerfiles for .NET 8
- Apply container security best practices

---

## 1. Containers vs Virtual Machines

```
VM:  App → Guest OS → Hypervisor → Host OS → Hardware
Container: App → Container Engine → Host OS (shared kernel) → Hardware
```

| Aspect | VM | Container |
|--------|-----|-----------|
| Isolation | Full OS | Process namespace |
| Startup | Minutes | Seconds |
| Size | GBs | MBs |
| Density | 10-50 per host | 100+ per host |
| Use case | Legacy, different OS | Microservices, CI/CD |

**Architect:** Containers share kernel — Linux containers on Linux host. Windows containers require Windows host (or Linux containers on Linux for .NET 8).

---

## 2. Docker Architecture

| Component | Role |
|-----------|------|
| **Dockerfile** | Build instructions |
| **Image** | Immutable layers (read-only) |
| **Container** | Running instance of image |
| **Registry** | Image storage (ACR, ECR, Docker Hub) |
| **docker compose** | Multi-container local dev |

**Copy-on-write:** Container layer writable; image layers shared across containers.

---

## 3. Multi-Stage Dockerfile for .NET 8

```dockerfile
# Stage 1: Build
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["OrderApi/OrderApi.csproj", "OrderApi/"]
RUN dotnet restore "OrderApi/OrderApi.csproj"
COPY . .
RUN dotnet publish "OrderApi/OrderApi.csproj" -c Release -o /app/publish

# Stage 2: Runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
COPY --from=build /app/publish .
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8080/health || exit 1
ENTRYPOINT ["dotnet", "OrderApi.dll"]
```

**Architect checklist:**
- [ ] Multi-stage (small final image — no SDK in prod)
- [ ] Non-root user
- [ ] Specific tag (not `latest`)
- [ ] HEALTHCHECK defined
- [ ] `.dockerignore` excludes bin/obj

---

## 4. Image Security

| Practice | Why |
|----------|-----|
| Scan images (Trivy, Defender) | CVE detection |
| Minimal base (`aspnet` not `sdk`) | Smaller attack surface |
| Pin versions (`8.0.5` not `8.0`) | Reproducible builds |
| No secrets in image | Use env vars / Key Vault at runtime |
| Distroless/Alpine (advanced) | Further reduce surface |

---

## 5. Container Networking

| Network Mode | Use |
|--------------|-----|
| bridge | Default, containers on same host |
| host | Container uses host network stack |
| none | No networking |
| overlay | Multi-host (Swarm/K8s) |

**Port mapping:** `-p 8080:80` — host:container

---

## 6. When Docker vs PaaS vs VMs

| Choose Docker/K8s | Choose PaaS (App Service) | Choose VMs |
|-------------------|----------------------------|------------|
| Microservices at scale | Simple .NET API | Legacy Windows apps |
| CI/CD pipeline maturity | Fast time to market | Full OS control |
| Multi-cloud portability | Managed ops preferred | License constraints |

**Architect default for .NET:** App Service first → Container Apps/AKS when container benefits justify ops cost.

**Next:** [02-intermediate.md](02-intermediate.md)
