from collections.abc import Sequence
from typing import TypeAlias

from sage.categories.category import Category
from sage.categories.drinfeld_modules import DrinfeldModules
from sage.rings.function_field.drinfeld_modules.action import DrinfeldModuleAction
from sage.rings.function_field.drinfeld_modules.homset import DrinfeldModuleHomset
from sage.rings.function_field.drinfeld_modules.morphism import DrinfeldModuleMorphism
from sage.rings.integer import Integer
from sage.rings.morphism import RingHomomorphism
from sage.rings.polynomial.ore_polynomial_element import OrePolynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.ring_extension import RingExtension_generic
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

DrinfeldGeneratorInput: TypeAlias = OrePolynomial | Sequence[ElementConstructorInput]
BasicJParameter: TypeAlias = tuple[tuple[int, ...], tuple[int, ...]]
JInvariantParameter: TypeAlias = BasicJParameter | int | Integer | None
AField: TypeAlias = Parent[RingElement] | RingExtension_generic

class DrinfeldModule(Parent[OrePolynomial], UniqueRepresentation):
    @staticmethod
    def __classcall_private__(
        class_: type[DrinfeldModule],
        function_ring: PolynomialRing_generic,
        gen: DrinfeldGeneratorInput,
        A_field: AField | None = ...,
        name: str = ...,
    ) -> DrinfeldModule: ...
    def __init__(
        self,
        gen: OrePolynomial,
        category: DrinfeldModules,
    ) -> None: ...
    def __call__(self, a: ElementConstructorInput) -> OrePolynomial: ...
    def _Hom_(
        self,
        other: DrinfeldModule,
        category: Category,
    ) -> DrinfeldModuleHomset: ...
    def __hash__(self) -> int: ...
    def action(self) -> DrinfeldModuleAction: ...
    def basic_j_invariant_parameters(
        self,
        coeff_indices: Sequence[int | Integer] | None = ...,
        nonzero: bool = ...,
    ) -> list[BasicJParameter]: ...
    def basic_j_invariants(
        self,
        nonzero: bool = ...,
    ) -> dict[BasicJParameter, RingElement]: ...
    def coefficient(self, n: int | Integer) -> RingElement: ...
    def coefficients(self, sparse: bool = ...) -> list[RingElement]: ...
    def change_A_field(self, A_field: AField) -> DrinfeldModule: ...
    def gen(self) -> OrePolynomial: ...
    def height(self) -> Integer: ...
    def is_isomorphic(
        self,
        other: DrinfeldModule,
        absolutely: bool = ...,
    ) -> bool: ...
    def is_finite(self) -> bool: ...
    def j_invariant(
        self,
        parameter: JInvariantParameter = ...,
        check: bool = ...,
    ) -> RingElement: ...
    def jk_invariants(self) -> dict[Integer, RingElement]: ...
    def morphism(self) -> RingHomomorphism: ...
    def rank(self) -> Integer: ...
    def velu(self, isog: OrePolynomial) -> DrinfeldModule: ...
    def hom(
        self,
        x: DrinfeldModuleMorphism | OrePolynomial | ElementConstructorInput,
        codomain: DrinfeldModule | None = ...,
    ) -> DrinfeldModuleMorphism: ...
    def scalar_multiplication(
        self,
        x: ElementConstructorInput,
    ) -> DrinfeldModuleMorphism: ...
    def frobenius_relative(
        self,
        n: int | Integer = ...,
    ) -> DrinfeldModuleMorphism: ...
    def _test_category(self, **options: bool | int | str | None) -> None: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
