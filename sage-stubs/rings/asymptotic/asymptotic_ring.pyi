from typing import TYPE_CHECKING
from sage.misc.fast_methods import WithLocals
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

if TYPE_CHECKING:
    from sage.rings.ring import Ring

class AsymptoticExpansion: ...

class AsymptoticRing(Parent, UniqueRepresentation, WithLocals):
    def variable_names(self) -> tuple[str, ...]: ...
    def base_ring(self) -> "Ring": ...
    def gens(self) -> tuple[AsymptoticExpansion, ...]: ...
