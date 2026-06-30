# Linux for Architects — Production Operations

> **Week 28** | **Module:** [linux](../../../modules/linux/README.md)

## Learning Objectives
- Use essential Linux commands for troubleshooting
- Understand networking and process management on Linux hosts/AKS nodes
- Write basic shell scripts for automation

---

## 1. Essential Commands

| Command | Purpose |
|---------|---------|
| `ls -la` | List files with permissions |
| `cd`, `pwd` | Navigate |
| `cat`, `less`, `tail -f` | View logs (live: `tail -f app.log`) |
| `grep -r "error" /var/log` | Search logs |
| `find / -name "*.log" -mtime -1` | Find recent files |
| `ps aux` | Running processes |
| `top` / `htop` | Live process monitor |
| `df -h` | Disk usage |
| `free -m` | Memory |
| `du -sh *` | Directory sizes |

---

## 2. Process & Service Management (systemd)

```bash
systemctl status nginx
systemctl restart docker
journalctl -u docker -f    # service logs
journalctl -k              # kernel logs
```

**AKS nodes:** systemd manages kubelet, containerd.

---

## 3. Networking Commands

```bash
ip addr show              # interfaces and IPs
ss -tulpn                 # listening ports (modern netstat)
curl -v https://api.local # HTTP debug
nslookup mydb.database.windows.net
dig api.example.com
traceroute 10.0.1.5
tcpdump -i eth0 port 443  # packet capture (careful in prod)
```

**Troubleshooting pod networking:**
```bash
kubectl exec -it pod-name -- curl http://other-service:8080/health
kubectl run tmp --rm -it --image=nicolaka/netshoot -- bash  # debug pod
```

---

## 4. File Permissions

```bash
chmod 600 secrets.env
chown appuser:appuser /app
```

**Architect:** Containers should run non-root. File permissions matter for secrets mounted as volumes.

---

## 5. Shell Scripting for Architects

```bash
#!/bin/bash
set -euo pipefail

NAMESPACE=${1:-default}
PODS=$(kubectl get pods -n "$NAMESPACE" -o jsonpath='{.items[*].metadata.name}')

for pod in $PODS; do
  STATUS=$(kubectl get pod "$pod" -n "$NAMESPACE" -o jsonpath='{.status.phase}')
  if [[ "$STATUS" != "Running" ]]; then
    echo "ALERT: $pod is $STATUS"
  fi
done
```

**Use cases:** Health check scripts, log rotation, deployment smoke tests, FinOps reports.

---

## 6. PowerShell vs Bash on Azure

| Task | Linux/Bash | PowerShell |
|------|------------|------------|
| AKS troubleshooting | kubectl + bash | kubectl + pwsh |
| Azure automation | Azure CLI | Az module (richer) |
| CI/CD agents | Ubuntu agents | Windows agents |

**Architect on Windows shop:** Know both — AKS nodes are Linux; Azure automation often PowerShell.

**Next:** [labs/](../labs/)
