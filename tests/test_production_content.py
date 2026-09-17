from __future__ import annotations

from tools.validate_production_content import validate


def test_frozen_production_content_is_structurally_complete() -> None:
    assert validate() == []
