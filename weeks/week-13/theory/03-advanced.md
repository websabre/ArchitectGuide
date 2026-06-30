# Azure Networking — Advanced

> **Week 13** | **Level:** Advanced

## Application Gateway vs Front Door

| Factor | App Gateway | Front Door |
|--------|-------------|------------|
| Layer | Regional L7 | Global L7 |
| WAF | Regional WAF | Global WAF |
| Use | Single region | Multi-region, global users |

## DNS Strategy

- Azure DNS private zones linked to VNets
- Split-horizon DNS for hybrid
- TTL planning for failover (lower TTL = faster failover, more queries)

## Capstone Tie-In

Design hub-spoke for 3 teams with shared firewall and private SQL access.

**Cross-cutting:** [Networking fundamentals](../../../docs/cross-cutting/networking-fundamentals/README.md)

## Architect Deep Dive: Multi-Region Networking

### Active-passive DNS
Front Door priority routing: primary region priority 1, secondary priority 2. Health probes on `/health` every 30s — automatic failover when primary unhealthy.

### Cross-region data
Networking failover ≠ data failover — align RPO with SQL geo-replication or Cosmos multi-region config before claiming DR readiness.

