
from sage.combinat.backtrack import GenericBacktracker
from sage.combinat.crystals.crystals import Crystal
from typing import Any

class CrystalBacktracker(GenericBacktracker):
    

    def __init__(self, crystal: Crystal, index_set: Any = None) -> None: ...
    def _rec(self, x: Any, state: Any) -> Any: ...
