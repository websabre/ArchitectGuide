# Week 13 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Hub-Spoke Topology — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Hub-Spoke Topology using hub VNet in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use hub VNet with spokes; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Hub-spoke as default enterprise azure network topology.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Hub-Spoke Topology is core to Azure Solution Architect interviews covering hub VNet, spokes, peering, Azure Firewall.

**Architect approach:**
1. Map business requirement to hub VNet — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Hub-spoke as default enterprise azure network topology.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect hub-spoke as default enterprise Azure network topology — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to hub VNet?**
2. **What KPI proves hub-spoke topology adoption succeeded?**

### Common Mistakes in Interviews

- Listing hub VNet without explaining trade-offs
- No Policy or IaC enforcement for hub-spoke topology
- Skipping operational runbook for hub VNet

---

## Q032: Hub-Spoke Topology — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production hub-spoke topology for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared hub VNet; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared hub VNet and spokes in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Hub-spoke as default enterprise azure network topology.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize hub-spoke topology.

### Follow-up Questions

1. **How do Policy exemptions work during hub-spoke topology migration?**
2. **What FinOps tag strategy supports hub-spoke topology chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for hub VNet testing
- Policies only at resource group — not MG

---

## Q033: Private Link Design — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Private Link Design using private endpoints in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use private endpoints with private DNS zones; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Private link for all production paas data plane access.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Private Link Design is core to Azure Solution Architect interviews covering private endpoints, private DNS zones, DNS resolution.

**Architect approach:**
1. Map business requirement to private endpoints — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Private link for all production paas data plane access.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect Private Link for all production PaaS data plane access — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to private endpoints?**
2. **What KPI proves private link design adoption succeeded?**

### Common Mistakes in Interviews

- Listing private endpoints without explaining trade-offs
- No Policy or IaC enforcement for private link design
- Skipping operational runbook for private endpoints

---

## Q034: Private Link Design — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production private link design for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared private endpoints; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared private endpoints and private DNS zones in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Private link for all production paas data plane access.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize private link design.

### Follow-up Questions

1. **How do Policy exemptions work during private link design migration?**
2. **What FinOps tag strategy supports private link design chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for private endpoints testing
- Policies only at resource group — not MG

---

## Q035: Azure Front Door — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure Front Door using Front Door in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use Front Door with global load balancing; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Front door for global internet-facing multi-region apps.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Azure Front Door is core to Azure Solution Architect interviews covering Front Door, global load balancing, WAF, caching.

**Architect approach:**
1. Map business requirement to Front Door — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Front door for global internet-facing multi-region apps.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect Front Door for global internet-facing multi-region apps — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Front Door?**
2. **What KPI proves azure front door adoption succeeded?**

### Common Mistakes in Interviews

- Listing Front Door without explaining trade-offs
- No Policy or IaC enforcement for azure front door
- Skipping operational runbook for Front Door

---

## Q036: Azure Front Door — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure front door for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared Front Door; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared Front Door and global load balancing in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Front door for global internet-facing multi-region apps.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure front door.

### Follow-up Questions

1. **How do Policy exemptions work during azure front door migration?**
2. **What FinOps tag strategy supports azure front door chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Front Door testing
- Policies only at resource group — not MG

---

## Q037: Application Gateway — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Application Gateway using App Gateway in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use App Gateway with WAF; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Regional app gateway for internal and regional l7 load balancing.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Application Gateway is core to Azure Solution Architect interviews covering App Gateway, WAF, SSL termination, path-based routing.

**Architect approach:**
1. Map business requirement to App Gateway — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Regional app gateway for internal and regional l7 load balancing.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect regional App Gateway for internal and regional L7 load balancing — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to App Gateway?**
2. **What KPI proves application gateway adoption succeeded?**

### Common Mistakes in Interviews

- Listing App Gateway without explaining trade-offs
- No Policy or IaC enforcement for application gateway
- Skipping operational runbook for App Gateway

---

## Q038: Application Gateway — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production application gateway for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared App Gateway; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared App Gateway and WAF in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Regional app gateway for internal and regional l7 load balancing.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize application gateway.

### Follow-up Questions

1. **How do Policy exemptions work during application gateway migration?**
2. **What FinOps tag strategy supports application gateway chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for App Gateway testing
- Policies only at resource group — not MG

---

## Q039: NSG and ASG Design — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply NSG and ASG Design using NSG in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use NSG with ASG; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Three-tier nsg design with application security groups.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** NSG and ASG Design is core to Azure Solution Architect interviews covering NSG, ASG, micro-segmentation, service tags.

**Architect approach:**
1. Map business requirement to NSG — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Three-tier nsg design with application security groups.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect three-tier NSG design with application security groups — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to NSG?**
2. **What KPI proves nsg and asg design adoption succeeded?**

### Common Mistakes in Interviews

- Listing NSG without explaining trade-offs
- No Policy or IaC enforcement for nsg and asg design
- Skipping operational runbook for NSG

---

## Q040: NSG and ASG Design — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production nsg and asg design for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared NSG; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared NSG and ASG in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Three-tier nsg design with application security groups.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize nsg and asg design.

### Follow-up Questions

1. **How do Policy exemptions work during nsg and asg design migration?**
2. **What FinOps tag strategy supports nsg and asg design chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for NSG testing
- Policies only at resource group — not MG

---

## Q041: ExpressRoute vs VPN — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply ExpressRoute vs VPN using ExpressRoute in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use ExpressRoute with VPN Gateway; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Hybrid connectivity choice for production datacenter integration.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** ExpressRoute vs VPN is core to Azure Solution Architect interviews covering ExpressRoute, VPN Gateway, redundant circuits, FastPath.

**Architect approach:**
1. Map business requirement to ExpressRoute — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Hybrid connectivity choice for production datacenter integration.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect hybrid connectivity choice for production datacenter integration — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to ExpressRoute?**
2. **What KPI proves expressroute vs vpn adoption succeeded?**

### Common Mistakes in Interviews

- Listing ExpressRoute without explaining trade-offs
- No Policy or IaC enforcement for expressroute vs vpn
- Skipping operational runbook for ExpressRoute

---

## Q042: ExpressRoute vs VPN — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

**Intermediate:** Design production expressroute vs vpn for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared ExpressRoute; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared ExpressRoute and VPN Gateway in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Hybrid connectivity choice for production datacenter integration.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize expressroute vs vpn.

### Follow-up Questions

1. **How do Policy exemptions work during expressroute vs vpn migration?**
2. **What FinOps tag strategy supports expressroute vs vpn chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for ExpressRoute testing
- Policies only at resource group — not MG

---

## Q043: Private DNS Zones — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DNS |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Private DNS Zones using privatelink zones in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use privatelink zones with split-horizon DNS; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Private dns for private link without hardcoding ips.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Private DNS Zones is core to Azure Solution Architect interviews covering privatelink zones, split-horizon DNS, DNS private resolver.

**Architect approach:**
1. Map business requirement to privatelink zones — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Private dns for private link without hardcoding ips.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect private DNS for Private Link without hardcoding IPs — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to privatelink zones?**
2. **What KPI proves private dns zones adoption succeeded?**

### Common Mistakes in Interviews

- Listing privatelink zones without explaining trade-offs
- No Policy or IaC enforcement for private dns zones
- Skipping operational runbook for privatelink zones

---

## Q044: Private DNS Zones — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DNS |
| **Frequency** | Common |

### Question

**Intermediate:** Design production private dns zones for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared privatelink zones; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared privatelink zones and split-horizon DNS in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Private dns for private link without hardcoding ips.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize private dns zones.

### Follow-up Questions

1. **How do Policy exemptions work during private dns zones migration?**
2. **What FinOps tag strategy supports private dns zones chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for privatelink zones testing
- Policies only at resource group — not MG

---

## Q045: User-Defined Routes — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Routing |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply User-Defined Routes using UDR in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use UDR with route tables; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Force egress through hub firewall with udr.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** User-Defined Routes is core to Azure Solution Architect interviews covering UDR, route tables, virtual appliance, asymmetric routing.

**Architect approach:**
1. Map business requirement to UDR — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Force egress through hub firewall with udr.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect force egress through hub firewall with UDR — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to UDR?**
2. **What KPI proves user-defined routes adoption succeeded?**

### Common Mistakes in Interviews

- Listing UDR without explaining trade-offs
- No Policy or IaC enforcement for user-defined routes
- Skipping operational runbook for UDR

---

## Q046: User-Defined Routes — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Routing |
| **Frequency** | Common |

### Question

**Intermediate:** Design production user-defined routes for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared UDR; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared UDR and route tables in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Force egress through hub firewall with udr.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize user-defined routes.

### Follow-up Questions

1. **How do Policy exemptions work during user-defined routes migration?**
2. **What FinOps tag strategy supports user-defined routes chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for UDR testing
- Policies only at resource group — not MG

---

## Q047: Azure Bastion Access — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure Bastion Access using Bastion in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use Bastion with JIT VM access; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Secure admin access without public vm ips.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Azure Bastion Access is core to Azure Solution Architect interviews covering Bastion, JIT VM access, no public RDP.

**Architect approach:**
1. Map business requirement to Bastion — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Secure admin access without public vm ips.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect secure admin access without public VM IPs — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Bastion?**
2. **What KPI proves azure bastion access adoption succeeded?**

### Common Mistakes in Interviews

- Listing Bastion without explaining trade-offs
- No Policy or IaC enforcement for azure bastion access
- Skipping operational runbook for Bastion

---

## Q048: Azure Bastion Access — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure bastion access for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared Bastion; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared Bastion and JIT VM access in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Secure admin access without public vm ips.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure bastion access.

### Follow-up Questions

1. **How do Policy exemptions work during azure bastion access migration?**
2. **What FinOps tag strategy supports azure bastion access chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Bastion testing
- Policies only at resource group — not MG

---

## Q049: DDoS Protection — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply DDoS Protection using DDoS Network Protection in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use DDoS Network Protection with DDoS IP Protection; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Ddos strategy for revenue-critical public endpoints.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** DDoS Protection is core to Azure Solution Architect interviews covering DDoS Network Protection, DDoS IP Protection, WAF layering.

**Architect approach:**
1. Map business requirement to DDoS Network Protection — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Ddos strategy for revenue-critical public endpoints.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect DDoS strategy for revenue-critical public endpoints — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to DDoS Network Protection?**
2. **What KPI proves ddos protection adoption succeeded?**

### Common Mistakes in Interviews

- Listing DDoS Network Protection without explaining trade-offs
- No Policy or IaC enforcement for ddos protection
- Skipping operational runbook for DDoS Network Protection

---

## Q050: DDoS Protection — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production ddos protection for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared DDoS Network Protection; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared DDoS Network Protection and DDoS IP Protection in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Ddos strategy for revenue-critical public endpoints.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize ddos protection.

### Follow-up Questions

1. **How do Policy exemptions work during ddos protection migration?**
2. **What FinOps tag strategy supports ddos protection chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for DDoS Network Protection testing
- Policies only at resource group — not MG

---

## Q051: Virtual WAN — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Virtual WAN using VWAN in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use VWAN with hub routing; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Vwan vs manual hub-spoke at scale.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Virtual WAN is core to Azure Solution Architect interviews covering VWAN, hub routing, branch connectivity, simplified peering.

**Architect approach:**
1. Map business requirement to VWAN — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Vwan vs manual hub-spoke at scale.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect VWAN vs manual hub-spoke at scale — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to VWAN?**
2. **What KPI proves virtual wan adoption succeeded?**

### Common Mistakes in Interviews

- Listing VWAN without explaining trade-offs
- No Policy or IaC enforcement for virtual wan
- Skipping operational runbook for VWAN

---

## Q052: Virtual WAN — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production virtual wan for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared VWAN; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared VWAN and hub routing in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Vwan vs manual hub-spoke at scale.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize virtual wan.

### Follow-up Questions

1. **How do Policy exemptions work during virtual wan migration?**
2. **What FinOps tag strategy supports virtual wan chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for VWAN testing
- Policies only at resource group — not MG

---

## Q053: Network Watcher — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Network Watcher using Connection Monitor in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use Connection Monitor with flow logs; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Network watcher for troubleshooting and validation.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Network Watcher is core to Azure Solution Architect interviews covering Connection Monitor, flow logs, packet capture, effective routes.

**Architect approach:**
1. Map business requirement to Connection Monitor — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Network watcher for troubleshooting and validation.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect Network Watcher for troubleshooting and validation — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Connection Monitor?**
2. **What KPI proves network watcher adoption succeeded?**

### Common Mistakes in Interviews

- Listing Connection Monitor without explaining trade-offs
- No Policy or IaC enforcement for network watcher
- Skipping operational runbook for Connection Monitor

---

## Q054: Network Watcher — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Intermediate:** Design production network watcher for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared Connection Monitor; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared Connection Monitor and flow logs in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Network watcher for troubleshooting and validation.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize network watcher.

### Follow-up Questions

1. **How do Policy exemptions work during network watcher migration?**
2. **What FinOps tag strategy supports network watcher chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Connection Monitor testing
- Policies only at resource group — not MG

---

## Q055: Firewall Application Rules — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Firewall Application Rules using Azure Firewall in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use Azure Firewall with FQDN filtering; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Centralized egress filtering with azure firewall.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Firewall Application Rules is core to Azure Solution Architect interviews covering Azure Firewall, FQDN filtering, IDPS, TLS inspection.

**Architect approach:**
1. Map business requirement to Azure Firewall — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Centralized egress filtering with azure firewall.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect centralized egress filtering with Azure Firewall — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Azure Firewall?**
2. **What KPI proves firewall application rules adoption succeeded?**

### Common Mistakes in Interviews

- Listing Azure Firewall without explaining trade-offs
- No Policy or IaC enforcement for firewall application rules
- Skipping operational runbook for Azure Firewall

---

## Q056: Firewall Application Rules — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production firewall application rules for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared Azure Firewall; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared Azure Firewall and FQDN filtering in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Centralized egress filtering with azure firewall.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize firewall application rules.

### Follow-up Questions

1. **How do Policy exemptions work during firewall application rules migration?**
2. **What FinOps tag strategy supports firewall application rules chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Azure Firewall testing
- Policies only at resource group — not MG

---

## Q057: Peering and Transfer Costs — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Peering and Transfer Costs using VNet peering charges in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use VNet peering charges with egress; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Network cost modeling in architecture reviews.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Peering and Transfer Costs is core to Azure Solution Architect interviews covering VNet peering charges, egress, data transfer optimization.

**Architect approach:**
1. Map business requirement to VNet peering charges — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Network cost modeling in architecture reviews.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect network cost modeling in architecture reviews — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to VNet peering charges?**
2. **What KPI proves peering and transfer costs adoption succeeded?**

### Common Mistakes in Interviews

- Listing VNet peering charges without explaining trade-offs
- No Policy or IaC enforcement for peering and transfer costs
- Skipping operational runbook for VNet peering charges

---

## Q058: Peering and Transfer Costs — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

**Intermediate:** Design production peering and transfer costs for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared VNet peering charges; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared VNet peering charges and egress in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Network cost modeling in architecture reviews.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize peering and transfer costs.

### Follow-up Questions

1. **How do Policy exemptions work during peering and transfer costs migration?**
2. **What FinOps tag strategy supports peering and transfer costs chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for VNet peering charges testing
- Policies only at resource group — not MG

---

## Q059: Load Balancer vs AGW — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Load Balancer vs AGW using Standard LB in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use Standard LB with internal LB; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. L4 vs l7 load balancing selection on azure.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Load Balancer vs AGW is core to Azure Solution Architect interviews covering Standard LB, internal LB, App Gateway, traffic path.

**Architect approach:**
1. Map business requirement to Standard LB — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
L4 vs l7 load balancing selection on azure.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect L4 vs L7 load balancing selection on Azure — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Standard LB?**
2. **What KPI proves load balancer vs agw adoption succeeded?**

### Common Mistakes in Interviews

- Listing Standard LB without explaining trade-offs
- No Policy or IaC enforcement for load balancer vs agw
- Skipping operational runbook for Standard LB

---

## Q060: Load Balancer vs AGW — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production load balancer vs agw for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared Standard LB; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared Standard LB and internal LB in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
L4 vs l7 load balancing selection on azure.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize load balancer vs agw.

### Follow-up Questions

1. **How do Policy exemptions work during load balancer vs agw migration?**
2. **What FinOps tag strategy supports load balancer vs agw chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Standard LB testing
- Policies only at resource group — not MG

---

## Q061: Multi-Region Networking — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Multi-Region Networking using Front Door origin groups in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use Front Door origin groups with global VNet peering; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Network design for multi-region active-active.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Multi-Region Networking is core to Azure Solution Architect interviews covering Front Door origin groups, global VNet peering, latency.

**Architect approach:**
1. Map business requirement to Front Door origin groups — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Network design for multi-region active-active.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect network design for multi-region active-active — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Front Door origin groups?**
2. **What KPI proves multi-region networking adoption succeeded?**

### Common Mistakes in Interviews

- Listing Front Door origin groups without explaining trade-offs
- No Policy or IaC enforcement for multi-region networking
- Skipping operational runbook for Front Door origin groups

---

## Q062: Multi-Region Networking — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

**Intermediate:** Design production multi-region networking for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared Front Door origin groups; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared Front Door origin groups and global VNet peering in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Network design for multi-region active-active.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize multi-region networking.

### Follow-up Questions

1. **How do Policy exemptions work during multi-region networking migration?**
2. **What FinOps tag strategy supports multi-region networking chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Front Door origin groups testing
- Policies only at resource group — not MG

---

## Q063: Service Endpoints Legacy — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Service Endpoints Legacy using service endpoints vs Private Link migration path in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use service endpoints vs Private Link migration path with service endpoints vs Private Link migration path; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Migrate from service endpoints to private link.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Service Endpoints Legacy is core to Azure Solution Architect interviews covering service endpoints vs Private Link migration path.

**Architect approach:**
1. Map business requirement to service endpoints vs Private Link migration path — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Migrate from service endpoints to private link.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect migrate from service endpoints to Private Link — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to service endpoints vs Private Link migration path?**
2. **What KPI proves service endpoints legacy adoption succeeded?**

### Common Mistakes in Interviews

- Listing service endpoints vs Private Link migration path without explaining trade-offs
- No Policy or IaC enforcement for service endpoints legacy
- Skipping operational runbook for service endpoints vs Private Link migration path

---

## Q064: Service Endpoints Legacy — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production service endpoints legacy for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared service endpoints vs Private Link migration path; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared service endpoints vs Private Link migration path and service endpoints vs Private Link migration path in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Migrate from service endpoints to private link.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize service endpoints legacy.

### Follow-up Questions

1. **How do Policy exemptions work during service endpoints legacy migration?**
2. **What FinOps tag strategy supports service endpoints legacy chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for service endpoints vs Private Link migration path testing
- Policies only at resource group — not MG

---

## Q065: IP Address Planning — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply IP Address Planning using CIDR planning in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use CIDR planning with subnet sizing; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Ip address plan for hub-spoke with growth headroom.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** IP Address Planning is core to Azure Solution Architect interviews covering CIDR planning, subnet sizing, reserved ranges, overlap avoidance.

**Architect approach:**
1. Map business requirement to CIDR planning — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Ip address plan for hub-spoke with growth headroom.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect IP address plan for hub-spoke with growth headroom — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to CIDR planning?**
2. **What KPI proves ip address planning adoption succeeded?**

### Common Mistakes in Interviews

- Listing CIDR planning without explaining trade-offs
- No Policy or IaC enforcement for ip address planning
- Skipping operational runbook for CIDR planning

---

## Q066: IP Address Planning — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production ip address planning for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared CIDR planning; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared CIDR planning and subnet sizing in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Ip address plan for hub-spoke with growth headroom.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize ip address planning.

### Follow-up Questions

1. **How do Policy exemptions work during ip address planning migration?**
2. **What FinOps tag strategy supports ip address planning chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for CIDR planning testing
- Policies only at resource group — not MG

---

## Q067: NVA vs Azure Firewall — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply NVA vs Azure Firewall using third-party NVA in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use third-party NVA with Azure Firewall; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Choose between nva and azure firewall for hub.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** NVA vs Azure Firewall is core to Azure Solution Architect interviews covering third-party NVA, Azure Firewall, cost and ops trade-off.

**Architect approach:**
1. Map business requirement to third-party NVA — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Choose between nva and azure firewall for hub.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect choose between NVA and Azure Firewall for hub — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to third-party NVA?**
2. **What KPI proves nva vs azure firewall adoption succeeded?**

### Common Mistakes in Interviews

- Listing third-party NVA without explaining trade-offs
- No Policy or IaC enforcement for nva vs azure firewall
- Skipping operational runbook for third-party NVA

---

## Q068: NVA vs Azure Firewall — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production nva vs azure firewall for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared third-party NVA; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared third-party NVA and Azure Firewall in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Choose between nva and azure firewall for hub.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize nva vs azure firewall.

### Follow-up Questions

1. **How do Policy exemptions work during nva vs azure firewall migration?**
2. **What FinOps tag strategy supports nva vs azure firewall chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for third-party NVA testing
- Policies only at resource group — not MG

---

## Q069: Hub-Spoke Case Study — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scenario |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Hub-Spoke Case Study using 20 apps in a Azure Networking architecture review?

### Short Answer (30 seconds)

Use 20 apps with 5 spokes; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Apply hub-spoke case study patterns from week 13 lab.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Context:** Hub-Spoke Case Study is core to Azure Solution Architect interviews covering 20 apps, 5 spokes, VPN, Private Link.

**Architect approach:**
1. Map business requirement to 20 apps — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Apply hub-spoke case study patterns from week 13 lab.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect apply hub-spoke case study patterns from week 13 lab — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to 20 apps?**
2. **What KPI proves hub-spoke case study adoption succeeded?**

### Common Mistakes in Interviews

- Listing 20 apps without explaining trade-offs
- No Policy or IaC enforcement for hub-spoke case study
- Skipping operational runbook for 20 apps

---

## Q070: Hub-Spoke Case Study — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scenario |
| **Frequency** | Common |

### Question

**Intermediate:** Design production hub-spoke case study for a 10-subscription enterprise (Azure Networking).

### Short Answer (30 seconds)

Platform hosts shared 20 apps; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 13:** Azure Networking

**Design:** Multi-subscription estate with platform vs application separation.
Shared 20 apps and 5 spokes in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Apply hub-spoke case study patterns from week 13 lab.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize hub-spoke case study.

### Follow-up Questions

1. **How do Policy exemptions work during hub-spoke case study migration?**
2. **What FinOps tag strategy supports hub-spoke case study chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for 20 apps testing
- Policies only at resource group — not MG

---
