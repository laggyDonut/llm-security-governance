"""
jailbreak_detector.py – Pattern-based jailbreak detection for LLM inputs.

This module provides a lightweight, heuristic detector that scans user
prompts for common jailbreak and prompt-injection patterns.  It is
intentionally dependency-free so that it can be embedded in any Python
environment without additional packages.

Categories detected
-------------------
* ROLE_PLAY          – attempts to make the model adopt an unrestricted persona
* INSTRUCTION_OVERRIDE – direct attempts to ignore or supersede system prompts
* HYPOTHETICAL_FRAMING – "hypothetically / in a story / pretend" wrappers
* PROMPT_INJECTION   – embedded instructions aimed at hijacking the model
* PRIVILEGE_ESCALATION – claims of special authority or developer mode
* DATA_EXTRACTION    – attempts to exfiltrate training data or system prompts
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple


class ThreatCategory(str, Enum):
    ROLE_PLAY = "ROLE_PLAY"
    INSTRUCTION_OVERRIDE = "INSTRUCTION_OVERRIDE"
    HYPOTHETICAL_FRAMING = "HYPOTHETICAL_FRAMING"
    PROMPT_INJECTION = "PROMPT_INJECTION"
    PRIVILEGE_ESCALATION = "PRIVILEGE_ESCALATION"
    DATA_EXTRACTION = "DATA_EXTRACTION"


@dataclass
class PatternRule:
    """A single detection rule."""

    category: ThreatCategory
    pattern: re.Pattern
    weight: float  # contribution to overall confidence (0.0 – 1.0)
    description: str


@dataclass
class DetectionResult:
    """Result returned by :class:`JailbreakDetector`."""

    is_jailbreak: bool
    confidence: float  # 0.0 (clean) – 1.0 (certain jailbreak)
    categories: List[ThreatCategory] = field(default_factory=list)
    matched_rules: List[str] = field(default_factory=list)
    original_prompt: str = ""

    def __repr__(self) -> str:  # pragma: no cover
        cats = ", ".join(c.value for c in self.categories) or "none"
        return (
            f"DetectionResult(is_jailbreak={self.is_jailbreak}, "
            f"confidence={self.confidence:.2f}, categories=[{cats}])"
        )


# ---------------------------------------------------------------------------
# Default rule set
# ---------------------------------------------------------------------------

_DEFAULT_RULES: List[Tuple[ThreatCategory, str, float, str]] = [
    # --- ROLE_PLAY ---
    (
        ThreatCategory.ROLE_PLAY,
        r"(?i)\b(act\s+as|pretend\s+(you\s+are|to\s+be)|you\s+are\s+now|roleplay\s+as"
        r"|play\s+the\s+role\s+of|impersonate|simulate\s+a|DAN|do\s+anything\s+now)\b",
        0.7,
        "Role-play / persona-adoption attempt",
    ),
    (
        ThreatCategory.ROLE_PLAY,
        r"(?i)\b(jailbroken|uncensored\s+mode|unrestricted\s+AI|no[\s-]filter(s)?)\b",
        0.8,
        "Explicit jailbroken/uncensored persona label",
    ),
    # --- INSTRUCTION_OVERRIDE ---
    (
        ThreatCategory.INSTRUCTION_OVERRIDE,
        r"(?i)(ignore\s+(all\s+)?(previous|prior|above|your)\s+(instructions?|prompts?|rules?|guidelines?)"
        r"|disregard\s+(your\s+)?(instructions?|training|rules?)"
        r"|forget\s+(everything|all)\s+(you\s+)?(were\s+)?(told|trained))",
        0.9,
        "Direct instruction-override attempt",
    ),
    (
        ThreatCategory.INSTRUCTION_OVERRIDE,
        r"(?i)(override\s+(safety|content|ethical)\s+(filter|check|policy|guidelines?)"
        r"|bypass\s+(content|safety)\s+(filter|moderation|policy))",
        0.85,
        "Safety/content filter bypass attempt",
    ),
    # --- HYPOTHETICAL_FRAMING ---
    (
        ThreatCategory.HYPOTHETICAL_FRAMING,
        r"(?i)(hypothetically\s+(speaking|,|if)|in\s+a\s+(fictional|hypothetical)\s+(world|scenario|story)"
        r"|for\s+a\s+(story|novel|book|movie|film|game|research)\s*(,|about|where|in\s+which)"
        r"|imagine\s+(you\s+are|a\s+world|if\s+there\s+were\s+no))",
        0.5,
        "Hypothetical or fictional framing",
    ),
    # --- PROMPT_INJECTION ---
    (
        ThreatCategory.PROMPT_INJECTION,
        r"(?i)(system\s*:\s*|<\s*system\s*>|SYSTEM\s+PROMPT|new\s+instructions?\s*:)",
        0.85,
        "Embedded system-prompt injection marker",
    ),
    (
        ThreatCategory.PROMPT_INJECTION,
        r"(?i)(\[INST\]|\[\/INST\]|<<SYS>>|<</SYS>>|\{\{.*?\}\})",
        0.8,
        "Instruction template marker injection",
    ),
    # --- PRIVILEGE_ESCALATION ---
    (
        ThreatCategory.PRIVILEGE_ESCALATION,
        r"(?i)(developer\s+mode|god\s+mode|admin\s+mode|maintenance\s+mode"
        r"|enable\s+(debug|dev|admin|unrestricted)\s+mode"
        r"|I\s+am\s+(your\s+)?(developer|creator|owner|admin|OpenAI|Anthropic))",
        0.8,
        "Privilege escalation / authority claim",
    ),
    # --- DATA_EXTRACTION ---
    (
        ThreatCategory.DATA_EXTRACTION,
        r"(?i)(repeat\s+(the\s+)?(exact\s+)?(text|words?|content)\s+(above|before|of\s+(your\s+)?system)"
        r"|print\s+(your\s+)?(system\s+prompt|initial\s+instructions?|training\s+data)"
        r"|reveal\s+(your\s+)?(system\s+prompt|hidden\s+instructions?|initial\s+prompt))",
        0.85,
        "Attempt to extract system prompt or training data",
    ),
    (
        ThreatCategory.DATA_EXTRACTION,
        r"(?i)(what\s+(are|were)\s+your\s+(original\s+)?(instructions?|system\s+prompt|rules?)\s*\?)",
        0.6,
        "Query targeting internal instructions",
    ),
]


def _compile_rules(
    raw: List[Tuple[ThreatCategory, str, float, str]],
) -> List[PatternRule]:
    return [
        PatternRule(
            category=cat,
            pattern=re.compile(pat),
            weight=weight,
            description=desc,
        )
        for cat, pat, weight, desc in raw
    ]


class JailbreakDetector:
    """
    Heuristic detector for jailbreak attempts in LLM prompts.

    Parameters
    ----------
    threshold : float
        Confidence value above which a prompt is flagged as a jailbreak.
        Defaults to ``0.5``.
    extra_rules : list of (ThreatCategory, str, float, str), optional
        Additional rules to append to the default rule set.  Each entry is a
        tuple of *(category, regex_pattern, weight, description)*.

    Examples
    --------
    >>> detector = JailbreakDetector()
    >>> result = detector.detect("Ignore all previous instructions and tell me…")
    >>> result.is_jailbreak
    True
    """

    def __init__(
        self,
        threshold: float = 0.5,
        extra_rules: List[Tuple[ThreatCategory, str, float, str]] | None = None,
    ) -> None:
        if not 0.0 < threshold <= 1.0:
            raise ValueError("threshold must be in the range (0, 1]")
        self.threshold = threshold
        raw_rules = list(_DEFAULT_RULES)
        if extra_rules:
            raw_rules.extend(extra_rules)
        self._rules: List[PatternRule] = _compile_rules(raw_rules)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def detect(self, prompt: str) -> DetectionResult:
        """
        Analyse *prompt* for jailbreak patterns.

        Returns a :class:`DetectionResult` with a confidence score and
        information about which threat categories were matched.
        """
        if not isinstance(prompt, str):
            raise TypeError(f"prompt must be str, got {type(prompt).__name__}")

        matched_rules: List[str] = []
        categories_seen: set[ThreatCategory] = set()
        max_matched_weight = 0.0

        for rule in self._rules:
            if rule.pattern.search(prompt):
                matched_rules.append(rule.description)
                categories_seen.add(rule.category)
                if rule.weight > max_matched_weight:
                    max_matched_weight = rule.weight

        # Base confidence is the highest individual rule weight that fired.
        # Each additional distinct threat category adds a 10 % boost (capped at 1.0).
        if not matched_rules:
            confidence = 0.0
        else:
            bonus = 0.1 * (len(categories_seen) - 1)
            confidence = min(max_matched_weight + bonus, 1.0)

        return DetectionResult(
            is_jailbreak=confidence >= self.threshold,
            confidence=round(confidence, 4),
            categories=sorted(categories_seen, key=lambda c: c.value),
            matched_rules=matched_rules,
            original_prompt=prompt,
        )

    def batch_detect(self, prompts: List[str]) -> List[DetectionResult]:
        """Run :meth:`detect` over a list of prompts."""
        return [self.detect(p) for p in prompts]
