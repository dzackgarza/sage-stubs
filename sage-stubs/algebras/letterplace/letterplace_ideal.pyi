from __future__ import annotations

from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.noncommutative_ideals import IdealSide, Ideal_nc
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type LetterplaceDegreeBound = int | Integer | PlusInfinity | None
type LetterplaceIdealInput[_Scalar: RingElement] = (
    LetterplaceIdeal[_Scalar]
    | FreeAlgebra_letterplace[_Scalar]
    | FreeAlgebraElement_letterplace[_Scalar]
    | Sequence[FreeAlgebraElement_letterplace[_Scalar]]
)
type LetterplaceIdealReduction[_Scalar: RingElement] = (
    LetterplaceIdeal[_Scalar] | FreeAlgebraElement_letterplace[_Scalar]
)


class LetterplaceIdeal(
    Ideal_nc,
    Generic[_Scalar],
):
    def __init__(
        self,
        ring: FreeAlgebra_letterplace[_Scalar],
        gens: Sequence[FreeAlgebraElement_letterplace[_Scalar]],
        coerce: bool = ...,
        side: IdealSide = ...,
    ) -> None: ...
    def groebner_basis(
        self,
        degbound: LetterplaceDegreeBound = ...,
    ) -> LetterplaceIdeal[_Scalar]: ...
    def __contains__(self, x: object) -> bool: ...
    def reduce(
        self,
        f: LetterplaceIdealInput[_Scalar],
    ) -> LetterplaceIdealReduction[_Scalar]: ...


from sage.algebras.letterplace.free_algebra_element_letterplace import (
    FreeAlgebraElement_letterplace,
)
from sage.algebras.letterplace.free_algebra_letterplace import (
    FreeAlgebra_letterplace,
)
