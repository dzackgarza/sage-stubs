from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_generic, FreeModule_submodule
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.polynomial.ore_polynomial_element import OrePolynomial
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class OreModule(Generic[_Scalar]):
    def __init__(
        self,
        module: FreeModule_generic[_Scalar],
        ore_ring: OrePolynomialRing,
        action_matrix: Matrix[_Scalar],
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def ore_ring(self) -> OrePolynomialRing: ...
    def module(self) -> FreeModule_generic[_Scalar]: ...
    def rank(self) -> int: ...
    def action_matrix(self) -> Matrix[_Scalar]: ...
    def action(
        self,
        operator: OrePolynomial,
        vector: FreeModuleElement[_Scalar],
    ) -> FreeModuleElement[_Scalar]: ...
    def annihilator(
        self,
        vector: FreeModuleElement[_Scalar],
    ) -> OrePolynomial: ...
    def minimal_polynomial(
        self,
        vector: FreeModuleElement[_Scalar] | None = ...,
    ) -> OrePolynomial: ...
    def characteristic_polynomial(self, var: str = ...) -> Polynomial: ...
    def cyclic_vector(self) -> FreeModuleElement[_Scalar]: ...
    def cyclic_submodule(
        self,
        vector: FreeModuleElement[_Scalar],
    ) -> FreeModule_submodule[_Scalar]: ...
    def solution_space(
        self,
        operator: OrePolynomial,
    ) -> FreeModule_submodule[_Scalar]: ...
