# Lab 25: Production Dockerfile for .NET 8 API

| **Week** | 25 | **Duration** | 90 min |

## Objectives
- [ ] Multi-stage Dockerfile with non-root user
- [ ] Image scan with Trivy
- [ ] Run with health check and resource limits

## Steps

```bash
dotnet new webapi -n ContainerLab --use-minimal-apis
cd ContainerLab
# Add /health endpoint
```

**Dockerfile** — see [theory/01-fundamentals.md](../theory/01-fundamentals.md)

```bash
docker build -t order-api:1.0.0 .
docker scan order-api:1.0.0   # or: trivy image order-api:1.0.0
docker run -p 8080:8080 --memory=512m --cpus=1 order-api:1.0.0
curl http://localhost:8080/health
```

## Break-It
Run as root (remove USER directive). Scan image — note CVE surface difference with sdk base image.

## Report
1. Final image size (aspnet vs sdk)?
2. When would you choose Windows containers?
3. ACR vs Docker Hub for production?
