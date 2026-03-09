"""
detection package for LLM Security Governance.

This package provides tools for detecting jailbreak attempts and other
adversarial inputs targeting Large Language Models.
"""

from .jailbreak_detector import JailbreakDetector, DetectionResult

__all__ = ["JailbreakDetector", "DetectionResult"]
