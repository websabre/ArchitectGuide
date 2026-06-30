# Week 31 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Bicep Module Composition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Bicep |
| **Frequency** | Very Common |

### Question

How would you implement Bicep Module Composition with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Reusable modules for VNet, AKS, Key Vault; semantic versioning; what-if on PR.

### Detailed Answer (3–5 minutes)

**Bicep Module Composition** (IaC context)

Reusable modules for VNet, AKS, Key Vault; semantic versioning; what-if on PR.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Bicep Module Composition separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Bicep-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q072: Terraform State Backend

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Terraform |
| **Frequency** | Very Common |

### Question

How would you implement Terraform State Backend with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Azure Storage backend with state locking; separate state per environment; RBAC on state container.

### Detailed Answer (3–5 minutes)

**Terraform State Backend** (IaC context)

Azure Storage backend with state locking; separate state per environment; RBAC on state container.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Terraform State Backend separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Terraform-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q073: ARM vs Bicep vs Terraform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement ARM vs Bicep vs Terraform with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

ARM verbose; Bicep Azure-native transpile; Terraform multi-cloud — choose per team skill and scope.

### Detailed Answer (3–5 minutes)

**ARM vs Bicep vs Terraform** (IaC context)

ARM verbose; Bicep Azure-native transpile; Terraform multi-cloud — choose per team skill and scope.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

ARM vs Bicep vs Terraform separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q074: Drift Detection Scheduled

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement Drift Detection Scheduled with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Terraform plan cron; Azure Policy compliance scan; alert on unmanaged changes.

### Detailed Answer (3–5 minutes)

**Drift Detection Scheduled** (IaC context)

Terraform plan cron; Azure Policy compliance scan; alert on unmanaged changes.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Drift Detection Scheduled separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q075: GitOps Infrastructure Argo

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | GitOps |
| **Frequency** | Very Common |

### Question

How would you implement GitOps Infrastructure Argo with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Argo CD syncs cluster desired state from Git; PR for infra changes; automated sync with manual prod approve.

### Detailed Answer (3–5 minutes)

**GitOps Infrastructure Argo** (IaC context)

Argo CD syncs cluster desired state from Git; PR for infra changes; automated sync with manual prod approve.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

GitOps Infrastructure Argo separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — GitOps-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q076: Bicep Parameter Files

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Bicep |
| **Frequency** | Very Common |

### Question

How would you implement Bicep Parameter Files with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Environment-specific .bicepparam; Key Vault references for secrets; no secrets in Git.

### Detailed Answer (3–5 minutes)

**Bicep Parameter Files** (IaC context)

Environment-specific .bicepparam; Key Vault references for secrets; no secrets in Git.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Bicep Parameter Files separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Bicep-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q077: Terraform Module Registry

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Terraform |
| **Frequency** | Very Common |

### Question

How would you implement Terraform Module Registry with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Private registry for org modules; version pinning; changelog per module.

### Detailed Answer (3–5 minutes)

**Terraform Module Registry** (IaC context)

Private registry for org modules; version pinning; changelog per module.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Terraform Module Registry separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Terraform-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q078: Remote State Partitioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Terraform |
| **Frequency** | Very Common |

### Question

How would you implement Remote State Partitioning with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

State per subscription/environment; blast radius isolation; cross-stack data sources.

### Detailed Answer (3–5 minutes)

**Remote State Partitioning** (IaC context)

State per subscription/environment; blast radius isolation; cross-stack data sources.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Remote State Partitioning separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Terraform-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q079: Policy as Code Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Policy |
| **Frequency** | Very Common |

### Question

How would you implement Policy as Code Azure with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Azure Policy definitions in Git; deploy via pipeline; deny non-compliant resources.

### Detailed Answer (3–5 minutes)

**Policy as Code Azure** (IaC context)

Azure Policy definitions in Git; deploy via pipeline; deny non-compliant resources.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Policy as Code Azure separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Policy-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q080: Landing Zone Accelerator

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Landing Zones |
| **Frequency** | Very Common |

### Question

How would you implement Landing Zone Accelerator with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Azure Landing Zone reference architecture; platform subscription vs workload subscriptions.

### Detailed Answer (3–5 minutes)

**Landing Zone Accelerator** (IaC context)

Azure Landing Zone reference architecture; platform subscription vs workload subscriptions.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Landing Zone Accelerator separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Landing Zones-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q081: IaC Testing Terratest

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement IaC Testing Terratest with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Integration tests post-deploy; validate NSG rules, RBAC assignments programmatically.

### Detailed Answer (3–5 minutes)

**IaC Testing Terratest** (IaC context)

Integration tests post-deploy; validate NSG rules, RBAC assignments programmatically.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Testing Terratest separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q082: Import Existing Resources

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement Import Existing Resources with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Terraform import for brownfield; document in ADR; avoid manual portal edits going forward.

### Detailed Answer (3–5 minutes)

**Import Existing Resources** (IaC context)

Terraform import for brownfield; document in ADR; avoid manual portal edits going forward.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Import Existing Resources separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q083: IaC Secret Rotation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement IaC Secret Rotation with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Key Vault auto-rotation; update references not hardcoded values; pipeline validates connectivity.

### Detailed Answer (3–5 minutes)

**IaC Secret Rotation** (IaC context)

Key Vault auto-rotation; update references not hardcoded values; pipeline validates connectivity.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Secret Rotation separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q084: Multi-Subscription Deployment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement Multi-Subscription Deployment with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Pipeline service principal scoped per sub; management group hierarchy in Bicep.

### Detailed Answer (3–5 minutes)

**Multi-Subscription Deployment** (IaC context)

Pipeline service principal scoped per sub; management group hierarchy in Bicep.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Multi-Subscription Deployment separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q085: IaC Code Review Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement IaC Code Review Checklist with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

NSG overly permissive, public endpoints, missing tags, no diagnostic settings.

### Detailed Answer (3–5 minutes)

**IaC Code Review Checklist** (IaC context)

NSG overly permissive, public endpoints, missing tags, no diagnostic settings.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Code Review Checklist separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q086: Bicep CI What-If

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Bicep |
| **Frequency** | Very Common |

### Question

How would you implement Bicep CI What-If with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

az deployment group what-if in PR comment; block merge on destructive unexpected changes.

### Detailed Answer (3–5 minutes)

**Bicep CI What-If** (IaC context)

az deployment group what-if in PR comment; block merge on destructive unexpected changes.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Bicep CI What-If separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Bicep-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q087: Terraform Workspace Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Terraform |
| **Frequency** | Very Common |

### Question

How would you implement Terraform Workspace Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Workspaces vs separate directories — recommend separate state for prod isolation.

### Detailed Answer (3–5 minutes)

**Terraform Workspace Strategy** (IaC context)

Workspaces vs separate directories — recommend separate state for prod isolation.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Terraform Workspace Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Terraform-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q088: IaC Rollback Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement IaC Rollback Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Git revert + pipeline apply; state backup before major changes; never manual state edit.

### Detailed Answer (3–5 minutes)

**IaC Rollback Strategy** (IaC context)

Git revert + pipeline apply; state backup before major changes; never manual state edit.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Rollback Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q089: Resource Naming Convention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement Resource Naming Convention with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

CAF naming in Bicep variables; enforce via policy; consistent across 50 subscriptions.

### Detailed Answer (3–5 minutes)

**Resource Naming Convention** (IaC context)

CAF naming in Bicep variables; enforce via policy; consistent across 50 subscriptions.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Resource Naming Convention separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q090: IaC Documentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How would you implement IaC Documentation with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

README per module: inputs, outputs, dependencies, example usage.

### Detailed Answer (3–5 minutes)

**IaC Documentation** (IaC context)

README per module: inputs, outputs, dependencies, example usage.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Documentation separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q091: Brownfield IaC Adoption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How would you implement Brownfield IaC Adoption with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Inventory portal resources; import critical path first; freeze manual changes.

### Detailed Answer (3–5 minutes)

**Brownfield IaC Adoption** (IaC context)

Inventory portal resources; import critical path first; freeze manual changes.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Brownfield IaC Adoption separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q092: IaC Performance Large State

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How would you implement IaC Performance Large State with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

State file >50MB — split stacks; targeted applies; reduce resource count per state.

### Detailed Answer (3–5 minutes)

**IaC Performance Large State** (IaC context)

State file >50MB — split stacks; targeted applies; reduce resource count per state.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Performance Large State separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q093: Cross-Stack References

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Terraform |
| **Frequency** | Common |

### Question

How would you implement Cross-Stack References with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Remote state outputs consumed by app stack; version output contracts.

### Detailed Answer (3–5 minutes)

**Cross-Stack References** (IaC context)

Remote state outputs consumed by app stack; version output contracts.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Cross-Stack References separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Terraform-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q094: IaC Security Scanning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How would you implement IaC Security Scanning with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Checkov/tfsec on PR; block public storage accounts; require private endpoints.

### Detailed Answer (3–5 minutes)

**IaC Security Scanning** (IaC context)

Checkov/tfsec on PR; block public storage accounts; require private endpoints.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Security Scanning separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q095: Hub-Spoke Bicep Module

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Bicep |
| **Frequency** | Common |

### Question

How would you implement Hub-Spoke Bicep Module with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Hub VNet module; spoke peering; Azure Firewall routes; reusable across workloads.

### Detailed Answer (3–5 minutes)

**Hub-Spoke Bicep Module** (IaC context)

Hub VNet module; spoke peering; Azure Firewall routes; reusable across workloads.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Hub-Spoke Bicep Module separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Bicep-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q096: AKS IaC Best Practices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How would you implement AKS IaC Best Practices with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Private cluster, workload identity, Azure CNI overlay, node pool autoscale in Bicep.

### Detailed Answer (3–5 minutes)

**AKS IaC Best Practices** (IaC context)

Private cluster, workload identity, Azure CNI overlay, node pool autoscale in Bicep.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

AKS IaC Best Practices separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q097: IaC Environment Parity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How would you implement IaC Environment Parity with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Same modules dev/prod; scale parameters differ; avoid snowflake prod-only config.

### Detailed Answer (3–5 minutes)

**IaC Environment Parity** (IaC context)

Same modules dev/prod; scale parameters differ; avoid snowflake prod-only config.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Environment Parity separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q098: Terraform Cloud vs Self-Hosted

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How would you implement Terraform Cloud vs Self-Hosted with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

TFC for state/run management vs Azure DevOps agents — cost and compliance trade-off.

### Detailed Answer (3–5 minutes)

**Terraform Cloud vs Self-Hosted** (IaC context)

TFC for state/run management vs Azure DevOps agents — cost and compliance trade-off.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Terraform Cloud vs Self-Hosted separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q099: IaC Disaster Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How would you implement IaC Disaster Recovery with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

State geo-replication; module source mirror; rebuild region from Git in RTO target.

### Detailed Answer (3–5 minutes)

**IaC Disaster Recovery** (IaC context)

State geo-replication; module source mirror; rebuild region from Git in RTO target.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

IaC Disaster Recovery separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q100: Platform Team IaC Standards

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How would you implement Platform Team IaC Standards with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Approved module catalog; exception process; quarterly module deprecation review.

### Detailed Answer (3–5 minutes)

**Platform Team IaC Standards** (IaC context)

Approved module catalog; exception process; quarterly module deprecation review.

**Production implementation:**
```bicep
module vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {
  params: { name: 'vnet-${environment}' }
}
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Platform Team IaC Standards separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — IaC-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---
