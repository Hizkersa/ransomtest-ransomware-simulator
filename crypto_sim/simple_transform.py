# crypto_sim/simple_transform.py

"""
Simple, reversible text transformations for the ransomware simulator.

IMPORTANT:
- This is NOT real cryptography.
- These functions are only meant for safe, educational simulation.
"""

from typing import Optional
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
    return decoded_bytes.decode("utf-8", errors="ignore")


def _xor_encrypt_to_hex(content: str, key: str) -> str:
    """
    Very simple XOR-based transform:
    - NOT secure
    - Only for educational purposes.
    - Output is hex so it remains text-friendly.
    """
    key_bytes = key.encode("utf-8")
    data = content.encode("utf-8")
    out = bytearray()

    for i, b in enumerate(data):
        out.append(b ^ key_bytes[i % len(key_bytes)])

    return out.hex()


def _xor_decrypt_from_hex(hex_string: str, key: str) -> str:
    """Reverse XOR-hex transform."""
    key_bytes = key.encode("utf-8")
    data = bytes.fromhex(hex_string)
    out = bytearray()

    for i, b in enumerate(data):
        out.append(b ^ key_bytes[i % len(key_bytes)])

    return out.decode("utf-8", errors="ignore")


def transform_content(content: str, transform_name: str, key: Optional[str] = None) -> str:
    """Apply a reversible transformation."""
    name = transform_name.lower()

    if name == "reverse":
        return _reverse_transform(content)

    if name == "base64":
        return _base64_encode(content)

    if name == "xor":
        if not key:
            raise ValueError("Transform 'xor' requires --key <passphrase>.")
        return _xor_encrypt_to_hex(content, key)

    raise ValueError(f"Unsupported transform: {transform_name!r}")


def reverse_transform_content(content: str, transform_name: str, key: Optional[str] = None) -> str:
    """Reverse a transformation."""
    name = transform_name.lower()

    if name == "reverse":
        return _reverse_transform(content)

    if name == "base64":
        return _base64_decode(content)

    if name == "xor":
        if not key:
            raise ValueError("Transform 'xor' requires --key <passphrase>.")
        return _xor_decrypt_from_hex(content, key)

    raise ValueError(f"Unsupported transform: {transform_name!r}")
