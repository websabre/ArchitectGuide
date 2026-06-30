# Lab 27: GitOps with ArgoCD

| **Week** | 27 | **Duration** | 120 min |

## Objectives
- [ ] Install ArgoCD on cluster
- [ ] Git repo as source of truth for manifests
- [ ] Demonstrate drift detection

## Steps
1. `kubectl create namespace argocd`
2. Install ArgoCD manifests
3. Create Git repo with `k8s/` folder (deployment, service)
4. Create ArgoCD Application pointing to repo
5. Change replica count in Git → observe sync
6. `kubectl scale` manually → observe drift → ArgoCD corrects

## Architect Report
GitOps vs CI/CD pipeline pushing with kubectl — trade-offs?
