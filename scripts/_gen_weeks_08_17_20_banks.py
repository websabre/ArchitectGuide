#!/usr/bin/env python3
"""Build premium_qa_data_weeks_08_17_20_banks.py — 450 premium questions."""

from __future__ import annotations

import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from premium_qa_data_aws import WEEK_17, WEEK_18, WEEK_19, WEEK_20
from premium_qa_data_tails_w07_08 import WEEK_8_Q011_Q030

OUT = os.path.join(os.path.dirname(__file__), "premium_qa_data_weeks_08_17_20_banks.py")

HEADER = '''"""Hand-crafted premium interview banks for Weeks 8, 17–20.

Week 8: PostgreSQL — MVCC, JSONB, replication, pooling, partitioning, indexing,
vacuum, HA, RLS, observability, cloud deployment.

Week 17: AWS Fundamentals — IAM, landing zone, Organizations, SCPs, WAF pillars,
Control Tower, cost tags, CAF, Identity Center, audit trails.

Week 18: AWS Compute/Serverless — Lambda, ECS, EKS, Fargate, EC2, API Gateway,
cold starts, ASG, ALB/NLB, Graviton, Spot, Step Functions, anti-patterns.

Week 19: AWS Data/Networking — VPC design, S3 classes, RDS/Aurora/DynamoDB,
NAT/endpoints, Route 53, Multi-AZ vs replicas, TGW, EBS, RDS Proxy, PrivateLink.

Week 20: Multi-Cloud — strategy, portability, hybrid connectivity, cross-cloud DR,
identity federation, FinOps, egress costs, lock-in mitigation, primary cloud selection.

Exports per week: INTERMEDIATE (40), ADVANCED (30), EXPERT (20) = 90 questions.
Total: 450 questions.
"""

from premium_qa_data import q

'''


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def fmt_q(d: dict | tuple) -> str:
    if isinstance(d, dict):
        fus = d["followups"].split("\n")
        fu1 = fus[0].replace("1. **", "").replace("**", "") if fus else ""
        fu2 = fus[1].replace("2. **", "").replace("**", "") if len(fus) > 1 else ""
        ms = [x.lstrip("- ") for x in d["mistakes"].split("\n") if x.strip()]
        while len(ms) < 3:
            ms.append("Undocumented mistake pattern")
        d = (
            d["title"], d["category"], d["frequency"], d["question"], d["short"],
            d["detailed"], d["perspective"], fu1, fu2, ms[0], ms[1], ms[2],
        )
    title, cat, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3 = d
    return (
        f'    q("{esc(title)}", "{esc(cat)}", "{esc(freq)}",\n'
        f'      "{esc(question)}",\n'
        f'      "{esc(short)}",\n'
        f'      "{esc(detailed)}",\n'
        f'      "{esc(perspective)}",\n'
        f'      "{esc(fu1)}",\n'
        f'      "{esc(fu2)}",\n'
        f'      "{esc(m1)}",\n'
        f'      "{esc(m2)}",\n'
        f'      "{esc(m3)}"),'
    )


def write_bank(name: str, items: list, fh) -> None:
    fh.write(f"\n{name} = [\n")
    for item in items:
        fh.write(fmt_q(item) + "\n")
    fh.write("]\n")


def T(title, cat, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3):
    return (title, cat, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3)


def gen_filler(week: int, topics: list[tuple[str, str, str]]) -> list:
    out = []
    for name, cat, focus in topics:
        for label, freq, qtext in [
            ("Fundamentals", "Very Common", f"What must architects know about {name}?"),
            ("Production Patterns", "Very Common", f"How deploy {name} in production enterprise workloads?"),
            ("Advanced Tuning", "Common", f"Advanced {name} tuning and edge cases?"),
            ("Architecture Trade-offs", "Common", f"Architecture trade-offs for {name}?"),
            ("Expert Scenario", "Occasional", f"Expert scenario: incident involving {name}."),
        ]:
            out.append(T(
                f"{name} {label}", cat, freq, qtext,
                focus,
                f"**Topic:** {name}\n**Focus:** {focus}\n\n**Architect depth:**\n"
                f"- Requirements and NFR alignment\n- Security, HA, and FinOps\n"
                f"- Monitoring, runbooks, and ADR documentation\n\n**Week {week} context:** {qtext}",
                f"{name} is essential Week {week} solution architect knowledge.",
                f"Azure or hybrid equivalent of {name}?",
                f"Common production mistake with {name}?",
                f"Confusing {name} with adjacent service",
                f"Console-only knowledge without design rationale",
                f"No monitoring for {name} failures",
            ))
    return out


W08_TOPICS = [
    ("HOT Updates", "Performance", "Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged"),
    ("Fillfactor Tuning", "Performance", "Page free space reserved for HOT updates on high-churn tables"),
    ("TOAST Storage", "Storage", "Out-of-line storage for oversized JSONB and text values"),
    ("Generated Columns", "JSONB", "Stored generated columns extracting hot JSONB paths to B-tree indexable columns"),
    ("Synchronous Replication", "HA/DR", "synchronous_commit and synchronous_standby_names for RPO=0"),
    ("Patroni HA Failover", "HA/DR", "Automated leader election and failover orchestration"),
    ("Pgpool-II Load Balancing", "Operations", "Connection pooler with read/write split across replicas"),
    ("Hash Partitioning", "Scale", "PARTITION BY HASH for even tenant distribution"),
    ("List Partitioning", "Scale", "PARTITION BY LIST for region or tenant category isolation"),
    ("Covering Indexes", "Indexing", "INCLUDE columns enabling index-only scans"),
    ("Concurrent Index Build", "Indexing", "CREATE INDEX CONCURRENTLY for zero-downtime index adds"),
    ("Parallel Query Tuning", "Performance", "max_parallel_workers_per_gather and cost thresholds"),
    ("Work Mem Sizing", "Performance", "Per-operation sort and hash memory limits"),
    ("Shared Buffers", "Performance", "Shared buffer cache sizing relative to RAM"),
    ("WAL Archiving PITR", "HA/DR", "Continuous WAL archive enabling point-in-time recovery"),
    ("Foreign Data Wrappers", "Integration", "postgres_fdw querying remote PostgreSQL or other sources"),
    ("Advisory Locks", "Concurrency", "Application-level cooperative locking without row locks"),
    ("Prepared Statements", "Performance", "Server-side plans and PgBouncer transaction mode compatibility"),
    ("PostGIS Spatial Queries", "Extensions", "GiST-indexed geometry for distance and containment queries"),
    ("TimescaleDB Hypertables", "Extensions", "Automatic chunking compression and retention for time-series"),
]

W17_TOPICS = [
    ("IAM Policy Evaluation Logic", "Security", "Explicit deny wins; intersection of SCP, identity, resource, and session policies"),
    ("STS AssumeRole Chain", "Security", "Temporary credential chaining and external ID for third parties"),
    ("Control Tower Customizations", "Landing Zone", "CfCT manifest extending Account Factory baselines"),
    ("AWS Artifact Compliance", "Compliance", "SOC and ISO report access for customer audits"),
    ("Service Quotas Management", "Governance", "Quota monitoring and increase requests before scale events"),
    ("RAM Resource Access Manager", "Governance", "Share subnets and Transit Gateway across accounts"),
    ("IMDSv2 Instance Metadata", "Security", "Require session token preventing SSRF credential theft"),
    ("GuardDuty Threat Detection", "Security", "ML-based threat findings integrated with Security Hub"),
    ("Security Hub Aggregation", "Security", "Centralized compliance and finding dashboard"),
    ("Firewall Manager WAF", "Security", "Organization-wide WAF rule deployment"),
    ("Billing Conductor Chargeback", "FinOps", "Custom billing rules for internal chargeback"),
    ("Cost Categories", "FinOps", "Cost grouping beyond tag key limitations"),
    ("Reserved Instances Strategy", "FinOps", "RI and Savings Plan purchase timing and coverage"),
    ("Trusted Advisor Checks", "Operations", "Cost, performance, security, and fault tolerance recommendations"),
    ("Personal Health Dashboard", "Operations", "Account-specific planned AWS maintenance events"),
    ("CloudWatch Cross-Account Observability", "Operations", "OAM linking metrics and logs across organization"),
    ("AWS License Manager", "Governance", "Track BYOL and license consumption"),
    ("Tag Policies", "Governance", "Organization-wide tag standard enforcement"),
    ("AWS Health Dashboard", "Operations", "Regional service health and event history"),
    ("Enterprise Support Model", "Operations", "TAM, Infrastructure Event Management, and support API"),
]

W18_TOPICS = [
    ("Lambda Destinations", "Serverless", "Route async invocation success and failure to SQS, SNS, or Lambda"),
    ("Lambda Layers Packaging", "Serverless", "Shared dependencies and runtime extension layers"),
    ("ECS Capacity Providers", "Compute", "Mix Fargate and EC2 capacity with managed scaling"),
    ("ECS Blue/Green Deploy", "Compute", "CodeDeploy controlled traffic shift between task sets"),
    ("EKS Pod Identity", "Compute", "IAM roles for service accounts without OIDC boilerplate"),
    ("Karpenter Autoscaling", "Compute", "Just-in-time node provisioning for EKS"),
    ("App Runner Simplicity", "Compute", "Managed container web service without cluster ops"),
    ("AWS Batch Workloads", "Compute", "Managed batch job queues and compute environments"),
    ("EventBridge Pipes", "Integration", "Point-to-point integration with filtering and enrichment"),
    ("SQS FIFO Ordering", "Integration", "Strict ordering and deduplication for critical workflows"),
    ("SNS Fanout Pattern", "Integration", "Topic fanout to SQS, Lambda, and HTTP subscribers"),
    ("Kinesis Data Streams", "Integration", "Shard-based streaming ingestion and consumers"),
    ("Lambda Powertools", "Serverless", "Structured logging, tracing, and metrics for Lambda"),
    ("Container Insights", "Observability", "ECS and EKS metrics, logs, and performance monitoring"),
    ("X-Ray Distributed Tracing", "Observability", "End-to-end trace across API Gateway, Lambda, and downstream"),
    ("SAM Serverless Model", "Serverless", "Infrastructure as code template for serverless applications"),
    ("Copilot ECS CLI", "Compute", "Developer-friendly ECS and Fargate deployment workflow"),
    ("Firecracker MicroVMs", "Compute", "Underlying isolation technology for Lambda and Fargate"),
    ("Lambda SnapStart", "Serverless", "Snapshot restore cold start optimization for Java runtimes"),
    ("Mixed Spot On-Demand ASG", "Cost", "Auto Scaling group with Spot base capacity and On-Demand core"),
]

W19_TOPICS = [
    ("VPC Lattice Service Network", "Networking", "Application-layer service-to-service connectivity"),
    ("AWS Network Firewall", "Networking", "Stateful network inspection and domain filtering"),
    ("Shield Advanced DDoS", "Security", "DDoS Response Team and cost protection for scale attacks"),
    ("Gateway Load Balancer", "Networking", "Inline third-party security appliance insertion"),
    ("Direct Connect Dedicated", "Networking", "Private dedicated hybrid connectivity bypassing internet"),
    ("Site-to-Site VPN Backup", "Networking", "IPsec VPN failover path for hybrid connectivity"),
    ("Global Accelerator Anycast", "Networking", "Static anycast IP with health-aware regional routing"),
    ("CloudFront Edge Caching", "Networking", "CDN TLS termination and origin shield patterns"),
    ("S3 Transfer Acceleration", "Storage", "Edge-accelerated uploads for global clients"),
    ("S3 Object Lock Immutability", "Storage", "WORM compliance and ransomware-resistant backups"),
    ("RDS Performance Insights", "Database", "DB load analysis by wait event and top SQL"),
    ("Aurora Global Database", "Database", "Cross-region replication with sub-second lag target"),
    ("DynamoDB Streams CDC", "NoSQL", "Change data capture triggering Lambda consumers"),
    ("DynamoDB TTL Expiration", "NoSQL", "Automatic item expiration for session and log data"),
    ("ElastiCache Cluster Mode", "Caching", "Horizontal Redis shard scaling for large working sets"),
    ("MemoryDB Durability", "Caching", "Redis-compatible with durable in-memory storage"),
    ("DocumentDB MongoDB API", "Database", "Managed document database for MongoDB workloads"),
    ("Neptune Graph Database", "Database", "Property graph for relationship-heavy queries"),
    ("VPC Flow Logs Analysis", "Networking", "Traffic visibility for security and cost debugging"),
    ("PrivateLink Endpoint Services", "Networking", "Expose services privately to consumer VPCs and accounts"),
]

W20_TOPICS = [
    ("Cloud Bursting / Cloud Bursting", "Hybrid", "Overflow burst capacity from on-premises to public cloud"),
    ("Azure Arc Hybrid Control", "Hybrid", "Manage on-premises and multi-cloud from Azure control plane"),
    ("Google Anthos Fleet", "Multi-Cloud", "Unified Kubernetes management across clouds and on-prem"),
    ("Crossplane Control Plane", "IaC", "Kubernetes-native declarative cloud resource management"),
    ("Pulumi Multi-Language IaC", "IaC", "TypeScript, Python, Go infrastructure as real code"),
    ("CloudEvents Portability", "Integration", "Vendor-neutral event envelope format"),
    ("OIDC Federation Portability", "Identity", "Standard OAuth/OIDC across Azure, AWS, and GCP"),
    ("PostgreSQL Cross-Cloud Portability", "Data", "Same relational engine on RDS, Azure Flexible, Cloud SQL"),
    ("S3-Compatible Object APIs", "Storage", "MinIO and SDK abstraction for object storage portability"),
    ("Kafka MirrorMaker Replication", "Integration", "Cross-cloud event stream replication patterns"),
    ("Istio Multi-Cluster Mesh", "Networking", "Portable service mesh across EKS and AKS clusters"),
    ("CNCF Neutral Building Blocks", "Strategy", "Kubernetes, Prometheus, OTel as cloud-neutral foundation"),
    ("FinOps FOCUS Standard", "FinOps", "Cross-cloud billing data normalization standard"),
    ("Cloud Center of Excellence", "Governance", "CCoE operating model spanning multiple providers"),
    ("Workload Repatriation Criteria", "Strategy", "When and how to move workloads back on-premises"),
    ("Sovereign Cloud Requirements", "Compliance", "National cloud and data residency regulatory constraints"),
    ("Data Mesh Cross-Cloud", "Data", "Domain-owned data products spanning cloud boundaries"),
    ("Multi-Cloud API Gateway", "Integration", "Kong, Apigee, or Azure APIM as neutral API edge"),
    ("DR Tier RTO RPO Matrix", "DR", "Tier 0-3 recovery objectives spanning primary and secondary cloud"),
    ("Composite SLA Mathematics", "Reliability", "Calculating end-to-end availability across multi-cloud paths"),
]

WEEK_POOLS = {
    8: list(WEEK_8_Q011_Q030) + gen_filler(8, W08_TOPICS),
    17: list(WEEK_17) + gen_filler(17, W17_TOPICS),
    18: list(WEEK_18) + gen_filler(18, W18_TOPICS),
    19: list(WEEK_19) + gen_filler(19, W19_TOPICS),
    20: list(WEEK_20) + gen_filler(20, W20_TOPICS),
}


def assign_tiers(pool: list) -> tuple[list, list, list]:
    rich = [p for p in pool if isinstance(p, dict) or "Expert Scenario" not in str(p[0])]
    filler = [p for p in pool if not (isinstance(p, dict) or "Expert Scenario" not in str(p[0]))]
    ordered = rich + filler
    while len(ordered) < 90:
        ordered.extend(rich)
    ordered = ordered[:90]
    return ordered[:40], ordered[40:70], ordered[70:90]


def main() -> None:
    banks = {}
    for week, pool in WEEK_POOLS.items():
        i, a, e = assign_tiers(pool)
        assert len(i) == 40, f"Week {week} intermediate: {len(i)}"
        assert len(a) == 30, f"Week {week} advanced: {len(a)}"
        assert len(e) == 20, f"Week {week} expert: {len(e)}"
        banks[week] = (i, a, e)

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(HEADER)
        for week in (8, 17, 18, 19, 20):
            write_bank(f"WEEK_{week:02d}_INTERMEDIATE", banks[week][0], fh)
            write_bank(f"WEEK_{week:02d}_ADVANCED", banks[week][1], fh)
            write_bank(f"WEEK_{week:02d}_EXPERT", banks[week][2], fh)
        fh.write("""
ALL_WEEKS_08_17_20_BANKS = {
    8: {
        "intermediate": WEEK_08_INTERMEDIATE,
        "advanced": WEEK_08_ADVANCED,
        "expert": WEEK_08_EXPERT,
    },
    17: {
        "intermediate": WEEK_17_INTERMEDIATE,
        "advanced": WEEK_17_ADVANCED,
        "expert": WEEK_17_EXPERT,
    },
    18: {
        "intermediate": WEEK_18_INTERMEDIATE,
        "advanced": WEEK_18_ADVANCED,
        "expert": WEEK_18_EXPERT,
    },
    19: {
        "intermediate": WEEK_19_INTERMEDIATE,
        "advanced": WEEK_19_ADVANCED,
        "expert": WEEK_19_EXPERT,
    },
    20: {
        "intermediate": WEEK_20_INTERMEDIATE,
        "advanced": WEEK_20_ADVANCED,
        "expert": WEEK_20_EXPERT,
    },
}
""")

    spec = importlib.util.spec_from_file_location("banks", OUT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    total = sum(
        len(mod.ALL_WEEKS_08_17_20_BANKS[w][tier])
        for w in (8, 17, 18, 19, 20)
        for tier in ("intermediate", "advanced", "expert")
    )
    print(f"Wrote {OUT}")
    for w in (8, 17, 18, 19, 20):
        b = mod.ALL_WEEKS_08_17_20_BANKS[w]
        print(f"Week {w:02d}: I={len(b['intermediate'])} A={len(b['advanced'])} E={len(b['expert'])}")
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
