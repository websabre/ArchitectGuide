# Week 26 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Pod Lifecycle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Walk through Kubernetes pod lifecycle phases and architect implications.

### Short Answer (30 seconds)

Phases: Pending (scheduled) → Running (containers started) → Succeeded/Failed → Terminating. Containers have waiting/running/terminated states.

### Detailed Answer (3–5 minutes)

**Pending causes:** Insufficient resources, image pull, PVC bind, taints. **Running:** probes determine ready. **Termination:** `terminationGracePeriodSeconds` — .NET needs graceful shutdown.

**Architect:** Set `preStop` hook + drain connections; liveness ≠ readiness; monitor `CrashLoopBackOff` and `ImagePullBackOff` in alerts.

### Architecture Perspective

Pod lifecycle drives availability during deploy and failure.

### Follow-up Questions

1. **Pod phase vs container state? — Init containers affect startup sequence.**
2. **Eviction? — Node pressure kills pods — QoS class matters.**

### Common Mistakes in Interviews

- Ignore terminationGracePeriod — hard kill mid-request
- No preStop for connection draining
- Alert only on pod Running not Ready

---

## Q002: Deployment vs StatefulSet

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

When Deployment vs StatefulSet for .NET workloads?

### Short Answer (30 seconds)

Deployment: stateless APIs, random pod names, interchangeable replicas. StatefulSet: stable network ID, ordered deploy, persistent identity — databases, Kafka, clustered state.

### Detailed Answer (3–5 minutes)

**Deployment:** Orders API, BFF, workers — scale horizontally, any pod serves any request.

**StatefulSet:** SQL on K8s (rare), Redis cluster, Elasticsearch — stable `pod-0`, `pod-1` DNS.

**Architect:** Default Deployment; StatefulSet only with documented stateful need. Managed Azure SQL/Redis preferred over StatefulSet for data.

### Architecture Perspective

Workload statefulness drives controller choice.

### Follow-up Questions

1. **DaemonSet when? — Log collector, node agent on every node.**
2. **Job/CronJob? — Batch migrate, scheduled reports.**

### Common Mistakes in Interviews

- StatefulSet for stateless API
- Deployment for database without external storage plan
- Ignore ordered rollout in clustered stateful app

---

## Q003: Service ClusterIP LoadBalancer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Explain Kubernetes Service types — ClusterIP, NodePort, LoadBalancer.

### Short Answer (30 seconds)

ClusterIP: internal VIP — pod-to-pod. NodePort: host port exposure. LoadBalancer: cloud LB provisions public IP (AKS Azure LB).

### Detailed Answer (3–5 minutes)

**Typical AKS:**
- API pods behind ClusterIP Service
- Ingress controller Service type LoadBalancer (or internal LB)
- East-west traffic ClusterIP only

**Architect:** Never expose every service as LoadBalancer — cost and attack surface. Single ingress entry point; NetworkPolicy restricts internal traffic.

### Architecture Perspective

Service types define traffic entry and cost.

### Follow-up Questions

1. **Internal LoadBalancer annotation? — Private ingress for corp network.**
2. **Headless Service? — StatefulSet stable DNS — ClusterIP None.**

### Common Mistakes in Interviews

- LoadBalancer per microservice
- NodePort in production without firewall
- ClusterIP assumed routable from internet

---

## Q004: Ingress Controller

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design ingress architecture for .NET APIs on AKS.

### Short Answer (30 seconds)

Ingress controller (NGINX, App Gateway Ingress Controller) routes HTTP/S by host/path to ClusterIP services. TLS termination at ingress; WAF optional.

### Detailed Answer (3–5 minutes)

**Layers:**
1. Azure Front Door / App Gateway (WAF, global)
2. Ingress controller (path routing, cert-manager TLS)
3. Service → Pod

**Architect:** One ingress class per cluster; annotate for AGIC vs NGINX; rate limiting and auth at edge; backend protocol HTTP/2 to Kestrel.

### Architecture Perspective

Ingress is L7 routing layer — central policy enforcement point.

### Follow-up Questions

1. **Gateway API vs Ingress? — Gateway API successor — evaluate for new clusters.**
2. **Multiple ingress controllers? — Separate internal/external controllers.**

### Common Mistakes in Interviews

- Ingress without TLS in prod
- Path routing conflicts between teams
- Bypass ingress — expose Service LoadBalancer directly

---

## Q005: ConfigMap vs Secret

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

When ConfigMap vs Secret for .NET app configuration on K8s?

### Short Answer (30 seconds)

ConfigMap: non-sensitive config (feature flags, logging level). Secret: credentials, connection strings, API keys — base64 encoded at rest, encrypt etcd.

### Detailed Answer (3–5 minutes)

**.NET pattern:**
```yaml
env:
- name: Logging__LogLevel__Default
  valueFrom: { configMapKeyRef: ... }
- name: ConnectionStrings__Default
  valueFrom: { secretKeyRef: ... }
```

**Architect:** Prefer Key Vault CSI over native Secrets for rotation; never commit Secret YAML to Git; Sealed Secrets for GitOps.

### Architecture Perspective

Config separation prevents credential leakage in logs and repos.

### Follow-up Questions

1. **Secret encryption at rest? — Enable AKS KMS/etcd encryption.**
2. **Reload on ConfigMap change? — .NET reloadable options vs restart required.**

### Common Mistakes in Interviews

- Secrets in ConfigMap because 'base64 is encryption'
- Secrets committed to Git plain YAML
- Same ConfigMap prod and dev values

---

## Q006: Liveness vs Readiness Probes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design liveness and readiness probes for ASP.NET Core on AKS.

### Short Answer (30 seconds)

Liveness: restart if process deadlocked. Readiness: remove from Service endpoints if cannot serve (DB down). Startup: slow init before liveness kicks in.

### Detailed Answer (3–5 minutes)

```yaml
livenessProbe:
  httpGet: { path: /health/live, port: 8080 }
  initialDelaySeconds: 10
readinessProbe:
  httpGet: { path: /health/ready, port: 8080 }
startupProbe:
  httpGet: { path: /health/live, port: 8080 }
  failureThreshold: 30
```

**Architect:** DB check in readiness only — not liveness — avoids restart storm on DB blip.

### Architecture Perspective

Probe design prevents cascading outages — top AKS interview topic.

### Follow-up Questions

1. **grpc health probe? — Native gRPC health for gRPC services.**
2. **Probe timeout tuning? — Shorter than P99 handler time.**

### Common Mistakes in Interviews

- External payment API in liveness probe
- No startup probe on slow .NET cold start
- Readiness always true — traffic to broken pods

---

## Q007: Resource Requests Limits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

How set CPU/memory requests and limits for .NET pods?

### Short Answer (30 seconds)

Requests: scheduler placement guarantee. Limits: max usage — memory limit triggers OOMKill. Set requests ≈ steady state; limits headroom for spikes.

### Detailed Answer (3–5 minutes)

**Process:**
1. Load test without limits — observe usage
2. Request = P95 usage; Limit = P99 × 1.5 for memory
3. Use VPA recommendations as starting point

**QoS:** Requests = Limits → Guaranteed; only requests → Burstable.

**Architect:** Namespace quotas cap team totals; deny pods without requests.

### Architecture Perspective

Right-sizing prevents node overload and wasted capacity.

### Follow-up Questions

1. **.NET memory under limit? — GC adapts to cgroup — validate under load.**
2. **CPU limit throttling? — .NET CPU-bound may throttle — measure.**

### Common Mistakes in Interviews

- No requests — BestEffort evicted first
- Limit 128Mi on .NET API — OOMKill
- Copy limits from blog without load test

---

## Q008: Namespace Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Design namespace strategy for multi-team AKS platform.

### Short Answer (30 seconds)

Namespace per team per environment slice, or per application system. Apply RBAC, ResourceQuota, NetworkPolicy per namespace.

### Detailed Answer (3–5 minutes)

**Patterns:**
- `team-orders-dev`, `team-orders-prod` — or single cluster prod with `orders-prod`
- Platform namespace: `ingress-nginx`, `cert-manager`, `monitoring`

**Architect:** Avoid namespace-per-microservice sprawl; NetworkPolicy default deny between namespaces; label standards enforced.

### Architecture Perspective

Namespaces are blast-radius and RBAC boundaries.

### Follow-up Questions

1. **Namespace per env vs cluster per env? — Prod cluster isolation common.**
2. **Hierarchical namespaces? — Subnamespace operator — advanced.**

### Common Mistakes in Interviews

- Everything in default namespace
- 50 namespaces no RBAC
- Cross-namespace traffic wide open

---

## Q009: kubectl Debugging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

kubectl commands for debugging failing .NET pod in production?

### Short Answer (30 seconds)

`kubectl describe pod`, `kubectl logs`, `kubectl get events`, `kubectl exec`, `kubectl port-forward`, ephemeral debug containers.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. `kubectl get pods -n orders` — status Restarts/CrashLoop
2. `kubectl describe pod` — Events: OOMKilled, FailedMount
3. `kubectl logs pod --previous` — crash before restart
4. `kubectl port-forward` — local curl health endpoint

**Architect:** Restrict prod exec to break-glass RBAC; prefer observability over shell in prod.

### Architecture Perspective

Systematic kubectl flow impresses in platform interviews.

### Follow-up Questions

1. **kubectl debug ephemeral container? — Distroless debug with shell.**
2. **stern/lens? — Multi-pod log tail — ops tooling.**

### Common Mistakes in Interviews

- kubectl delete pod first without logs
- exec as root in prod without audit
- Ignore Events section in describe

---

## Q010: Helm Charts Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

How use Helm for packaging .NET microservices on AKS?

### Short Answer (30 seconds)

Helm chart templates K8s YAML with values per environment. Chart: Deployment, Service, Ingress, HPA, ConfigMap references.

### Detailed Answer (3–5 minutes)

**Structure:**
- `values.yaml` defaults
- `values-prod.yaml` overrides replicas, resources
- `helm upgrade --install orders ./chart -f values-prod.yaml`

**Architect:** OCI Helm registry in ACR; chart library for common .NET patterns; version charts with app semver.

### Architecture Perspective

Helm is package manager — reduces YAML duplication.

### Follow-up Questions

1. **Helm vs Kustomize? — Helm templating vs overlay patches — both valid.**
2. **Helm hooks? — Pre-upgrade migration Job.**

### Common Mistakes in Interviews

- Raw YAML copy-paste per env
- Secrets in values.yaml committed
- Unpinned chart dependencies

---

## Q011: K8s Networking Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Explain Kubernetes networking model — pod IP, CNI, Services.

### Short Answer (30 seconds)

Every pod gets unique cluster-routable IP. CNI plugin (Azure CNI, Calico) implements networking. Services provide stable VIP via kube-proxy or eBPF dataplane.

### Detailed Answer (3–5 minutes)

**Rules:**
- Pods communicate by IP without NAT within cluster
- Service abstracts pod churn
- NetworkPolicy optional L3/L4 firewall

**AKS:** Azure CNI assigns VNet IPs — plan IP exhaustion. Overlay mode conserves IPs.

**Architect:** IP planning in landing zone; document CNI choice in platform ADR.

### Architecture Perspective

Networking model underpins service mesh and security design.

### Follow-up Questions

1. **kube-proxy modes? — iptables vs IPVS vs eBPF (Cilium).**
2. **Host network pod? — Rare — bypasses network isolation.**

### Common Mistakes in Interviews

- Assume unlimited pod IPs in VNet
- Ignore Azure CNI IP preallocation
- No NetworkPolicy because 'internal network'

---

## Q012: DNS in Cluster

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

How does DNS work inside Kubernetes for service discovery?

### Short Answer (30 seconds)

CoreDNS resolves `service.namespace.svc.cluster.local`. Pods use short names `http://orders-api.orders` within same namespace.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Full FQDN: `orders-api.orders.svc.cluster.local`
- Cross-namespace: `http://payment.payment.svc.cluster.local`
- Headless: returns pod A records directly

**Architect:** Align K8s service names with local Compose names for dev parity. Custom stub domains via CoreDNS config for external services.

### Architecture Perspective

Cluster DNS is service discovery — names must be stable contracts.

### Follow-up Questions

1. **ndots and search paths? — Misconfig causes external DNS leakage.**
2. **ExternalName service? — CNAME to external host — migration bridge.**

### Common Mistakes in Interviews

- Hardcode pod IPs in app config
- Wrong namespace short name assumption
- Ignore DNS for private link endpoints

---

## Q013: PersistentVolume Claims

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

When do .NET workloads need PVCs on AKS?

### Short Answer (30 seconds)

Stateless APIs: no PVC. Need PVC: file uploads on disk, local cache, legacy app requiring filesystem state. Prefer blob storage over PVC for files.

### Detailed Answer (3–5 minutes)

**AKS:** StorageClass `managed-csi` provisions Azure Disk. Access modes: RWO typical. StatefulSet + volumeClaimTemplates for stable storage per pod.

**Architect:** Default stateless; Azure Blob via SDK for uploads; PVC only with backup/restore runbook.

### Architecture Perspective

PVC introduces state — complicates pod mobility.

### Follow-up Questions

1. **Azure Files vs Disk? — Files ReadWriteMany — shared storage niche.**
2. **Volume expansion? — Allow resize — plan capacity.**

### Common Mistakes in Interviews

- PVC for every API 'just in case'
- No backup for stateful PVC
- RWO disk attached to multiple pods

---

## Q014: Rolling Update Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Configure rolling update for zero-downtime .NET API deploy?

### Short Answer (30 seconds)

Deployment `strategy: RollingUpdate` with `maxUnavailable: 0`, `maxSurge: 1`. Readiness probe gates new pods before old terminate.

### Detailed Answer (3–5 minutes)

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 25%
    maxUnavailable: 0
```

**Architect:** PDB ensures min available during drain; graceful shutdown handles in-flight requests; blue/green or canary for high-risk releases.

### Architecture Perspective

Rolling update + readiness = safe default deploy.

### Follow-up Questions

1. **Recreate strategy? — Downtime — dev only.**
2. **minReadySeconds? — Extra stability before counting ready.**

### Common Mistakes in Interviews

- maxUnavailable 50% on single replica
- No readiness — traffic to starting pods
- Kill pods without graceful shutdown

---

## Q015: ReplicaSet Purpose

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

What is a ReplicaSet and relationship to Deployment?

### Short Answer (30 seconds)

ReplicaSet maintains desired pod replica count via label selector. Deployment manages ReplicaSets — handles rolling updates by creating new ReplicaSet.

### Detailed Answer (3–5 minutes)

**Flow:** Deployment spec change → new ReplicaSet scaled up → old scaled down.

**Architect:** Never manage ReplicaSet directly — always Deployment. `kubectl rollout history` for revision tracking.

### Architecture Perspective

Deployment abstracts ReplicaSet lifecycle for updates.

### Follow-up Questions

1. **Manual ReplicaSet? — Only advanced rollback scenarios.**
2. **Replica count 0? — Pause service without deleting Deployment.**

### Common Mistakes in Interviews

- Edit ReplicaSet directly for image update
- Label selector mismatch — orphan pods
- Ignore rollout history for rollback

---

## Q016: Labels Selectors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design label taxonomy for AKS multi-team platform.

### Short Answer (30 seconds)

Standard labels: `app`, `version`, `team`, `env`, `tier`. Services select pods via `app: orders-api`.

### Detailed Answer (3–5 minutes)

**Example:**
```yaml
labels:
  app.kubernetes.io/name: orders-api
  app.kubernetes.io/version: "2.4.1"
  team: commerce
  env: prod
```

**Architect:** Enforce required labels via admission policy; used in NetworkPolicy, HPA, Service selectors, cost allocation.

### Architecture Perspective

Labels are platform metadata backbone — design early.

### Follow-up Questions

1. **Recommended labels? — kubernetes.io/docs recommended standard labels.**
2. **Annotations vs labels? — Annotations non-identifying metadata — not in selectors.**

### Common Mistakes in Interviews

- Random labels per developer
- Selector too broad — captures wrong pods
- No labels — cannot filter metrics or logs

---

## Q017: K8s RBAC Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Explain Kubernetes RBAC — Role, ClusterRole, Binding.

### Short Answer (30 seconds)

Role: namespace permissions. ClusterRole: cluster-wide. RoleBinding/ClusterRoleBinding attach to User/Group/ServiceAccount.

### Detailed Answer (3–5 minutes)

**Example:** Developer Role `get,list,watch pods,logs` in `orders-dev` namespace. CI ServiceAccount `deploy` Role with `apply` on specific resources.

**Architect:** Least privilege; no cluster-admin for apps; Azure AD integration with AKS for group bindings; audit RBAC quarterly.

### Architecture Perspective

RBAC prevents lateral movement in compromised cluster.

### Follow-up Questions

1. **Aggregate ClusterRoles? — Extend default roles carefully.**
2. **impersonate permission? — Powerful — restrict.**

### Common Mistakes in Interviews

- cluster-admin for all developers
- Shared ServiceAccount across all deployments
- No RBAC — ABAC legacy

---

## Q018: Service Account

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

How use Kubernetes ServiceAccount for .NET pod identity?

### Short Answer (30 seconds)

Each pod runs as ServiceAccount — mounts token for K8s API access. On AKS, link to Azure Workload Identity for Azure resource access without secrets.

### Detailed Answer (3–5 minutes)

**Pattern:**
```yaml
serviceAccountName: orders-api
```

**Workload Identity:** Federated credential → pod SA → Key Vault, Storage, SQL AAD.

**Architect:** One SA per microservice; disable default SA token mount if unused (`automountServiceAccountToken: false`).

### Architecture Perspective

ServiceAccount is pod identity for K8s and cloud federation.

### Follow-up Questions

1. **Legacy pod-managed identity? — Deprecated on AKS — migrate WI.**
2. **Token projection? — Bound short-lived tokens — security.**

### Common Mistakes in Interviews

- Default SA for all pods with API access
- Long-lived Azure client secret in pod
- Same SA cluster-wide admin rights

---

## Q019: Node Pools AKS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design AKS node pool strategy for .NET platform.

### Short Answer (30 seconds)

Separate pools: system (critical addons), user workloads, GPU (if ML), spot (batch). Size pools per workload profile; autoscale node pools.

### Detailed Answer (3–5 minutes)

**Example:**
- `system` — 3 nodes min, taint `CriticalAddonsOnly`
- `apps` — D4s_v5, cluster autoscaler 3-20
- `spot` — batch workers, taint `kubernetes.azure.com/scalesetpriority=spot`

**Architect:** AZ spread across pools; patch surge settings; monitor node CPU/memory pressure.

### Architecture Perspective

Node pools isolate workload types and cost profiles.

### Follow-up Questions

1. **Node image upgrade? — AKS channel — plan maintenance windows.**
2. **Private cluster? — API server private — jump host or ARC.**

### Common Mistakes in Interviews

- Single node pool everything
- Spot pool without tolerations
- No system pool — apps evict addons

---

## Q020: K8s vs App Service Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

When AKS vs Azure App Service for .NET APIs?

### Short Answer (30 seconds)

App Service: faster time-to-market, slots, built-in auth, less ops. AKS: multi-service platform, custom networking, service mesh, fine-grained control.

### Detailed Answer (3–5 minutes)

**App Service when:** Small team, few APIs, PaaS ops preference, VNet integration sufficient.

**AKS when:** 10+ services, GitOps platform team, KEDA/custom operators, multi-tenant cluster.

**Architect:** Honest TCO — AKS needs platform engineers; App Service + Container Apps middle ground.

### Architecture Perspective

Orchestration choice is org capability as much as tech.

### Follow-up Questions

1. **Container Apps vs AKS? — Serverless containers — simpler — evaluate.**
2. **Migrate App Service to AKS trigger? — Team scale, K8s-specific needs.**

### Common Mistakes in Interviews

- AKS for single CRUD API startup
- App Service for complex service mesh
- Decision without 3-year ops cost model

---

## Q021: Multi-Container Pods

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

When put multiple containers in one pod vs separate deployments?

### Short Answer (30 seconds)

Same pod: tight coupling, shared network (localhost), shared volumes — sidecar, adapter, log shipper. Separate deployments: independent scale and lifecycle.

### Detailed Answer (3–5 minutes)

**Same pod:** App + Envoy sidecar, app + log forwarder.

**Separate:** Orders API and Catalog API — different scale curves.

**Architect:** Default one primary app container per pod; add sidecars deliberately with resource accounting.

### Architecture Perspective

Pod = atomic scheduling unit — co-scheduled containers.

### Follow-up Questions

1. **Share process namespace? — `shareProcessNamespace: true` — debug niche.**
2. **Adapter container pattern? — Normalize legacy protocol.**

### Common Mistakes in Interviews

- Two microservices in one pod for convenience
- Sidecar without resource limits
- Scale pod because sidecar needs scale not app

---

## Q022: Ephemeral Containers Debug

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

How debug distroless .NET pod without shell using ephemeral containers?

### Short Answer (30 seconds)

`kubectl debug` attaches ephemeral container with shell/tools into running pod namespace — no restart required.

### Detailed Answer (3–5 minutes)

```bash
kubectl debug -it pod/orders-api --image=mcr.microsoft.com/dotnet/sdk:8.0 --target=orders-api --share-processes
```

**Architect:** Enable EphemeralContainers feature (GA); RBAC restrict debug; audit trail; prefer logs/traces over prod debug.

### Architecture Perspective

Ephemeral debug is break-glass for minimal images.

### Follow-up Questions

1. **Copy debug tools via kubectl cp? — Alternative without ephemeral.**
2. **Network capture sidecar? — tcpdump ephemeral for connectivity.**

### Common Mistakes in Interviews

- Restart prod pod to add debug image permanently
- Unrestricted debug for all developers in prod
- No audit of ephemeral container usage

---

## Q023: K8s API Server

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Occasional |

### Question

Role of Kubernetes API server in control plane?

### Short Answer (30 seconds)

API server is front door — validates, persists to etcd, admits resources. All kubectl, controllers, schedulers communicate via API.

### Detailed Answer (3–5 minutes)

**Architect:** Secure API — private cluster, authorized IPs, Azure AD auth. Rate limit abusive clients. Audit logging enabled for compliance.

**High availability:** Multiple API server instances behind load balancer in managed AKS.

### Architecture Perspective

API server security is cluster security perimeter.

### Follow-up Questions

1. **API aggregation? — Extension APIs — metrics, custom metrics.**
2. **Watch vs list? — Controllers watch for changes — efficient.**

### Common Mistakes in Interviews

- Public API server unauthenticated
- Disable audit logs
- Direct etcd access for app config

---

## Q024: etcd Role

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Occasional |

### Question

What does etcd store and why backup matters on AKS?

### Short Answer (30 seconds)

etcd is K8s backing store — all cluster state: pods, secrets, configmaps, deployments. AKS manages etcd — you backup cluster state via Azure Backup or Velero.

### Detailed Answer (3–5 minutes)

**Architect:** etcd loss = cluster brain loss. Use Velero for resource backup; Azure Backup for AKS; test restore quarterly. Application data backup separate (SQL, Blob).

### Architecture Perspective

Cluster backup ≠ application data backup.

### Follow-up Questions

1. **Velero? — Backup K8s resources to Blob — migration and DR.**
2. **etcd encryption? — AKS encrypt secrets at rest.**

### Common Mistakes in Interviews

- Assume AKS backup covers app databases
- Never test cluster restore
- Store critical state only in ConfigMap without backup

---

## Q025: Scheduler Function

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

How does Kubernetes scheduler place pods on nodes?

### Short Answer (30 seconds)

Filters (resource, taints, affinity) → score nodes → bind pod. Considers requests, affinity/anti-affinity, topology spread, priority.

### Detailed Answer (3–5 minutes)

**Architect controls:**
- `nodeSelector` / `nodeAffinity` — GPU, spot
- `podAntiAffinity` — spread replicas across AZ
- `topologySpreadConstraints` — even distribution
- `PriorityClass` — preempt lower priority if needed

### Architecture Perspective

Scheduling affects HA and cost — not random.

### Follow-up Questions

1. **Custom scheduler? — Scheduler framework plugins — advanced.**
2. **Descheduler? — Rebalance pods after node changes.**

### Common Mistakes in Interviews

- No requests — scheduler blind to memory needs
- All pods on single AZ
- Ignore taints on specialized pools

---

## Q026: Kubelet Responsibilities

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Occasional |

### Question

What does kubelet do on each AKS node?

### Short Answer (30 seconds)

Kubelet: register node, watch API for pod specs, run containers via CRI (containerd), report status, run probes, mount volumes.

### Detailed Answer (3–5 minutes)

**Architect relevance:** Kubelet failures → NodeNotReady → pod eviction. Node problems surface in `kubectl describe node` — disk pressure, memory pressure, PID pressure.

**Patching:** AKS node image updates recycle kubelets — plan surge.

### Architecture Perspective

Node health starts with kubelet — understand pressure signals.

### Follow-up Questions

1. **CRI-O vs containerd? — AKS uses containerd.**
2. **Kubelet config? — Eviction thresholds — tune for workloads.**

### Common Mistakes in Interviews

- Ignore NodeNotReady alerts
- Disk pressure from container logs unrotated
- Manual containerd bypass kubelet

---

## Q027: Container Runtime containerd

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

What is containerd and how does it relate to Docker on AKS?

### Short Answer (30 seconds)

containerd is CRI-compliant runtime pulling images and running containers. AKS uses containerd directly — Docker CLI optional for dev only.

### Detailed Answer (3–5 minutes)

**Flow:** kubelet → CRI → containerd → runc → container.

**Architect:** Build images in CI (ACR Tasks), not on nodes. `crictl` for node-level debug. Docker Desktop dev still fine — image format compatible.

### Architecture Perspective

Runtime layer changed — Docker daemon not on AKS nodes.

### Follow-up Questions

1. **nerdctl? — Docker-compatible CLI for containerd nodes.**
2. **Runtime class? — gVisor/Kata via RuntimeClass resource.**

### Common Mistakes in Interviews

- SSH to node and docker run
- Assume Docker socket on AKS worker
- Build images on production nodes

---

## Q028: K8s Security Contexts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Configure securityContext for production .NET pod?

### Short Answer (30 seconds)

runAsNonRoot, readOnlyRootFilesystem, drop ALL capabilities, allowPrivilegeEscalation: false, seccompProfile RuntimeDefault.

### Detailed Answer (3–5 minutes)

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1654
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities:
    drop: [ALL]
```

**Architect:** Pod Security Standards `restricted` enforced via admission; platform chart defaults secure context.

### Architecture Perspective

securityContext is pod-level CIS compliance.

### Follow-up Questions

1. **fsGroup for volume write? — Supplemental group for mounted volumes.**
2. **Capabilities add NET_BIND_SERVICE? — Only if binding <1024 — prefer >1024.**

### Common Mistakes in Interviews

- Privileged true for file access
- Run as root with writable root FS
- No security context — platform default only

---

## Q029: NetworkPolicy Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Design NetworkPolicy for zero-trust between namespaces?

### Short Answer (30 seconds)

Default deny all ingress/egress; allow explicit: ingress from ingress-nginx namespace, egress to kube-dns and Azure SQL private endpoint.

### Detailed Answer (3–5 minutes)

```yaml
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
  ingress:
  - from: [{ namespaceSelector: { matchLabels: { name: ingress } } }]
```

**Architect:** Azure CNI + network policy addon (Calico or Azure NPM); test policies in staging — misconfig causes silent failures.

### Architecture Perspective

NetworkPolicy is micro-segmentation inside cluster.

### Follow-up Questions

1. **Egress to internet? — Explicit allow Azure services tags or proxy.**
2. **Cilium network policies? — L7 policies — advanced.**

### Common Mistakes in Interviews

- No NetworkPolicy — flat cluster trust
- Policy blocks DNS — all egress fails
- Copy policy without testing staging

---

## Q030: K8s Learning Path for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Recommended Kubernetes learning path for .NET architects?

### Short Answer (30 seconds)

CKA fundamentals → deploy sample .NET API → ingress/TLS → observability → GitOps → security (PSA, NetworkPolicy) → AKS production checklist.

### Detailed Answer (3–5 minutes)

**Phases:**
1. **Week 1-2:** Pods, Deployments, Services, kubectl fluency
2. **Week 3-4:** Helm, probes, resources, ConfigMap/Secret
3. **Week 5-6:** AKS — node pools, ACR, Workload Identity
4. **Week 7-8:** HPA, PDB, upgrades, DR, cost

**Architect:** Build platform reference app; whiteboard pod networking; read AKS well-architected.

### Architecture Perspective

Architects need breadth across app, platform, and ops — not only kubectl trivia.

### Follow-up Questions

1. **CKA vs CKAD vs CKS? — CKA admin; CKAD app dev; CKS security — architect benefits CKA+CKS awareness.**
2. **Local kind cluster enough? — Supplement with AKS lab for Azure integration.**

### Common Mistakes in Interviews

- Certification without hands-on deploy
- Only YAML memorization
- Skip Linux and networking fundamentals

---
