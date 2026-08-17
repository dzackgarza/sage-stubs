from sage.categories.action import Action
from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.rings.function_field.drinfeld_modules.morphism import DrinfeldModuleMorphism
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Ring
from sage.sets.family import Family
from sage.structure.element import Element
from sage.structure.parent import ElementConstructorInput

class DrinfeldModuleMorphismAction(Action):
    def __init__(
        self,
        A: Element | ElementConstructorInput,
        H: Polynomial | MPolynomial,
        is_left: bool,
        op: Ring,
    ) -> None: ...

class DrinfeldModuleHomset(Homset):
    def __init__(
        self,
        X: Element | ElementConstructorInput,
        Y: Element | ElementConstructorInput,
        category: Category = ...,
        check: bool = ...,
    ) -> None: ...
    def __contains__(self, x: object) -> bool: ...
    def an_element(self, degree: int | Integer = ...) -> Element: ...
    def zero(self) -> Element: ...
    def basis(self, degree: int | Integer = ...) -> Family[Element]: ...
    def basis_over_frobenius(self) -> Element: ...
    def random_element(self, degree: int | Integer = ...) -> Element: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self, *args: ElementConstructorInput, **kwds: ElementConstructorInput
    ) -> DrinfeldModuleMorphism: ...
