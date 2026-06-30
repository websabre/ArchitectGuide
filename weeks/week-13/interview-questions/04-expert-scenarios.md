# Week 13 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Hub-Spoke Topology — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in hub-spoke topology. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via hub VNet → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Hub-Spoke Topology gap; Resource Graph inventory of hub VNet, spokes, peering, Azure Firewall.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on hub VNet.
Hub-spoke as default enterprise azure network topology. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for hub-spoke topology?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q102: Private Link Design — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in private link design. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via private endpoints → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Private Link Design gap; Resource Graph inventory of private endpoints, private DNS zones, DNS resolution.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on private endpoints.
Private link for all production paas data plane access. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for private link design?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q103: Azure Front Door — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in azure front door. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Front Door → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Azure Front Door gap; Resource Graph inventory of Front Door, global load balancing, WAF, caching.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Front Door.
Front door for global internet-facing multi-region apps. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for azure front door?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q104: Application Gateway — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in application gateway. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via App Gateway → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Application Gateway gap; Resource Graph inventory of App Gateway, WAF, SSL termination, path-based routing.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on App Gateway.
Regional app gateway for internal and regional l7 load balancing. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for application gateway?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q105: NSG and ASG Design — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in nsg and asg design. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via NSG → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to NSG and ASG Design gap; Resource Graph inventory of NSG, ASG, micro-segmentation, service tags.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on NSG.
Three-tier nsg design with application security groups. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for nsg and asg design?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q106: ExpressRoute vs VPN — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in expressroute vs vpn. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via ExpressRoute → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to ExpressRoute vs VPN gap; Resource Graph inventory of ExpressRoute, VPN Gateway, redundant circuits, FastPath.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on ExpressRoute.
Hybrid connectivity choice for production datacenter integration. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for expressroute vs vpn?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q107: Private DNS Zones — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in private dns zones. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via privatelink zones → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Private DNS Zones gap; Resource Graph inventory of privatelink zones, split-horizon DNS, DNS private resolver.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on privatelink zones.
Private dns for private link without hardcoding ips. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for private dns zones?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q108: User-Defined Routes — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in user-defined routes. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via UDR → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to User-Defined Routes gap; Resource Graph inventory of UDR, route tables, virtual appliance, asymmetric routing.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on UDR.
Force egress through hub firewall with udr. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for user-defined routes?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q109: Azure Bastion Access — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in azure bastion access. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Bastion → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Azure Bastion Access gap; Resource Graph inventory of Bastion, JIT VM access, no public RDP.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Bastion.
Secure admin access without public vm ips. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for azure bastion access?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q110: DDoS Protection — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in ddos protection. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via DDoS Network Protection → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to DDoS Protection gap; Resource Graph inventory of DDoS Network Protection, DDoS IP Protection, WAF layering.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on DDoS Network Protection.
Ddos strategy for revenue-critical public endpoints. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for ddos protection?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q111: Virtual WAN — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in virtual wan. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via VWAN → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Virtual WAN gap; Resource Graph inventory of VWAN, hub routing, branch connectivity, simplified peering.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on VWAN.
Vwan vs manual hub-spoke at scale. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for virtual wan?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q112: Network Watcher — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in network watcher. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Connection Monitor → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Network Watcher gap; Resource Graph inventory of Connection Monitor, flow logs, packet capture, effective routes.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Connection Monitor.
Network watcher for troubleshooting and validation. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for network watcher?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q113: Firewall Application Rules — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in firewall application rules. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Azure Firewall → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Firewall Application Rules gap; Resource Graph inventory of Azure Firewall, FQDN filtering, IDPS, TLS inspection.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Azure Firewall.
Centralized egress filtering with azure firewall. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for firewall application rules?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q114: Peering and Transfer Costs — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in peering and transfer costs. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via VNet peering charges → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Peering and Transfer Costs gap; Resource Graph inventory of VNet peering charges, egress, data transfer optimization.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on VNet peering charges.
Network cost modeling in architecture reviews. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for peering and transfer costs?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q115: Load Balancer vs AGW — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in load balancer vs agw. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Standard LB → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Load Balancer vs AGW gap; Resource Graph inventory of Standard LB, internal LB, App Gateway, traffic path.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Standard LB.
L4 vs l7 load balancing selection on azure. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for load balancer vs agw?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q116: Multi-Region Networking — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in multi-region networking. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Front Door origin groups → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Multi-Region Networking gap; Resource Graph inventory of Front Door origin groups, global VNet peering, latency.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Front Door origin groups.
Network design for multi-region active-active. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for multi-region networking?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q117: Service Endpoints Legacy — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in service endpoints legacy. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via service endpoints vs Private Link migration path → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Service Endpoints Legacy gap; Resource Graph inventory of service endpoints vs Private Link migration path.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on service endpoints vs Private Link migration path.
Migrate from service endpoints to private link. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for service endpoints legacy?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q118: IP Address Planning — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in ip address planning. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via CIDR planning → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to IP Address Planning gap; Resource Graph inventory of CIDR planning, subnet sizing, reserved ranges, overlap avoidance.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on CIDR planning.
Ip address plan for hub-spoke with growth headroom. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for ip address planning?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q119: NVA vs Azure Firewall — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in nva vs azure firewall. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via third-party NVA → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to NVA vs Azure Firewall gap; Resource Graph inventory of third-party NVA, Azure Firewall, cost and ops trade-off.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on third-party NVA.
Choose between nva and azure firewall for hub. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for nva vs azure firewall?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q120: Hub-Spoke Case Study — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in hub-spoke case study. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via 20 apps → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 13:** Azure Networking

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Hub-Spoke Case Study gap; Resource Graph inventory of 20 apps, 5 spokes, VPN, Private Link.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on 20 apps.
Apply hub-spoke case study patterns from week 13 lab. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for hub-spoke case study?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---
