from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.combinat.backtrack import GenericBacktracker

class CrystalBacktracker(GenericBacktracker):
    """Backtracker for crystals using depth-first search on spanning tree."""

    def __init__(self, crystal, index_set=None) -> None: ...
    def _rec(self, x, state): ...
