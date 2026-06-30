# Lab 26: Deploy .NET API to minikube/AKS

| **Week** | 26 | **Duration** | 120 min |

## Objectives
- [ ] Deploy Deployment + Service + Ingress
- [ ] Configure probes and resource limits
- [ ] Scale with `kubectl scale`

## Steps

```bash
minikube start
docker build -t order-api:local .
minikube image load order-api:local

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -w
kubectl port-forward svc/order-api 8080:80
```

**deployment.yaml essentials:** replicas: 3, livenessProbe, readinessProbe, resources requests/limits.

```bash
kubectl scale deployment order-api --replicas=5
kubectl describe hpa order-api-hpa  # if HPA configured
```

## AKS variant
```bash
az aks create --name aks-lab --resource-group rg-lab --node-count 2
az aks get-credentials --name aks-lab --resource-group rg-lab
# Push to ACR, deploy with image pull secret
```

## Report
Draw pod → service → ingress flow from memory.
