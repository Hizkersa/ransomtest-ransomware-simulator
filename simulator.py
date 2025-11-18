#!/usr/bin/env python3
"""
ransomtest - Safe ransomware simulator (educational & sandboxed).

- Only operates inside a sandbox directory (default: lab_files/).
- Does NOT modify or delete original files by default.
- Uses simple, reversible text transforms (NOT real cryptography).
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime, timezone
import hashlib

from crypto_sim.simple_transform import transform_content, reverse_transform_content


TEXT_EXTENSIONS = {".txt", ".log", ".md", ".csv"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="ransomtest - safe ransomware simulator (educational only)."
    )

    parser.add_argument(
        "--mode",
        required=True,
        choices=["encrypt", "restore"],
        help="Operation mode: encrypt (simulate encryption) or restore (simulate decryption).",
    )

    parser.add_argument(
        "--target-dir",
        default="lab_files",
        help="Directory containing original lab files (sandbox). Used in encrypt mode.",
    )

    parser.add_argument(
        "--encrypted-dir",
        default="encrypted_files",
        help="Directory to store simulated encrypted files (.simenc).",
    )

    parser.add_argument(
        "--restored-dir",
        default="restored_files",
        help="Directory to store restored files in restore mode.",
    )

    parser.add_argument(
        "--reports-dir",
        default="reports",
        help="Directory to store simulation logs.",
    )

    parser.add_argument(
        "--transform",
        default="reverse",
        help="Name of the simple reversible transform to use (reverse, base64, xor).",
    )

    parser.add_argument(
        "--key",
        help="Optional key/passphrase for transforms that require it (xor).",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without writing any files.",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed output during execution.",
    )

    parser.add_argument(
        "--overwrite-original",
        action="store_true",
        help="WARNING: Overwrite original files in lab_files/ with transformed content.",
    )

    parser.add_argument(
        "--log-format",
        choices=["text", "json"],
        default="text",
        help="Logging format: text (default) or json.",
    )

    return parser.parse_args()


def sha256_of_text(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def log_line(reports_dir: Path, message: str, json_mode: bool = False, **fields) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    log_file = reports_dir / "simulation_log.txt"
    timestamp = datetime.now(timezone.utc).isoformat()

    if json_mode:
        import json
        fields["timestamp"] = timestamp
        fields["message"] = message
        line = json.dumps(fields)
    else:
        line = f"{timestamp} | {message}"

    with log_file.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def verbose_print(enabled: bool, message: str) -> None:
    if enabled:
        print(message)


def simulate_encrypt(
    target_dir: Path,
    encrypted_dir: Path,
    reports_dir: Path,
    transform_name: str,
    key: str | None,
    dry_run: bool,
    verbose: bool,
    overwrite_original: bool,
    log_format: str,
) -> None:

    json_mode = log_format == "json"

    if not target_dir.is_dir():
        print(f"[ERROR] Target directory does not exist: {target_dir}")
        sys.exit(1)

    verbose_print(verbose, f"[INFO] Starting ENCRYPT simulation on {target_dir}")
    encrypted_dir.mkdir(parents=True, exist_ok=True)

    for path in target_dir.rglob("*"):
        if not path.is_file():
            continue

        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        rel = path.relative_to(target_dir)
        enc_path = encrypted_dir / (str(rel) + ".simenc")
        enc_path.parent.mkdir(parents=True, exist_ok=True)

        verbose_print(verbose, f"[PROCESS] {path} -> {enc_path}")

        try:
            original = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            continue

        orig_hash = sha256_of_text(original)

        transformed = transform_content(original, transform_name, key=key)
        enc_hash = sha256_of_text(transformed)

        if not dry_run:
            enc_path.write_text(transformed, encoding="utf-8")

        log_line(
            reports_dir,
            "ENCRYPT",
            json_mode=json_mode,
            src=str(path),
            dst=str(enc_path),
            transform=transform_name,
            orig_sha256=orig_hash,
            enc_sha256=enc_hash,
            dry_run=dry_run,
        )

        if overwrite_original and not dry_run:
            path.write_text(transformed, encoding="utf-8")

    ransom_note = target_dir / "README_RECOVER.txt"
    ransom_note.write_text(
        "=== RANSOMTEST EDUCATIONAL NOTE ===\n\n"
        "Your files have been SIMULATED as encrypted...\n"
        "This tool is for training purposes ONLY.",
        encoding="utf-8",
    )

    verbose_print(verbose, "[INFO] ENCRYPT completed.")



def simulate_restore(
    encrypted_dir: Path,
    restored_dir: Path,
    reports_dir: Path,
    transform_name: str,
    key: str | None,
    dry_run: bool,
    verbose: bool,
    log_format: str,
) -> None:

    json_mode = log_format == "json"

    if not encrypted_dir.is_dir():
        print(f"[ERROR] Encrypted directory does not exist: {encrypted_dir}")
        sys.exit(1)

    verbose_print(verbose, f"[INFO] Starting RESTORE simulation from {encrypted_dir}")
    restored_dir.mkdir(parents=True, exist_ok=True)

    for path in encrypted_dir.rglob("*.simenc"):
        rel = path.relative_to(encrypted_dir)
        original_name = rel.name.replace(".simenc", "")
        out_path = restored_dir / rel.parent / original_name
        out_path.parent.mkdir(parents=True, exist_ok=True)

        verbose_print(verbose, f"[RESTORE] {path} -> {out_path}")

        enc_content = path.read_text(encoding="utf-8", errors="ignore")
        enc_hash = sha256_of_text(enc_content)

        restored = reverse_transform_content(enc_content, transform_name, key=key)
        rest_hash = sha256_of_text(restored)

        if not dry_run:
            out_path.write_text(restored, encoding="utf-8")

        log_line(
            reports_dir,
            "RESTORE",
            json_mode=json_mode,
            src=str(path),
            dst=str(out_path),
            transform=transform_name,
            enc_sha256=enc_hash,
            restored_sha256=rest_hash,
            dry_run=dry_run,
        )

    verbose_print(verbose, "[INFO] RESTORE completed.")


def main():
    args = parse_args()

    if args.transform.lower() == "xor" and not args.key:
        print("[ERROR] XOR transform requires: --key <passphrase>")
        sys.exit(1)

    if args.mode == "encrypt":
        simulate_encrypt(
            target_dir=Path(args.target_dir),
            encrypted_dir=Path(args.encrypted_dir),
            reports_dir=Path(args.reports_dir),
            transform_name=args.transform,
            key=args.key,
            dry_run=args.dry_run,
            verbose=args.verbose,
            overwrite_original=args.overwrite_original,
            log_format=args.log_format,
        )

    else:
        simulate_restore(
            encrypted_dir=Path(args.encrypted_dir),
            restored_dir=Path(args.restored_dir),
            reports_dir=Path(args.reports_dir),
            transform_name=args.transform,
            key=args.key,
            dry_run=args.dry_run,
            verbose=args.verbose,
            log_format=args.log_format,
        )


if __name__ == "__main__":
    main()
    