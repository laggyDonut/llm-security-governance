# Compliance Implications of LLM Deployments

## Overview

Deploying Large Language Models introduces compliance obligations across
multiple regulatory frameworks.  These obligations vary by jurisdiction,
sector, and the nature of the data processed.  This document summarises the
key frameworks, their applicability to LLM deployments, and the controls
required to achieve and maintain compliance.

---

## 1. EU AI Act

The EU AI Act (Regulation (EU) 2024/1689) is the world's first comprehensive
AI regulation.  It applies a risk-based approach, classifying AI systems into
four tiers.

### 1.1 Risk Classification

| Tier | Definition | LLM Examples |
|------|-----------|-------------|
| **Unacceptable risk** | Prohibited AI practices | Subliminal manipulation, social scoring |
| **High risk** | AI systems in critical sectors or affecting fundamental rights | CV screening, credit scoring, biometric identification |
| **Limited risk** | Chatbots and AI-generated content requiring disclosure obligations | Customer-facing LLM chatbots, synthetic content generators |
| **Minimal risk** | All other AI | Internal productivity tools, spam filters |

### 1.2 General-Purpose AI (GPAI) Models

Providers of foundation models / GPAI models must:

- Prepare and maintain technical documentation.
- Comply with EU copyright law regarding training data.
- Publish a sufficiently detailed summary of training data.
- Implement a policy to comply with copyright law.
- GPAI models with systemic risk (≥ 10²⁵ FLOPs training compute) face
  additional obligations: adversarial testing, incident reporting, cybersecurity
  measures, and energy efficiency reporting.

### 1.3 Compliance Actions for LLM Deployers

| Obligation | Required Action |
|------------|----------------|
| Conformity assessment (High-risk) | Document risk management system, data governance, technical robustness, and human oversight |
| Transparency (Limited risk – chatbots) | Disclose AI interaction to users; label synthetic content |
| Human oversight (High-risk) | Implement human-in-the-loop for consequential outputs (OPS-05) |
| Post-market monitoring | Log incidents; report serious incidents to national authority |
| Data governance | Document training and operational data practices |

**Relevant framework controls:** PRE-05 (DPIA equivalent), OPS-05, OPS-07, MON-03.

---

## 2. General Data Protection Regulation (GDPR) / UK GDPR

The GDPR applies whenever an LLM system processes personal data of EU/UK data
subjects.  LLMs present specific GDPR challenges because they may memorise and
reproduce personal data from training corpora.

### 2.1 Lawful Basis

Processing personal data through LLMs requires a valid lawful basis.  For most
commercial deployments, this will be:

- **Legitimate interests** – requires a balancing test demonstrating that
  interests are not overridden by data subject rights.
- **Contract performance** – where the LLM feature is central to a contracted
  service.
- **Consent** – impractical for most high-volume conversational applications.

### 2.2 Key Obligations

| Obligation | LLM-specific Consideration |
|------------|---------------------------|
| **Data minimisation** | Limit personal data included in prompts; avoid logging full conversation context unless necessary |
| **Purpose limitation** | Do not use conversation logs to fine-tune models without a separate lawful basis |
| **Accuracy** | LLM hallucinations may produce inaccurate personal data; implement correction mechanisms |
| **Storage limitation** | Define and enforce retention periods for conversation logs and any derived data |
| **Security (Article 32)** | Implement appropriate technical and organisational measures (TOMs) — see Governance Framework controls |
| **DPIA (Article 35)** | Required for systematic profiling or processing that is likely to result in high risk |
| **Data subject rights** | Right of access, erasure ("right to be forgotten"), and rectification must be honoured, including for data that may be encoded in model weights |

### 2.3 Third-Country Transfers

Where an LLM provider's infrastructure is located outside the EU/UK, data
transfer mechanisms must be in place:

- Standard Contractual Clauses (SCCs) — most common for cloud LLM providers.
- Adequacy decisions — limited to approved countries.
- Binding Corporate Rules — for intra-group transfers.

### 2.4 Compliance Actions

**Relevant framework controls:** PRE-05, OPS-07, OPS-08, Section 6 of the
Governance Framework (Supplier Management).

---

## 3. California Consumer Privacy Act / CPRA (CCPA)

California residents have rights over personal information including:

- Right to know what personal information is collected.
- Right to delete personal information.
- Right to opt out of sale or sharing.
- Right to correct inaccurate personal information.

LLM deployments that process California residents' personal information must
honour these rights, including reviewing whether conversation data constitutes
"personal information" and whether LLM providers are "service providers" or
"third parties" under the CCPA definition.

---

## 4. NIST AI Risk Management Framework (AI RMF)

The NIST AI RMF (2023) provides voluntary guidance structured around four
functions: **Govern**, **Map**, **Measure**, and **Manage**.

| NIST Function | LLM Governance Mapping |
|---------------|------------------------|
| **Govern** | Roles and responsibilities (Section 2), policy review cycle (Section 8) |
| **Map** | Risk classification (Section 3), threat modelling (PRE-01) |
| **Measure** | Red-team testing (PRE-03), confidence scoring, monitoring (MON-01, MON-02) |
| **Manage** | Vulnerability management SLAs (Section 5), incident response (MON-03) |

The NIST AI RMF is increasingly referenced by US federal agencies and
procurement requirements and provides a strong baseline for any organisation
deploying LLMs in the US market.

---

## 5. Financial Services Regulations

Organisations deploying LLMs in financial services contexts face additional
sector-specific obligations.

### 5.1 EU Digital Operational Resilience Act (DORA)

For financial entities in the EU, DORA requires:

- ICT risk management framework covering AI-based tools.
- Incident classification and reporting for LLM-related operational failures.
- Third-party risk management for LLM providers as ICT service providers.
- Digital operational resilience testing including adversarial scenarios.

### 5.2 US Model Risk Management (SR 11-7)

The Federal Reserve's SR 11-7 guidance on model risk management applies to
LLMs used in credit, market risk, or regulatory capital calculations:

- Model inventory including LLM-based models.
- Conceptual soundness documentation.
- Ongoing monitoring for model drift and unexpected outputs.
- Independent model validation.

---

## 6. Healthcare and Life Sciences

LLMs processing protected health information (PHI) in the US are subject to
HIPAA:

- Business Associate Agreements (BAAs) with LLM providers.
- Minimum necessary principle — limit PHI in prompts.
- Audit controls for all PHI access.
- Breach notification obligations if LLM misuse results in PHI disclosure.

---

## 7. Compliance Monitoring and Reporting

| Activity | Frequency | Owner |
|----------|-----------|-------|
| DPIA review for high-risk LLM systems | Annually or upon material change | DPO / Legal |
| Audit of conversation log retention | Quarterly | Engineering / Security |
| Supplier compliance review | Annually | Legal / Procurement |
| Regulatory horizon scanning (new AI regulation) | Ongoing | Legal / AISO |
| Incident reporting to supervisory authority | Within 72 hours of awareness | DPO / Legal |
| Transparency disclosure review | Annually | Legal / Product |

---

## 8. Summary: Regulatory Mapping to Framework Controls

| Regulation | Key Requirement | Governance Control |
|------------|----------------|-------------------|
| EU AI Act | Conformity assessment, human oversight | PRE-05, OPS-05, MON-03 |
| GDPR / UK GDPR | DPIA, data minimisation, breach notification | PRE-05, OPS-08, MON-03 |
| CCPA / CPRA | Data rights, disclosure | OPS-08, Section 6 |
| NIST AI RMF | Risk mapping and measurement | PRE-01, PRE-03, MON-01 |
| DORA | ICT resilience, third-party risk | PRE-06, MON-03 |
| SR 11-7 | Model validation, ongoing monitoring | PRE-03, MON-02 |
| HIPAA | PHI protection, BAAs | OPS-08, Section 6 |

---

## References

- EU AI Act (Regulation (EU) 2024/1689)
- EU General Data Protection Regulation (Regulation (EU) 2016/679)
- UK GDPR (as retained in UK law by the European Union (Withdrawal) Act 2018)
- California Consumer Privacy Act / CPRA (Cal. Civ. Code § 1798.100 et seq.)
- NIST AI Risk Management Framework (NIST AI 100-1, 2023)
- EU Digital Operational Resilience Act (Regulation (EU) 2022/2554)
- US Federal Reserve SR 11-7 (Guidance on Model Risk Management, 2011)
- HIPAA Security Rule (45 CFR Part 164)
