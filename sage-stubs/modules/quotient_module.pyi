from collections.abc import Iterable, Sequence
from typing import Generic, Self, TypeVar

from sage.categories.morphism import Morphism
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import (
    FreeModule_ambient,
    FreeModule_ambient_field,
    FreeModule_generic,
    Module_free_ambient,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.structure.element import ElementConstructorInput, RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class QuotientModule_free_ambient(
    Module_free_ambient[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        module: FreeModule_ambient[_Scalar] | QuotientModule_free_ambient[_Scalar],
        sub: Submodule_free_ambient[_Scalar],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __hash__(self) -> int: ...
    def gens(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def gen(self, i: int = ...) -> FreeModuleElement[_Scalar]: ...
    def _coerce_map_from_(
        self,
        M: FreeModule_generic[_Scalar],
    ) -> bool | Morphism | None: ...
    def ambient_module(self) -> Self: ...
    def cover(
        self,
    ) -> FreeModule_ambient[_Scalar] | QuotientModule_free_ambient[_Scalar]: ...
    V = cover
    def relations(self) -> Submodule_free_ambient[_Scalar]: ...
    W = relations
    def free_cover(self) -> FreeModule_ambient[_Scalar]: ...
    def free_relations(self) -> Submodule_free_ambient[_Scalar]: ...

class FreeModule_ambient_field_quotient(
    FreeModule_ambient_field[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        domain: FreeModule_ambient_field[_Scalar],
        sub: FreeModule_generic[_Scalar],
        quotient_matrix: Matrix[_Scalar],
        lift_matrix: Matrix[_Scalar],
        inner_product_matrix: Matrix[_Scalar] | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __hash__(self) -> int: ...
    def _element_constructor_(
        self,
        x: FreeModuleElement[_Scalar]
        | Sequence[ElementConstructorInput],
    ) -> FreeModuleElement[_Scalar]: ...
    def _coerce_map_from_(
        self,
        M: FreeModule_generic[_Scalar],
    ) -> Morphism | None: ...
    def quotient_map(self) -> FreeModuleMorphism[_Scalar]: ...
    def lift_map(self) -> FreeModuleMorphism[_Scalar]: ...
    def lift(
        self,
        x: FreeModuleElement[_Scalar],
    ) -> FreeModuleElement[_Scalar]: ...
    def cover(self) -> FreeModule_ambient_field[_Scalar]: ...
    V = cover
    def relations(self) -> FreeModule_generic[_Scalar]: ...
    W = relations

FreeModule_quotient = FreeModule_ambient_field_quotient

from sage.modules.submodule import Submodule_free_ambient
