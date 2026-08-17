from sage.rings.integer import Integer
from sage.rings.padics.padic_generic_element import pAdicGenericElement
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.parent import ElementConstructorInput

def raise_error(
    error: int | Integer | Rational | RealNumber,
    permissive: ElementConstructorInput = ...,
) -> pAdicGenericElement: ...
