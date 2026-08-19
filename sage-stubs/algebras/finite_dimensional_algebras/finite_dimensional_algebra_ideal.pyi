from typing import Generic, Self, TypeVar

from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra import (
    FiniteDimensionalAlgebra,
    FiniteDimensionalIdealInput,
)
from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_element import (
    FiniteDimensionalAlgebraElement,
)
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.rings.ideal import Ideal_generic
from sage.structure.element import FieldElement

_Scalar = TypeVar(
    "_Scalar",
    bound=FieldElement,
    default=FieldElement,
)

class FiniteDimensionalAlgebraIdeal(
    Ideal_generic,
    Generic[_Scalar],
):
    def __init__(
        self,
        A: FiniteDimensionalAlgebra[_Scalar],
        gens: FiniteDimensionalIdealInput[_Scalar] = None,
        given_by_matrix: bool = False,
    ) -> None: ...
    def ring(self) -> FiniteDimensionalAlgebra[_Scalar]: ...
    def _richcmp_(self, other: Self, op: int) -> bool: ...
    def __contains__(
        self,
        elt: FiniteDimensionalAlgebraElement[_Scalar] | Element,
    ) -> bool: ...
    def basis_matrix(self) -> Matrix[_Scalar]: ...
    def vector_space(self) -> FreeModule_generic[_Scalar]: ...
