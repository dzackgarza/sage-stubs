from collections.abc import Sequence

from sage.rings.ideal import Ideal_generic
from sage.rings.polynomial.infinite_polynomial_element import InfinitePolynomial
from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialRing_sparse
from sage.structure.element import Element
from sage.structure.parent import Parent

class SymmetricIdeal(Ideal_generic):
    def __init__(
        self,
        ring: InfinitePolynomialRing_sparse | Parent,
        gens: object | Sequence[Element] | Element,
        coerce: bool = True,
    ) -> None: ...
    def _latex_(self) -> str: ...
    def _contains_(self, p: object) -> bool: ...
    def __mul__(self, other: SymmetricIdeal) -> SymmetricIdeal: ...
    def __pow__(self, n: int) -> SymmetricIdeal: ...
    def is_maximal(self) -> bool: ...
    def reduce(
        self, I: object | Element, tailreduce: bool = False
    ) -> InfinitePolynomial: ...
    def interreduction(
        self,
        tailreduce: bool = True,
        sorted: bool = False,
        report: object = None,
        RStrat: object = None,
    ) -> None: ...
    def interreduced_basis(self) -> list[InfinitePolynomial]: ...
    def symmetrisation(
        self,
        N: object = None,
        tailreduce: bool = False,
        report: object = None,
        use_full_group: bool = False,
    ) -> SymmetricIdeal: ...
    def symmetric_basis(self) -> list[InfinitePolynomial]: ...
    def normalisation(self) -> SymmetricIdeal: ...
    def squeezed(self) -> SymmetricIdeal: ...
    def groebner_basis(
        self,
        tailreduce: bool = False,
        reduced: bool = True,
        algorithm: object = None,
        report: object = None,
        use_full_group: bool = False,
    ) -> list[InfinitePolynomial]: ...
