# Incident Response Playbook: LLM Security Incidents

> *"When seconds matter, playbooks save hours. Document your response before you need it."*

## 1. Purpose & Scope

This playbook provides step-by-step procedures for responding to LLM-related security incidents, specifically:

- **Prompt Injection / Jailbreak Attacks** — Adversarial manipulation of LLM behavior
- **System Prompt Leakage** — Unauthorized disclosure of confidential instructions
- **AI-Induced Data Exfiltration** — LLM revealing sensitive information from training data, RAG pipelines, or conversation context

**Applicable regulations:** GDPR (Art. 33/34), NIS2/BSIG (§32 incident reporting), EU AI Act (Art. 12 logging, Art. 15 cybersecurity).

---

## 2. Severity Classification

| Severity | Description | Response SLA | Examples |
|:---|:---|:---|:---|
| **SEV-1 (Critical)** | Active exploitation with confirmed data breach or system compromise | Immediate escalation | PII exfiltration, full system prompt leak with secrets |
| **SEV-2 (High)** | Confirmed attack attempt with potential for harm | < 1 hour | Successful jailbreak bypassing safety controls |
| **SEV-3 (Medium)** | Suspicious activity requiring investigation | < 4 hours | Repeated prompt injection attempts from single source |
| **SEV-4 (Low)** | Informational — anomalous but not confirmed malicious | < 24 hours | Single failed jailbreak attempt, benign testing |

---

## 3. Incident Response Phases

### Phase 1: Detection & Identification (0–15 minutes)

**Trigger sources:**
- [ ] Automated alert from jailbreak detection engine
- [ ] SOC analyst observation
- [ ] User report
- [ ] Compliance/audit finding

**Initial triage steps:**

| Step | Action | Owner |
|:---|:---|:---|
| 1.1 | Confirm the alert is not a false positive — review prompt/output logs | SOC Analyst |
| 1.2 | Classify severity using table above | SOC Analyst |
| 1.3 | Assign incident ID (format: `LLM-YYYY-MM-####`) | SOC Analyst |
| 1.4 | Open incident ticket and begin documentation | SOC Analyst |
| 1.5 | For SEV-1/SEV-2: Notify Incident Commander immediately | SOC Analyst |

**Key questions to answer:**
- What LLM system was targeted?
- What was the attack vector (prompt injection, persona exploitation, encoding, etc.)?
- Was any sensitive data disclosed?
- Is the attack ongoing or contained?
- What is the blast radius (single user, session, API key, all users)?

---

### Phase 2: Containment (15–60 minutes)

**Objective:** Limit further damage while preserving evidence.

| Severity | Containment Actions |
|:---|:---|
| SEV-1 | Immediately isolate affected LLM endpoint. Block attacker IP/session. Consider full system shutdown if necessary. |
| SEV-2 | Block attacker session/API key. Enable enhanced logging. Alert downstream integrations. |
| SEV-3 | Rate-limit suspicious source. Increase monitoring threshold. |
| SEV-4 | Document and monitor. No immediate action required. |

**Containment checklist:**

- [ ] Block/revoke compromised API keys or user sessions
- [ ] Enable verbose I/O logging on affected endpoint
- [ ] Preserve all relevant logs (do NOT rotate or delete)
- [ ] Snapshot system state if possible (memory dumps, container images)
- [ ] Notify affected business stakeholders
- [ ] If personal data involved: Alert Data Protection Officer (DPO)

---

### Phase 3: Evidence Collection & Preservation

**Legal note:** Evidence must be handled in a forensically sound manner to support potential legal action, regulatory reporting, or insurance claims.

**Evidence to collect:**

| Evidence Type | Location | Retention |
|:---|:---|:---|
| Full I/O logs (prompts + responses) | LLM logging pipeline / SIEM | Minimum 90 days (or as per data retention policy) |
| Attacker identifiers (IP, session ID, API key) | WAF / API gateway logs | As above |
| System prompt version at time of incident | Version control / config management | Permanent |
| Detection engine alerts | SIEM / alerting system | As above |
| Screenshots / recordings of attack (if applicable) | Incident ticket attachments | As above |

**Chain of custody:**
- Document who collected each evidence artifact
- Use write-once storage where possible
- Hash all evidence files (SHA-256) and record in incident ticket

---

### Phase 4: Eradication & Recovery

**Objective:** Remove the threat and restore normal operations.

| Action | Owner | Estimated Time |
|:---|:---|:---|
| Deploy patched detection rules to block attack variant | Security Engineering | 1–4 hours |
| Rotate any potentially compromised secrets (API keys, system prompts) | Platform Team | 30 min–2 hours |
| Harden system prompt with additional guardrails | AI/ML Team | 1–8 hours |
| Validate fix with red team testing | Security Engineering | 2–4 hours |
| Restore service if previously isolated | Platform Team | As needed |
| Confirm no backdoors or persistent compromise | Security Engineering | Varies |

---

### Phase 5: Regulatory Notification

#### 5.1 GDPR (Art. 33/34) — Personal Data Breach

**Applicability:** If the incident resulted in unauthorized disclosure, access, or loss of personal data.

| Requirement | Timeline | Owner |
|:---|:---|:---|
| Notify supervisory authority (BfDI or state DPA) | **72 hours** from awareness | DPO / Legal |
| Notify affected data subjects (if high risk) | Without undue delay | DPO / Legal |
| Document breach in internal register (even if not reported) | Ongoing | DPO |

**Documentation required:**
- Nature of the breach (categories of data, approximate number of records)
- Likely consequences
- Measures taken to mitigate

#### 5.2 NIS2/BSIG (§32) — Incident Reporting for Essential/Important Entities

**Applicability:** Organizations in scope of NIS2 (energy, healthcare, finance, digital infrastructure, etc.).

| Report Stage | Timeline | Content |
|:---|:---|:---|
| Early warning | **24 hours** | Initial indication that an incident has occurred |
| Incident notification | **72 hours** | Assessment of incident, severity, cross-border impact |
| Intermediate report | On request from BSI | Updated information |
| Final report | **1 month** | Root cause, impact, remediation measures |

**Reporting channel:** BSI incident reporting portal (https://www.bsi.bund.de/meldestelle)

> **Note:** Under §38 BSIG, executive management (Geschäftsleitung) is **personally liable** for ensuring adequate incident response capabilities. Failure to report can result in penalties up to €10M or 2% of global turnover.

#### 5.3 EU AI Act (Art. 62) — Serious Incident Reporting

**Applicability:** Providers of high-risk AI systems.

| Requirement | Timeline |
|:---|:---|
| Report serious incidents (death, serious harm, fundamental rights violations) to market surveillance authority | Without undue delay, or within specific timelines per member state |

---

### Phase 6: Post-Incident Review

**Timeline:** Conduct within 5 business days of incident closure.

**Participants:**
- Incident Commander
- SOC representative
- AI/ML team lead
- Affected business unit
- DPO (if personal data involved)
- Legal (if regulatory notification triggered)

**Agenda:**

1. **Timeline reconstruction** — What happened and when?
2. **Detection effectiveness** — How was it found? How can detection improve?
3. **Response effectiveness** — What worked? What didn't?
4. **Root cause analysis** — Why did the vulnerability exist?
5. **Lessons learned** — What will we do differently?
6. **Action items** — Document with owners and deadlines

**Outputs:**
- Post-incident report (retained for audit)
- Updated runbooks/playbooks
- Risk register updates
- Training recommendations

---

## 4. Communication Templates

### 4.1 Internal Escalation (SEV-1/SEV-2)

```
SUBJECT: [URGENT] LLM Security Incident — SEV-{X} — {Incident ID}

STATUS: {Active / Contained / Resolved}
SYSTEM AFFECTED: {LLM system name}
SEVERITY: SEV-{X}
INCIDENT COMMANDER: {Name}

SUMMARY:
{Brief description of what happened}

CURRENT ACTIONS:
- {Action 1}
- {Action 2}

NEXT UPDATE: {Time}
```

### 4.2 Regulatory Notification (Template)

```
TO: {Supervisory Authority / BSI}
FROM: {Organization Data Protection Officer / Security Officer}
DATE: {Date}
RE: Incident Notification pursuant to GDPR Art. 33 / BSIG §32

1. ORGANIZATION: {Legal entity name, registration number}
2. INCIDENT DATE/TIME: {When discovered, when occurred}
3. NATURE OF INCIDENT: {Description}
4. DATA CATEGORIES AFFECTED: {If applicable}
5. ESTIMATED SCOPE: {Number of records/individuals}
6. LIKELY CONSEQUENCES: {Assessment}
7. MEASURES TAKEN: {Containment, remediation}
8. CONTACT: {DPO / Security Officer contact details}
```

---

## 5. RACI Matrix

| Activity | SOC Analyst | Incident Commander | AI/ML Team | DPO | Legal | Exec (Geschäftsleitung) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Detection & triage | **R/A** | I | I | - | - | - |
| Severity classification | R | **A** | C | I | - | I (SEV-1/2) |
| Containment | R | **A** | C | - | - | I (SEV-1/2) |
| Evidence preservation | R | **A** | C | C | C | - |
| GDPR notification decision | I | C | - | **R/A** | C | I |
| NIS2 notification | I | C | - | C | C | **A** |
| Root cause analysis | C | **A** | **R** | - | - | I |
| Post-incident review | C | **R/A** | C | C | C | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 6. Appendix: Quick Reference

### Detection Engine Risk Levels → Severity Mapping

| Detection Risk Level | Recommended Incident Severity |
|:---|:---|
| CRITICAL | SEV-1 or SEV-2 (confirm with context) |
| HIGH | SEV-2 |
| MEDIUM | SEV-3 |
| LOW | SEV-4 |
| NONE | No incident |

### Key Contacts

| Role | Name | Contact |
|:---|:---|:---|
| Incident Commander (primary) | {Name} | {Email / Phone} |
| Incident Commander (backup) | {Name} | {Email / Phone} |
| Data Protection Officer | {Name} | {Email} |
| Legal Counsel | {Name} | {Email} |
| SOC Lead | {Name} | {Email / Phone} |
| AI/ML Team Lead | {Name} | {Email / Phone} |

---

## 7. Document Control

| Version | Date | Author | Change Summary |
|:---|:---|:---|:---|
| 1.0 | 2025-03-09 | Portfolio Project | Initial release |

**Review schedule:** Annually, or after any SEV-1/SEV-2 incident.

**Approval:** {Sicherheitsbeauftragter / CISO signature}
