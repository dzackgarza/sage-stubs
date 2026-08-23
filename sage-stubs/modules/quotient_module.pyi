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
from sage.structure.element import Element, FieldElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_FieldScalar = TypeVar(
    "_FieldScalar",
    bound=FieldElement,
    default=FieldElement,
)
_SourceElement = TypeVar("_SourceElement", bound=Element)


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
        M: Parent[_SourceElement],
    ) -> bool | None: ...
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
    FreeModule_ambient_field[_FieldScalar],
    Generic[_FieldScalar],
):
    def __init__(
        self,
        domain: FreeModule_ambient_field[_FieldScalar],
        sub: FreeModule_generic[_FieldScalar],
        quotient_matrix: Matrix[_FieldScalar],
        lift_matrix: Matrix[_FieldScalar],
        inner_product_matrix: Matrix[_FieldScalar] | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __hash__(self) -> int: ...
    def _element_constructor_(
        self,
        x: ElementConstructorInput,
    ) -> FreeModuleElement[_FieldScalar]: ...
    def _coerce_map_from_(
        self,
        M: Parent[_SourceElement],
    ) -> Morphism[_SourceElement, FreeModuleElement[_FieldScalar]] | None: ...
    def quotient_map(
        self,
    ) -> FreeModuleMorphism[_FieldScalar, _FieldScalar]: ...
    def lift_map(
        self,
    ) -> FreeModuleMorphism[_FieldScalar, _FieldScalar]: ...
    def lift(
        self,
        x: FreeModuleElement[_FieldScalar],
    ) -> FreeModuleElement[_FieldScalar]: ...
    def cover(self) -> FreeModule_ambient_field[_FieldScalar]: ...
    V = cover
    def relations(self) -> FreeModule_generic[_FieldScalar]: ...
    W = relations


FreeModule_quotient = FreeModule_ambient_field_quotient


from sage.modules.submodule import Submodule_free_ambient
