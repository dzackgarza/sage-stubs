from collections.abc import Callable

from sage.categories.action import Action
from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.rings.function_field.drinfeld_modules.drinfeld_module import DrinfeldModule
from sage.rings.function_field.drinfeld_modules.morphism import DrinfeldModuleMorphism
from sage.rings.integer import Integer
from sage.rings.polynomial.ore_polynomial_element import OrePolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic

class DrinfeldModuleMorphismAction(Action):
    def __init__(
        self,
        A: PolynomialRing_generic,
        H: DrinfeldModuleHomset,
        is_left: bool,
        op: Callable[[object, object], object],
    ) -> None: ...
    def _act_(
        self,
        a: Polynomial,
        f: DrinfeldModuleMorphism,
    ) -> DrinfeldModuleMorphism: ...

class DrinfeldModuleHomset(
    Homset[DrinfeldModuleMorphism, OrePolynomial, OrePolynomial]
):
    Element: type[DrinfeldModuleMorphism]
    element_class: type[DrinfeldModuleMorphism]
    def __init__(
        self,
        X: DrinfeldModule,
        Y: DrinfeldModule,
        category: Category | None = ...,
        check: bool = ...,
    ) -> None: ...
    def domain(self) -> DrinfeldModule: ...
    def codomain(self) -> DrinfeldModule: ...
    def __contains__(self, x: object) -> bool: ...
    def _element_constructor_(
        self,
        *args: object,
        **kwds: object,
    ) -> DrinfeldModuleMorphism: ...
    def an_element(
        self,
        degree: int | Integer | None = ...,
    ) -> DrinfeldModuleMorphism: ...
    def zero(self) -> DrinfeldModuleMorphism: ...
    def _A_basis(self) -> list[DrinfeldModuleMorphism]: ...
    def _Fq_basis(
        self,
        degree: int | Integer,
    ) -> list[DrinfeldModuleMorphism]: ...
    def basis(
        self,
        degree: int | Integer | None = ...,
    ) -> list[DrinfeldModuleMorphism]: ...
    def basis_over_frobenius(self) -> list[DrinfeldModuleMorphism]: ...
    def random_element(
        self,
        degree: int | Integer | None = ...,
    ) -> DrinfeldModuleMorphism: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
