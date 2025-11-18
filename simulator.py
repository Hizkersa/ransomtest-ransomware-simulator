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
import json

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
        help="Name of the simple reversible transform to use (e.g. reverse, base64).",
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
        help="Format for simulation_log.txt: 'text' (default) or 'json' (JSON lines).",
    )

    return parser.parse_args()


def sha256_of_text(content: str) -> str:
    """
    Compute SHA-256 hash of a text string (UTF-8).
    This is for DFIR-style logging, not for security.
    """
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def log_line(reports_dir: Path, data: dict, log_format: str = "text") -> None:
    """
    Append a log line to reports/simulation_log.txt.

    - If log_format == "text": human-readable with key=value pairs.
    - If log_format == "json": one JSON object per line (JSONL).
    """
    reports_dir.mkdir(parents=True, exist_ok=True)
    log_file = reports_dir / "simulation_log.txt"

    timestamp = datetime.now(timezone.utc).isoformat()
    record = {"timestamp": timestamp, **data}

    if log_format == "json":
        line = json.dumps(record, ensure_ascii=False)
    else:
        # text format: timestamp | key=value | key2=value2 ...
        kv_parts = [f"{k}={v}" for k, v in data.items()]
        line = f"{timestamp} | " + " | ".join(kv_parts)

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
    dry_run: bool,
    verbose: bool,
    overwrite_original: bool,
    log_format: str,
) -> None:
    if not target_dir.is_dir():
        print(f"[ERROR] Target directory does not exist or is not a directory: {target_dir}")
        sys.exit(1)

    verbose_print(verbose, f"[INFO] Starting ENCRYPT simulation on {target_dir}")

    encrypted_dir.mkdir(parents=True, exist_ok=True)

    for path in target_dir.rglob("*"):
        if not path.is_file():
            continue

        if path.name == "README_RECOVER.txt":
            continue

        if path.suffix.lower() not in TEXT_EXTENSIONS:
            verbose_print(verbose, f"[SKIP] Non-text file: {path}")
            continue

        rel_path = path.relative_to(target_dir)
        enc_rel_name = rel_path.as_posix() + ".simenc"
        enc_path = encrypted_dir / enc_rel_name
        enc_path.parent.mkdir(parents=True, exist_ok=True)

        verbose_print(verbose, f"[PROCESS] {path} -> {enc_path}")

        try:
            original_content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            verbose_print(verbose, f"[ERROR] Could not read {path}: {e}")
            log_line(
                reports_dir,
                {
                    "event": "ERROR",
                    "action": "read",
                    "file": str(path),
                    "error": str(e),
                    "mode": "encrypt",
                },
                log_format,
            )
            continue

        # DFIR-style metadata
        orig_size = len(original_content.encode("utf-8"))
        orig_hash = sha256_of_text(original_content)

        try:
            transformed_content = transform_content(original_content, transform_name)
        except Exception as e:
            verbose_print(verbose, f"[ERROR] Transform failed for {path}: {e}")
            log_line(
                reports_dir,
                {
                    "event": "ERROR",
                    "action": "transform",
                    "file": str(path),
                    "transform": transform_name,
                    "error": str(e),
                    "mode": "encrypt",
                },
                log_format,
            )
            continue

        enc_size = len(transformed_content.encode("utf-8"))
        enc_hash = sha256_of_text(transformed_content)

        if not dry_run:
            try:
                enc_path.write_text(transformed_content, encoding="utf-8")
            except Exception as e:
                verbose_print(verbose, f"[ERROR] Could not write {enc_path}: {e}")
                log_line(
                    reports_dir,
                    {
                        "event": "ERROR",
                        "action": "write_encrypted",
                        "file": str(enc_path),
                        "error": str(e),
                        "mode": "encrypt",
                    },
                    log_format,
                )
                continue

        log_line(
            reports_dir,
            {
                "event": "ENCRYPT",
                "src_file": str(path),
                "dst_file": str(enc_path),
                "transform": transform_name,
                "orig_size": orig_size,
                "orig_sha256": orig_hash,
                "enc_size": enc_size,
                "enc_sha256": enc_hash,
                "dry_run": dry_run,
                "mode": "encrypt",
            },
            log_format,
        )

        # Optional overwrite of original inside lab_files/
        if overwrite_original and not dry_run:
            try:
                path.write_text(transformed_content, encoding="utf-8")
                verbose_print(verbose, f"[OVERWRITE] Original file overwritten: {path}")
                log_line(
                    reports_dir,
                    {
                        "event": "OVERWRITE",
                        "file": str(path),
                        "transform": transform_name,
                        "sha256": enc_hash,
                        "mode": "encrypt",
                    },
                    log_format,
                )
            except Exception as e:
                verbose_print(verbose, f"[ERROR] Could not overwrite {path}: {e}")
                log_line(
                    reports_dir,
                    {
                        "event": "ERROR",
                        "action": "overwrite_original",
                        "file": str(path),
                        "error": str(e),
                        "mode": "encrypt",
                    },
                    log_format,
                )

    # Ransom note educativa
    ransom_note_path = target_dir / "README_RECOVER.txt"
    ransom_note_content = (
        "=== RANSOMTEST EDUCATIONAL NOTE ===\n\n"
        "Your files in this sandbox have been SIMULATED as 'encrypted' by the "
        "ransomtest educational ransomware simulator.\n\n"
        "No real harm has been done:\n"
        "- Original files may remain untouched in this lab_files/ directory (safe mode), "
        "or be overwritten only if explicitly requested.\n"
        "- Transformed copies are stored separately in encrypted_files/.\n\n"
        "This tool is strictly for learning DFIR and blue-team analysis.\n"
        "Do NOT run it outside controlled lab environments.\n"
    )

    if not dry_run:
        try:
            ransom_note_path.write_text(ransom_note_content, encoding="utf-8")
            verbose_print(verbose, f"[INFO] Ransom note created at {ransom_note_path}")
            log_line(
                reports_dir,
                {
                    "event": "RANSOM_NOTE",
                    "file": str(ransom_note_path),
                    "mode": "encrypt",
                },
                log_format,
            )
        except Exception as e:
            verbose_print(verbose, f"[ERROR] Could not write ransom note {ransom_note_path}: {e}")
            log_line(
                reports_dir,
                {
                    "event": "ERROR",
                    "action": "write_ransom_note",
                    "file": str(ransom_note_path),
                    "error": str(e),
                    "mode": "encrypt",
                },
                log_format,
            )

    log_line(
        reports_dir,
        {
            "event": "ENCRYPT_COMPLETED",
            "transform": transform_name,
            "dry_run": dry_run,
            "mode": "encrypt",
        },
        log_format,
    )
    verbose_print(verbose, "[INFO] ENCRYPT simulation completed.")


def simulate_restore(
    encrypted_dir: Path,
    restored_dir: Path,
    reports_dir: Path,
    transform_name: str,
    dry_run: bool,
    verbose: bool,
    log_format: str,
) -> None:
    if not encrypted_dir.is_dir():
        print(f"[ERROR] Encrypted directory does not exist or is not a directory: {encrypted_dir}")
        sys.exit(1)

    verbose_print(verbose, f"[INFO] Starting RESTORE simulation from {encrypted_dir}")

    restored_dir.mkdir(parents=True, exist_ok=True)

    for path in encrypted_dir.rglob("*.simenc"):
        if not path.is_file():
            continue

        rel_path = path.relative_to(encrypted_dir)

        if rel_path.name.endswith(".simenc"):
            original_name = rel_path.name[:-7]  # len(".simenc") = 7
        else:
            original_name = rel_path.name

        restored_path = restored_dir / rel_path.parent / original_name
        restored_path.parent.mkdir(parents=True, exist_ok=True)

        verbose_print(verbose, f"[RESTORE] {path} -> {restored_path}")

        try:
            enc_content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            verbose_print(verbose, f"[ERROR] Could not read {path}: {e}")
            log_line(
                reports_dir,
                {
                    "event": "ERROR",
                    "action": "read_encrypted",
                    "file": str(path),
                    "error": str(e),
                    "mode": "restore",
                },
                log_format,
            )
            continue

        enc_size = len(enc_content.encode("utf-8"))
        enc_hash = sha256_of_text(enc_content)

        try:
            restored_content = reverse_transform_content(enc_content, transform_name)
        except Exception as e:
            verbose_print(verbose, f"[ERROR] Reverse transform failed for {path}: {e}")
            log_line(
                reports_dir,
                {
                    "event": "ERROR",
                    "action": "reverse_transform",
                    "file": str(path),
                    "transform": transform_name,
                    "error": str(e),
                    "mode": "restore",
                },
                log_format,
            )
            continue

        rest_size = len(restored_content.encode("utf-8"))
        rest_hash = sha256_of_text(restored_content)

        if not dry_run:
            try:
                restored_path.write_text(restored_content, encoding="utf-8")
            except Exception as e:
                verbose_print(verbose, f"[ERROR] Could not write {restored_path}: {e}")
                log_line(
                    reports_dir,
                    {
                        "event": "ERROR",
                        "action": "write_restored",
                        "file": str(restored_path),
                        "error": str(e),
                        "mode": "restore",
                    },
                    log_format,
                )
                continue

        log_line(
            reports_dir,
            {
                "event": "RESTORE",
                "src_file": str(path),
                "dst_file": str(restored_path),
                "transform": transform_name,
                "enc_size": enc_size,
                "enc_sha256": enc_hash,
                "rest_size": rest_size,
                "rest_sha256": rest_hash,
                "dry_run": dry_run,
                "mode": "restore",
            },
            log_format,
        )

    log_line(
        reports_dir,
        {
            "event": "RESTORE_COMPLETED",
            "transform": transform_name,
            "dry_run": dry_run,
            "mode": "restore",
        },
        log_format,
    )
    verbose_print(verbose, "[INFO] RESTORE simulation completed.")


def main() -> None:
    args = parse_args()

    target_dir = Path(args.target_dir).resolve()
    encrypted_dir = Path(args.encrypted_dir).resolve()
    restored_dir = Path(args.restored_dir).resolve()
    reports_dir = Path(args.reports_dir).resolve()

    if args.mode == "encrypt":
        simulate_encrypt(
            target_dir=target_dir,
            encrypted_dir=encrypted_dir,
            reports_dir=reports_dir,
            transform_name=args.transform,
            dry_run=args.dry_run,
            verbose=args.verbose,
            overwrite_original=args.overwrite_original,
            log_format=args.log_format,
        )
    elif args.mode == "restore":
        simulate_restore(
            encrypted_dir=encrypted_dir,
            restored_dir=restored_dir,
            reports_dir=reports_dir,
            transform_name=args.transform,
            dry_run=args.dry_run,
            verbose=args.verbose,
            log_format=args.log_format,
        )
    else:
        print(f"[ERROR] Unsupported mode: {args.mode}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    