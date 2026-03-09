# AI Risk Governance Framework for LLM Deployments

> *"Governance matters most. Technical controls are necessary but insufficient — organizations need systematic, auditable processes to manage AI risk."*

## 1. Purpose

This framework provides a structured approach for enterprise Information Security Officers (*Sicherheitsbeauftragte*) to govern the risks associated with deploying Large Language Models. It is aligned with:

- **OWASP Top 10 for LLM Applications (2025)**
- **EU AI Act** (Regulation (EU) 2024/1689)
- **NIS2 Directive** (as transposed into German law via BSIG amendments, effective December 2025)
- **GDPR** (Regulation (EU) 2016/679)
- **ISO 27001:2022** — Information Security Management Systems
- **NIST AI RMF** — AI Risk Management Framework

## 2. AI Risk Assessment Methodology

### 2.1 Risk Identification

Every LLM deployment must undergo a structured risk identification process:

| Risk Domain | Key Questions |
|:---|:---|
| **Data Exposure** | What data does the LLM have access to? Can it be exfiltrated via prompt injection? |
| **Output Integrity** | Can the LLM produce harmful, misleading, or policy-violating outputs? |
| **Access Control** | Who can interact with the LLM? Are there role-based restrictions? |
| **Tool Integration** | Does the LLM trigger actions (API calls, code execution, database queries)? |
| **Supply Chain** | Are third-party models, plugins, or datasets used? Are they vetted? |
| **Compliance** | Does the use case fall under high-risk AI (EU AI Act Annex III)? |

### 2.2 Risk Classification Matrix

| Likelihood \ Impact | Low | Medium | High | Critical |
|:---|:---|:---|:---|:---|
| **Very Likely** | Medium | High | Critical | Critical |
| **Likely** | Low | Medium | High | Critical |
| **Possible** | Low | Medium | Medium | High |
| **Unlikely** | Low | Low | Medium | Medium |

### 2.3 Risk Treatment Options

1. **Mitigate** — Implement controls to reduce likelihood or impact
2. **Transfer** — Shift risk via insurance or contractual arrangements
3. **Accept** — Document the residual risk with management sign-off
4. **Avoid** — Do not proceed with the deployment

## 3. Mitigation Controls

### 3.1 Technical Controls

| Control ID | Control | OWASP Mapping | Priority |
|:---|:---|:---|:---|
| TC-01 | Input validation and prompt injection detection | LLM01 | Critical |
| TC-02 | Output filtering and content safety classifiers | LLM05 | High |
| TC-03 | System prompt hardening and canary tokens | LLM07 | High |
| TC-04 | Rate limiting and anomaly detection | LLM10 | Medium |
| TC-05 | Sandboxed execution for tool integrations | LLM06 | Critical |
| TC-06 | Data loss prevention (DLP) on LLM I/O | LLM02 | Critical |
| TC-07 | Model supply chain verification & integrity checks | LLM03 | High |
| TC-08 | RAG pipeline input sanitization | LLM01, LLM08 | High |

### 3.2 Organizational Controls

| Control ID | Control | Regulatory Basis | Priority |
|:---|:---|:---|:---|
| OC-01 | Establish an AI Governance Committee | EU AI Act Art. 9, NIS2 | Critical |
| OC-02 | Define an AI-specific Acceptable Use Policy | GDPR Art. 5, ISO 27001 A.5.10 | Critical |
| OC-03 | Mandatory AI security training for all employees | EU AI Act Art. 4, NIS2 §38 BSIG | High |
| OC-04 | Regular red-team exercises against LLM deployments | OWASP LLM01–LLM10 | High |
| OC-05 | Vendor risk assessment for third-party AI services | NIS2, EU AI Act Art. 28 | High |
| OC-06 | Data Protection Impact Assessment (DPIA) for LLMs | GDPR Art. 35 | Critical |
| OC-07 | Executive accountability and sign-off for AI risk | NIS2 §38 BSIG (Geschäftsleitung) | Critical |

### 3.3 Monitoring & Incident Response

| Control ID | Control | Requirement |
|:---|:---|:---|
| MR-01 | Continuous logging of all LLM inputs and outputs | Retain for minimum audit period |
| MR-02 | Real-time alerting on jailbreak detection triggers | < 5 minute response SLA |
| MR-03 | AI-specific incident response playbook | Must address prompt injection, data leak, and model compromise scenarios |
| MR-04 | Incident reporting to BSI (NIS2) | Initial notification within 24h, detail within 72h, final report within 30 days |
| MR-05 | Quarterly AI risk review and control effectiveness audit | Document findings and remediation actions |
| MR-06 | Post-incident lessons learned and control updates | Mandatory after every AI-related security incident |

## 4. Roles & Responsibilities

| Role | Responsibility |
|:---|:---|
| **Sicherheitsbeauftragter (ISO)** | Overall AI risk governance, policy ownership, compliance monitoring |
| **Datenschutzbeauftragter (DPO)** | GDPR compliance, DPIA oversight, data subject rights for AI processing |
| **AI Governance Committee** | Strategic risk decisions, deployment approval, regulatory alignment |
| **IT Security Team** | Technical control implementation, monitoring, incident response |
| **Development / MLOps Team** | Secure LLM integration, prompt hardening, model lifecycle management |
| **Geschäftsleitung (Executive Management)** | Ultimate accountability under NIS2 §38 BSIG, risk acceptance sign-off |

## 5. Governance Lifecycle

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  1. IDENTIFY │───▶│  2. ASSESS   │───▶│  3. MITIGATE │───▶│  4. MONITOR  │
│  AI use case │    │  Risk level  │    │  Controls    │    │  Continuous  │
└─────────────┘    └──────────────┘    └──────────────┘    └──────┬───────┘
                                                                  │
       ┌──────────────────────────────────────────────────────────┘
       ▼
┌──────────────┐    ┌──────────────┐
│  5. RESPOND  │───▶│  6. IMPROVE  │──── (Cycle restarts)
│  Incidents   │    │  Lessons     │
└──────────────┘    └──────────────┘
```

## 6. Key Takeaway

> **Enterprises are underprepared.** The regulatory clock is ticking — EU AI Act high-risk obligations are enforceable from August 2, 2026, and Germany's NIS2 implementation (BSIG) is already in effect with a registration deadline of March 2026. Organizations deploying LLMs without a governance framework are accumulating legal, operational, and reputational debt.

This framework is designed to be actionable, auditable, and aligned with the expectations of German regulatory authorities (BSI, BfDI) and European standards bodies.
