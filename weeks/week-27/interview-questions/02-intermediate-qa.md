# Week 27 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Horizontal Pod Autoscaler

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design HPA for .NET API on AKS — metrics and pitfalls?

### Short Answer (30 seconds)

HPA scales Deployment replicas based on metrics — typically CPU/memory or custom (requests/sec). Needs resource requests set; min/max bounds; scale-down stabilization.

### Detailed Answer (3–5 minutes)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
spec:
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource: { name: cpu, target: { type: Utilization, averageUtilization: 70 } }
```

**Architect:** CPU alone insufficient for IO-bound — use KEDA or custom metrics from Prometheus. Cooldown prevents flapping.

### Architecture Perspective

HPA is default scale mechanism — configure with load test validation.

### Follow-up Questions

1. **HPA v2 behavior? — Multiple metrics — max of recommendations.**
2. **Scale to zero? — HPA min 1 — use KEDA for zero.**

### Common Mistakes in Interviews

- HPA without resource requests
- maxReplicas unlimited — cost surprise
- CPU target 90% — no headroom for spikes

---

## Q032: Vertical Pod Autoscaler

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

When use Vertical Pod Autoscaler vs HPA?

### Short Answer (30 seconds)

VPA adjusts CPU/memory requests per pod — right-sizing. HPA adds replicas. Use VPA in recommendation mode first; avoid VPA + HPA on same CPU metric conflict.

### Detailed Answer (3–5 minutes)

**Modes:** Off (recommend only), Initial, Auto (restart pods to apply).

**Architect:** Run VPA recommender — review recommendations quarterly; apply to batch jobs; for APIs prefer HPA + manual request tuning after load test.

### Architecture Perspective

VPA solves 'wrong request size' not 'need more pods'.

### Follow-up Questions

1. **VPA updater eviction? — Auto mode restarts pods — plan disruption.**
2. **Goldilocks? — Dashboard for VPA recommendations.**

### Common Mistakes in Interviews

- VPA Auto on prod without PDB
- VPA and HPA same CPU metric
- Ignore VPA recommendations forever

---

## Q033: KEDA Event Scaling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Scale .NET worker from zero using KEDA on Azure Service Bus?

### Short Answer (30 seconds)

KEDA ScaledObject watches queue depth — scales Deployment 0→N. No messages = zero replicas — cost savings.

### Detailed Answer (3–5 minutes)

```yaml
spec:
  scaleTargetRef: { name: order-worker }
  minReplicaCount: 0
  maxReplicaCount: 30
  triggers:
  - type: azure-servicebus
    metadata:
      queueName: orders
      messageCount: "5"
```

**Architect:** KEDA on AKS via add-on; idempotent workers mandatory; cold start acceptable for async workloads.

### Architecture Perspective

KEDA enables event-driven scale including zero — cloud cost optimization.

### Follow-up Questions

1. **KEDA vs HPA? — KEDA for external metrics and scale-to-zero.**
2. **Multiple triggers? — Scale on max of queue depth and CPU.**

### Common Mistakes in Interviews

- Non-idempotent worker at scale
- minReplicaCount 0 with strict latency SLA
- No dead-letter handling at scale-out

---

## Q034: GitOps Argo CD

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Implement GitOps with Argo CD for .NET microservices on AKS?

### Short Answer (30 seconds)

Git repo is source of truth — Argo CD syncs cluster state to manifests/Helm. PR merge triggers deploy; drift detection and rollback via Git revert.

### Detailed Answer (3–5 minutes)

**Architecture:**
- Repo: `deploy/orders-api/overlays/prod`
- Argo Application per service or app-of-apps
- Image updater or CI commits new tag to Git

**Architect:** RBAC on Argo; secrets via External Secrets; progressive sync waves for CRDs first.

### Architecture Perspective

GitOps provides audit trail and reproducible deploys.

### Follow-up Questions

1. **App of apps pattern? — Bootstrap cluster apps from one root Application.**
2. **Sync hooks? — PreSync migration Job.**

### Common Mistakes in Interviews

- kubectl apply from laptop prod
- Manual cluster changes not reverted
- Secrets in Git plain text

---

## Q035: Flux vs Argo

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Compare Flux and Argo CD for AKS GitOps platform?

### Short Answer (30 seconds)

Argo CD: UI-first, application-centric, strong multi-cluster dashboard. Flux: CNCF, controller-native, integrates with Helm/Kustomize, lighter UI.

### Detailed Answer (3–5 minutes)

**Argo strengths:** Visibility for many teams, RBAC projects, sync waves.

**Flux strengths:** Git-native composition, Terraform integration, smaller footprint.

**Architect:** Pick one per org — both excellent. Azure GitOps (Flux-based) is managed option on AKS.

### Architecture Perspective

Tool choice less important than GitOps discipline.

### Follow-up Questions

1. **Azure GitOps Flux extension? — Managed install on AKS.**
2. **Multi-cluster Argo? — ApplicationSet — fleet deploy.**

### Common Mistakes in Interviews

- Both Flux and Argo same cluster fighting
- No drift detection enabled
- GitOps without PR review

---

## Q036: Service Mesh Istio Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

When adopt Istio service mesh for .NET microservices?

### Short Answer (30 seconds)

When you need: mTLS east-west, traffic splitting canary, unified telemetry, retries/timeouts as policy without code change — and team can operate mesh complexity.

### Detailed Answer (3–5 minutes)

**Components:** Control plane (istiod) + data plane sidecar (Envoy).

**Architect:** Start without mesh; add when 8+ services need mTLS policy; evaluate ambient mesh for reduced sidecar overhead.

### Architecture Perspective

Service mesh is platform investment — not day-one default.

### Follow-up Questions

1. **Linkerd vs Istio? — Linkerd simpler lighter — Istio feature-rich.**
2. **Dapr vs mesh? — Dapr app-level building blocks — can coexist.**

### Common Mistakes in Interviews

- Mesh for two services
- No mesh observability before adoption
- Sidecar resource cost ignored in capacity plan

---

## Q037: mTLS East-West

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Why mTLS for east-west traffic in Kubernetes?

### Short Answer (30 seconds)

Encrypts pod-to-pod traffic — zero-trust inside cluster. Prevents lateral eavesdropping if attacker compromises one pod.

### Detailed Answer (3–5 minutes)

**Istio:** PeerAuthentication STRICT — auto mTLS. **Without mesh:** manual cert distribution impractical at scale.

**Architect:** Compliance (PCI, HIPAA) may require encryption in transit even 'internal'. Document performance overhead (~1-5% latency).

### Architecture Perspective

East-west mTLS is zero-trust inside the perimeter.

### Follow-up Questions

1. **SPIFFE/SPIRE? — Identity framework underlying mesh certs.**
2. **PERMISSIVE mode? — Migration — not prod end state.**

### Common Mistakes in Interviews

- TLS only at ingress — plaintext inside cluster
- Shared cert all services — no identity
- mTLS without rotation plan

---

## Q038: Canary with Argo Rollouts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Implement canary deployment for .NET API using Argo Rollouts?

### Short Answer (30 seconds)

Argo Rollouts replaces Deployment — progressive traffic shift 10%→50%→100% with analysis gates on error rate and latency.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Install Rollouts controller
2. Define Rollout with canary steps and AnalysisTemplate (Prometheus metrics)
3. Ingress/Service mesh splits traffic

**Architect:** Automated rollback on SLO breach; manual promotion gate for high-risk changes.

### Architecture Perspective

Canary reduces blast radius vs big-bang rolling update.

### Follow-up Questions

1. **Flagger vs Rollouts? — Flagger similar — GitOps native.**
2. **Blue/green vs canary? — Blue/green instant switch — higher resource cost.**

### Common Mistakes in Interviews

- Canary without metrics analysis
- 10% canary on untested error budget
- No rollback automation

---

## Q039: Pod Disruption Budget

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Configure PDB during AKS node drain and cluster upgrade?

### Short Answer (30 seconds)

PDB ensures minAvailable or maxUnavailable pods during voluntary disruptions — node drain, rollout.

### Detailed Answer (3–5 minutes)

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
spec:
  minAvailable: 2
  selector:
    matchLabels: { app: orders-api }
```

**Architect:** PDB + minReplicas ≥ minAvailable + 1; without PDB node upgrade kills too many pods — outage.

### Architecture Perspective

PDB protects availability during planned maintenance.

### Follow-up Questions

1. **minAvailable vs maxUnavailable? — Choose one — math with replicas.**
2. **PDB blocks node drain? — Expected — scale up or adjust temporarily.**

### Common Mistakes in Interviews

- No PDB on critical API
- minAvailable equals replica count — no drains possible
- PDB only on Deployment not StatefulSet

---

## Q040: Cluster Autoscaling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

How cluster autoscaler works on AKS with multiple node pools?

### Short Answer (30 seconds)

Pending unschedulable pods trigger scale up; underutilized nodes scale down after cooldown. Per node pool autoscale profile.

### Detailed Answer (3–5 minutes)

**Settings:**
- `min-count`, `max-count` per pool
- Balance similar node groups
- PodDisruptionBudget affects drain speed

**Architect:** Set max to prevent runaway cost; separate spot pool autoscale; alert on failed scale-up (quota, subnet full).

### Architecture Perspective

Cluster autoscaler links pod demand to infrastructure cost.

### Follow-up Questions

1. **Scale-up failures? — Azure quota, subnet IP exhaustion — monitor.**
2. **Over-provisioning? — Placeholder pods reserve capacity — advanced.**

### Common Mistakes in Interviews

- max-count unlimited
- Single node pool autoscale only
- Ignore scale-up failures in alerts

---

## Q041: AKS Node Pool Taints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Use taints and tolerations for specialized AKS node pools?

### Short Answer (30 seconds)

Taint repels pods unless toleration matches — dedicates nodes to workloads (GPU, spot, system).

### Detailed Answer (3–5 minutes)

**Example:** Spot pool taint `kubernetes.azure.com/scalesetpriority=spot:NoSchedule` — only batch workers with toleration schedule there.

**Architect:** System pool taint protects addons; document toleration in Helm chart values for spot workloads.

### Architecture Perspective

Taints enforce workload placement policy.

### Follow-up Questions

1. **NoSchedule vs PreferNoSchedule? — Hard vs soft eviction.**
2. **Taint by default AKS? — CriticalAddonsOnly on system pool.**

### Common Mistakes in Interviews

- Spot workload without toleration — never schedules
- Taint user pool blocking all apps
- No taint on GPU pool — wrong workloads scheduled

---

## Q042: Spot Instances Workloads

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Which workloads suit AKS spot node pools?

### Short Answer (30 seconds)

Fault-tolerant batch: report generation, image processing, CI runners, queue workers with retry — not synchronous API frontends.

### Detailed Answer (3–5 minutes)

**Pattern:** Pod disruption toleration + graceful shutdown + checkpoint progress. Mix spot + on-demand pools — critical on on-demand.

**Architect:** Cost savings 60-90% — design for eviction notice (30s).

### Architecture Perspective

Spot is cost lever for interruptible compute.

### Follow-up Questions

1. **Spot eviction handler? — Save state on SIGTERM.**
2. **Spot-only API Deployment? — SLA risk — avoid.**

### Common Mistakes in Interviews

- Stateful API on spot without fallback
- Ignore eviction grace period
- No retry on spot preemption

---

## Q043: Multi-Zone Deployment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design multi-AZ deployment for .NET API on AKS?

### Short Answer (30 seconds)

Spread nodes across availability zones; pod anti-affinity or topologySpreadConstraints; zone-redundant Load Balancer; external dependencies multi-AZ.

### Detailed Answer (3–5 minutes)

```yaml
topologySpreadConstraints:
- maxSkew: 1
  topologyKey: topology.kubernetes.io/zone
  whenUnsatisfiable: DoNotSchedule
```

**Architect:** Azure SLA requires zones for 99.95%+; test single-AZ failure; SQL/Redis zone redundancy separate concern.

### Architecture Perspective

AZ spread is baseline HA for regional services.

### Follow-up Questions

1. **ZRS storage? — Zone redundant for PVC backup targets.**
2. **Cross-zone latency? — Usually negligible within region.**

### Common Mistakes in Interviews

- All nodes single AZ
- Replicas 2 across 3 zones — uneven spread
- Ignore dependency AZ redundancy

---

## Q044: Cluster Upgrades Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Plan AKS Kubernetes version upgrade with minimal risk?

### Short Answer (30 seconds)

Upgrade control plane first, then node pools one at a time with surge. Test in staging cluster; read release notes for breaking API changes.

### Detailed Answer (3–5 minutes)

**Process:**
1. Staging cluster on target version — run integration tests
2. Upgrade dev → staging → prod clusters
3. Node image upgrade with `maxSurge` — PDB respected
4. Pin deprecated API versions before upgrade

**Architect:** Stay within N-2 supported versions; automate `pluto` API deprecation scan.

### Architecture Perspective

Cluster upgrade is recurring platform event — plan not panic.

### Follow-up Questions

1. **Auto-upgrade channels? — patch vs stable — choose policy.**
2. **Blue cluster migration? — New cluster cutover for major jumps.**

### Common Mistakes in Interviews

- Skip staging upgrade test
- Upgrade prod control plane Friday 5pm
- Deprecated APIs break workloads post-upgrade

---

## Q045: etcd Backup

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Backup strategy for AKS cluster state beyond Azure-managed etcd?

### Short Answer (30 seconds)

Velero backs up K8s resources to Blob; Azure Backup for AKS; export critical manifests in Git (GitOps). Application data separate.

### Detailed Answer (3–5 minutes)

**Velero schedule:** Daily namespace backup; retention 30 days; test restore to dev cluster quarterly.

**Architect:** DR runbook: restore cluster + redeploy apps from Git + restore SQL from backup.

### Architecture Perspective

Cluster backup enables migration and disaster recovery of K8s config.

### Follow-up Questions

1. **Velero volume snapshots? — PVC snapshot — coordinate with Azure Disk.**
2. **Backup encryption? — Customer-managed keys in Blob.**

### Common Mistakes in Interviews

- Only GitOps — no Velero for cluster-scoped resources
- Never test restore
- Confuse etcd backup with database backup

---

## Q046: Disaster Recovery AKS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design DR for critical .NET platform on AKS?

### Short Answer (30 seconds)

Active-passive secondary region: ACR geo-replication, Terraform/Bicep infra, GitOps redeploy, SQL geo-replication, Front Door failover, RTO/RPO defined.

### Detailed Answer (3–5 minutes)

**Tiers:**
- **RPO 1h:** Async DB replicate + Velero + GitOps
- **RTO 4h:** Documented runbook + quarterly drill

**Architect:** DR is tested procedure not diagram — failover drill mandatory.

### Architecture Perspective

AKS DR spans registry, DNS, data, and Git — not just cluster.

### Follow-up Questions

1. **Multi-region active-active? — Complex — conflict resolution — rare.**
2. **Chaos failover test? — Game day validates runbook.**

### Common Mistakes in Interviews

- DR slide deck never tested
- Single region ACR no geo-rep
- RTO undefined — no prioritization

---

## Q047: Cost Optimization K8s

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Top Kubernetes cost optimizations on Azure for .NET workloads?

### Short Answer (30 seconds)

Right-size requests, KEDA scale-to-zero, spot pools for batch, cluster autoscaler max bounds, reserved instances for baseline nodes, ACR retention, off-hours dev cluster shutdown.

### Detailed Answer (3–5 minutes)

**FinOps:**
- VPA recommendations → reduce over-provisioned requests
- Remove unused LoadBalancers and orphaned PVCs
- Azure Cost Management tags by namespace label

**Architect:** Monthly cost review per team namespace; chargeback model.

### Architecture Perspective

K8s cost surprises come from idle capacity and forgotten resources.

### Follow-up Questions

1. **Kubecost? — Allocation visibility by label.**
2. **Dev cluster schedule? — Start/stop nights — 50% savings.**

### Common Mistakes in Interviews

- Requests 4x actual usage
- LoadBalancer per service
- No namespace cost allocation

---

## Q048: Resource Quotas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Apply ResourceQuota per team namespace on AKS?

### Short Answer (30 seconds)

ResourceQuota caps total CPU/memory/pods/objects per namespace — prevents one team consuming cluster.

### Detailed Answer (3–5 minutes)

```yaml
spec:
  hard:
    requests.cpu: "20"
    requests.memory: 40Gi
    pods: "50"
```

**Architect:** Pair with LimitRange for default container limits; quota aligned to cluster capacity / team allocation.

### Architecture Perspective

Quotas enforce fair sharing on multi-tenant platform.

### Follow-up Questions

1. **Object count quotas? — Limit ConfigMaps, Services explosion.**
2. **Quota increase process? — Ticket with capacity review.**

### Common Mistakes in Interviews

- No quotas — one team exhausts cluster
- Quota too low — legitimate deploy blocked silently
- Quota without LimitRange — pods with no limits

---

## Q049: Limit Ranges

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

What does LimitRange provide vs ResourceQuota?

### Short Answer (30 seconds)

LimitRange sets default/min/max per container or pod in namespace — ResourceQuota caps namespace total.

### Detailed Answer (3–5 minutes)

**Example:** Default request 100m CPU if unspecified; max single pod 4 CPU — prevents typo `cpu: 100`.

**Architect:** Admission rejects pods violating limits — safer than runtime OOM surprises.

### Architecture Perspective

LimitRange catches misconfigured manifests early.

### Follow-up Questions

1. **Default vs defaultRequest? — Request for scheduling; limit for cap.**
2. **PVC LimitRange? — Min/max storage per claim.**

### Common Mistakes in Interviews

- No defaults — BestEffort pods evicted
- Max limit blocks legitimate batch job
- LimitRange and quota conflict unreviewed

---

## Q050: Admission Controllers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

What admission controllers enforce on AKS and why architects care?

### Short Answer (30 seconds)

Mutating and validating webhooks intercept API requests — enforce labels, security context, image registry allowlist, resource requirements before pod schedules.

### Detailed Answer (3–5 minutes)

**Built-in:** NamespaceLifecycle, ResourceQuota, PodSecurity.

**Custom:** OPA Gatekeeper, Kyverno — policy as code.

**Architect:** Platform policies: deny `:latest`, require probes, require non-root, allowed registries only.

### Architecture Perspective

Admission is policy enforcement gate — shift-left security.

### Follow-up Questions

1. **Validating vs mutating? — Mutate injects sidecar/defaults; validate rejects.**
2. **Webhook failure policy? — Fail closed for security policies.**

### Common Mistakes in Interviews

- No admission policies — any image deploys
- Webhook timeout blocks all deploys
- Policies without exception workflow

---

## Q051: OPA Gatekeeper

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Example Gatekeeper policies for AKS .NET platform?

### Short Answer (30 seconds)

ConstraintTemplates + Constraints: require labels, block privileged, require resource limits, allowed ACR registry prefix only.

### Detailed Answer (3–5 minutes)

```rego
# Pseudologic: image must start with mycompany.azurecr.io
violation[{...}] {
  not startswith(input.review.object.spec.containers[_].image, "mycompany.azurecr.io/")
}
```

**Architect:** Start with 5 critical constraints; expand; dry-run audit mode before enforce.

### Architecture Perspective

OPA Gatekeeper is policy-as-code for K8s.

### Follow-up Questions

1. **Kyverno vs Gatekeeper? — Kyverno YAML-native — easier for some teams.**
2. **Azure Policy for AKS? — Managed Gatekeeper integration.**

### Common Mistakes in Interviews

- Policy sprawl 100 constraints day one
- Enforce without audit dry-run
- No exemption process for emergencies

---

## Q052: Secrets CSI Driver

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Integrate Azure Key Vault with AKS using Secrets Store CSI Driver?

### Short Answer (30 seconds)

CSI driver mounts Key Vault secrets as files in pod; sync to K8s Secret optional; Workload Identity authenticates without client secret.

### Detailed Answer (3–5 minutes)

**Flow:**
1. Enable Workload Identity on AKS
2. SecretProviderClass references Key Vault secrets
3. Pod volume mount → `/mnt/secrets-store`
4. .NET reads file or synced K8s Secret

**Architect:** Rotation without pod restart if app supports reload; prefer file mount over env for rotation.

### Architecture Perspective

CSI driver eliminates long-lived secrets in Git and images.

### Follow-up Questions

1. **Rotation poll interval? — Driver refreshes — app must reload.**
2. **Multiple Key Vaults? — SecretProviderClass per vault region.**

### Common Mistakes in Interviews

- Key Vault secrets in GitOps YAML
- Client secret in cluster for Key Vault
- No rotation — static mounted secret forever

---

## Q053: Workload Identity AKS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Configure Workload Identity for .NET pod accessing Azure SQL and Blob?

### Short Answer (30 seconds)

Federated identity credential links K8s SA to Entra app — pod gets token via OIDC — no secrets in cluster.

### Detailed Answer (3–5 minutes)

**Steps:**
1. AKS OIDC issuer enabled
2. Entra app + federated credential (namespace, SA name)
3. ServiceAccount annotation `azure.workload.identity/client-id`
4. .NET `DefaultAzureCredential` in pod

**Architect:** Replace pod-managed identity and secrets; audit federated credentials per service.

### Architecture Perspective

Workload Identity is standard Azure-K8s auth pattern.

### Follow-up Questions

1. **DefaultAzureCredential chain? — Works in pod with federated token.**
2. **Multi-tenant? — Separate app registration per environment.**

### Common Mistakes in Interviews

- Connection string with password in K8s Secret
- Shared Entra app all microservices
- Federated credential wildcard namespace

---

## Q054: Ingress TLS cert-manager

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Automate TLS certificates for AKS ingress with cert-manager?

### Short Answer (30 seconds)

cert-manager issues and renews certs from Let's Encrypt or private CA — stores in Secret; ingress references `tls.secretName`.

### Detailed Answer (3–5 minutes)

```yaml
annotations:
  cert-manager.io/cluster-issuer: letsencrypt-prod
```

**Architect:** DNS-01 for wildcard; HTTP-01 for simple; monitor cert expiry alerts as backup; private CA for internal services.

### Architecture Perspective

Automated TLS prevents expiry outages.

### Follow-up Questions

1. **cert-manager vs App Gateway managed cert? — Choose per ingress layer.**
2. **Rate limits Let's Encrypt? — Staging issuer for testing.**

### Common Mistakes in Interviews

- Manual cert paste yearly
- Expired cert outage no alert
- TLS only on external not internal east-west

---

## Q055: External DNS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

How External DNS manages Azure DNS for Kubernetes ingress?

### Short Answer (30 seconds)

External DNS controller watches Ingress/Service — creates/updates A records in Azure DNS zone automatically.

### Detailed Answer (3–5 minutes)

**Flow:** Ingress `host: api.mycompany.com` → External DNS → A record to LoadBalancer IP.

**Architect:** TXT registry ownership records; restrict DNS zone RBAC; GitOps still owns ingress manifest — DNS follows.

### Architecture Perspective

External DNS removes manual DNS ticket per deploy.

### Follow-up Questions

1. **Private DNS zone? — Internal ingress — private link integration.**
2. **DNS TTL? — Lower for faster failover — higher for cache.**

### Common Mistakes in Interviews

- Manual DNS per service deploy
- Wrong zone — prod record in dev zone
- No ownership TXT — orphan records

---

## Q056: Chaos Engineering K8s

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Occasional |

### Question

Run chaos experiments safely on AKS staging?

### Short Answer (30 seconds)

Use Chaos Mesh or Litmus to kill pods, inject network latency, fill disk — in staging with blast radius controls and steady-state hypothesis.

### Detailed Answer (3–5 minutes)

**Example experiment:** Kill 1 orders-api pod — hypothesis: error rate <0.1%, P99 <500ms.

**Architect:** Game days quarterly; never chaos in prod without mature observability and rollback; start with pod delete not network partition.

### Architecture Perspective

Chaos validates resilience assumptions before real incidents.

### Follow-up Questions

1. **Azure Chaos Studio? — Managed fault injection — VM and AKS.**
2. **Blast radius? — Namespace isolated staging — not shared.**

### Common Mistakes in Interviews

- Chaos in prod first experiment
- No steady-state metrics during chaos
- Chaos without PDB understanding

---

## Q057: Multi-Cluster Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

When operate multiple AKS clusters vs one large cluster?

### Short Answer (30 seconds)

Multi-cluster: blast isolation (prod/dev), regulatory boundaries, region presence, team autonomy. Single cluster: cost efficiency, simpler ops — namespaces isolate.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Prod cluster + non-prod cluster** — common minimum
- **Cluster per region** — data residency
- **Fleet management** — GitOps ApplicationSet

**Architect:** Avoid cluster sprawl without automation — each cluster needs upgrades and monitoring.

### Architecture Perspective

Cluster count is org and compliance decision.

### Follow-up Questions

1. **Hub-spoke clusters? — Centralized ingress/logging hub.**
2. **Cluster API? — Unified K8s API across clusters — advanced.**

### Common Mistakes in Interviews

- 20 clusters without GitOps automation
- Single prod cluster no env isolation
- Multi-cluster without fleet visibility

---

## Q058: Fleet Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Occasional |

### Question

What is Kubernetes fleet management for architects?

### Short Answer (30 seconds)

Unified governance across clusters — Azure Fleet Manager, Argo CD ApplicationSet, Cluster API — consistent policy, upgrade orchestration, multi-cluster deploy.

### Detailed Answer (3–5 minutes)

**Azure Fleet:** Update orchestration across member clusters; resource propagation.

**Architect:** Platform team operates fleet; application teams deploy via GitOps to assigned clusters; central policy (Azure Policy, OPA) synced.

### Architecture Perspective

Fleet scales GitOps and policy to many clusters.

### Follow-up Questions

1. **Hub cluster pattern? — Management cluster deploys to spokes.**
2. **Fleet upgrade waves? — Canary cluster first — then fleet.**

### Common Mistakes in Interviews

- Manual kubectl each cluster upgrade
- Inconsistent versions across fleet
- No central policy sync

---

## Q059: K8s Observability Stack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design observability stack for .NET on AKS?

### Short Answer (30 seconds)

Metrics: Prometheus + Grafana or Azure Monitor managed Prometheus. Logs: Fluent Bit → Log Analytics. Traces: OpenTelemetry → App Insights/Jaeger. Alerts on SLO burn rate.

### Detailed Answer (3–5 minutes)

**Layers:**
- **Infra:** Node metrics, kube-state-metrics
- **App:** OTel SDK in .NET — traces correlate logs
- **Synthetic:** Availability tests hit ingress

**Architect:** Standard dashboards per service golden signals; alert runbooks linked.

### Architecture Perspective

Observability is platform mandate — not per-team optional.

### Follow-up Questions

1. **Managed Grafana on Azure? — Integrated with AMP and AMW.**
2. **eBPF monitoring? — Cilium Hubble — network observability.**

### Common Mistakes in Interviews

- Logs only no metrics
- No trace propagation across services
- Alert on every pod restart without SLO context

---

## Q060: Production Readiness Checklist AKS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Production readiness checklist before .NET API on AKS go-live?

### Short Answer (30 seconds)

Probes, resources, PDB, HPA, NetworkPolicy, Workload Identity, image scan gate, GitOps deploy, DR tested, observability, runbooks, capacity tested, security context restricted.

### Detailed Answer (3–5 minutes)

**Checklist categories:**
1. **Reliability:** replicas≥3, multi-AZ, PDB, graceful shutdown
2. **Security:** non-root, WI, NetworkPolicy, no secrets in Git
3. **Ops:** on-call runbook, alerts, upgrade path
4. **Performance:** load test at 2× expected traffic
5. **Compliance:** SBOM, audit logs, backup verified

**Architect:** Sign-off gate — no exceptions without risk acceptance.

### Architecture Perspective

Production readiness is explicit gate — not implicit hope.

### Follow-up Questions

1. **Production readiness review template? — Platform team document — per service.**
2. **Go-live without game day? — Schedule post-launch hypercare.**

### Common Mistakes in Interviews

- Missing readiness probe go-live
- Single replica production
- No load test evidence in ADR

---

## Q061: Horizontal Pod Autoscaler Custom Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Horizontal Pod Autoscaler Custom Metrics — what do you need to know and decide?

### Short Answer (30 seconds)

Horizontal Pod Autoscaler Custom Metrics requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *Horizontal Pod Autoscaler Custom Metrics*
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

Intermediate interviewers expect you to connect Horizontal Pod Autoscaler Custom Metrics to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Horizontal Pod Autoscaler Custom Metrics is healthy in production?**
2. **What is the rollback plan if Horizontal Pod Autoscaler Custom Metrics change fails?**

### Common Mistakes in Interviews

- Treating Horizontal Pod Autoscaler Custom Metrics as set-and-forget with no monitoring
- No ADR documenting trade-offs for Horizontal Pod Autoscaler Custom Metrics
- Copying Horizontal Pod Autoscaler Custom Metrics pattern from blog without context fit

---

## Q062: KEDA ScaledObject

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: KEDA ScaledObject — what do you need to know and decide?

### Short Answer (30 seconds)

KEDA ScaledObject requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *KEDA ScaledObject*
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

Intermediate interviewers expect you to connect KEDA ScaledObject to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove KEDA ScaledObject is healthy in production?**
2. **What is the rollback plan if KEDA ScaledObject change fails?**

### Common Mistakes in Interviews

- Treating KEDA ScaledObject as set-and-forget with no monitoring
- No ADR documenting trade-offs for KEDA ScaledObject
- Copying KEDA ScaledObject pattern from blog without context fit

---

## Q063: Cluster Autoscaler Triggers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Cluster Autoscaler Triggers — what do you need to know and decide?

### Short Answer (30 seconds)

Cluster Autoscaler Triggers requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *Cluster Autoscaler Triggers*
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

Intermediate interviewers expect you to connect Cluster Autoscaler Triggers to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Cluster Autoscaler Triggers is healthy in production?**
2. **What is the rollback plan if Cluster Autoscaler Triggers change fails?**

### Common Mistakes in Interviews

- Treating Cluster Autoscaler Triggers as set-and-forget with no monitoring
- No ADR documenting trade-offs for Cluster Autoscaler Triggers
- Copying Cluster Autoscaler Triggers pattern from blog without context fit

---

## Q064: Pod Disruption Budget Game Day

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Pod Disruption Budget Game Day — what do you need to know and decide?

### Short Answer (30 seconds)

Pod Disruption Budget Game Day requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *Pod Disruption Budget Game Day*
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

Intermediate interviewers expect you to connect Pod Disruption Budget Game Day to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Pod Disruption Budget Game Day is healthy in production?**
2. **What is the rollback plan if Pod Disruption Budget Game Day change fails?**

### Common Mistakes in Interviews

- Treating Pod Disruption Budget Game Day as set-and-forget with no monitoring
- No ADR documenting trade-offs for Pod Disruption Budget Game Day
- Copying Pod Disruption Budget Game Day pattern from blog without context fit

---

## Q065: Pod Topology Spread

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Pod Topology Spread — what do you need to know and decide?

### Short Answer (30 seconds)

Pod Topology Spread requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *Pod Topology Spread*
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

Intermediate interviewers expect you to connect Pod Topology Spread to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Pod Topology Spread is healthy in production?**
2. **What is the rollback plan if Pod Topology Spread change fails?**

### Common Mistakes in Interviews

- Treating Pod Topology Spread as set-and-forget with no monitoring
- No ADR documenting trade-offs for Pod Topology Spread
- Copying Pod Topology Spread pattern from blog without context fit

---

## Q066: Affinity Anti-Affinity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Affinity Anti-Affinity — what do you need to know and decide?

### Short Answer (30 seconds)

Affinity Anti-Affinity requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *Affinity Anti-Affinity*
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

Intermediate interviewers expect you to connect Affinity Anti-Affinity to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Affinity Anti-Affinity is healthy in production?**
2. **What is the rollback plan if Affinity Anti-Affinity change fails?**

### Common Mistakes in Interviews

- Treating Affinity Anti-Affinity as set-and-forget with no monitoring
- No ADR documenting trade-offs for Affinity Anti-Affinity
- Copying Affinity Anti-Affinity pattern from blog without context fit

---

## Q067: Taints Tolerations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Taints Tolerations — what do you need to know and decide?

### Short Answer (30 seconds)

Taints Tolerations requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *Taints Tolerations*
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

Intermediate interviewers expect you to connect Taints Tolerations to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Taints Tolerations is healthy in production?**
2. **What is the rollback plan if Taints Tolerations change fails?**

### Common Mistakes in Interviews

- Treating Taints Tolerations as set-and-forget with no monitoring
- No ADR documenting trade-offs for Taints Tolerations
- Copying Taints Tolerations pattern from blog without context fit

---

## Q068: Node Selector Pools

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Node Selector Pools — what do you need to know and decide?

### Short Answer (30 seconds)

Node Selector Pools requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *Node Selector Pools*
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

Intermediate interviewers expect you to connect Node Selector Pools to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Node Selector Pools is healthy in production?**
2. **What is the rollback plan if Node Selector Pools change fails?**

### Common Mistakes in Interviews

- Treating Node Selector Pools as set-and-forget with no monitoring
- No ADR documenting trade-offs for Node Selector Pools
- Copying Node Selector Pools pattern from blog without context fit

---

## Q069: GPU Node Pool

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: GPU Node Pool — what do you need to know and decide?

### Short Answer (30 seconds)

GPU Node Pool requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *GPU Node Pool*
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

Intermediate interviewers expect you to connect GPU Node Pool to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove GPU Node Pool is healthy in production?**
2. **What is the rollback plan if GPU Node Pool change fails?**

### Common Mistakes in Interviews

- Treating GPU Node Pool as set-and-forget with no monitoring
- No ADR documenting trade-offs for GPU Node Pool
- Copying GPU Node Pool pattern from blog without context fit

---

## Q070: Ingress TLS cert-manager

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Ingress TLS cert-manager — what do you need to know and decide?

### Short Answer (30 seconds)

Ingress TLS cert-manager requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 27 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 27 — Kubernetes):**
- Scenario: production system at scale needs a decision involving *Ingress TLS cert-manager*
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

Intermediate interviewers expect you to connect Ingress TLS cert-manager to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Ingress TLS cert-manager is healthy in production?**
2. **What is the rollback plan if Ingress TLS cert-manager change fails?**

### Common Mistakes in Interviews

- Treating Ingress TLS cert-manager as set-and-forget with no monitoring
- No ADR documenting trade-offs for Ingress TLS cert-manager
- Copying Ingress TLS cert-manager pattern from blog without context fit

---
