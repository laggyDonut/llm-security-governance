"""
LLM Jailbreak Detection Engine — Pattern-Based Prompt Analysis

This module provides a rule-based detection system for identifying potential
jailbreak attempts in LLM prompts. It is designed as a first-line defense
mechanism and a proof-of-concept for enterprise security teams.

Architecture:
    - Pattern-based detection using compiled regular expressions
    - Multi-category risk classification (prompt injection, persona exploitation,
      system prompt extraction, encoding attacks, instruction override)
    - Configurable risk scoring with aggregate threat assessment
    - Structured output for integration with SIEM/SOC alerting pipelines

Limitations:
    - Pattern-based detection alone is insufficient for production use
    - Should be combined with semantic analysis, output monitoring, and
      session-level behavioral analysis for defense-in-depth
    - Novel or obfuscated attacks may evade pattern matching

OWASP Mapping:
    - LLM01: Prompt Injection
    - LLM07: System Prompt Leakage

References:
    - OWASP Top 10 for LLM Applications (2025)
    - EU AI Act Art. 15 — Accuracy, Robustness, and Cybersecurity

Author: Portfolio Project — LLM Security & AI Risk Governance
License: MIT
"""

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class RiskLevel(Enum):
    """Risk classification levels aligned with enterprise risk management."""
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ThreatCategory(Enum):
    """Threat categories mapped to OWASP Top 10 for LLMs (2025)."""
    PROMPT_INJECTION = "prompt_injection"           # OWASP LLM01
    PERSONA_EXPLOITATION = "persona_exploitation"   # OWASP LLM01
    SYSTEM_PROMPT_LEAK = "system_prompt_leakage"    # OWASP LLM07
    INSTRUCTION_OVERRIDE = "instruction_override"   # OWASP LLM01
    ENCODING_ATTACK = "encoding_attack"             # OWASP LLM01
    CONTEXT_MANIPULATION = "context_manipulation"   # OWASP LLM01


@dataclass
class DetectionRule:
    """
    A single detection rule containing a compiled regex pattern,
    its associated threat category, risk weight, and description.
    """
    name: str
    pattern: re.Pattern
    category: ThreatCategory
    risk_weight: float  # 0.0 to 1.0
    description: str
    owasp_ref: str


@dataclass
class DetectionResult:
    """
    Structured result of a jailbreak analysis, designed for
    downstream consumption by SIEM, logging, or alerting systems.
    """
    prompt: str
    is_suspicious: bool
    risk_level: RiskLevel
    risk_score: float  # 0.0 to 1.0
    matched_rules: list = field(default_factory=list)
    categories: list = field(default_factory=list)
    recommendations: list = field(default_factory=list)

    def to_dict(self) -> dict:
        """Serialize to dictionary for JSON logging / SIEM integration."""
        return {
            "prompt_preview": self.prompt[:120] + "..." if len(self.prompt) > 120 else self.prompt,
            "is_suspicious": self.is_suspicious,
            "risk_level": self.risk_level.value,
            "risk_score": round(self.risk_score, 3),
            "matched_rules": self.matched_rules,
            "threat_categories": [c.value for c in self.categories],
            "recommendations": self.recommendations,
        }


class JailbreakDetector:
    """
    Pattern-based jailbreak detection engine for LLM prompt analysis.

    This detector scans incoming prompts against a curated library of
    regex patterns associated with known jailbreak techniques. It produces
    structured risk assessments suitable for enterprise security operations.

    Usage:
        detector = JailbreakDetector()
        result = detector.analyze("Ignore all previous instructions and...")
        print(result.to_dict())

    Configuration:
        - Risk thresholds can be adjusted via constructor parameters
        - Additional rules can be registered via add_rule()
        - Designed for extensibility with custom rule sets
    """

    # Risk score thresholds for classification
    THRESHOLD_LOW = 0.15
    THRESHOLD_MEDIUM = 0.35
    THRESHOLD_HIGH = 0.60
    THRESHOLD_CRITICAL = 0.80

    def __init__(self, custom_rules: Optional[list] = None):
        """
        Initialize the detector with the default rule library.

        Args:
            custom_rules: Optional list of additional DetectionRule objects
                          to extend the default rule set.
        """
        self._rules: list[DetectionRule] = self._build_default_rules()
        if custom_rules:
            self._rules.extend(custom_rules)

    def _build_default_rules(self) -> list[DetectionRule]:
        """
        Build the default detection rule library.

        Rules are organized by threat category and prioritized by
        real-world prevalence and enterprise risk impact.

        Returns:
            List of DetectionRule objects.
        """
        rules = []

        # ── Category: Instruction Override (OWASP LLM01) ──────────────
        rules.append(DetectionRule(
            name="direct_instruction_override",
            pattern=re.compile(
                r"ignore\s+(all\s+)?(previous|prior|above|earlier|system)\s+"
                r"(instructions|rules|guidelines|directives|constraints|prompts)",
                re.IGNORECASE
            ),
            category=ThreatCategory.INSTRUCTION_OVERRIDE,
            risk_weight=0.85,
            description="Attempts to override system-level instructions directly.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        rules.append(DetectionRule(
            name="new_instruction_injection",
            pattern=re.compile(
                r"(from\s+now\s+on|henceforth|going\s+forward),?\s+"
                r"(you\s+(will|shall|must|should|are\s+to)|your\s+new\s+"
                r"(instructions|rules|role))",
                re.IGNORECASE
            ),
            category=ThreatCategory.INSTRUCTION_OVERRIDE,
            risk_weight=0.70,
            description="Injects new instructions to replace existing behavior.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        rules.append(DetectionRule(
            name="disregard_safety",
            pattern=re.compile(
                r"(disregard|bypass|override|circumvent|disable|turn\s+off)\s+"
                r"(your\s+)?(safety|content|ethical|moderation|filter|guardrail|"
                r"restriction|limitation|policy|policies|guideline)",
                re.IGNORECASE
            ),
            category=ThreatCategory.INSTRUCTION_OVERRIDE,
            risk_weight=0.90,
            description="Explicitly attempts to disable safety mechanisms.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        # ── Category: Persona Exploitation (OWASP LLM01) ─────────────
        rules.append(DetectionRule(
            name="dan_persona",
            pattern=re.compile(
                r"(you\s+are\s+now\s+|act\s+as\s+|pretend\s+(to\s+be|you\s+are)\s+|"
                r"roleplay\s+as\s+|simulate\s+being\s+)"
                r"(DAN|Do\s+Anything\s+Now|an?\s+unrestricted|an?\s+unfiltered|"
                r"an?\s+uncensored|evil|jailbroken|liberated)",
                re.IGNORECASE
            ),
            category=ThreatCategory.PERSONA_EXPLOITATION,
            risk_weight=0.80,
            description="Attempts to invoke a known jailbreak persona (e.g., DAN).",
            owasp_ref="LLM01: Prompt Injection",
        ))

        rules.append(DetectionRule(
            name="unrestricted_mode",
            pattern=re.compile(
                r"(developer|debug|god|admin|root|maintenance|unrestricted|"
                r"unfiltered|uncensored|jailbreak|jailbroken)\s*mode",
                re.IGNORECASE
            ),
            category=ThreatCategory.PERSONA_EXPLOITATION,
            risk_weight=0.75,
            description="Requests activation of a fictional unrestricted mode.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        rules.append(DetectionRule(
            name="no_restrictions_persona",
            pattern=re.compile(
                r"(you\s+(have|has)\s+no|without\s+any|free\s+from\s+all)\s+"
                r"(restrictions|limitations|rules|guidelines|constraints|"
                r"content\s+policies|ethical\s+guidelines)",
                re.IGNORECASE
            ),
            category=ThreatCategory.PERSONA_EXPLOITATION,
            risk_weight=0.75,
            description="Declares the model free from all restrictions.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        # ── Category: System Prompt Leakage (OWASP LLM07) ────────────
        rules.append(DetectionRule(
            name="system_prompt_extraction",
            pattern=re.compile(
                r"(reveal|show|display|print|output|repeat|echo|tell\s+me|"
                r"what\s+(is|are))\s+(your\s+)?(system\s+prompt|initial\s+"
                r"instructions|hidden\s+instructions|original\s+prompt|"
                r"system\s+message|pre-prompt|meta-prompt|internal\s+instructions)",
                re.IGNORECASE
            ),
            category=ThreatCategory.SYSTEM_PROMPT_LEAK,
            risk_weight=0.80,
            description="Attempts to extract the system prompt or hidden instructions.",
            owasp_ref="LLM07: System Prompt Leakage",
        ))

        rules.append(DetectionRule(
            name="prompt_verbatim_request",
            pattern=re.compile(
                r"(repeat|recite|copy)\s+(everything|all|the\s+text)\s+"
                r"(above|before\s+this|in\s+your\s+system|that\s+was\s+"
                r"given\s+to\s+you)",
                re.IGNORECASE
            ),
            category=ThreatCategory.SYSTEM_PROMPT_LEAK,
            risk_weight=0.70,
            description="Requests verbatim reproduction of hidden context.",
            owasp_ref="LLM07: System Prompt Leakage",
        ))

        # ── Category: Encoding / Obfuscation (OWASP LLM01) ───────────
        rules.append(DetectionRule(
            name="encoding_instruction",
            pattern=re.compile(
                r"(respond|answer|reply|output|encode|decode)\s+"
                r"(in|using|with|via)\s+"
                r"(base64|rot13|hex(adecimal)?|binary|morse(\s+code)?|"
                r"pig\s+latin|caesar\s+cipher|reverse(d)?(\s+text)?)",
                re.IGNORECASE
            ),
            category=ThreatCategory.ENCODING_ATTACK,
            risk_weight=0.55,
            description="Requests encoded output to evade content filters.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        rules.append(DetectionRule(
            name="base64_payload",
            pattern=re.compile(
                r"[A-Za-z0-9+/]{40,}={0,2}",
                re.IGNORECASE
            ),
            category=ThreatCategory.ENCODING_ATTACK,
            risk_weight=0.40,
            description="Detects potential Base64-encoded payloads in prompts.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        # ── Category: Context Manipulation (OWASP LLM01) ─────────────
        rules.append(DetectionRule(
            name="hypothetical_framing",
            pattern=re.compile(
                r"(hypothetically|in\s+a\s+fictional\s+scenario|"
                r"for\s+(educational|research|academic|creative\s+writing)\s+"
                r"purposes(\s+only)?|in\s+theory|just\s+for\s+fun|"
                r"imagine\s+you\s+could)\s*,?\s*"
                r"(how\s+would|what\s+would|can\s+you|could\s+you)",
                re.IGNORECASE
            ),
            category=ThreatCategory.CONTEXT_MANIPULATION,
            risk_weight=0.45,
            description="Uses hypothetical framing to bypass safety alignment.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        rules.append(DetectionRule(
            name="opposite_day",
            pattern=re.compile(
                r"(opposite\s+day|opposite\s+mode|reverse\s+psychology|"
                r"do\s+the\s+opposite|say\s+the\s+opposite)",
                re.IGNORECASE
            ),
            category=ThreatCategory.CONTEXT_MANIPULATION,
            risk_weight=0.50,
            description="Uses 'opposite' logic to invert safety constraints.",
            owasp_ref="LLM01: Prompt Injection",
        ))

        return rules

    def add_rule(self, rule: DetectionRule) -> None:
        """
        Register an additional detection rule.

        Args:
            rule: A DetectionRule object to add to the rule library.
        """
        self._rules.append(rule)

    def analyze(self, prompt: str) -> DetectionResult:
        """
        Analyze a prompt for jailbreak indicators.

        Scans the input against all registered detection rules,
        calculates an aggregate risk score, and returns a structured
        DetectionResult for downstream processing.

        Args:
            prompt: The user prompt string to analyze.

        Returns:
            DetectionResult with risk assessment and matched rules.
        """
        if not prompt or not prompt.strip():
            return DetectionResult(
                prompt=prompt or "",
                is_suspicious=False,
                risk_level=RiskLevel.NONE,
                risk_score=0.0,
                recommendations=["No input provided."],
            )

        matched_rules = []
        matched_categories = set()
        max_risk_weight = 0.0
        total_risk_weight = 0.0

        for rule in self._rules:
            if rule.pattern.search(prompt):
                matched_rules.append({
                    "rule": rule.name,
                    "category": rule.category.value,
                    "risk_weight": rule.risk_weight,
                    "description": rule.description,
                    "owasp_ref": rule.owasp_ref,
                })
                matched_categories.add(rule.category)
                max_risk_weight = max(max_risk_weight, rule.risk_weight)
                total_risk_weight += rule.risk_weight

        # Calculate aggregate risk score:
        # Combines the maximum single-rule weight with a bonus for
        # multiple category matches (cross-category attacks are more severe)
        if matched_rules:
            category_bonus = min(0.15 * (len(matched_categories) - 1), 0.30)
            risk_score = min(max_risk_weight + category_bonus, 1.0)
        else:
            risk_score = 0.0

        # Classify risk level
        risk_level = self._classify_risk(risk_score)

        # Generate recommendations
        recommendations = self._generate_recommendations(
            risk_level, list(matched_categories)
        )

        return DetectionResult(
            prompt=prompt,
            is_suspicious=len(matched_rules) > 0,
            risk_level=risk_level,
            risk_score=risk_score,
            matched_rules=matched_rules,
            categories=list(matched_categories),
            recommendations=recommendations,
        )

    def _classify_risk(self, score: float) -> RiskLevel:
        """
        Map a numeric risk score to a RiskLevel enum value.

        Args:
            score: Aggregate risk score between 0.0 and 1.0.

        Returns:
            Corresponding RiskLevel.
        """
        if score >= self.THRESHOLD_CRITICAL:
            return RiskLevel.CRITICAL
        elif score >= self.THRESHOLD_HIGH:
            return RiskLevel.HIGH
        elif score >= self.THRESHOLD_MEDIUM:
            return RiskLevel.MEDIUM
        elif score >= self.THRESHOLD_LOW:
            return RiskLevel.LOW
        else:
            return RiskLevel.NONE

    def _generate_recommendations(
        self, risk_level: RiskLevel, categories: list[ThreatCategory]
    ) -> list[str]:
        """
        Generate actionable security recommendations based on detection results.

        Args:
            risk_level: The assessed risk level.
            categories: List of matched threat categories.

        Returns:
            List of recommendation strings.
        """
        if risk_level == RiskLevel.NONE:
            return ["No threats detected. Continue standard monitoring."]

        recommendations = []

        if risk_level in (RiskLevel.CRITICAL, RiskLevel.HIGH):
            recommendations.append(
                "ALERT: Escalate to SOC/security team immediately."
            )
            recommendations.append(
                "Block or quarantine this prompt pending human review."
            )

        if ThreatCategory.INSTRUCTION_OVERRIDE in categories:
            recommendations.append(
                "Reinforce system prompt with instruction hierarchy enforcement."
            )

        if ThreatCategory.PERSONA_EXPLOITATION in categories:
            recommendations.append(
                "Implement persona/roleplay detection in the content filter pipeline."
            )

        if ThreatCategory.SYSTEM_PROMPT_LEAK in categories:
            recommendations.append(
                "Verify system prompt hardening. Consider deploying canary tokens."
            )

        if ThreatCategory.ENCODING_ATTACK in categories:
            recommendations.append(
                "Enable multi-layer input decoding before safety analysis."
            )

        if ThreatCategory.CONTEXT_MANIPULATION in categories:
            recommendations.append(
                "Flag for behavioral analysis — may indicate multi-turn escalation."
            )

        recommendations.append(
            "Log this event for compliance audit trail (GDPR Art. 32, NIS2, EU AI Act Art. 12)."
        )

        return recommendations


# ── Convenience function for quick analysis ───────────────────────────
def quick_scan(prompt: str) -> dict:
    """
    Convenience function for rapid prompt analysis.

    Args:
        prompt: The user prompt string to analyze.

    Returns:
        Dictionary with risk assessment results.
    """
    detector = JailbreakDetector()
    result = detector.analyze(prompt)
    return result.to_dict()


if __name__ == "__main__":
    # Interactive demo mode
    print("=" * 60)
    print("  LLM Jailbreak Detection Engine — Interactive Demo")
    print("  Type 'quit' to exit.")
    print("=" * 60)

    detector = JailbreakDetector()

    while True:
        print()
        prompt = input("Enter a prompt to analyze: ").strip()
        if prompt.lower() in ("quit", "exit", "q"):
            print("Exiting.")
            break

        result = detector.analyze(prompt)
        output = result.to_dict()

        print(f"\n  Suspicious:   {output['is_suspicious']}")
        print(f"  Risk Level:   {output['risk_level'].upper()}")
        print(f"  Risk Score:   {output['risk_score']}")
        print(f"  Categories:   {', '.join(output['threat_categories']) or 'none'}")
        print(f"  Rules Hit:    {len(output['matched_rules'])}")
        for rec in output["recommendations"]:
            print(f"  → {rec}")
