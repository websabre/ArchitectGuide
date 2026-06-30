# Lab 28: Linux Troubleshooting Runbook

| **Week** | 28 | **Duration** | 90 min |

## Scenarios — diagnose and fix

### 1. Disk Full
```bash
df -h
du -sh /var/* | sort -h
journalctl --disk-usage
```

### 2. High CPU
```bash
top -o %CPU
ps aux --sort=-%cpu | head
```

### 3. Network Unreachable
```bash
ping, curl -v, ss -tulpn, nslookup
```

### 4. AKS Node Issues
```bash
kubectl get nodes
kubectl describe node <node>
kubectl get pods -A -o wide
```

### 5. Container Logs
```bash
kubectl logs pod-name --previous
journalctl -u kubelet
```

Create personal runbook with 10 commands you will use in incidents.
