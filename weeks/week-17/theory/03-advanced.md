# AWS Fundamentals — Advanced

> **Week 17** | **Level:** Advanced

## Multi-Account Strategy

```
Organization Root
├── Security OU (log archive, audit)
├── Infrastructure OU (shared networking)
└── Workloads OU
    ├── prod-account
    └── nonprod-account
```

## Cost Allocation

- Mandatory tags via SCP + Config rules
- Cost Explorer + CUR to S3 for FinOps
- Reserved Instances / Savings Plans for baseline

**Premium Q&A:** [AWS Top 50](../../../interview-prep/aws-top-50-index.md)

## Architect Deep Dive: Hybrid Identity

### Entra ID + AWS IAM Identity Center
Single sign-on for engineers across clouds — reduces credential sprawl and audit complexity.

