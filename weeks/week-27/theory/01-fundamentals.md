# Kubernetes Advanced — GitOps, HPA, Production Operations

> **Week 27** | **Level:** Advanced → Expert

## 1. Horizontal Pod Autoscaler (HPA)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-api
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

**Custom metrics:** Scale on queue depth (KEDA), RPS from Prometheus.

**Architect:** HPA needs resource requests set. Cooldown periods prevent flapping.

---

## 2. GitOps (ArgoCD / Flux)

```
Git repo (manifests) → ArgoCD watches → applies to cluster
```

**Principles:**
- Git is source of truth
- Declarative desired state
- Automated sync (or manual approval for prod)
- Drift detection and correction

**Architect:** No `kubectl apply` from laptops in production — PR-based deployments only.

---

## 3. Service Mesh (Istio Overview)

- mTLS between all pods (zero trust)
- Traffic splitting: 90% v1, 10% v2 canary
- Retries, timeouts at mesh level
- Observability: golden metrics per service

**Cost:** Operational complexity. Justify with security/compliance or 20+ services.

---

## 4. Pod Disruption Budgets

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: order-api-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: order-api
```

Ensures node drains/upgrades don't take all replicas offline.

---

## 5. AKS vs EKS Operations

| Task | AKS | EKS |
|------|-----|-----|
| Identity | Entra Workload ID | IRSA |
| Ingress | App Gateway, NGINX | ALB Ingress Controller |
| Monitoring | Azure Monitor | CloudWatch |
| Registry | ACR | ECR |

**Portable:** Helm charts, K8s manifests, ArgoCD.

---

## 6. Production Checklist

- [ ] Resource requests/limits on all pods
- [ ] Liveness + readiness probes
- [ ] PDB for critical deployments
- [ ] Network policies (default deny + allow rules)
- [ ] RBAC least privilege
- [ ] Secrets via External Secrets Operator / Key Vault
- [ ] Image scanning in CI
- [ ] Cluster autoscaling + HPA
- [ ] Centralized logging (Container Insights / Datadog)

**Next:** Week 28 Linux
