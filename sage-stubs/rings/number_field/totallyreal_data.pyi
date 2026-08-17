from sage.rings.function_field.divisor import FunctionFieldDivisor
from sage.rings.integer import Integer
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject

ZZx: NumberFieldElement

def hermite_constant(n: int | Integer) -> NumberFieldElement: ...
def eval_seq_as_poly(
    f: ElementConstructorInput,
    n: int | Integer,
    x: NumberFieldElement | ElementConstructorInput,
) -> NumberFieldElement: ...
def newton(
    f: ElementConstructorInput,
    df: ElementConstructorInput,
    n: int | Integer,
    x0: ElementConstructorInput,
    eps: ElementConstructorInput,
) -> NumberFieldElement: ...
def lagrange_degree_3(
    n: int | Integer,
    an1: ElementConstructorInput,
    an2: ElementConstructorInput,
    an3: ElementConstructorInput,
) -> NumberFieldElement: ...

primessq_py: NumberFieldElement

def int_has_small_square_divisor(
    d: ElementConstructorInput,
) -> FunctionFieldDivisor: ...
def eval_seq_as_poly_int(
    f: ElementConstructorInput,
    n: int | Integer,
    x: NumberFieldElement | ElementConstructorInput,
) -> NumberFieldElement: ...

eps_abs: NumberFieldElement
phi: NumberFieldElement
sqrt2: NumberFieldElement

def easy_is_irreducible(
    a: NumberFieldElement | ElementConstructorInput, n: int | Integer
) -> NumberFieldElement: ...
def easy_is_irreducible_py(f: ElementConstructorInput) -> NumberFieldElement: ...

eps_global: NumberFieldElement

class tr_data(SageObject):
    def __init__(
        self,
        n: int | Integer,
        B: NumberFieldElement | ElementConstructorInput,
        a: NumberFieldElement | ElementConstructorInput = ...,
    ) -> None: ...
    def __dealloc__(self) -> NumberFieldElement: ...
    def increment(
        self,
        verbose: ElementConstructorInput = ...,
        haltk: ElementConstructorInput = ...,
        phc: ElementConstructorInput = ...,
    ) -> NumberFieldElement: ...
    def incr(
        self,
        f_out: ElementConstructorInput,
        verbose: ElementConstructorInput,
        haltk: ElementConstructorInput,
        phc: ElementConstructorInput,
    ) -> NumberFieldElement: ...
    def printa(self) -> NumberFieldElement: ...
