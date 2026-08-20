from collections.abc import Iterable, Iterator
from typing import Generic, Literal, TypeVar, overload

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.categories.pushout import AlgebraicExtensionFunctor
from sage.interfaces.expect import Expect
from sage.modules.free_module import FreeModule_generic
from sage.rings.algebraic_closure_finite_field import AlgebraicClosureFiniteField_generic
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.finite_rings.galois_group import GaloisGroup_GF
from sage.rings.finite_rings.hom_finite_field import FrobeniusEndomorphism_finite_field
from sage.rings.finite_rings.maps_finite_field import FiniteFieldVectorSpaceIsomorphism
from sage.rings.integer import Integer
from sage.rings.morphism import RingHomomorphism
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.ring import Field, Ring
from sage.structure.element import Element
from sage.structure.factorization import Factorization
from sage.structure.factory import FactoryArgument
from sage.structure.parent import Parent

_FiniteElement = TypeVar(
    "_FiniteElement",
    bound=FiniteRingElement,
    default=FiniteRingElement,
)


class SageInputBuilder: ...


class FiniteField(Field, Generic[_FiniteElement]):
    Element: type[_FiniteElement]

    def __init__(
        self,
        base: FiniteField,
        names: str | tuple[str, ...],
        normalize: bool,
        category: Category | None = ...,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __richcmp__(self, other: Parent, m: int) -> bool: ...
    def _latex_(self) -> str: ...
    def _gap_init_(self) -> str: ...
    def _magma_init_(self, magma: Expect | None) -> str: ...
    def _macaulay2_init_(self, macaulay2: Expect | None = ...) -> str: ...
    def _fricas_init_(self) -> str: ...
    def _sage_input_(
        self,
        sib: SageInputBuilder,
        coerced: bool,
    ) -> Element: ...
    def _is_valid_homomorphism_(
        self,
        codomain: Parent,
        im_gens: tuple[Element, ...],
        base_map: Map | None = ...,
    ) -> bool: ...
    def _Hom_(
        self,
        codomain: Parent,
        category: Category | None = ...,
    ) -> Homset: ...
    def _squarefree_decomposition_univariate_polynomial(
        self,
        f: Polynomial,
    ) -> Factorization: ...
    def _element_of_factored_order(
        self,
        F: Factorization,
    ) -> _FiniteElement: ...
    def _coerce_map_from_(self, R: Parent) -> Morphism | bool | None: ...
    def _convert_map_from_(self, R: Parent) -> Morphism | None: ...
    def _compatible_family(self) -> list[FiniteField]: ...

    @overload
    def _roots_univariate_polynomial(
        self,
        f: Polynomial,
        ring: Ring | None = ...,
        multiplicities: Literal[True] = ...,
        algorithm: str | None = ...,
    ) -> list[tuple[_FiniteElement, int]]: ...
    @overload
    def _roots_univariate_polynomial(
        self,
        f: Polynomial,
        ring: Ring | None = ...,
        multiplicities: Literal[False] = ...,
        algorithm: str | None = ...,
    ) -> list[_FiniteElement]: ...
    @overload
    def _roots_univariate_polynomial(
        self,
        f: Polynomial,
        ring: Ring | None = ...,
        multiplicities: bool = ...,
        algorithm: str | None = ...,
    ) -> list[_FiniteElement] | list[tuple[_FiniteElement, int]]: ...

    def __iter__(self) -> Iterator[_FiniteElement]: ...
    def absolute_degree(self) -> int: ...
    def from_integer(
        self,
        n: int | Integer,
        reverse: bool = ...,
    ) -> _FiniteElement: ...
    def gen(self, n: int = ...) -> _FiniteElement: ...
    def gens(self) -> tuple[_FiniteElement, ...]: ...
    def multiplicative_generator(self) -> _FiniteElement: ...
    primitive_element = multiplicative_generator
    def ngens(self) -> int: ...
    def order(self) -> Integer: ...
    cardinality = order
    def factored_order(self) -> Factorization: ...
    def factored_unit_order(self) -> Factorization: ...
    def unit_group_exponent(self) -> Integer: ...
    def is_prime_field(self) -> bool: ...
    def modulus(self) -> Integer | Polynomial: ...
    def polynomial(self, name: str | None = ...) -> Polynomial: ...
    def random_element(
        self,
        *args: int | Integer,
        **kwds: int | Integer | bool,
    ) -> _FiniteElement: ...
    def some_elements(self) -> list[_FiniteElement]: ...
    def polynomial_ring(
        self,
        variable_name: str | None = ...,
    ) -> PolynomialRing_generic: ...

    @overload
    def free_module(
        self,
        base: Ring | None = ...,
        basis: list[_FiniteElement] | None = ...,
        map: Literal[False] = ...,
    ) -> FreeModule_generic[FiniteRingElement]: ...
    @overload
    def free_module(
        self,
        base: Ring | None,
        basis: list[_FiniteElement] | None,
        map: Literal[True],
    ) -> tuple[
        FreeModule_generic[FiniteRingElement],
        FiniteFieldVectorSpaceIsomorphism,
        FiniteFieldVectorSpaceIsomorphism,
    ]: ...

    def construction(
        self,
    ) -> tuple[AlgebraicExtensionFunctor, FiniteField] | None: ...
    def extension(
        self,
        poly: int | Integer | Polynomial | NumberFieldElement,
        name: str | None = ...,
        names: str | tuple[str, ...] | None = ...,
        latex_name: str | None = ...,
        latex_names: str | tuple[str, ...] | None = ...,
        *args: str,
        **kwds: str,
    ) -> FiniteField: ...

    @overload
    def subfield(
        self,
        degree: int | Integer,
        name: str | None = ...,
        map: Literal[False] = ...,
    ) -> FiniteField: ...
    @overload
    def subfield(
        self,
        degree: int | Integer,
        name: str | None,
        map: Literal[True],
    ) -> tuple[FiniteField, RingHomomorphism, RingHomomorphism]: ...

    def subfields(
        self,
        degree: int | Integer = ...,
        name: str | None = ...,
    ) -> list[tuple[FiniteField, RingHomomorphism]]: ...
    def algebraic_closure(self) -> AlgebraicClosureFiniteField_generic: ...
    def is_conway(self) -> bool: ...
    def an_embedding(self, K: FiniteField) -> RingHomomorphism: ...
    def embeddings(self, K: FiniteField) -> list[RingHomomorphism]: ...
    def frobenius_endomorphism(
        self,
        n: int | Integer = ...,
    ) -> FrobeniusEndomorphism_finite_field: ...
    def galois_group(self) -> GaloisGroup_GF: ...
    def dual_basis(
        self,
        basis: list[_FiniteElement] | None = ...,
        check: bool = ...,
    ) -> list[_FiniteElement]: ...
    def from_bytes(
        self,
        input_bytes: bytes | Iterable[int],
        byteorder: str = ...,
    ) -> _FiniteElement: ...
    def characteristic(self) -> Integer: ...
    def degree(self) -> Integer: ...
    def prime_subfield(self) -> FiniteField: ...
    def is_perfect(self) -> bool: ...
    def zeta(self, n: int | Integer = ...) -> _FiniteElement: ...


def unpickle_FiniteField_ext(
    _type: type,
    order: int | Integer,
    variable_name: str,
    modulus: Polynomial,
    kwargs: dict[str, FactoryArgument],
) -> FiniteField: ...


def unpickle_FiniteField_prm(
    _type: type,
    order: int | Integer,
    variable_name: str,
    kwargs: dict[str, FactoryArgument],
) -> FiniteField: ...
