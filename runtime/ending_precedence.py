from __future__ import annotations

# Direct runtime projection of docs/MACHINE_ENDING_PRECEDENCE_TABLE_01.json.
# The source contract is explicit data; no ordering is inferred from code.
END_SECOND_FOUNDER = "END_SECOND_FOUNDER"
END_PEOPLES_CHARTER = "END_PEOPLES_CHARTER"
END_GOLDEN_COMPACT = "END_GOLDEN_COMPACT"
END_STEWARD = "END_STEWARD"
END_IRON_CROWN = "END_IRON_CROWN"

POSITIVE_PRIORITY = (
    END_SECOND_FOUNDER,
    END_PEOPLES_CHARTER,
    END_GOLDEN_COMPACT,
    END_STEWARD,
    END_IRON_CROWN,
)

AUTHORED_PRIORITY = {
    (higher, lower): higher
    for index, higher in enumerate(POSITIVE_PRIORITY)
    for lower in POSITIVE_PRIORITY[index + 1 :]
}
