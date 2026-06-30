# Week 13 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Hub-Spoke Topology — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling hub-spoke topology across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for hub VNet.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Hub-Spoke Topology must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full hub-spoke topology immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** hub VNet, spokes, peering, Azure Firewall. Mitigation: Policy exemptions with expiry; game day validation.
Hub-spoke as default enterprise azure network topology.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating hub-spoke topology for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q072: Hub-Spoke Topology — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling hub-spoke topology across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for hub VNet.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Hub-Spoke Topology must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full hub-spoke topology immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** hub VNet, spokes, peering, Azure Firewall. Mitigation: Policy exemptions with expiry; game day validation.
Hub-spoke as default enterprise azure network topology.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating hub-spoke topology for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q073: Private Link Design — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling private link design across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for private endpoints.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Private Link Design must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full private link design immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** private endpoints, private DNS zones, DNS resolution. Mitigation: Policy exemptions with expiry; game day validation.
Private link for all production paas data plane access.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating private link design for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q074: Private Link Design — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to private link design without downtime?

### Short Answer (30 seconds)

Tier workloads, phase private link design rollout, time-bound exemptions, golden-path IaC using private endpoints.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to private link design without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full private link design on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** private endpoints, private DNS zones, DNS resolution. Anchor: **private endpoints** + **private DNS zones**.
Private link for all production paas data plane access.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same private link design strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q075: Azure Front Door — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to azure front door without downtime?

### Short Answer (30 seconds)

Tier workloads, phase azure front door rollout, time-bound exemptions, golden-path IaC using Front Door.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to azure front door without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full azure front door on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Front Door, global load balancing, WAF. Anchor: **Front Door** + **global load balancing**.
Front door for global internet-facing multi-region apps.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same azure front door strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q076: Azure Front Door — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling azure front door across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Front Door.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure Front Door must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure front door immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Front Door, global load balancing, WAF, caching. Mitigation: Policy exemptions with expiry; game day validation.
Front door for global internet-facing multi-region apps.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure front door for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q077: Application Gateway — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling application gateway across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for App Gateway.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Application Gateway must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full application gateway immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** App Gateway, WAF, SSL termination, path-based routing. Mitigation: Policy exemptions with expiry; game day validation.
Regional app gateway for internal and regional l7 load balancing.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating application gateway for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q078: Application Gateway — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling application gateway across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for App Gateway.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Application Gateway must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full application gateway immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** App Gateway, WAF, SSL termination, path-based routing. Mitigation: Policy exemptions with expiry; game day validation.
Regional app gateway for internal and regional l7 load balancing.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating application gateway for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q079: NSG and ASG Design — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling nsg and asg design across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for NSG.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
NSG and ASG Design must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full nsg and asg design immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** NSG, ASG, micro-segmentation, service tags. Mitigation: Policy exemptions with expiry; game day validation.
Three-tier nsg design with application security groups.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating nsg and asg design for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q080: NSG and ASG Design — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to nsg and asg design without downtime?

### Short Answer (30 seconds)

Tier workloads, phase nsg and asg design rollout, time-bound exemptions, golden-path IaC using NSG.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to nsg and asg design without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full nsg and asg design on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** NSG, ASG, micro-segmentation. Anchor: **NSG** + **ASG**.
Three-tier nsg design with application security groups.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same nsg and asg design strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q081: ExpressRoute vs VPN — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to expressroute vs vpn without downtime?

### Short Answer (30 seconds)

Tier workloads, phase expressroute vs vpn rollout, time-bound exemptions, golden-path IaC using ExpressRoute.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to expressroute vs vpn without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full expressroute vs vpn on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** ExpressRoute, VPN Gateway, redundant circuits. Anchor: **ExpressRoute** + **VPN Gateway**.
Hybrid connectivity choice for production datacenter integration.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same expressroute vs vpn strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q082: ExpressRoute vs VPN — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling expressroute vs vpn across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for ExpressRoute.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
ExpressRoute vs VPN must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full expressroute vs vpn immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** ExpressRoute, VPN Gateway, redundant circuits, FastPath. Mitigation: Policy exemptions with expiry; game day validation.
Hybrid connectivity choice for production datacenter integration.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating expressroute vs vpn for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q083: Private DNS Zones — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DNS |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling private dns zones across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for privatelink zones.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Private DNS Zones must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full private dns zones immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** privatelink zones, split-horizon DNS, DNS private resolver. Mitigation: Policy exemptions with expiry; game day validation.
Private dns for private link without hardcoding ips.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating private dns zones for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q084: Private DNS Zones — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DNS |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling private dns zones across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for privatelink zones.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Private DNS Zones must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full private dns zones immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** privatelink zones, split-horizon DNS, DNS private resolver. Mitigation: Policy exemptions with expiry; game day validation.
Private dns for private link without hardcoding ips.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating private dns zones for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q085: User-Defined Routes — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Routing |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling user-defined routes across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for UDR.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
User-Defined Routes must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full user-defined routes immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** UDR, route tables, virtual appliance, asymmetric routing. Mitigation: Policy exemptions with expiry; game day validation.
Force egress through hub firewall with udr.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating user-defined routes for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q086: User-Defined Routes — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Routing |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to user-defined routes without downtime?

### Short Answer (30 seconds)

Tier workloads, phase user-defined routes rollout, time-bound exemptions, golden-path IaC using UDR.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to user-defined routes without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full user-defined routes on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** UDR, route tables, virtual appliance. Anchor: **UDR** + **route tables**.
Force egress through hub firewall with udr.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same user-defined routes strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q087: Azure Bastion Access — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to azure bastion access without downtime?

### Short Answer (30 seconds)

Tier workloads, phase azure bastion access rollout, time-bound exemptions, golden-path IaC using Bastion.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to azure bastion access without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full azure bastion access on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Bastion, JIT VM access, no public RDP. Anchor: **Bastion** + **JIT VM access**.
Secure admin access without public vm ips.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same azure bastion access strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q088: Azure Bastion Access — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling azure bastion access across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Bastion.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure Bastion Access must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure bastion access immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Bastion, JIT VM access, no public RDP. Mitigation: Policy exemptions with expiry; game day validation.
Secure admin access without public vm ips.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure bastion access for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q089: DDoS Protection — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling ddos protection across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for DDoS Network Protection.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
DDoS Protection must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full ddos protection immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** DDoS Network Protection, DDoS IP Protection, WAF layering. Mitigation: Policy exemptions with expiry; game day validation.
Ddos strategy for revenue-critical public endpoints.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating ddos protection for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q090: DDoS Protection — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling ddos protection across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for DDoS Network Protection.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
DDoS Protection must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full ddos protection immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** DDoS Network Protection, DDoS IP Protection, WAF layering. Mitigation: Policy exemptions with expiry; game day validation.
Ddos strategy for revenue-critical public endpoints.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating ddos protection for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q091: Virtual WAN — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling virtual wan across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for VWAN.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Virtual WAN must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full virtual wan immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** VWAN, hub routing, branch connectivity, simplified peering. Mitigation: Policy exemptions with expiry; game day validation.
Vwan vs manual hub-spoke at scale.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating virtual wan for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q092: Network Watcher — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to network watcher without downtime?

### Short Answer (30 seconds)

Tier workloads, phase network watcher rollout, time-bound exemptions, golden-path IaC using Connection Monitor.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to network watcher without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full network watcher on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Connection Monitor, flow logs, packet capture. Anchor: **Connection Monitor** + **flow logs**.
Network watcher for troubleshooting and validation.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same network watcher strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q093: Firewall Application Rules — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling firewall application rules across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Azure Firewall.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Firewall Application Rules must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full firewall application rules immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Azure Firewall, FQDN filtering, IDPS, TLS inspection. Mitigation: Policy exemptions with expiry; game day validation.
Centralized egress filtering with azure firewall.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating firewall application rules for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q094: Peering and Transfer Costs — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling peering and transfer costs across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for VNet peering charges.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Peering and Transfer Costs must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full peering and transfer costs immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** VNet peering charges, egress, data transfer optimization. Mitigation: Policy exemptions with expiry; game day validation.
Network cost modeling in architecture reviews.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating peering and transfer costs for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q095: Load Balancer vs AGW — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to load balancer vs agw without downtime?

### Short Answer (30 seconds)

Tier workloads, phase load balancer vs agw rollout, time-bound exemptions, golden-path IaC using Standard LB.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to load balancer vs agw without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full load balancer vs agw on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Standard LB, internal LB, App Gateway. Anchor: **Standard LB** + **internal LB**.
L4 vs l7 load balancing selection on azure.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same load balancer vs agw strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q096: Multi-Region Networking — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling multi-region networking across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Front Door origin groups.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Multi-Region Networking must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full multi-region networking immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Front Door origin groups, global VNet peering, latency. Mitigation: Policy exemptions with expiry; game day validation.
Network design for multi-region active-active.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating multi-region networking for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q097: Service Endpoints Legacy — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling service endpoints legacy across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for service endpoints vs Private Link migration path.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Service Endpoints Legacy must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full service endpoints legacy immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** service endpoints vs Private Link migration path. Mitigation: Policy exemptions with expiry; game day validation.
Migrate from service endpoints to private link.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating service endpoints legacy for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q098: IP Address Planning — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to ip address planning without downtime?

### Short Answer (30 seconds)

Tier workloads, phase ip address planning rollout, time-bound exemptions, golden-path IaC using CIDR planning.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Scenario:** Migrating brownfield workloads to ip address planning without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full ip address planning on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** CIDR planning, subnet sizing, reserved ranges. Anchor: **CIDR planning** + **subnet sizing**.
Ip address plan for hub-spoke with growth headroom.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same ip address planning strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q099: NVA vs Azure Firewall — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling nva vs azure firewall across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for third-party NVA.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
NVA vs Azure Firewall must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full nva vs azure firewall immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** third-party NVA, Azure Firewall, cost and ops trade-off. Mitigation: Policy exemptions with expiry; game day validation.
Choose between nva and azure firewall for hub.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating nva vs azure firewall for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q100: Hub-Spoke Case Study — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scenario |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling hub-spoke case study across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for 20 apps.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 13:** Azure Networking

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Hub-Spoke Case Study must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full hub-spoke case study immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** 20 apps, 5 spokes, VPN, Private Link. Mitigation: Policy exemptions with expiry; game day validation.
Apply hub-spoke case study patterns from week 13 lab.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating hub-spoke case study for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---
