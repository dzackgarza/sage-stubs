from collections.abc import Callable, Mapping, Sequence
from typing import Generic, Self, TypeVar, overload

from sage.algebras.free_algebra import FreeAlgebra_generic, PBWBasisOfFreeAlgebra
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.monoids.free_monoid_element import FreeMonoidElement
from sage.rings.integer import Integer
from sage.structure.element import AlgebraElement, Element, RingElement
from sage.structure.factorization import Factorization
from sage.structure.parent import Parent

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)

type FreeAlgebraElementData[_Coefficient: RingElement] = (
    FreeAlgebraElement[_Coefficient]
    | AlgebraElement
    | FreeMonoidElement
    | Mapping[
        FreeMonoidElement | object,
        _Coefficient | int | Integer,
    ]
)

class FreeAlgebraElement(
    IndexedFreeModuleElement[FreeMonoidElement, _Coefficient],
    Generic[_Coefficient],
):
    def __init__(
        self,
        A: FreeAlgebra_generic[_Coefficient],
        x: FreeAlgebraElementData[_Coefficient],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    @overload
    def __call__(
        self,
        *x: FreeAlgebraElement[_Coefficient],
        **kwds: FreeAlgebraElement[_Coefficient],
    ) -> FreeAlgebraElement[_Coefficient]: ...
    @overload
    def __call__[Evaluation](
        self,
        *x: Evaluation,
        **kwds: Evaluation,
    ) -> Evaluation | Element: ...
    def _mul_(self, y: Self) -> Self: ...
    def is_unit(self) -> bool: ...
    def __invert__(self) -> Self: ...
    def _acted_upon_(
        self,
        scalar: RingElement | int | Integer | Factorization,
        self_on_left: bool = ...,
    ) -> Self | Factorization | None: ...
    def _im_gens_[CodomainElement: Element](
        self,
        codomain: Parent[CodomainElement],
        im_gens: Sequence[CodomainElement],
        base_map: Callable[[_Coefficient], CodomainElement] | None,
    ) -> CodomainElement: ...
    def variables(self) -> list[FreeAlgebraElement[_Coefficient]]: ...
    def to_pbw_basis(self) -> PBWBasisOfFreeAlgebra.Element: ...
