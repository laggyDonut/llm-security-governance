# AI & LLM Acceptable Use Policy

> *"Clear policies prevent ambiguity. Enforceable policies enable accountability."*

**Document ID:** POL-AI-001  
**Version:** 1.0  
**Effective Date:** {Insert Date}  
**Review Date:** {Annual Review}  
**Owner:** Sicherheitsbeauftragter / Information Security Officer  
**Approval:** Geschäftsleitung (Executive Management)

---

## 1. Purpose

This policy establishes the rules and responsibilities for the acceptable use of Artificial Intelligence (AI) systems, including Large Language Models (LLMs), within {Organization Name}. It ensures that AI usage aligns with organizational values, legal obligations, and security requirements.

---

## 2. Scope

This policy applies to:

- **All employees, contractors, and third parties** who access or use AI systems provided or sanctioned by the organization
- **All AI systems**, including but not limited to:
  - Internally deployed LLMs and chatbots
  - Third-party AI services (e.g., OpenAI, Azure AI, Google Vertex AI)
  - AI-powered tools embedded in business applications
  - AI-assisted development tools (e.g., code assistants)

---

## 3. Definitions

| Term | Definition |
|:---|:---|
| **AI System** | Any machine-based system that generates outputs such as predictions, recommendations, or content for a given set of inputs |
| **LLM** | Large Language Model — an AI system trained on text data to understand and generate natural language |
| **Prompt** | Input provided to an AI system to elicit a response |
| **System Prompt** | Hidden instructions that configure AI behavior (not visible to end users) |
| **Jailbreak** | An attempt to manipulate an AI system to bypass its safety controls |
| **Personal Data** | Any information relating to an identified or identifiable natural person (per GDPR Art. 4) |

---

## 4. Acceptable Use

### 4.1 Permitted Uses

Users **MAY** use organizational AI systems for:

- ✅ Legitimate business tasks aligned with job responsibilities
- ✅ Research, learning, and professional development
- ✅ Drafting, editing, and summarizing business documents
- ✅ Code generation, review, and debugging (subject to code review)
- ✅ Data analysis and visualization (with anonymized/aggregated data)
- ✅ Customer service assistance (within approved workflows)

### 4.2 Prohibited Uses

Users **MUST NOT**:

| Prohibited Action | Rationale |
|:---|:---|
| ❌ Input personal data (PII) without documented necessity and approval | GDPR compliance, data minimization |
| ❌ Input confidential or trade secret information into external AI services | Data leakage risk |
| ❌ Attempt to jailbreak, bypass, or manipulate AI safety controls | Security policy violation |
| ❌ Use AI to generate harmful, illegal, discriminatory, or unethical content | Legal and reputational risk |
| ❌ Use AI for unauthorized surveillance or profiling of individuals | GDPR, fundamental rights |
| ❌ Rely on AI outputs for high-risk decisions without human review | EU AI Act Art. 14 human oversight |
| ❌ Present AI-generated content as human-authored without disclosure | Transparency requirements |
| ❌ Use personal/unauthorized AI tools for business purposes | Shadow IT risk |
| ❌ Share AI access credentials or API keys | Access control violation |

---

## 5. Data Protection Requirements

### 5.1 Personal Data

- **Do not input personal data** into AI systems unless:
  1. A lawful basis exists (GDPR Art. 6)
  2. The use has been documented and approved
  3. A Data Protection Impact Assessment (DPIA) has been completed where required
  4. Appropriate technical safeguards are in place

- **Assume AI systems retain data.** Treat all inputs as potentially persistent.

### 5.2 Confidential Information

- **Do not input** trade secrets, strategic plans, financial projections, or other confidential information into external AI services
- **Internal AI systems** approved for confidential data must be documented in the AI System Inventory

### 5.3 AI Outputs

- **Verify accuracy** of all AI-generated outputs before use in business decisions
- **Do not assume** AI outputs are factually correct, legally compliant, or free from bias

---

## 6. Security Requirements

### 6.1 Access Control

- Use only **organizational accounts** to access AI systems
- **Never share** credentials or API keys
- Report lost or compromised credentials immediately

### 6.2 Incident Reporting

Report the following to the Security Team / SOC immediately:

- Suspected jailbreak or prompt injection attacks
- AI system producing unexpected, harmful, or policy-violating outputs
- Suspected data leakage through AI
- Discovery of vulnerabilities in AI systems

**Reporting channel:** {security@organization.com / internal ticketing system}

### 6.3 Logging & Monitoring

- All AI interactions may be logged for security, compliance, and audit purposes
- Users should have no expectation of privacy when using organizational AI systems

---

## 7. Regulatory Compliance

### 7.1 EU AI Act

- AI systems must be classified according to EU AI Act risk categories
- **High-risk AI systems** (Annex III) require:
  - Risk management system
  - Human oversight
  - Technical documentation
  - Conformity assessment before deployment
- **AI literacy** is mandatory for all staff using AI systems (Art. 4)

### 7.2 GDPR

- AI use involving personal data must comply with all GDPR principles
- Data subjects have rights regarding automated decision-making (Art. 22)
- DPIAs are required for high-risk AI processing

### 7.3 NIS2/BSIG

- AI security incidents must be reported per NIS2 timelines (24h/72h/30d)
- AI systems are in scope for mandatory risk management measures

---

## 8. Roles & Responsibilities

| Role | Responsibility |
|:---|:---|
| **All Users** | Comply with this policy; report incidents; complete AI literacy training |
| **Line Managers** | Ensure team compliance; approve appropriate AI use cases |
| **Sicherheitsbeauftragter** | Maintain policy; oversee AI security controls; coordinate incident response |
| **Data Protection Officer** | Advise on GDPR compliance; review DPIAs; handle data subject requests |
| **AI/ML Team** | Manage AI systems; implement technical controls; support security audits |
| **Geschäftsleitung** | Approve policy; ensure adequate resources; accept residual risk |

---

## 9. Training Requirements

| Requirement | Audience | Frequency |
|:---|:---|:---|
| AI Literacy Training (EU AI Act Art. 4) | All AI users | Annual |
| AI Security Awareness | All AI users | Annual |
| Advanced AI Risk Management | AI/ML Team, Security Team | Annual |

---

## 10. Policy Violations

Violations of this policy may result in:

- Disciplinary action up to and including termination
- Revocation of AI system access
- Legal action where applicable
- Reporting to regulatory authorities if required by law

---

## 11. Exceptions

Exceptions to this policy require:

1. Written business justification
2. Risk assessment
3. Approval by Sicherheitsbeauftragter and relevant stakeholder (DPO for data protection, Legal for compliance)
4. Documentation in the exception register

---

## 12. Related Documents

| Document | Description |
|:---|:---|
| [Incident Response Playbook — LLM](incident-response-playbook-llm.md) | Procedures for AI security incidents |
| [LLM Risk Register](llm-risk-register-template.md) | Documented AI-related risks |
| [Governance Framework](governance-framework.md) | Enterprise AI governance controls |
| [Compliance Implications](compliance-implications.md) | GDPR, NIS2, EU AI Act obligations |
| Information Security Policy | Organizational security requirements |
| Data Protection Policy | GDPR compliance requirements |

---

## 13. Document Control

| Version | Date | Author | Change Summary |
|:---|:---|:---|:---|
| 1.0 | 2025-03-09 | Portfolio Project | Initial release |

**Next Review:** {Insert Date — within 12 months}

---

## 14. Acknowledgment

By using organizational AI systems, users acknowledge that they have read, understood, and agree to comply with this Acceptable Use Policy.

---

*This policy template is provided for educational purposes and should be adapted to your organization's specific context, risk appetite, and legal requirements.*
