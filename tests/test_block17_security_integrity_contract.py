from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_block17_security_contract_files_exist() -> None:
    assert (ROOT / "runtime" / "state.py").is_file()
    assert (ROOT / "tests" / "test_persistence_resume_boundary.py").is_file()


def test_save_store_has_versioned_integrity_envelope() -> None:
    source = (ROOT / "runtime" / "state.py").read_text(encoding="utf-8")
    assert "RUNTIME_SAVE_FORMAT_VERSION = 2" in source
    assert "snapshot_sha256" in source
    assert "hashlib.sha256" in source
    assert "integrity digest is malformed" in source
    assert "runtime save integrity check failed" in source


def test_security_regression_suite_covers_tampering_and_recovery() -> None:
    source = (ROOT / "tests" / "test_persistence_resume_boundary.py").read_text(encoding="utf-8")
    for marker in (
        "test_tampered_snapshot_digest_is_rejected",
        "test_invalid_backup_does_not_mask_primary_corruption",
        "test_tampered_digest_format_is_rejected_before_snapshot_use",
        "test_tampered_digest_with_wrong_hex_length_is_rejected",
        "test_tampered_digest_with_uppercase_hex_is_rejected_as_noncanonical",
    ):
        assert marker in source
