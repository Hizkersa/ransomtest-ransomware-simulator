# crypto_sim/simple_transform.py

"""
Simple, reversible text transformations for the ransomware simulator.

IMPORTANT:
- This is NOT real cryptography.
- These functions are only meant for safe, educational simulation.
"""

from typing import Callable
import base64


def _reverse_transform(content: str) -> str:
    """Very simple reversible transform: reverses the entire string."""
    return content[::-1]


def _base64_encode(content: str) -> str:
    """Encode content using Base64."""
    encoded_bytes = base64.b64encode(content.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def _base64_decode(content: str) -> str:
    """Decode previously Base64 encoded content."""
    decoded_bytes = base64.b64decode(content.encode("utf-8"))
    return decoded_bytes.decode("utf-8")


# Registry of available transforms with encoder + decoder support
_TRANSFORMS: dict[str, dict[str, Callable[[str], str]]] = {
    "reverse": {
        "encoder": _reverse_transform,
        "decoder": _reverse_transform,  # reverse again
    },
    "base64": {
        "encoder": _base64_encode,
        "decoder": _base64_decode,
    },
}


def transform_content(content: str, transform_name: str) -> str:
    """Apply reversible transformation."""
    try:
        return _TRANSFORMS[transform_name]["encoder"](content)
    except KeyError:
        raise ValueError(f"Unsupported transform: {transform_name!r}")


def reverse_transform_content(content: str, transform_name: str) -> str:
    """Reverse transformation."""
    try:
        return _TRANSFORMS[transform_name]["decoder"](content)
    except KeyError:
        raise ValueError(f"Unsupported transform: {transform_name!r}")