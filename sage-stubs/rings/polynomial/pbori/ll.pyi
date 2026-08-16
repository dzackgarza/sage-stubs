from sage.rings.polynomial.pbori.pbori import BooleanPolynomial, BooleanPolynomialRing
from sage.rings.polynomial.pbori.PyPolyBoRi import BoolePolynomialVector

class RingMap:
    from_map: BoolePolynomialVector
    to_map: BoolePolynomialVector
    from_ring: BooleanPolynomialRing
    to_ring: BooleanPolynomialRing

    def __init__(
        self, to_ring: BooleanPolynomialRing, from_ring: BooleanPolynomialRing
    ) -> None: ...
    def __call__(self, poly: BooleanPolynomial) -> BooleanPolynomial: ...
    def invert(self, poly: BooleanPolynomial) -> BooleanPolynomial: ...

def combine(self, p: object, reduce: object = None) -> list[object]: ...
def llredsb_Cudd_style(self) -> list[object]: ...
def ll_encode(
    self, reduce: bool = False, prot: bool = False, reduce_by_linear: bool = True
) -> list[object]: ...
def eliminate(
    self,
    on_the_fly: bool = False,
    prot: bool = False,
    reduction_function: object = None,
    reduce_by_linear: bool = True,
) -> list[object]: ...
def construct_map_by_indices(self, idx_mapping: object) -> RingMap: ...
def eliminate_ll_ranked(
    self,
    to_reduce: object,
    reduction_function: object = None,
    reduce_by_linear: bool = True,
) -> list[object]: ...
