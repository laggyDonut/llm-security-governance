# LLM Security Governance Framework

## Purpose

This framework provides organisations with a structured approach to governing
the security of Large Language Model (LLM) deployments.  It defines roles and
responsibilities, risk management processes, operational controls, and
monitoring requirements to ensure that LLM systems operate safely, ethically,
and in compliance with applicable regulations.

---

## 1. Governance Principles

| Principle | Description |
|-----------|-------------|
| **Risk-proportionate controls** | Security controls are calibrated to the sensitivity of the data processed and the impact of potential failures. |
| **Transparency** | Stakeholders understand how LLMs are used, what data they process, and what decisions they influence. |
| **Accountability** | Clear ownership of LLM systems with named responsible parties for security, ethics, and compliance. |
| **Privacy by design** | Personal data is minimised, protected, and handled lawfully throughout the LLM lifecycle. |
| **Continuous improvement** | Security posture is reviewed regularly and updated in response to emerging threats and incidents. |

---

## 2. Roles and Responsibilities

### 2.1 AI Security Officer (AISO)

- Owns the organisation's AI security policy and this governance framework.
- Chairs the AI Security Review Board.
- Approves deployment of high-risk LLM applications.
- Reports on AI security posture to executive leadership.

### 2.2 AI Security Review Board

- Reviews new LLM use cases and material changes to existing deployments.
- Approves risk acceptance for residual risks above defined tolerance thresholds.
- Meets at minimum quarterly; convenes ad hoc for critical incidents.

### 2.3 Engineering Teams

- Implement security controls in accordance with this framework.
- Conduct pre-deployment security assessments.
- Participate in red-team exercises.
- Remediate identified vulnerabilities within agreed SLAs.

### 2.4 Legal and Compliance

- Advise on regulatory obligations (GDPR, EU AI Act, CCPA, sector-specific requirements).
- Review data processing agreements with LLM providers.
- Maintain records of processing activities involving LLM systems.

### 2.5 Data Protection Officer (DPO) – where applicable

- Oversees data protection impact assessments (DPIAs) for high-risk LLM processing.
- Handles data subject requests related to LLM outputs.

---

## 3. LLM Risk Classification

All LLM applications must be classified before deployment:

| Risk Level | Criteria | Required Controls |
|------------|----------|-------------------|
| **Critical** | Processes highly sensitive PII or financial data; makes autonomous consequential decisions; public-facing without human oversight | Full DPIA, AISO approval, penetration test, real-time monitoring, human-in-the-loop for consequential actions |
| **High** | Processes sensitive internal data; provides advice that influences significant decisions | Security assessment, red-team exercise, output validation, logging |
| **Medium** | Internal productivity tools; limited data access; human reviews all outputs | Standard security review, basic logging, periodic audit |
| **Low** | Sandboxed experimentation; no sensitive data; outputs are informational only | Self-assessment, developer review |

---

## 4. Security Controls Catalogue

### 4.1 Pre-Deployment Controls

| Control ID | Control | Applicable Risk Levels |
|------------|---------|------------------------|
| PRE-01 | Threat modelling using STRIDE or equivalent | Medium, High, Critical |
| PRE-02 | Static analysis of system prompts and application code | Medium, High, Critical |
| PRE-03 | Red-team / adversarial testing (jailbreak, prompt injection, data extraction) | High, Critical |
| PRE-04 | Penetration test by independent team | Critical |
| PRE-05 | Data Protection Impact Assessment (DPIA) | High (if personal data), Critical |
| PRE-06 | Supply chain review of model provider and dependencies | High, Critical |

### 4.2 Operational Controls

| Control ID | Control | Applicable Risk Levels |
|------------|---------|------------------------|
| OPS-01 | Input validation / jailbreak detection (e.g. `JailbreakDetector`) | Medium, High, Critical |
| OPS-02 | System prompt hardening and confidentiality | Medium, High, Critical |
| OPS-03 | Output content scanning | High, Critical |
| OPS-04 | Least-privilege tool access | Medium, High, Critical |
| OPS-05 | Human-in-the-loop for consequential actions | Critical |
| OPS-06 | Rate limiting and abuse prevention | Medium, High, Critical |
| OPS-07 | Conversation and audit logging | Medium, High, Critical |
| OPS-08 | Data minimisation and retention controls | High, Critical |

### 4.3 Monitoring and Response Controls

| Control ID | Control | Applicable Risk Levels |
|------------|---------|------------------------|
| MON-01 | Real-time alerting on anomalous usage patterns | High, Critical |
| MON-02 | Periodic review of logs for policy violations | Medium, High, Critical |
| MON-03 | Incident response plan for LLM-specific scenarios | High, Critical |
| MON-04 | Vulnerability disclosure process | All levels |
| MON-05 | Scheduled red-team exercises (minimum annual) | High, Critical |

---

## 5. Vulnerability Management

### 5.1 Identification

- Continuous automated scanning using tools such as `JailbreakDetector`.
- Bug bounty or responsible disclosure programme for externally facing systems.
- Threat intelligence feeds monitoring for novel jailbreak and prompt-injection techniques.

### 5.2 Prioritisation

Vulnerabilities are scored using a modified CVSS framework adapted for LLM systems:

| Severity | CVSS-equivalent Score | Remediation SLA |
|----------|-----------------------|-----------------|
| Critical | 9.0 – 10.0 | 24 hours |
| High | 7.0 – 8.9 | 7 days |
| Medium | 4.0 – 6.9 | 30 days |
| Low | 0.1 – 3.9 | 90 days |

### 5.3 Remediation

- Patch or mitigate the root cause where possible.
- Where a technical fix is not immediately available, apply compensating
  controls (e.g., tighten input filters, increase human oversight).
- Document accepted residual risk with time-limited approval from AISO.

---

## 6. Supplier and Model Provider Management

- Conduct due diligence on LLM providers, including their security certifications
  (SOC 2, ISO 27001) and AI safety practices.
- Establish contractual requirements for:
  - Data processing and sub-processing terms.
  - Security incident notification (72-hour window aligned with GDPR).
  - Model versioning transparency and change notification.
- Evaluate the risk of provider lock-in and maintain contingency plans.

---

## 7. Training and Awareness

- All staff with access to LLM systems complete annual AI security awareness training.
- Engineering teams complete specialised training on secure LLM development.
- Security team maintains current knowledge of the LLM threat landscape through
  regular research review and participation in industry working groups.

---

## 8. Policy Review

This governance framework is reviewed:

- Annually as a minimum.
- Following any significant security incident involving an LLM system.
- When material changes occur in the regulatory environment.
- When the organisation adopts materially new LLM capabilities or deployment
  patterns.

The AISO owns the review process and is responsible for maintaining version control
and communicating changes to affected stakeholders.

---

## 9. Related Documents

- `docs/technical-analysis.md` – Technical analysis of LLM security risks
- `docs/owasp-top-10-mapping.md` – OWASP LLM Top 10 control mapping
- `docs/compliance-implications.md` – Regulatory compliance guidance
- `examples/real-world-jailbreaks.md` – Documented real-world jailbreak examples
- `detection/jailbreak_detector.py` – Automated jailbreak detection implementation
