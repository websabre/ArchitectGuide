# Week 13 — Azure Networking Diagrams

## 1. Hub-Spoke Topology

```mermaid
flowchart TB
    subgraph Hub["Hub VNet"]
        FW[Azure Firewall]
        VPN[VPN Gateway]
        DNS[Private DNS Zone]
    end
    subgraph SpokeApp["Spoke: Application"]
        App[App Service VNet Integration]
    end
    subgraph SpokeData["Spoke: Data"]
        SQL[(Private Endpoint SQL)]
    end
    Hub --> SpokeApp
    Hub --> SpokeData
    OnPrem[On-Prem] --> VPN
```

## 2. Private Link Data Path

```mermaid
flowchart LR
    App[App in VNet] --> PE[Private Endpoint]
    PE --> PLS[Private Link Service]
    PLS --> SQL[(Azure SQL)]
    Note[Traffic stays on Microsoft backbone]
```

## 3. NSG Flow — Allow/Deny

```mermaid
flowchart TD
    Req[Inbound 443] --> NSG[NSG Rules]
    NSG -->|Allow AppSubnet| App[App Tier]
    NSG -->|Deny*| Block[Blocked]
```

## 4. Application Gateway + WAF

```mermaid
flowchart LR
    User --> FD[Front Door optional]
    FD --> AGW[App Gateway WAF]
    AGW --> App[Internal App Service]
```

## 5. DNS Private Resolution

```mermaid
flowchart LR
    VM[VM in Spoke] --> DNS[Azure Private DNS]
    DNS --> Name[sql.database.windows.net resolves to private IP]
```

> **Architect note:** Hub owns centralized egress via Firewall — avoid spoke-to-internet bypass.

## Practice Exercise

Compare hub-spoke vs virtual WAN for 15 spokes across 3 regions.

---

[← Back to Week 13](../README.md)
