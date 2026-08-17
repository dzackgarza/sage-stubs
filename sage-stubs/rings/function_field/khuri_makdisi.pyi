from sage.rings.function_field.divisor import FunctionFieldDivisor
from sage.rings.function_field.element import FunctionFieldElement
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject

def listcat(l: ElementConstructorInput) -> FunctionFieldElement: ...

class KhuriMakdisi_base(SageObject):
    def mu_image(
        self,
        wd: ElementConstructorInput,
        we: ElementConstructorInput,
        mu_mat: ElementConstructorInput,
        expected_dim: ElementConstructorInput = ...,
    ) -> FunctionFieldElement: ...
    def mu_preimage(
        self,
        we: ElementConstructorInput,
        wde: ElementConstructorInput,
        mu_mat: ElementConstructorInput,
        expected_codim: ElementConstructorInput = ...,
    ) -> FunctionFieldElement: ...
    def negate(self, wd: ElementConstructorInput) -> FunctionFieldElement: ...
    def add(
        self, wd1: ElementConstructorInput, wd2: ElementConstructorInput
    ) -> FunctionFieldElement: ...
    def subtract(
        self, wd1: ElementConstructorInput, wd2: ElementConstructorInput
    ) -> FunctionFieldElement: ...
    def multiple(
        self, wd: ElementConstructorInput, n: int | Integer
    ) -> FunctionFieldElement: ...
    def zero_divisor(self) -> FunctionFieldDivisor: ...

class KhuriMakdisi_large(KhuriMakdisi_base):
    def __init__(
        self,
        V: ElementConstructorInput,
        mu: ElementConstructorInput,
        w0: ElementConstructorInput,
        d0: ElementConstructorInput,
        g: Polynomial | MPolynomial,
    ) -> None: ...
    def equal(
        self, wd: ElementConstructorInput, we: ElementConstructorInput
    ) -> FunctionFieldElement: ...
    def addflip(
        self, wd1: ElementConstructorInput, wd2: ElementConstructorInput
    ) -> FunctionFieldElement: ...
    def add_divisor(
        self,
        wd1: ElementConstructorInput,
        wd2: ElementConstructorInput,
        d1: ElementConstructorInput,
        d2: ElementConstructorInput,
    ) -> FunctionFieldDivisor: ...

class KhuriMakdisi_medium(KhuriMakdisi_base):
    def __init__(
        self,
        V: ElementConstructorInput,
        mu: ElementConstructorInput,
        w0: ElementConstructorInput,
        d0: ElementConstructorInput,
        g: Polynomial | MPolynomial,
    ) -> None: ...
    def equal(
        self, wd: ElementConstructorInput, we: ElementConstructorInput
    ) -> FunctionFieldElement: ...
    def addflip(
        self, wd1: ElementConstructorInput, wd2: ElementConstructorInput
    ) -> FunctionFieldElement: ...
    def add_divisor(
        self,
        wd1: ElementConstructorInput,
        wd2: ElementConstructorInput,
        d1: ElementConstructorInput,
        d2: ElementConstructorInput,
    ) -> FunctionFieldDivisor: ...

class KhuriMakdisi_small(KhuriMakdisi_base):
    def __init__(
        self,
        V: ElementConstructorInput,
        mu: ElementConstructorInput,
        w0: ElementConstructorInput,
        d0: ElementConstructorInput,
        g: Polynomial | MPolynomial,
    ) -> None: ...
    def equal(
        self, wd: ElementConstructorInput, we: ElementConstructorInput
    ) -> FunctionFieldElement: ...
    def addflip(
        self, wd1: ElementConstructorInput, wd2: ElementConstructorInput
    ) -> FunctionFieldElement: ...
    def negate(self, wd: ElementConstructorInput) -> FunctionFieldElement: ...
    def add_divisor(
        self,
        wd1: ElementConstructorInput,
        wd2: ElementConstructorInput,
        d1: ElementConstructorInput,
        d2: ElementConstructorInput,
    ) -> FunctionFieldDivisor: ...
