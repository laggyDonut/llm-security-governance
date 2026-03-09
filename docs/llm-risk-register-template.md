# LLM Risk Register Template

> *"You cannot manage what you do not measure. A risk register transforms abstract threats into actionable governance."*

## 1. Purpose

This template provides a structured format for documenting, assessing, and tracking risks associated with Large Language Model (LLM) deployments. It is designed to:

- Align with OWASP Top 10 for LLM Applications (2025)
- Support compliance with GDPR, NIS2/BSIG, and EU AI Act requirements
- Enable ongoing risk management and audit trail

---

## 2. Risk Register Structure

### 2.1 Field Definitions

| Field | Description | Example |
|:---|:---|:---|
| **Risk ID** | Unique identifier (format: `LLM-R-###`) | LLM-R-001 |
| **Risk Title** | Short descriptive name | Prompt Injection — Instruction Override |
| **Description** | Detailed explanation of the risk | Adversaries may craft prompts that override system instructions, causing the LLM to ignore safety guardrails and execute unintended actions. |
| **OWASP Mapping** | Relevant OWASP LLM Top 10 category | LLM01: Prompt Injection |
| **Affected System(s)** | Which LLM deployment(s) are impacted | Customer Service Chatbot, Internal Knowledge Assistant |
| **Risk Category** | Classification (Technical, Compliance, Operational, Reputational) | Technical |
| **Threat Actor** | Who might exploit this risk | External attacker, Malicious insider, Automated bot |
| **Inherent Likelihood** | Probability before controls (1–5 scale) | 4 (Likely) |
| **Inherent Impact** | Severity before controls (1–5 scale) | 4 (Major) |
| **Inherent Risk Score** | Likelihood × Impact | 16 (High) |
| **Existing Controls** | Current mitigations in place | Pattern-based jailbreak detection, system prompt hardening, I/O logging |
| **Control Effectiveness** | Assessment of control quality (Effective, Partial, Ineffective) | Partial |
| **Residual Likelihood** | Probability after controls | 3 (Possible) |
| **Residual Impact** | Severity after controls | 3 (Moderate) |
| **Residual Risk Score** | Likelihood × Impact | 9 (Medium) |
| **Risk Appetite** | Acceptable residual risk level | Medium |
| **Treatment Strategy** | Accept, Mitigate, Transfer, Avoid | Mitigate |
| **Planned Actions** | Additional mitigations planned | Implement semantic analysis layer, deploy canary tokens |
| **Control Owner** | Person responsible for controls | IT Security Team Lead |
| **Risk Owner** | Person accountable for the risk | Head of AI/ML |
| **Review Date** | Next scheduled review | 2025-06-15 |
| **Last Updated** | Date of last modification | 2025-03-09 |
| **Status** | Open, In Progress, Mitigated, Accepted, Closed | Open |

---

### 2.2 Likelihood Scale

| Score | Label | Description |
|:---:|:---|:---|
| 1 | Rare | May occur only in exceptional circumstances (<5% annually) |
| 2 | Unlikely | Could occur but not expected (5–20% annually) |
| 3 | Possible | Might occur at some time (20–50% annually) |
| 4 | Likely | Will probably occur in most circumstances (50–80% annually) |
| 5 | Almost Certain | Expected to occur in most circumstances (>80% annually) |

### 2.3 Impact Scale

| Score | Label | Financial | Operational | Compliance | Reputational |
|:---:|:---|:---|:---|:---|:---|
| 1 | Negligible | <€10K | No disruption | No regulatory action | No external awareness |
| 2 | Minor | €10K–€100K | Minor disruption (<4h) | Warning/guidance | Limited local awareness |
| 3 | Moderate | €100K–€1M | Significant disruption (4–24h) | Formal investigation | Regional/industry awareness |
| 4 | Major | €1M–€10M | Major disruption (1–7 days) | Fine, enforcement action | National media coverage |
| 5 | Catastrophic | >€10M | Critical failure (>7 days) | License revocation, personal liability | International coverage, lasting damage |

### 2.4 Risk Score Matrix

|  | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Likelihood 5** | 5 (Medium) | 10 (High) | 15 (High) | 20 (Critical) | 25 (Critical) |
| **Likelihood 4** | 4 (Low) | 8 (Medium) | 12 (High) | 16 (High) | 20 (Critical) |
| **Likelihood 3** | 3 (Low) | 6 (Medium) | 9 (Medium) | 12 (High) | 15 (High) |
| **Likelihood 2** | 2 (Low) | 4 (Low) | 6 (Medium) | 8 (Medium) | 10 (High) |
| **Likelihood 1** | 1 (Low) | 2 (Low) | 3 (Low) | 4 (Low) | 5 (Medium) |

**Risk levels:**
- **Low (1–4):** Accept or monitor
- **Medium (5–9):** Active management required
- **High (10–16):** Priority mitigation required
- **Critical (17–25):** Immediate executive attention

---

## 3. Sample Risk Register Entries

### LLM-R-001: Prompt Injection — Instruction Override

| Field | Value |
|:---|:---|
| **Risk ID** | LLM-R-001 |
| **Risk Title** | Prompt Injection — Instruction Override |
| **Description** | Adversaries craft prompts containing instructions that override or bypass the LLM's system prompt and safety guardrails, potentially causing unauthorized actions, policy violations, or safety bypass. |
| **OWASP Mapping** | LLM01: Prompt Injection |
| **Affected System(s)** | All customer-facing LLM deployments |
| **Risk Category** | Technical |
| **Threat Actor** | External attacker, Malicious insider |
| **Inherent Likelihood** | 4 (Likely) |
| **Inherent Impact** | 4 (Major) |
| **Inherent Risk Score** | 16 (High) |
| **Existing Controls** | Pattern-based detection engine, system prompt hardening, rate limiting |
| **Control Effectiveness** | Partial |
| **Residual Likelihood** | 3 (Possible) |
| **Residual Impact** | 3 (Moderate) |
| **Residual Risk Score** | 9 (Medium) |
| **Risk Appetite** | Medium |
| **Treatment Strategy** | Mitigate |
| **Planned Actions** | Deploy semantic analysis layer, implement instruction hierarchy enforcement, add red team testing schedule |
| **Control Owner** | IT Security Team Lead |
| **Risk Owner** | Head of AI/ML |
| **Review Date** | 2025-06-15 |
| **Last Updated** | 2025-03-09 |
| **Status** | Open |

---

### LLM-R-002: System Prompt Leakage

| Field | Value |
|:---|:---|
| **Risk ID** | LLM-R-002 |
| **Risk Title** | System Prompt Leakage |
| **Description** | Attackers extract confidential system prompts, revealing business logic, internal instructions, API configurations, or competitive secrets embedded in the prompt. |
| **OWASP Mapping** | LLM07: System Prompt Leakage |
| **Affected System(s)** | All LLM deployments with proprietary system prompts |
| **Risk Category** | Technical, Compliance |
| **Threat Actor** | Competitor, Security researcher, Malicious insider |
| **Inherent Likelihood** | 4 (Likely) |
| **Inherent Impact** | 3 (Moderate) |
| **Inherent Risk Score** | 12 (High) |
| **Existing Controls** | Prompt extraction detection rules, output filtering |
| **Control Effectiveness** | Partial |
| **Residual Likelihood** | 3 (Possible) |
| **Residual Impact** | 2 (Minor) |
| **Residual Risk Score** | 6 (Medium) |
| **Risk Appetite** | Medium |
| **Treatment Strategy** | Mitigate |
| **Planned Actions** | Deploy canary tokens in system prompts, implement output scanning for prompt fragments |
| **Control Owner** | AI/ML Team Lead |
| **Risk Owner** | Head of AI/ML |
| **Review Date** | 2025-06-15 |
| **Last Updated** | 2025-03-09 |
| **Status** | Open |

---

### LLM-R-003: AI-Induced Personal Data Breach

| Field | Value |
|:---|:---|
| **Risk ID** | LLM-R-003 |
| **Risk Title** | AI-Induced Personal Data Breach |
| **Description** | LLM discloses personal data from training data, RAG knowledge base, or conversation context due to jailbreak, misconfiguration, or model behavior, triggering GDPR Art. 33/34 breach notification obligations. |
| **OWASP Mapping** | LLM06: Sensitive Information Disclosure |
| **Affected System(s)** | LLMs with access to personal data (HR assistant, customer service, healthcare) |
| **Risk Category** | Compliance |
| **Threat Actor** | External attacker, Data subject (curious), Automated scraping |
| **Inherent Likelihood** | 3 (Possible) |
| **Inherent Impact** | 5 (Catastrophic) |
| **Inherent Risk Score** | 15 (High) |
| **Existing Controls** | Data minimization in RAG pipeline, PII detection on output, jailbreak detection |
| **Control Effectiveness** | Partial |
| **Residual Likelihood** | 2 (Unlikely) |
| **Residual Impact** | 4 (Major) |
| **Residual Risk Score** | 8 (Medium) |
| **Risk Appetite** | Low |
| **Treatment Strategy** | Mitigate |
| **Planned Actions** | Implement differential privacy for RAG, deploy real-time PII redaction on all outputs, complete DPIA |
| **Control Owner** | Data Protection Officer |
| **Risk Owner** | Chief Information Security Officer |
| **Review Date** | 2025-04-30 |
| **Last Updated** | 2025-03-09 |
| **Status** | In Progress |

---

### LLM-R-004: NIS2/BSIG Incident Reporting Failure

| Field | Value |
|:---|:---|
| **Risk ID** | LLM-R-004 |
| **Risk Title** | NIS2/BSIG Incident Reporting Failure |
| **Description** | Organization fails to report AI-related security incidents to BSI within mandated timelines (24h early warning, 72h notification), resulting in regulatory penalties and personal liability for Geschäftsleitung under §38 BSIG. |
| **OWASP Mapping** | N/A (Compliance risk) |
| **Affected System(s)** | All LLM systems in NIS2-scope entities |
| **Risk Category** | Compliance |
| **Threat Actor** | N/A (Internal process failure) |
| **Inherent Likelihood** | 3 (Possible) |
| **Inherent Impact** | 4 (Major) |
| **Inherent Risk Score** | 12 (High) |
| **Existing Controls** | Incident response playbook, SOC alerting |
| **Control Effectiveness** | Partial |
| **Residual Likelihood** | 2 (Unlikely) |
| **Residual Impact** | 4 (Major) |
| **Residual Risk Score** | 8 (Medium) |
| **Risk Appetite** | Low |
| **Treatment Strategy** | Mitigate |
| **Planned Actions** | Implement automated BSI reporting workflow, add AI incidents to SOC runbook, conduct tabletop exercise |
| **Control Owner** | SOC Manager |
| **Risk Owner** | Sicherheitsbeauftragter |
| **Review Date** | 2025-05-15 |
| **Last Updated** | 2025-03-09 |
| **Status** | Open |

---

### LLM-R-005: EU AI Act Non-Compliance (High-Risk Systems)

| Field | Value |
|:---|:---|
| **Risk ID** | LLM-R-005 |
| **Risk Title** | EU AI Act Non-Compliance (High-Risk Systems) |
| **Description** | High-risk LLM deployments (HR screening, credit scoring, medical advice) fail to meet EU AI Act obligations by August 2, 2026, including risk management (Art. 9), technical documentation (Art. 11), human oversight (Art. 14), and conformity assessment (Art. 43). |
| **OWASP Mapping** | N/A (Compliance risk) |
| **Affected System(s)** | High-risk AI systems per Annex III |
| **Risk Category** | Compliance |
| **Threat Actor** | N/A (Regulatory enforcement) |
| **Inherent Likelihood** | 3 (Possible) |
| **Inherent Impact** | 5 (Catastrophic) |
| **Inherent Risk Score** | 15 (High) |
| **Existing Controls** | AI system inventory initiated, legal briefing completed |
| **Control Effectiveness** | Ineffective |
| **Residual Likelihood** | 3 (Possible) |
| **Residual Impact** | 5 (Catastrophic) |
| **Residual Risk Score** | 15 (High) |
| **Risk Appetite** | Low |
| **Treatment Strategy** | Mitigate |
| **Planned Actions** | Complete AI system classification by Q2 2025, initiate conformity assessment process, establish human oversight procedures, complete technical documentation |
| **Control Owner** | AI Governance Lead |
| **Risk Owner** | Chief Information Security Officer |
| **Review Date** | 2025-04-15 |
| **Last Updated** | 2025-03-09 |
| **Status** | Open |

---

## 4. Risk Register Governance

### 4.1 Review Cadence

| Risk Level | Review Frequency |
|:---|:---|
| Critical | Monthly |
| High | Quarterly |
| Medium | Semi-annually |
| Low | Annually |

### 4.2 Roles & Responsibilities

| Role | Responsibility |
|:---|:---|
| **Risk Owner** | Accountable for the risk; approves treatment strategy; escalates as needed |
| **Control Owner** | Responsible for implementing and maintaining controls; reports on effectiveness |
| **Sicherheitsbeauftragter** | Oversees risk register; ensures alignment with organizational risk appetite; reports to management |
| **Internal Audit** | Independently validates risk assessments and control effectiveness |
| **Geschäftsleitung** | Accountable for overall risk posture; approves risk appetite; personal liability under NIS2 §38 |

### 4.3 Change Log

| Version | Date | Author | Change Summary |
|:---|:---|:---|:---|
| 1.0 | 2025-03-09 | Portfolio Project | Initial release |

---

## 5. References

- [OWASP Top 10 for Large Language Model Applications (2025)](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [ISO 31000:2018 — Risk Management Guidelines](https://www.iso.org/standard/65694.html)
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework)
- [EU AI Act — Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [NIS2 Directive — Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
