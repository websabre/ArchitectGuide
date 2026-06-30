# Week 28 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Essential File Permissions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Explain Linux file permissions and architect relevance for container hosts?

### Short Answer (30 seconds)

rwx for owner/group/others (octal 755, 640). Directories need x to traverse. Principle of least privilege on config, keys, and scripts.

### Detailed Answer (3–5 minutes)

**Key checks:**
```bash
ls -la /etc/shadow  # should be root-only
find / -perm -4000  # SUID binaries audit
```

**Architect:** AKS nodes — restrict SSH; app configs 640; no world-writable `/tmp` exploits. Container: non-root USER aligns with file ownership in image.

### Architecture Perspective

Permission mistakes are common privilege escalation path.

### Follow-up Questions

1. **chmod 777 fix? — Never in prod — diagnose owner/group instead.**
2. **ACLs getfacl? — Fine-grained beyond rwx — enterprise filesystems.**

### Common Mistakes in Interviews

- chmod 777 on app directory
- Secrets world-readable in /etc
- Run container as root to avoid permission issues

---

## Q032: Process Management ps top

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Use ps and top to diagnose high CPU on Linux AKS node?

### Short Answer (30 seconds)

`top` — live CPU/memory; `ps aux --sort=-%cpu | head` — snapshot ranking; `ps -ef` — full process tree.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. `top` — load average, which PID hot
2. `ps -p PID -o pid,ppid,cmd` — identify process
3. Map to container: `crictl ps` on AKS node

**Architect:** Distinguish node problem vs pod problem — drain node if kubelet healthy but noisy neighbor pod.

### Architecture Perspective

Process tools bridge host and container troubleshooting.

### Follow-up Questions

1. **htop/atop? — Better UX — atop records for post-mortem.**
2. **PID namespace? — Container PIDs differ from host view — use crictl.**

### Common Mistakes in Interviews

- Kill -9 first without identifying process
- Ignore load average vs CPU count
- Debug prod node without change control

---

## Q033: systemd Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

How does systemd relate to AKS nodes and Linux VMs?

### Short Answer (30 seconds)

systemd is init system — manages units (services, timers, mounts). AKS nodes run kubelet, containerd as systemd units.

### Detailed Answer (3–5 minutes)

**Commands:**
```bash
systemctl status kubelet
journalctl -u containerd -f
systemctl restart kubelet  # caution prod
```

**Architect:** On VMs (jump boxes, build agents): define services as unit files — `Restart=on-failure`, not manual nohup.

### Architecture Perspective

systemd is standard service lifecycle on Linux infrastructure.

### Follow-up Questions

1. **systemd vs Docker restart policy? — Different layers — kubelet manages pods.**
2. **Unit file hardening? — User=, ProtectSystem= for services.**

### Common Mistakes in Interviews

- nohup java & on production VM
- Restart kubelet without understanding impact
- Disable systemd logging

---

## Q034: journalctl Logging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Query systemd journal logs for kubelet failure on AKS node?

### Short Answer (30 seconds)

`journalctl -u kubelet --since '1 hour ago' -p err` — errors only; `-f` follow; `--no-pager` for scripts.

### Detailed Answer (3–5 minutes)

**Examples:**
```bash
journalctl -u kubelet -b  # current boot
journalctl -k  # kernel messages — OOM killer
```

**Architect:** Correlate journal timestamps with AKS control plane events and pod events. Export to Log Analytics for retention beyond local journal size.

### Architecture Perspective

journalctl is first stop for node-level failures.

### Follow-up Questions

1. **journal vacuum? — Disk full — limit journal size in /etc/systemd/journald.conf.**
2. **Structured fields? — journalctl -o json — parsing.**

### Common Mistakes in Interviews

- grep /var/log without checking journal
- Ignore kernel OOM in journal
- No central log shipping from nodes

---

## Q035: Networking ip ss curl

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Diagnose connectivity from Linux pod to Azure SQL using ip, ss, curl?

### Short Answer (30 seconds)

`ip addr/route` — interfaces and routing; `ss -tlnp` — listening ports; `curl -v telnet://host:1433` — TCP reachability.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. `nslookup sqlserver.database.windows.net` — DNS resolves?
2. `curl -v --connect-timeout 5 telnet://...` — port open?
3. `traceroute` / `mtr` — path issues
4. `ip route` — private endpoint route exists?

**Architect:** NetworkPolicy egress, NSG, private DNS zone — systematic elimination.

### Architecture Perspective

Linux network CLI is essential for connectivity triage.

### Follow-up Questions

1. **ss vs netstat? — ss faster modern replacement.**
2. **dig +trace? — DNS delegation debug.**

### Common Mistakes in Interviews

- ping only — ICMP blocked doesn't mean TCP dead
- Assume DNS works without nslookup
- Skip TLS layer when debugging HTTPS

---

## Q036: DNS Resolution Debug

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Debug DNS resolution failure from AKS pod to internal service?

### Short Answer (30 seconds)

Check `/etc/resolv.conf`, `nslookup`, `dig`, CoreDNS logs, ndots search path misconfiguration.

### Detailed Answer (3–5 minutes)

**Common issues:**
- Wrong search domain — `orders` vs `orders.svc.cluster.local`
- CoreDNS pod down — `kubectl get pods -n kube-system`
- Azure Private DNS zone not linked to VNet

**Architect:** Document required FQDN patterns; test DNS in CI smoke tests.

### Architecture Perspective

DNS failures look like application bugs — isolate early.

### Follow-up Questions

1. **dig @10.0.0.10? — Query specific CoreDNS IP.**
2. **ndots:5 issue? — Short name resolves externally wrongly.**

### Common Mistakes in Interviews

- Hardcode IP bypassing DNS debt
- Ignore resolv.conf in pod
- Private endpoint DNS zone missing link

---

## Q037: SSH Hardening

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

SSH hardening for Linux jump boxes and emergency AKS node access?

### Short Answer (30 seconds)

Key-only auth, disable root login, AllowUsers, fail2ban, non-standard port optional, audit logging, session timeout.

### Detailed Answer (3–5 minutes)

**sshd_config:**
```
PermitRootLogin no
PasswordAuthentication no
AllowUsers ops@corp.com
```

**Architect:** AKS — prefer `az aks command invoke` or bastion over SSH to nodes; break-glass only with MFA and session recording.

### Architecture Perspective

SSH is attack surface — minimize and audit.

### Follow-up Questions

1. **Bastion vs direct SSH? — Azure Bastion — no public IP on VM.**
2. **Certificate-based SSH? — Short-lived certs — Teleport/Okta.**

### Common Mistakes in Interviews

- Password SSH enabled
- Shared ops key on all servers
- Routine SSH to AKS nodes for app debug

---

## Q038: sudo Least Privilege

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Configure sudo least privilege for ops team on Linux?

### Short Answer (30 seconds)

sudoers per-command aliases — not ALL=(ALL) NOPASSWD:ALL. Use groups; log commands; require password for destructive ops.

### Detailed Answer (3–5 minutes)

**Example sudoers:**
```
%ops ALL=(ALL) /bin/systemctl restart nginx, /usr/bin/journalctl
```

**Architect:** Prefer identity-based access (Azure RBAC, AKS admin via AAD) over shared root; audit `/var/log/auth.log`.

### Architecture Perspective

sudo scope creep is insider threat vector.

### Follow-up Questions

1. **visudo? — Always edit sudoers safely — syntax check.**
2. **sudo without logging? — Enable auditd session recording.**

### Common Mistakes in Interviews

- NOPASSWD ALL for developers
- Shared root password
- sudo su - as daily workflow

---

## Q039: Package Management apt yum

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Package management on Ubuntu AKS nodes vs container images?

### Short Answer (30 seconds)

AKS nodes: apt for node OS patches (managed by AKS). Containers: install packages in Dockerfile build — not apt at runtime in prod.

### Detailed Answer (3–5 minutes)

**Commands:**
```bash
apt list --upgradable
apt-cache policy package
```

**Architect:** Don't SSH apt-upgrade nodes manually — use AKS node image upgrade. Pin package versions in Dockerfile `apt-get install package=version`.

### Architecture Perspective

Patch strategy differs for nodes vs containers.

### Follow-up Questions

1. **unattended-upgrades? — VMs yes — AKS nodes via platform.**
2. **RPM yum/dnf? — RHEL-based images — same principles.**

### Common Mistakes in Interviews

- apt install in running prod container
- Manual node patching outside AKS channel
- Unpinned packages in Dockerfile — drift

---

## Q040: Shell Scripting Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Shell scripting patterns for architect automation?

### Short Answer (30 seconds)

Use bash for glue: CI checks, backup scripts, health probes. `set -euo pipefail`, quote variables, log actions.

### Detailed Answer (3–5 minutes)

```bash
#!/bin/bash
set -euo pipefail
LOG_FILE=/var/log/deploy.log
exec > >(tee -a "$LOG_FILE") 2>&1
echo "$(date) Starting deploy"
```

**Architect:** Prefer Python/PowerShell for complex logic; bash for kubectl wrappers; idempotent scripts safe to re-run.

### Architecture Perspective

Script robustness prevents 3am automation failures.

### Follow-up Questions

1. **shellcheck? — Lint bash in CI.**
2. **Idempotent scripts? — Check state before create.**

### Common Mistakes in Interviews

- Unquoted $variables break on spaces
- set -e missing — silent failure
- Curl bash pipe install in prod script

---

## Q041: grep awk sed

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Use grep, awk, sed for log analysis during incident?

### Short Answer (30 seconds)

grep filters lines; awk columns and aggregates; sed stream edit — extract correlation IDs, count errors per minute.

### Detailed Answer (3–5 minutes)

**Examples:**
```bash
grep 'ERROR' app.log | wc -l
awk '$9 ~ /^5/ {count++} END {print count}' access.log
grep -oP 'CorrelationId=\K[^ ]+' app.log | sort | uniq -c
```

**Architect:** Prefer structured JSON logs + Log Analytics KQL at scale — CLI for quick SSH triage.

### Architecture Perspective

CLI log slicing is incident triage skill.

### Follow-up Questions

1. **jq for JSON logs? — Better than grep on structured logs.**
2. **zgrep? — Search compressed rotated logs.**

### Common Mistakes in Interviews

- grep million-line file without time filter
- Regex catastrophic backtracking
- Only CLI — no centralized log query

---

## Q042: Disk Usage df du

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Diagnose disk full on AKS node — df and du workflow?

### Short Answer (30 seconds)

`df -h` — filesystem usage; `du -sh /var/*` — find large dirs; common: container logs, images, journal.

### Detailed Answer (3–5 minutes)

**AKS:**
```bash
df -h /var/lib/containerd
ctr images ls
crictl rmi --prune
```

**Architect:** Alert disk >80% on nodes; image GC policy; log rotation; PVC capacity separate from node disk.

### Architecture Perspective

Disk full causes evictions and pod failures.

### Follow-up Questions

1. **du --inodes? — inode exhaustion rare but real.**
2. **ncdu? — Interactive du navigator.**

### Common Mistakes in Interviews

- Delete random files without identifying
- Ignore container image accumulation
- No disk alerts until 100%

---

## Q043: Memory Analysis free vmstat

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Interpret free and vmstat during memory pressure on Linux?

### Short Answer (30 seconds)

`free -h` — available memory (includes cache); `vmstat 1` — si/so swap, us/sy CPU, r runnable queue.

### Detailed Answer (3–5 minutes)

**OOM:** Kernel kills process — `dmesg | grep -i oom`. **Container:** cgroup limit triggers OOMKill before node OOM.

**Architect:** Distinguish node memory pressure (evictions) vs pod limit too low (.NET OOMKill).

### Architecture Perspective

Memory metrics misread causes wrong scaling decisions.

### Follow-up Questions

1. **available vs free? — Linux uses cache — available matters.**
2. **slab top? — Kernel cache — advanced tuning.**

### Common Mistakes in Interviews

- free shows 0 free — panic without reading available
- Ignore swap activity si/so
- Raise pod limit without investigating leak

---

## Q044: CPU Profiling top htop

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

CPU profiling approach on Linux for .NET container?

### Short Answer (30 seconds)

Host: `top -H -p PID` threads; `perf top` kernel/user. Container: `dotnet-trace`, `dotnet-counters` preferred over host perf for managed code.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. Confirm CPU in `kubectl top pod`
2. `dotnet-trace collect` CPU sample
3. Speedscope flame graph

**Architect:** CPU limit throttling shows as high throttled time — not always high CPU% — check cgroup metrics.

### Architecture Perspective

Right tool per layer — managed vs kernel profiling.

### Follow-up Questions

1. **perf permissions? — paranoid setting blocks — adjust carefully.**
2. **dotnet-gcdump? — Memory not CPU — complementary.**

### Common Mistakes in Interviews

- perf on managed without dotnet tools
- Ignore CPU throttling from limits
- Profile prod without approval

---

## Q045: Load Average Meaning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

What does load average mean on 8-core AKS node?

### Short Answer (30 seconds)

Load average = runnable + uninterruptible tasks averaged over 1/5/15 min. On 8 cores, load 8 ≈ full utilization; load 16 = sustained overload.

### Detailed Answer (3–5 minutes)

**Interpret:** High load + low CPU% → IO wait (disk). High load + high CPU → compute bound.

**Architect:** Alert load per core ratio; correlate with pod resource requests — oversubscription causes scheduling latency not just CPU.

### Architecture Perspective

Load average context requires core count.

### Follow-up Questions

1. **iowait in top? — Disk bottleneck despite low CPU.**
2. **run queue latency? — Scheduler delay — advanced.**

### Common Mistakes in Interviews

- Load 4 on 32 core called overload
- Ignore 15-min load trend
- Load high but all pods fine — miss IO wait

---

## Q046: File Descriptors ulimit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

File descriptor exhaustion — symptoms and fix on Linux?

### Short Answer (30 seconds)

Symptoms: 'too many open files', accept errors, connection failures. Check `ulimit -n`, `lsof -p PID | wc -l`, `/proc/PID/limits`.

### Detailed Answer (3–5 minutes)

**Fix:** Raise `nofile` in systemd unit or `/etc/security/limits.conf`; fix connection leaks in app (.NET HttpClientFactory).

**Architect:** Set reasonable container limits; monitor open FDs metric; load test connection counts.

### Architecture Perspective

FD leaks take down high-connection services silently.

### Follow-up Questions

1. **fs.file-max sysctl? — System-wide ceiling.**
2. **lsof -i? — Network connections as FDs.**

### Common Mistakes in Interviews

- ulimit unlimited in prod without monitoring
- new HttpClient per request leak
- Ignore TIME_WAIT socket accumulation

---

## Q047: Cron vs systemd Timers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Cron vs systemd timers for scheduled jobs?

### Short Answer (30 seconds)

Cron: simple time tables, universal. systemd timers: dependency aware, logging to journal, randomized delay, missed run catch-up.

### Detailed Answer (3–5 minutes)

**Architect:** K8s CronJob replaces host cron for containerized workloads. VM maintenance: systemd timer with `OnCalendar` and `Persistent=true`.

**Avoid:** Cron on AKS nodes — use K8s CronJob or Azure Functions timer.

### Architecture Perspective

Scheduler choice follows deployment model.

### Follow-up Questions

1. **CronJob concurrency policy? — Forbid overlap — long jobs.**
2. **at command? — One-off scheduled — rare.**

### Common Mistakes in Interviews

- Cron on node for app batch job
- Overlapping cron without lock
- No logging of cron failures

---

## Q048: Firewall ufw iptables

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Linux firewall relevance for AKS and Azure VMs?

### Short Answer (30 seconds)

Azure NSG is primary cloud firewall. Host ufw/iptables on VMs and optional defense-in-depth; AKS pod traffic via NetworkPolicy not iptables on node manually.

### Detailed Answer (3–5 minutes)

**VM:** `ufw allow 22/tcp`, default deny incoming.

**AKS:** Don't manually iptables on nodes — kube-proxy/CNI manages. Use Calico/Azure NPM NetworkPolicy.

**Architect:** Defense layers: NSG → NetworkPolicy → app auth.

### Architecture Perspective

Know which firewall layer applies where.

### Follow-up Questions

1. **iptables-nft vs legacy? — Modern distros use nft backend.**
2. **Azure Firewall vs NSG? — Centralized egress vs subnet.**

### Common Mistakes in Interviews

- Disable NSG relying on host ufw only
- Manual iptables on AKS worker
- NetworkPolicy wide open because NSG exists

---

## Q049: TLS Cert Inspection openssl

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Inspect TLS certificate expiry and chain with openssl?

### Short Answer (30 seconds)

```bash
openssl s_client -connect api.example.com:443 -servername api.example.com </dev/null 2>/dev/null | openssl x509 -noout -dates -subject
```

Check issuer, SAN, expiry — notAfter date.

### Detailed Answer (3–5 minutes)

**Architect:** Monitor cert expiry 30 days ahead; cert-manager automates on K8s; Azure Key Vault certs for apps. Test full chain trust — missing intermediate causes client errors.

### Architecture Perspective

openssl s_client is quick cert health check.

### Follow-up Questions

1. **check_cert_expiry scripts? — Nagios/Prometheus blackbox exporter.**
2. **TLS 1.0/1.1 test? — openssl s_client -tls1 — verify disabled protocols.**

### Common Mistakes in Interviews

- Expired cert discovered by users
- Self-signed in prod without trust chain
- Check cert but ignore hostname mismatch

---

## Q050: tcpdump Wireshark Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Occasional |

### Question

When use tcpdump for AKS network debugging?

### Short Answer (30 seconds)

Capture packets to diagnose DNS, TLS handshake, connection reset — ephemeral debug container with tcpdump on pod network namespace.

### Detailed Answer (3–5 minutes)

```bash
tcpdump -i any host 10.0.1.5 and port 443 -w capture.pcap
```

**Architect:** Break-glass only — sensitive data in captures; time-bound; prefer observability mesh telemetry over packet capture in steady state.

### Architecture Perspective

Packet capture is last resort — powerful and sensitive.

### Follow-up Questions

1. **nsenter pod network? — Host capture pod traffic.**
2. **Wireshark analyze offline? — Share pcap — scrub PII.**

### Common Mistakes in Interviews

- tcpdump in prod without approval
- Capture full payloads with PII
- No capture size limit — disk fill

---

## Q051: strace Debugging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Occasional |

### Question

When strace a process on Linux and limitations in containers?

### Short Answer (30 seconds)

strace traces syscalls — diagnose hanging I/O, permission denied, missing files. `strace -p PID -f -tt`.

### Detailed Answer (3–5 minutes)

**Container:** Need CAP_SYS_PTRACE or debug ephemeral container; distroless has no strace — use debug sidecar.

**Architect:** High overhead — don't strace prod under load long. Prefer app-level tracing OpenTelemetry.

### Architecture Perspective

strace is syscall microscope — use sparingly.

### Follow-up Questions

1. **strace connect hang? — See blocked connect syscall — firewall.**
2. **eBPF bpftrace? — Lower overhead modern alternative.**

### Common Mistakes in Interviews

- strace prod all day — performance kill
- strace without -f misses child processes
- No correlation with app trace ID

---

## Q052: lsof Network Ports

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Use lsof to find which process holds port 8080?

### Short Answer (30 seconds)

`lsof -i :8080` or `ss -tlnp | grep 8080`. Shows PID/command binding port — resolve port conflicts on VMs and debug Connection refused.

### Detailed Answer (3–5 minutes)

**Container host:** Map to container via crictl. **.NET:** Kestrel binding `ASPNETCORE_URLS` — address already in use means duplicate bind.

**Architect:** Document required ports per service; avoid hostNetwork unless necessary.

### Architecture Perspective

Port binding conflicts cause mysterious startup failures.

### Follow-up Questions

1. **lsof -p PID? — All open files for leak debug.**
2. **fuser -k? — Kill process on port — dangerous prod.**

### Common Mistakes in Interviews

- Kill random PID on port without identification
- hostNetwork:true without port coordination
- Ignore IPv6 vs IPv4 bind differences

---

## Q053: Environment Variables

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

How Linux environment variables affect .NET containers?

### Short Answer (30 seconds)

K8s sets env from ConfigMap/Secret; Docker `-e`; systemd `Environment=`. .NET config hierarchy: env vars override appsettings with `__` nesting.

### Detailed Answer (3–5 minutes)

**Inspect:**
```bash
printenv | sort
kubectl exec pod -- env | grep ConnectionStrings
```

**Architect:** Never log secrets from env; use `envFrom` carefully; document required env contract in Helm chart README.

### Architecture Perspective

Env vars are 12-factor config — understand precedence.

### Follow-up Questions

1. **.NET __ nesting? — `Logging__LogLevel__Default=Warning`.**
2. **export in profile only? — Non-interactive pods miss it.**

### Common Mistakes in Interviews

- Secrets printed in startup log
- Env var typo silent default misconfig
- Huge env block — use file mount instead

---

## Q054: Path and Symlinks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

PATH and symlink issues in containers and Linux scripts?

### Short Answer (30 seconds)

PATH order determines which binary runs; symlinks can break relative paths or point to wrong version. Use absolute paths in production scripts.

### Detailed Answer (3–5 minutes)

**Container:** Minimal PATH in distroless — only bundled binaries. **Shebang:** `#!/usr/bin/env bash` vs pinned `/bin/bash`.

**Architect:** Immutable infrastructure — don't rely on `/usr/local/bin` drift on nodes.

### Architecture Perspective

PATH assumptions cause 'works in dev shell' failures.

### Follow-up Questions

1. **readlink -f? — Resolve symlink canonical path.**
2. **which -a? — All PATH matches for command.**

### Common Mistakes in Interviews

- Relative path in cron job fails
- Symlink to wrong dotnet version
- Trust PATH on shared jump box

---

## Q055: Log Rotation logrotate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Configure logrotate for VM apps vs container stdout logging?

### Short Answer (30 seconds)

logrotate compresses/rotates file logs — `/etc/logrotate.d/app`. Containers should log stdout — collected by cluster not logrotate on node.

### Detailed Answer (3–5 minutes)

**VM example:**
```
/var/log/myapp/*.log {
  daily
  rotate 14
  compress
  copytruncate
}
```

**Architect:** AKS node disk — journald size limits; app logs via Fluent Bit — not files in container.

### Architecture Perspective

Log rotation prevents disk full — know your logging model.

### Follow-up Questions

1. **copytruncate vs create? — App must reopen log file — know app behavior.**
2. **Docker json-file max-size? — Dev Docker only.**

### Common Mistakes in Interviews

- Unbounded file logs in container
- logrotate missing on VM — disk full
- Rotate without ship to central store

---

## Q056: User Group Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

Linux user/group management for service accounts?

### Short Answer (30 seconds)

Dedicated service user per app — no login shell `/usr/sbin/nologin`. Group for shared file access. UID/GID stable for volume mounts.

### Detailed Answer (3–5 minutes)

**Container:** Match `runAsUser` with image USER. **VM:** `useradd -r -s /usr/sbin/nologin appuser`.

**Architect:** Central identity (AAD) for humans; local service accounts for processes only.

### Architecture Perspective

Service account hygiene limits compromise blast radius.

### Follow-up Questions

1. **usermod -aG? — Group membership for file access.**
2. **nscd/sssd? — Enterprise LDAP/NSS integration.**

### Common Mistakes in Interviews

- App runs as shared user 'app'
- UID mismatch volume permission denied
- Human users share service account

---

## Q057: SELinux AppArmor Awareness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Occasional |

### Question

SELinux and AppArmor awareness for container architects?

### Short Answer (30 seconds)

Mandatory access control — confines process capabilities beyond Unix permissions. AKS/Ubuntu may use AppArmor profiles for containers.

### Detailed Answer (3–5 minutes)

**Symptoms:** Permission denied despite chmod 777 — MAC blocking. **Check:** `aa-status`, audit logs.

**Architect:** Don't disable SELinux/AppArmor globally — adjust profiles. Container seccomp/AppArmor defaults from runtime.

### Architecture Perspective

MAC explains 'impossible' permission denials.

### Follow-up Questions

1. **seccomp profile? — K8s RuntimeDefault — syscall filter.**
2. **Privileged bypasses MAC? — Another reason deny privileged.**

### Common Mistakes in Interviews

- setenforce 0 as fix
- Custom profile without testing
- Ignore audit denials in logs

---

## Q058: Container Host Linux

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Common |

### Question

What Linux knowledge matters for AKS node troubleshooting?

### Short Answer (30 seconds)

cgroup memory/CPU, containerd/crictl, networking bridges/CNI, systemd kubelet, disk/image GC, logs journald, NSG + iptables interaction.

### Detailed Answer (3–5 minutes)

**Node triage order:**
1. Node Ready? `kubectl describe node`
2. Disk/memory pressure?
3. kubelet/containerd healthy? `systemctl status`
4. Image pull errors? `crictl pull`

**Architect:** Platform SRE owns nodes; app teams need basic fluency for joint incidents.

### Architecture Perspective

Container host is still Linux — abstractions leak.

### Follow-up Questions

1. **cgroup v2? — Unified hierarchy — .NET respects limits.**
2. **Node problem detector? — AKS addon — auto drain unhealthy nodes.**

### Common Mistakes in Interviews

- Treat AKS nodes as black boxes always
- crictl vs docker CLI confusion
- No runbook for NodeNotReady

---

## Q059: AKS Node Troubleshooting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Systematic AKS node NotReady troubleshooting?

### Short Answer (30 seconds)

Check node conditions (MemoryPressure, DiskPressure, PIDPressure), kubelet logs, recent upgrades, subnet/IP exhaustion, taints.

### Detailed Answer (3–5 minutes)

**Steps:**
1. `kubectl describe node` — Conditions and Events
2. `kubectl get pods -A -o wide | grep NodeName`
3. SSH/bastion: `journalctl -u kubelet`
4. Azure Portal: node pool health, scale set
5. Cordon/drain if unrecoverable — replace node

**Architect:** Automate node auto-repair; alert on NotReady >5 min.

### Architecture Perspective

Node issues affect all pods on host — prioritize resolution.

### Follow-up Questions

1. **Surge upgrade stuck? — PDB blocking — temporary scale.**
2. **Subnet full? — Scale fails — expand VNet prefix.**

### Common Mistakes in Interviews

- Delete node without drain
- Ignore DiskPressure until kubelet stops
- No monitoring on node conditions

---

## Q060: Linux Incident Triage Workflow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Linux incident triage workflow for platform architect?

### Short Answer (30 seconds)

Stabilize → assess blast radius → gather evidence → hypothesize → mitigate → postmortem. Use runbooks; communicate status; avoid random changes.

### Detailed Answer (3–5 minutes)

**First 15 minutes:**
1. User impact? SLO breach?
2. Recent deploy/change?
3. Golden signals: latency, errors, traffic, saturation
4. `kubectl get nodes,pods -A` — cluster healthy?
5. Top: CPU/memory/disk/errors from dashboards

**Architect:** Incident commander role; timeline doc; blameless postmortem with actions.

### Architecture Perspective

Structured triage beats heroic debugging.

### Follow-up Questions

1. **Severity levels? — SEV1 customer down — escalation path.**
2. **Rollback first? — If deploy correlated — roll back before deep debug.**

### Common Mistakes in Interviews

- Random reboot without hypothesis
- No incident timeline
- Skip postmortem for 'quick fix'

---

## Q061: systemd Unit Files

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: systemd Unit Files — what do you need to know and decide?

### Short Answer (30 seconds)

systemd Unit Files requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *systemd Unit Files*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect systemd Unit Files to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove systemd Unit Files is healthy in production?**
2. **What is the rollback plan if systemd Unit Files change fails?**

### Common Mistakes in Interviews

- Treating systemd Unit Files as set-and-forget with no monitoring
- No ADR documenting trade-offs for systemd Unit Files
- Copying systemd Unit Files pattern from blog without context fit

---

## Q062: journalctl Log Query

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: journalctl Log Query — what do you need to know and decide?

### Short Answer (30 seconds)

journalctl Log Query requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *journalctl Log Query*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect journalctl Log Query to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove journalctl Log Query is healthy in production?**
2. **What is the rollback plan if journalctl Log Query change fails?**

### Common Mistakes in Interviews

- Treating journalctl Log Query as set-and-forget with no monitoring
- No ADR documenting trade-offs for journalctl Log Query
- Copying journalctl Log Query pattern from blog without context fit

---

## Q063: logrotate Configuration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: logrotate Configuration — what do you need to know and decide?

### Short Answer (30 seconds)

logrotate Configuration requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *logrotate Configuration*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect logrotate Configuration to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove logrotate Configuration is healthy in production?**
2. **What is the rollback plan if logrotate Configuration change fails?**

### Common Mistakes in Interviews

- Treating logrotate Configuration as set-and-forget with no monitoring
- No ADR documenting trade-offs for logrotate Configuration
- Copying logrotate Configuration pattern from blog without context fit

---

## Q064: ulimit File Descriptors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: ulimit File Descriptors — what do you need to know and decide?

### Short Answer (30 seconds)

ulimit File Descriptors requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *ulimit File Descriptors*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect ulimit File Descriptors to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove ulimit File Descriptors is healthy in production?**
2. **What is the rollback plan if ulimit File Descriptors change fails?**

### Common Mistakes in Interviews

- Treating ulimit File Descriptors as set-and-forget with no monitoring
- No ADR documenting trade-offs for ulimit File Descriptors
- Copying ulimit File Descriptors pattern from blog without context fit

---

## Q065: TCP Tuning sysctl

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: TCP Tuning sysctl — what do you need to know and decide?

### Short Answer (30 seconds)

TCP Tuning sysctl requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *TCP Tuning sysctl*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect TCP Tuning sysctl to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove TCP Tuning sysctl is healthy in production?**
2. **What is the rollback plan if TCP Tuning sysctl change fails?**

### Common Mistakes in Interviews

- Treating TCP Tuning sysctl as set-and-forget with no monitoring
- No ADR documenting trade-offs for TCP Tuning sysctl
- Copying TCP Tuning sysctl pattern from blog without context fit

---

## Q066: ss vs netstat

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: ss vs netstat — what do you need to know and decide?

### Short Answer (30 seconds)

ss vs netstat requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *ss vs netstat*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect ss vs netstat to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove ss vs netstat is healthy in production?**
2. **What is the rollback plan if ss vs netstat change fails?**

### Common Mistakes in Interviews

- Treating ss vs netstat as set-and-forget with no monitoring
- No ADR documenting trade-offs for ss vs netstat
- Copying ss vs netstat pattern from blog without context fit

---

## Q067: dig nslookup DNS Debug

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: dig nslookup DNS Debug — what do you need to know and decide?

### Short Answer (30 seconds)

dig nslookup DNS Debug requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *dig nslookup DNS Debug*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect dig nslookup DNS Debug to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove dig nslookup DNS Debug is healthy in production?**
2. **What is the rollback plan if dig nslookup DNS Debug change fails?**

### Common Mistakes in Interviews

- Treating dig nslookup DNS Debug as set-and-forget with no monitoring
- No ADR documenting trade-offs for dig nslookup DNS Debug
- Copying dig nslookup DNS Debug pattern from blog without context fit

---

## Q068: curl HTTP Debug

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: curl HTTP Debug — what do you need to know and decide?

### Short Answer (30 seconds)

curl HTTP Debug requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *curl HTTP Debug*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect curl HTTP Debug to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove curl HTTP Debug is healthy in production?**
2. **What is the rollback plan if curl HTTP Debug change fails?**

### Common Mistakes in Interviews

- Treating curl HTTP Debug as set-and-forget with no monitoring
- No ADR documenting trade-offs for curl HTTP Debug
- Copying curl HTTP Debug pattern from blog without context fit

---

## Q069: tcpdump Packet Capture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: tcpdump Packet Capture — what do you need to know and decide?

### Short Answer (30 seconds)

tcpdump Packet Capture requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *tcpdump Packet Capture*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect tcpdump Packet Capture to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove tcpdump Packet Capture is healthy in production?**
2. **What is the rollback plan if tcpdump Packet Capture change fails?**

### Common Mistakes in Interviews

- Treating tcpdump Packet Capture as set-and-forget with no monitoring
- No ADR documenting trade-offs for tcpdump Packet Capture
- Copying tcpdump Packet Capture pattern from blog without context fit

---

## Q070: strace Syscall Trace

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Linux |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: strace Syscall Trace — what do you need to know and decide?

### Short Answer (30 seconds)

strace Syscall Trace requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 28 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 28 — Linux):**
- Scenario: production system at scale needs a decision involving *strace Syscall Trace*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect strace Syscall Trace to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove strace Syscall Trace is healthy in production?**
2. **What is the rollback plan if strace Syscall Trace change fails?**

### Common Mistakes in Interviews

- Treating strace Syscall Trace as set-and-forget with no monitoring
- No ADR documenting trade-offs for strace Syscall Trace
- Copying strace Syscall Trace pattern from blog without context fit

---
