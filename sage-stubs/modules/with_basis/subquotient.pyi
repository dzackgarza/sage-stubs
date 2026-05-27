from collections.abc import Hashable

from sage.categories.morphism import Morphism
from sage.combinat.free_module import CombinatorialFreeModule
from sage.structure.element import Element
from sage.structure.parent import Parent


class QuotientModuleWithBasis(CombinatorialFreeModule):
    def ambient(self) -> Parent: ...
    def lift(self, x: Element) -> Element: ...
    def retract(self, x: Element) -> Element: ...


class SubmoduleWithBasis(CombinatorialFreeModule):
    def ambient(self) -> Parent: ...
    lift: Morphism
    reduce: Morphism
    retract: Morphism
    def is_submodule(self, other: Parent | SubmoduleWithBasis) -> bool: ...
    def cokernel_basis_indices(self) -> list[Hashable]: ...
