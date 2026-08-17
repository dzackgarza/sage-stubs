from sage.rings.integer import Integer
from sage.rings.padics.padic_generic import pAdicGeneric
from sage.rings.padics.padic_generic_element import pAdicGenericElement
from sage.structure.parent import ElementConstructorInput

python_min: pAdicGenericElement
python_max: pAdicGenericElement

def gauss_sum(
    a: pAdicGenericElement | ElementConstructorInput,
    p: int | Integer,
    f: int | Integer,
    prec: int | Integer = ...,
    factored: int | Integer = ...,
    algorithm: str = ...,
    parent: pAdicGeneric = ...,
) -> pAdicGenericElement: ...
def min(*L: ElementConstructorInput) -> pAdicGenericElement: ...
def max(*L: ElementConstructorInput) -> pAdicGenericElement: ...
def precprint(
    prec_type: ElementConstructorInput,
    prec_cap: ElementConstructorInput,
    p: int | Integer,
) -> pAdicGenericElement: ...
def trim_zeros(L: ElementConstructorInput) -> pAdicGenericElement: ...
