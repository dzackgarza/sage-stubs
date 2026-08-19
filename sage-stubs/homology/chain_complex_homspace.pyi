from collections.abc import Hashable, Mapping
from typing import Generic, TypeVar

from sage.categories.homset import Homset
from sage.matrix.matrix import Matrix
from sage.structure.element import RingElement

_Degree = TypeVar("_Degree", bound=Hashable, default=int)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class ChainComplexHomspace(
    Homset[
        ChainComplexMorphism[_Degree, _Scalar],
        Chain_class[_Degree, _Scalar],
        Chain_class[_Degree, _Scalar],
    ],
    Generic[_Degree, _Scalar],
):
    Element: type[ChainComplexMorphism[_Degree, _Scalar]]
    element_class: type[ChainComplexMorphism[_Degree, _Scalar]]

    def domain(self) -> ChainComplex_class[_Degree, _Scalar]: ...
    def codomain(self) -> ChainComplex_class[_Degree, _Scalar]: ...
    def __call__(
        self,
        f: Mapping[_Degree, Matrix[_Scalar]],
    ) -> ChainComplexMorphism[_Degree, _Scalar]: ...


from sage.homology.chain_complex import Chain_class, ChainComplex_class
from sage.homology.chain_complex_morphism import ChainComplexMorphism
