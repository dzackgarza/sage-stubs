
from collections.abc import Iterable, Iterator, Sequence
from typing import Generic, Literal, Protocol, Self, TypeVar, overload

from sage.categories.category import Category
from sage.categories.rings import Rings
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.with_basis.morphism import ModuleMorphismByLinearity
from sage.rings.integer import Integer
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial_univariate
from sage.structure.element import Element, RingElement

type AskeyWilsonExponent = int | Integer
type AskeyWilsonExponentVector = tuple[
    AskeyWilsonExponent,
    AskeyWilsonExponent,
    AskeyWilsonExponent,
    AskeyWilsonExponent,
    AskeyWilsonExponent,
    AskeyWilsonExponent,
]
type AskeyWilsonGeneratorName = Literal["A", "B", "C", "a", "b", "g"]
type AskeyWilsonCoefficientInput[_Coefficient: RingElement] = (
    _Coefficient | RingElement | Integer | int
)

class AskeyWilsonBasisIndex(Protocol):
    value: AskeyWilsonExponentVector
    def __iter__(self) -> Iterator[AskeyWilsonExponent]: ...
    def __getitem__(self, i: int) -> AskeyWilsonExponent: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...

class MultiplicativeAlgebraElement(Element, Protocol):
    def __mul__(self: Self, other: Self) -> Self: ...
    def __pow__(self: Self, exponent: int | Integer) -> Self: ...

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_SourceCoefficient = TypeVar("_SourceCoefficient", bound=RingElement)
_CodomainElement = TypeVar(
    "_CodomainElement",
    bound=MultiplicativeAlgebraElement,
)
_CodomainParent = TypeVar("_CodomainParent", bound=Parent)

class _AskeyWilsonGeneratorFamily(Protocol[_Coefficient]):
    def __getitem__(
        self,
        name: AskeyWilsonGeneratorName,
    ) -> AskeyWilsonElement[_Coefficient]: ...
    def __iter__(self) -> Iterator[AskeyWilsonElement[_Coefficient]]: ...
    def keys(self) -> tuple[AskeyWilsonGeneratorName, ...]: ...
    def values(self) -> Iterable[AskeyWilsonElement[_Coefficient]]: ...

class _MorphismHomset(
    Protocol[_SourceCoefficient, _CodomainParent, _CodomainElement],
):
    def domain(self) -> AskeyWilsonAlgebra[_SourceCoefficient]: ...
    def codomain(self) -> _CodomainParent: ...
    def homset_category(self) -> Category: ...

class AskeyWilsonElement(
    CombinatorialFreeModule.Element,
    MultiplicativeAlgebraElement,
    Generic[_Coefficient],
):
    def parent(self) -> AskeyWilsonAlgebra[_Coefficient]: ...
    def monomial_coefficients(
        self,
        copy: bool = True,
    ) -> dict[AskeyWilsonBasisIndex, _Coefficient]: ...
    def __add__(self, other: Self) -> Self: ...
    def __sub__(self, other: Self) -> Self: ...
    def __neg__(self) -> Self: ...
    @overload
    def __mul__(self, other: Self) -> Self: ...
    @overload
    def __mul__(
        self,
        other: AskeyWilsonCoefficientInput[_Coefficient],
    ) -> Self: ...
    def __rmul__(
        self,
        other: AskeyWilsonCoefficientInput[_Coefficient],
    ) -> Self: ...
    def __pow__(self, exponent: int | Integer) -> Self: ...

class AskeyWilsonAlgebra(
    CombinatorialFreeModule,
    Generic[_Coefficient],
):
    Element: type[AskeyWilsonElement[_Coefficient]]
    element_class: type[AskeyWilsonElement[_Coefficient]]

    @staticmethod
    @overload
    def __classcall_private__(
        cls: type[AskeyWilsonAlgebra[LaurentPolynomial_univariate]],
        R: Rings.ParentMethods[RingElement],
        q: None = None,
    ) -> AskeyWilsonAlgebra[LaurentPolynomial_univariate]: ...
    @staticmethod
    @overload
    def __classcall_private__(
        cls: type[AskeyWilsonAlgebra[_Coefficient]],
        R: Rings.ParentMethods[_Coefficient],
        q: AskeyWilsonCoefficientInput[_Coefficient],
    ) -> AskeyWilsonAlgebra[_Coefficient]: ...
    def __init__(
        self,
        R: Rings.ParentMethods[_Coefficient],
        q: _Coefficient,
    ) -> None: ...
    def base_ring(self) -> Rings.ParentMethods[_Coefficient]: ...
    def _repr_term(self, t: AskeyWilsonBasisIndex) -> str: ...
    def _latex_term(self, t: AskeyWilsonBasisIndex) -> str: ...
    def _repr_(self) -> str: ...
    def algebra_generators(
        self,
    ) -> _AskeyWilsonGeneratorFamily[_Coefficient]: ...
    def gens(
        self,
    ) -> tuple[
        AskeyWilsonElement[_Coefficient],
        AskeyWilsonElement[_Coefficient],
        AskeyWilsonElement[_Coefficient],
        AskeyWilsonElement[_Coefficient],
        AskeyWilsonElement[_Coefficient],
        AskeyWilsonElement[_Coefficient],
    ]: ...
    def one_basis(self) -> AskeyWilsonBasisIndex: ...
    def q(self) -> _Coefficient: ...
    def _an_element_(self) -> AskeyWilsonElement[_Coefficient]: ...
    def an_element(self) -> AskeyWilsonElement[_Coefficient]: ...
    def some_elements(
        self,
    ) -> tuple[AskeyWilsonElement[_Coefficient], ...]: ...
    def casimir_element(self) -> AskeyWilsonElement[_Coefficient]: ...
    def product_on_basis(
        self,
        x: AskeyWilsonBasisIndex,
        y: AskeyWilsonBasisIndex,
    ) -> AskeyWilsonElement[_Coefficient]: ...
    def monomial(
        self,
        index: AskeyWilsonBasisIndex,
    ) -> AskeyWilsonElement[_Coefficient]: ...
    def one(self) -> AskeyWilsonElement[_Coefficient]: ...
    def prod(
        self,
        elements: Iterable[AskeyWilsonElement[_Coefficient]],
    ) -> AskeyWilsonElement[_Coefficient]: ...
    def permutation_automorphism(
        self,
    ) -> AlgebraMorphism[
        _Coefficient,
        AskeyWilsonAlgebra[_Coefficient],
        AskeyWilsonElement[_Coefficient],
    ]: ...
    def rho(
        self,
    ) -> AlgebraMorphism[
        _Coefficient,
        AskeyWilsonAlgebra[_Coefficient],
        AskeyWilsonElement[_Coefficient],
    ]: ...
    def reflection_automorphism(
        self,
    ) -> AlgebraMorphism[
        _Coefficient,
        AskeyWilsonAlgebra[_Coefficient],
        AskeyWilsonElement[_Coefficient],
    ]: ...
    def sigma(
        self,
    ) -> AlgebraMorphism[
        _Coefficient,
        AskeyWilsonAlgebra[_Coefficient],
        AskeyWilsonElement[_Coefficient],
    ]: ...
    def loop_representation(
        self,
    ) -> AlgebraMorphism[
        _Coefficient,
        MatrixSpace,
        Matrix[LaurentPolynomial_univariate],
    ]: ...
    def pi(
        self,
    ) -> AlgebraMorphism[
        _Coefficient,
        MatrixSpace,
        Matrix[LaurentPolynomial_univariate],
    ]: ...

def _basis_key(
    t: AskeyWilsonBasisIndex,
) -> tuple[int, AskeyWilsonExponentVector]: ...

class AlgebraMorphism(
    ModuleMorphismByLinearity,
    Generic[_Coefficient, _CodomainParent, _CodomainElement],
):
    _on_generators: tuple[
        _CodomainElement,
        _CodomainElement,
        _CodomainElement,
        _CodomainElement,
        _CodomainElement,
        _CodomainElement,
    ]

    def __init__(
        self,
        domain: AskeyWilsonAlgebra[_Coefficient],
        on_generators: Sequence[_CodomainElement],
        position: int = 0,
        codomain: _CodomainParent | None = None,
        category: Category | None = None,
    ) -> None: ...
    def domain(self) -> AskeyWilsonAlgebra[_Coefficient]: ...
    def codomain(self) -> _CodomainParent: ...
    def __call__(
        self,
        x: AskeyWilsonElement[_Coefficient],
    ) -> _CodomainElement: ...
    def __eq__(self, other: object) -> bool: ...
    def _on_basis(
        self,
        c: AskeyWilsonBasisIndex,
    ) -> _CodomainElement: ...
    def _composition_(
        self,
        right: AlgebraMorphism[
            _SourceCoefficient,
            AskeyWilsonAlgebra[_Coefficient],
            AskeyWilsonElement[_Coefficient],
        ],
        homset: _MorphismHomset[
            _SourceCoefficient,
            _CodomainParent,
            _CodomainElement,
        ],
    ) -> AlgebraMorphism[
        _SourceCoefficient,
        _CodomainParent,
        _CodomainElement,
    ]: ...
