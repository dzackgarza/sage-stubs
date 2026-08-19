
from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.algebras.iwahori_hecke_algebra import (
    IwahoriHeckeAlgebra,
    _CoefficientRing,
    _CoxeterGroup,
    _CoxeterGroupElement,
    _HeckeElement,
)
from sage.combinat.partition import Partition
from sage.rings.integer import Integer
from sage.structure.element import RingElement

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_WElement = TypeVar(
    "_WElement",
    bound=_CoxeterGroupElement,
    default=_CoxeterGroupElement,
)

type PartitionInput = Partition | Sequence[int | Integer]

class NilCoxeterAlgebra(
    IwahoriHeckeAlgebra.T[_Coefficient, _WElement],
    Generic[_Coefficient, _WElement],
):
    def __init__(
        self,
        W: _CoxeterGroup[_WElement],
        base_ring: _CoefficientRing[_Coefficient] = ...,
        prefix: str = "u",
    ) -> None: ...
    def _repr_(self) -> str: ...
    def homogeneous_generator_noncommutative_variables(
        self,
        r: int | Integer,
    ) -> _HeckeElement[_Coefficient, _WElement]: ...
    def homogeneous_noncommutative_variables(
        self,
        la: PartitionInput,
    ) -> _HeckeElement[_Coefficient, _WElement]: ...
    def k_schur_noncommutative_variables(
        self,
        la: PartitionInput,
    ) -> _HeckeElement[_Coefficient, _WElement]: ...
