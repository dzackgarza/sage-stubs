from collections.abc import Sequence

from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroupElement, AdditiveAbelianGroup_fixed_gens
from sage.rings.integer import Integer
from sage.structure.element import Element as StructureElement
from sage.structure.parent import Parent

class AdditiveAbelianGroupWrapperElement(AdditiveAbelianGroupElement):
    def element(self) -> StructureElement: ...

class AdditiveAbelianGroupWrapper(AdditiveAbelianGroup_fixed_gens):
    Element: type[AdditiveAbelianGroupWrapperElement]
    def __init__(self, universe: Parent, gens: Sequence[StructureElement], invariants: Sequence[int | Integer]) -> None: ...
    def gens(self) -> tuple[AdditiveAbelianGroupWrapperElement, ...]: ...
    def torsion_subgroup(self, n: int | Integer | None = None) -> AdditiveAbelianGroupWrapper: ...
