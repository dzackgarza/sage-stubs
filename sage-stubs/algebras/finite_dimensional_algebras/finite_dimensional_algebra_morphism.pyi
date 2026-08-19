from collections.abc import Sequence
from typing import Generic, TypeVar, overload

from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra import (
    FiniteDimensionalAlgebra,
    FiniteDimensionalAlgebraElementInput,
)
from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_element import (
    FiniteDimensionalAlgebraElement,
)
from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_ideal import (
    FiniteDimensionalAlgebraIdeal,
)
from sage.matrix.matrix0 import Matrix
from sage.rings.homset import RingHomset_generic
from sage.rings.morphism import RingHomomorphism_im_gens
from sage.structure.element import FieldElement

_Scalar = TypeVar(
    "_Scalar",
    bound=FieldElement,
    default=FieldElement,
)

type FiniteDimensionalLinearMapInput[_Scalar: FieldElement] = (
    Matrix[_Scalar]
    | Sequence[Sequence[_Scalar | int]]
)

class FiniteDimensionalAlgebraMorphism(
    RingHomomorphism_im_gens,
    Generic[_Scalar],
):
    def __init__(
        self,
        parent: FiniteDimensionalAlgebraHomset[_Scalar],
        f: Matrix[_Scalar],
        check: bool = True,
        unitary: bool = True,
    ) -> None: ...
    def parent(self) -> FiniteDimensionalAlgebraHomset[_Scalar]: ...
    def domain(self) -> FiniteDimensionalAlgebra[_Scalar]: ...
    def codomain(self) -> FiniteDimensionalAlgebra[_Scalar]: ...
    def _repr_(self) -> str: ...
    def __call__(
        self,
        x: FiniteDimensionalAlgebraElementInput[_Scalar],
    ) -> FiniteDimensionalAlgebraElement[_Scalar]: ...
    def __eq__(self, other: Element) -> bool: ...
    def __ne__(self, other: Element) -> bool: ...
    def matrix(self) -> Matrix[_Scalar]: ...
    def inverse_image(
        self,
        I: FiniteDimensionalAlgebraIdeal[_Scalar],
    ) -> FiniteDimensionalAlgebraIdeal[_Scalar]: ...

class FiniteDimensionalAlgebraHomset(
    RingHomset_generic[
        FiniteDimensionalAlgebraElement[_Scalar],
        FiniteDimensionalAlgebraElement[_Scalar],
    ],
    Generic[_Scalar],
):
    def domain(self) -> FiniteDimensionalAlgebra[_Scalar]: ...
    def codomain(self) -> FiniteDimensionalAlgebra[_Scalar]: ...
    def zero(self) -> FiniteDimensionalAlgebraMorphism[_Scalar]: ...
    @overload
    def __call__(
        self,
        f: FiniteDimensionalAlgebraMorphism[_Scalar],
        check: bool = True,
        unitary: bool = True,
    ) -> FiniteDimensionalAlgebraMorphism[_Scalar]: ...
    @overload
    def __call__(
        self,
        f: FiniteDimensionalLinearMapInput[_Scalar],
        check: bool = True,
        unitary: bool = True,
    ) -> FiniteDimensionalAlgebraMorphism[_Scalar]: ...
