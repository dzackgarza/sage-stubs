from __future__ import annotations

from collections.abc import Callable, Iterator, Sequence
from typing import Generic, Self, TypeVar, overload

from sage.algebras.free_algebra import FreeAlgebraElementInput, FreeAlgebra_generic, PBWBasisOfFreeAlgebra
from sage.monoids.free_monoid_element import FreeMonoidElement
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import AlgebraElement, Element, RingElement
from sage.structure.factorization import Factorization
from sage.structure.parent import Parent

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)


class FreeAlgebraElement(
    IndexedFreeModuleElement,
    AlgebraElement,
    Generic[_Coefficient],
):
    def __init__(
        self,
        A: FreeAlgebra_generic[_Coefficient],
        x: FreeAlgebraElementInput[_Coefficient],
    ) -> None: ...
    def parent(self) -> FreeAlgebra_generic[_Coefficient]: ...
    def __iter__(
        self,
    ) -> Iterator[tuple[FreeMonoidElement, _Coefficient]]: ...
    def monomial_coefficients(
        self,
        copy: bool = True,
    ) -> dict[FreeMonoidElement, _Coefficient]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...

    @overload
    def __call__(
        self,
        *x: FreeAlgebraElement[_Coefficient],
        **kwds: FreeAlgebraElement[_Coefficient],
    ) -> FreeAlgebraElement[_Coefficient]: ...
    @overload
    def __call__[_Evaluation](
        self,
        *x: _Evaluation,
        **kwds: _Evaluation,
    ) -> _Evaluation | FreeAlgebraElement[_Coefficient]: ...

    def _mul_(self, y: Self) -> Self: ...
    def __invert__(self) -> Self: ...
    def is_unit(self) -> bool: ...
    def _acted_upon_(
        self,
        scalar: RingElement | int | Integer | Factorization,
        self_on_left: bool = False,
    ) -> Self | Factorization | None: ...
    def _im_gens_[CodomainElement: Element](
        self,
        codomain: Parent[CodomainElement],
        im_gens: Sequence[CodomainElement],
        base_map: Callable[[_Coefficient], CodomainElement] | None,
    ) -> CodomainElement: ...
    def variables(self) -> list[FreeAlgebraElement[_Coefficient]]: ...
    def to_pbw_basis(self) -> PBWBasisOfFreeAlgebra.Element: ...
