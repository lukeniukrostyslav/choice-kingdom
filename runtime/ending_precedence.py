from __future__ import annotations

from typing import Mapping

from .endings import (
    END_GOLDEN_COMPACT,
    END_IRON_CROWN,
    END_PEOPLES_CHARTER,
    END_SECOND_FOUNDER,
    END_STEWARD,
)

# Explicit authored precedence data.  This module intentionally contains no
# ordering fallback: an omitted simultaneous pair is an error in the resolver.
# Values are the selected ending IDs for the pair.  The table is kept separate
# from resolver control flow so precedence cannot be inferred from source order.

POSITIVE_PRIORITY: Mapping[tuple[str, str], str] = {
    (END_STEWARD, END_PEOPLES_CHARTER): END_STEWARD,
    (END_STEWARD, END_GOLDEN_COMPACT): END_STEWARD,
    (END_STEWARD, END_IRON_CROWN): END_IRON_CROWN,
    (END_GOLDEN_COMPACT, END_PEOPLES_CHARTER): END_GOLDEN_COMPACT,
    (END_GOLDEN_COMPACT, END_SECOND_FOUNDER): END_SECOND_FOUNDER,
    (END_PEOPLES_CHARTER, END_SECOND_FOUNDER): END_SECOND_FOUNDER,
    (END_IRON_CROWN, END_STEWARD): END_IRON_CROWN,
    (END_IRON_CROWN, END_PEOPLES_CHARTER): END_IRON_CROWN,
}

# NOTE: The selected winners above are provisional runtime data only where the
# repository has not yet supplied an explicit authorial winner.  They must not
# be used to claim the QA matrix is verified until the authored source is closed.
