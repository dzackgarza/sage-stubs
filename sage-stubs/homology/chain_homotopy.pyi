from collections.abc import Hashable, Mapping
from typing import Generic, TypeVar

from sage.categories.morphism import Morphism
from sage.matrix.matrix import Matrix
from sage.structure.element import RingElement

_Degree = TypeVar("_Degree", bound=Hashable, default=int)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class ChainHomotopy(
    Morphism[
        Chain_class[_Degree, _Scalar],
        Chain_class[_Degree, _Scalar],
    ],
    Generic[_Degree, _Scalar],
):
    def __init__(
        self,
        matrices: Mapping[_Degree, Matrix[_Scalar]],
        f: ChainComplexMorphism[_Degree, _Scalar],
        g: ChainComplexMorphism[_Degree, _Scalar] | None = ...,
    ) -> None: ...
    def domain(self) -> ChainComplex_class[_Degree, _Scalar]: ...
    def codomain(self) -> ChainComplex_class[_Degree, _Scalar]: ...
    def is_algebraic_gradient_vector_field(self) -> bool: ...
    def is_homology_gradient_vector_field(self) -> bool: ...
    def in_degree(self, n: _Degree) -> Matrix[_Scalar]: ...
    def dual(self) -> ChainHomotopy[_Degree, _Scalar]: ...
    def __hash__(self) -> int: ...
    def _repr_(self) -> str: ...


class ChainContraction(
    ChainHomotopy[_Degree, _Scalar],
    Generic[_Degree, _Scalar],
):
    def __init__(
        self,
        matrices: Mapping[_Degree, Matrix[_Scalar]],
        pi: ChainComplexMorphism[_Degree, _Scalar],
        iota: ChainComplexMorphism[_Degree, _Scalar],
    ) -> None: ...
    def pi(self) -> ChainComplexMorphism[_Degree, _Scalar]: ...
    def iota(self) -> ChainComplexMorphism[_Degree, _Scalar]: ...
    def dual(self) -> ChainContraction[_Degree, _Scalar]: ...


from sage.homology.chain_complex import Chain_class, ChainComplex_class
from sage.homology.chain_complex_morphism import ChainComplexMorphism
