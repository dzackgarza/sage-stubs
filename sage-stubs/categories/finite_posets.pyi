from collections.abc import Callable

from sage.structure.parent import Parent

class FinitePosets:
    class ParentMethods:
        def is_poset_morphism(self, f: Callable[[object], object], codomain: Parent) -> bool: ...
        def order_ideals_lattice(self, as_ideals: bool = True, facade: bool | None = None) -> Parent: ...
