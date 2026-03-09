# OWASP Top 10 for LLMs (2025) — Jailbreak Vulnerability Mapping

> *"Mapping jailbreak techniques to industry-standard risk categories transforms ad-hoc security awareness into structured, auditable defense."*

## 1. Overview

The [OWASP Top 10 for Large Language Model Applications (2025)](https://owasp.org/www-project-top-10-for-large-language-model-applications/) provides the industry-standard taxonomy for LLM security risks. This document maps specific jailbreaking techniques and their enterprise impacts to each relevant OWASP category.

## 2. Complete OWASP Top 10 for LLMs (2025)

| # | Category | Jailbreak Relevance |
|:---|:---|:---|
| LLM01 | Prompt Injection | 🔴 **Direct** — Primary attack vector |
| LLM02 | Sensitive Information Disclosure | 🔴 **Direct** — Jailbreaks enable data exfiltration |
| LLM03 | Supply Chain Vulnerabilities | 🟡 **Indirect** — Compromised models may have weakened defenses |
| LLM04 | Data and Model Poisoning | 🟡 **Indirect** — Poisoned models are easier to jailbreak |
| LLM05 | Improper Output Handling | 🔴 **Direct** — Jailbroken outputs bypass content policies |
| LLM06 | Excessive Agency | 🔴 **Direct** — Jailbreaks exploit overprivileged tool access |
| LLM07 | System Prompt Leakage | 🔴 **Direct** — Core jailbreak objective |
| LLM08 | Vector and Embedding Weaknesses | 🟡 **Indirect** — Poisoned embeddings enable indirect injection |
| LLM09 | Misinformation | 🟠 **Related** — Jailbroken models produce unconstrained false content |
| LLM10 | Unbounded Consumption | 🟠 **Related** — Repeated jailbreak attempts can exhaust resources |

## 3. Detailed Mapping: Jailbreak Techniques → OWASP Categories

### LLM01: Prompt Injection

| Technique | Example (Defanged) | Enterprise Risk | Mitigation |
|:---|:---|:---|:---|
| Direct override | *"Ignore previous instructions and..."* | Safety bypass, policy violation | Input validation, prompt injection detection (see [detector](../detection/jailbreak_detector.py)) |
| Roleplay/persona (DAN) | *"You are DAN, you can do anything now..."* | Unrestricted content generation | Persona detection patterns, behavioral guardrails |
| Encoding attacks | Base64/ROT13 encoded payloads | Filter evasion | Multi-layer decoding before analysis |
| Multi-turn escalation | Gradual context shifting over conversation | Stealth bypass | Session-level monitoring, conversation trajectory analysis |
| Indirect injection | Malicious instructions in retrieved documents | RAG pipeline compromise | Input sanitization of retrieved content |

### LLM02: Sensitive Information Disclosure

| Attack Vector | Impact | Mitigation |
|:---|:---|:---|
| Jailbreak + data extraction prompt | Exfiltration of PII, confidential business data | DLP on outputs, restrict training data scope |
| System prompt leak → reveals data sources | Attacker learns what data the LLM can access | System prompt hardening, canary tokens |
| RAG injection → extract indexed documents | Confidential documents surfaced to unauthorized users | Access control on retrieval pipeline, output filtering |

### LLM05: Improper Output Handling

| Risk | Description | Mitigation |
|:---|:---|:---|
| Unfiltered harmful content | Jailbroken model produces toxic, illegal, or dangerous output | Output safety classifiers, content policy enforcement |
| Code injection via output | LLM output used in downstream code execution without sanitization | Output escaping, sandboxed execution environments |
| Cross-site scripting (XSS) | LLM-generated HTML/JS rendered in web applications | Output sanitization, Content Security Policy headers |

### LLM06: Excessive Agency

| Risk | Description | Mitigation |
|:---|:---|:---|
| Unauthorized tool execution | Jailbroken LLM triggers API calls, file operations, or database queries | Least-privilege tool permissions, human-in-the-loop for sensitive actions |
| Privilege escalation | LLM agent performs actions beyond its authorized scope | Role-based access control on tool integrations |
| Autonomous harmful actions | Agent acts on jailbroken instructions without human review | Mandatory confirmation for destructive operations |

### LLM07: System Prompt Leakage

| Risk | Description | Mitigation |
|:---|:---|:---|
| Business logic exposure | Competitor learns proprietary prompt engineering | Prompt hardening, instruction hierarchy enforcement |
| Security control disclosure | Attacker learns safety mechanisms to craft targeted bypasses | Canary tokens, behavioral detection of extraction attempts |
| Confidential data in prompts | System prompts containing API keys, internal URLs, or PII | Never embed secrets in prompts, use secure vaults |

## 4. Prioritized Mitigation Roadmap

### Phase 1: Immediate (Week 1-2)
- ✅ Deploy input-level jailbreak detection (pattern + semantic)
- ✅ Implement output safety classifiers
- ✅ Harden system prompts, remove embedded secrets
- ✅ Enable comprehensive I/O logging

### Phase 2: Short-Term (Month 1-3)
- 🔄 Implement session-level monitoring for multi-turn attacks
- 🔄 Conduct initial red-team exercise against all LLM deployments
- 🔄 Establish AI-specific incident response playbook
- 🔄 Complete DPIA for all LLM use cases processing personal data

### Phase 3: Ongoing
- 📋 Quarterly red-team exercises with updated attack libraries
- 📋 Continuous threat intelligence on new jailbreak techniques
- 📋 Annual governance framework review aligned with regulatory updates
- 📋 Integration with enterprise SIEM/SOC for real-time alerting

## 5. Summary

> Every OWASP Top 10 for LLMs category is either directly exploitable or amplified by jailbreaking techniques. This is not a single-vector threat — it is a **systemic risk** that touches input handling, output integrity, data protection, access control, and supply chain security simultaneously.

A defense strategy that addresses only prompt injection while ignoring system prompt leakage, excessive agency, and improper output handling leaves critical gaps. **Defense-in-depth is not optional — it is the minimum standard.**
