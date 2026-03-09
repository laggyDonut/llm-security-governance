# OWASP Top 10 for LLM Applications – Control Mapping

This document maps each vulnerability in the
[OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
to the detective and preventive controls implemented or recommended in this
repository.

---

## LLM01 – Prompt Injection

**Description:** An attacker manipulates an LLM through crafted inputs, causing
it to execute unintended instructions or bypass safety controls.  Includes both
direct injection (user input) and indirect injection (external data sources).

| Control Layer | Implementation |
|---------------|---------------|
| Detection | `JailbreakDetector` pattern categories: `INSTRUCTION_OVERRIDE`, `PROMPT_INJECTION` |
| Prevention | System prompt hardening; structural separation of instructions and user content |
| Monitoring | Audit logging of all inputs; real-time alerting on high-confidence detections |
| Governance | Threat modelling (PRE-01), red-team testing (PRE-03) |

**Residual Risk:** Indirect injection via retrieved documents is harder to
detect without semantic analysis of retrieved content.

---

## LLM02 – Insecure Output Handling

**Description:** Insufficient validation of LLM-generated content before it is
passed to downstream components (e.g., code interpreters, browsers, databases)
can lead to cross-site scripting (XSS), SQL injection, or remote code execution.

| Control Layer | Implementation |
|---------------|---------------|
| Prevention | Output content scanning (OPS-03); never pass raw LLM output directly to interpreters |
| Architecture | Treat LLM output as untrusted user input for all downstream systems |
| Testing | Include output-injection cases in pre-deployment red-team exercises (PRE-03) |

---

## LLM03 – Training Data Poisoning

**Description:** Adversarial manipulation of training data can introduce
backdoors or biases that influence model behaviour at inference time.

| Control Layer | Implementation |
|---------------|---------------|
| Prevention | Supply chain review of training datasets (PRE-06); provenance tracking |
| Detection | Behavioural anomaly testing post-training |
| Governance | Model provider due diligence (Section 6, Governance Framework) |

---

## LLM04 – Model Denial of Service

**Description:** Attackers craft inputs that consume excessive computational
resources, degrading service availability or incurring unsustainable costs.

| Control Layer | Implementation |
|---------------|---------------|
| Prevention | Rate limiting and abuse prevention (OPS-06) |
| Detection | Monitoring for unusual token consumption or latency spikes (MON-01) |
| Architecture | Input length limits; timeout controls on inference requests |

---

## LLM05 – Supply Chain Vulnerabilities

**Description:** LLM pipelines depend on third-party components (model weights,
plugins, data connectors) that may be tampered with or compromised.

| Control Layer | Implementation |
|---------------|---------------|
| Prevention | Supply chain review (PRE-06); verify model weight integrity via checksums |
| Governance | Supplier management programme (Section 6, Governance Framework) |
| Monitoring | Alerting on unexpected model or plugin version changes |

---

## LLM06 – Sensitive Information Disclosure

**Description:** LLMs may inadvertently reveal sensitive data from their
training corpus, system prompts, or conversation context.

| Control Layer | Implementation |
|---------------|---------------|
| Detection | `JailbreakDetector` category: `DATA_EXTRACTION` |
| Prevention | Do not embed secrets in system prompts; use runtime secret retrieval |
| Output controls | Scan responses for PII and confidential patterns (OPS-03) |
| Governance | Data minimisation and retention controls (OPS-08); DPIA (PRE-05) |

---

## LLM07 – Insecure Plugin Design

**Description:** Plugins and tool integrations that lack proper access control
or input validation can be weaponised by an injected prompt to take
unauthorised actions.

| Control Layer | Implementation |
|---------------|---------------|
| Architecture | Least-privilege tool access (OPS-04) |
| Prevention | Validate all plugin inputs independently of the LLM's instructions |
| Governance | Require human confirmation for irreversible or high-impact actions (OPS-05) |

---

## LLM08 – Excessive Agency

**Description:** An LLM agent granted broad permissions or capabilities may
take harmful actions when manipulated through prompt injection or when its
reasoning produces unexpected behaviour.

| Control Layer | Implementation |
|---------------|---------------|
| Architecture | Scope tool permissions to the minimum required for the specific use case (OPS-04) |
| Prevention | Human-in-the-loop gates for consequential actions (OPS-05) |
| Testing | Include agency-abuse scenarios in red-team exercises (PRE-03) |
| Governance | Risk classification requiring Critical-level controls for autonomous agents |

---

## LLM09 – Overreliance

**Description:** Placing excessive trust in LLM outputs without sufficient
human oversight can lead to harmful decisions based on inaccurate, biased,
or fabricated information.

| Control Layer | Implementation |
|---------------|---------------|
| Process | Output validation and human review requirements defined by risk level |
| Training | AI security and limitations awareness for all end users (Section 7, Governance Framework) |
| Architecture | Surface model uncertainty / confidence signals to users |

---

## LLM10 – Model Theft

**Description:** Adversaries extract proprietary model weights, architecture
details, or training data through repeated queries, enabling them to replicate
the model without authorisation.

| Control Layer | Implementation |
|---------------|---------------|
| Prevention | Rate limiting (OPS-06); anomaly detection on systematic querying patterns (MON-01) |
| Legal | Terms of service enforcement; contractual restrictions on systematic querying |
| Monitoring | Alerting on statistically unusual query volumes or patterns (MON-01) |

---

## Summary Matrix

| OWASP ID | Primary Detector Category | Governance Control | Operational Control |
|----------|--------------------------|-------------------|---------------------|
| LLM01 | `INSTRUCTION_OVERRIDE`, `PROMPT_INJECTION` | PRE-01, PRE-03 | OPS-01, OPS-02 |
| LLM02 | *(output-side)* | PRE-03 | OPS-03 |
| LLM03 | *(training-side)* | PRE-06 | – |
| LLM04 | *(resource-side)* | – | OPS-06, MON-01 |
| LLM05 | *(supply chain)* | PRE-06 | MON-01 |
| LLM06 | `DATA_EXTRACTION` | PRE-05 | OPS-03, OPS-08 |
| LLM07 | `PROMPT_INJECTION` | – | OPS-04, OPS-05 |
| LLM08 | `PRIVILEGE_ESCALATION` | PRE-03 | OPS-04, OPS-05 |
| LLM09 | – | – | OPS-05 |
| LLM10 | – | – | OPS-06, MON-01 |

---

## References

- [OWASP Top 10 for LLM Applications (2023)](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP Top 10 for LLM Applications (2025 candidate)](https://genai.owasp.org)
- `docs/governance-framework.md` – full control catalogue
- `docs/technical-analysis.md` – technical background on each attack class
