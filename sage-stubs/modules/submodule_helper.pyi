from typing import Generic, TypeVar

from sage.matrix.matrix0 import Matrix
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class SubmoduleHelper(Generic[_Scalar]):
    rank: int
    basis: Matrix[_Scalar]
    complement: Matrix[_Scalar]
    coordinates: Matrix[_Scalar]
    is_saturated: bool

    @staticmethod
    def __classcall_private__(
        class_: type[SubmoduleHelper[_Scalar]],
        mat: Matrix[_Scalar],
        saturate: bool = ...,
    ) -> SubmoduleHelper[_Scalar]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...

class SubmoduleHelper_field(SubmoduleHelper[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        mat: Matrix[_Scalar],
        saturate: bool,
    ) -> None: ...

class SubmoduleHelper_PID(SubmoduleHelper[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        mat: Matrix[_Scalar],
        saturate: bool,
    ) -> None: ...

class SubmoduleHelper_polynomial_ring(
    SubmoduleHelper[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        mat: Matrix[_Scalar],
        saturate: bool,
    ) -> None: ...
