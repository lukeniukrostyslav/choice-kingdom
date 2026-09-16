from __future__ import annotations

from runtime.endings import (
    END_GOLDEN_COMPACT,
    END_IRON_CROWN,
    END_PEOPLES_CHARTER,
    END_SECOND_FOUNDER,
    END_STEWARD,
)

# This table is a direct runtime projection of
# docs/MACHINE_ENDING_PRECEDENCE_TABLE_01.json. It is not inferred from
# enum order, event IDs, source-file order, or resolver branch order.
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
