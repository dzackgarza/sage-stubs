from sage.rings.polynomial.padics.polynomial_padic import Polynomial_padic
from sage.rings.polynomial.polynomial_element import Polynomial_generic_dense
from sage.structure.parent import Parent

class Polynomial_padic_flat(Polynomial_generic_dense, Polynomial_padic):
    def __init__(self, parent: Parent, x: object = None, check: bool = True, is_gen: bool = False, construct: bool = False, absprec: object = None) -> None: ...
