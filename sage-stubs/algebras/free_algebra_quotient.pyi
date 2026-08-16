from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Generic, Protocol, TypeVar

from sage.algebras.free_algebra import FreeAlgebra_generic
from sage.algebras.free_algebra_element import FreeAlgebraElement
from sage.algebras.free_algebra_quotient_element import FreeAlgebraQuotientElement
from sage.categories.rings import Rings
from sage.matrix.matrix0 import Matrix
from sage.monoids.free_monoid import FreeMonoid
from sage.monoids.free_monoid_element import FreeMonoidElement
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_AmbientCoefficient = TypeVar(
    "_AmbientCoefficient",
    bound=RingElement,
    covariant=True,
)


class AmbientQuotientAlgebraElement(Protocol[_AmbientCoefficient]):
    def ambient_algebra(
        self,
    ) -> FreeAlgebraQuotient[_AmbientCoefficient]: ...
    def ambient_algebra_element(
        self,
    ) -> FreeAlgebraQuotientElement[_AmbientCoefficient]: ...


type FreeAlgebraQuotientElementInput[_InputCoefficient: RingElement] = (
    FreeAlgebraQuotientElement[_InputCoefficient]
    | FreeAlgebraElement[_InputCoefficient]
    | FreeMonoidElement
    | FreeModuleElement[_InputCoefficient]
    | _InputCoefficient
    | int
    | Integer
    | Sequence[_InputCoefficient | int | Integer]
    | Mapping[FreeMonoidElement, _InputCoefficient | int | Integer]
    | AmbientQuotientAlgebraElement[_InputCoefficient]
)


class FreeAlgebraQuotient(
    UniqueRepresentation,
    Parent[FreeAlgebraQuotientElement[_Coefficient]],
    Generic[_Coefficient],
):
    Element: type[FreeAlgebraQuotientElement[_Coefficient]]
    element_class: type[FreeAlgebraQuotientElement[_Coefficient]]

    @staticmethod
    def __classcall__(
        cls: type[FreeAlgebraQuotient[_Coefficient]],
        A: FreeAlgebra_generic[_Coefficient],
        mons: Sequence[FreeMonoidElement],
        mats: Sequence[Matrix[_Coefficient]],
        names: Sequence[str],
    ) -> FreeAlgebraQuotient[_Coefficient]: ...
    def __init__(
        self,
        A: FreeAlgebra_generic[_Coefficient],
        mons: Sequence[FreeMonoidElement],
        mats: Sequence[Matrix[_Coefficient]],
        names: Sequence[str],
    ) -> None: ...
    def base_ring(self) -> Rings.ParentMethods[_Coefficient]: ...
    def _element_constructor_(
        self,
        x: FreeAlgebraQuotientElementInput[_Coefficient],
    ) -> FreeAlgebraQuotientElement[_Coefficient]: ...
    def __call__(
        self,
        x: FreeAlgebraQuotientElementInput[_Coefficient] = 0,
    ) -> FreeAlgebraQuotientElement[_Coefficient]: ...
    def _coerce_map_from_(self, S: Parent | type) -> bool: ...
    def _repr_(self) -> str: ...
    def gen(self, i: int | Integer) -> FreeAlgebraQuotientElement[_Coefficient]: ...
    def gens(self) -> tuple[FreeAlgebraQuotientElement[_Coefficient], ...]: ...
    def ngens(self) -> int: ...
    def dimension(self) -> int: ...
    def matrix_action(self) -> tuple[Matrix[_Coefficient], ...]: ...
    def monomial_basis(self) -> tuple[FreeMonoidElement, ...]: ...
    def rank(self) -> int: ...
    def module(self) -> FreeModule_generic[_Coefficient]: ...
    def monoid(self) -> FreeMonoid: ...
    def free_algebra(self) -> FreeAlgebra_generic[_Coefficient]: ...


def hamilton_quatalg[
    _HamiltonCoefficient: RingElement
](
    R: Rings.ParentMethods[_HamiltonCoefficient],
) -> tuple[
    FreeAlgebraQuotient[_HamiltonCoefficient],
    tuple[FreeAlgebraQuotientElement[_HamiltonCoefficient], ...],
]: ...
