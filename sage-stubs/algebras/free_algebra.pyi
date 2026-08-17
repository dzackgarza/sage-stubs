from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Generic, Literal, Protocol, Self, TypeVar, overload

from sage.algebras.free_algebra_element import FreeAlgebraElement
from sage.algebras.free_algebra_quotient import FreeAlgebraQuotient
from sage.algebras.letterplace.free_algebra_letterplace import FreeAlgebra_letterplace
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.pushout import ConstructionFunctor
from sage.categories.rings import Rings
from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.words.finite_word import FiniteWord_class
from sage.matrix.matrix0 import Matrix
from sage.monoids.free_monoid import FreeMonoid
from sage.monoids.free_monoid_element import FreeMonoidElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.plural import NCPolynomialRing_plural
from sage.rings.polynomial.term_order import TermOrder
from sage.structure.element import Element, RingElement
from sage.structure.factory import FactoryVersion, UniqueFactory
from sage.structure.parent import Parent

type FreeAlgebraNames = str | Sequence[str]
type FreeAlgebraDegree = int | Integer
type FreeAlgebraDegrees = FreeAlgebraDegree | Sequence[FreeAlgebraDegree]
type FreeAlgebraImplementation = Literal["generic", "letterplace"]
type FreeAlgebraFactoryArgument = int | Integer | FreeAlgebraNames | None
type FreeAlgebraFactoryKey = (
    tuple[Parent]
    | tuple[tuple[FreeAlgebraDegree, ...], Parent]
    | tuple[Rings.ParentMethods[RingElement], tuple[str, ...]]
    | tuple[
        Rings.ParentMethods[RingElement],
        tuple[str, ...],
        tuple[FreeAlgebraDegree, ...],
    ]
)
type FreeAlgebraElementInput[_Coefficient: RingElement] = (
    FreeAlgebraElement[_Coefficient]
    | FreeMonoidElement
    | _Coefficient
    | int
    | Integer
    | str
    | Mapping[FreeMonoidElement, _Coefficient | int | Integer]
    | Element
)
type FreeAlgebraRelation[_Coefficient: RingElement] = Mapping[
    FreeAlgebraElement[_Coefficient],
    FreeAlgebraElement[_Coefficient],
]
type FreeAlgebraIdealInput[_Coefficient: RingElement] = (
    Ideal_generic
    | FreeAlgebraElement[_Coefficient]
    | Sequence[FreeAlgebraElement[_Coefficient]]
)
type FreeAlgebraQuotientKwarg = (
    bool | str | int | Integer | Category | type[Parent] | None
)
type FreeAlgebraQuotientBasis = Sequence[FreeMonoidElement]
type FreeAlgebraQuotientMatrices[_Coefficient: RingElement] = Sequence[
    Matrix[_Coefficient]
]

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_GeneratorCoefficient = TypeVar(
    "_GeneratorCoefficient",
    bound=RingElement,
    covariant=True,
)


class FreeAlgebraGeneratorFamily(Protocol[_GeneratorCoefficient]):
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[FreeAlgebraElement[_GeneratorCoefficient]]: ...
    def __getitem__(self, name: str) -> FreeAlgebraElement[_GeneratorCoefficient]: ...
    def keys(self) -> Iterable[str]: ...
    def values(self) -> Iterable[FreeAlgebraElement[_GeneratorCoefficient]]: ...
    def items(
        self,
    ) -> Iterable[tuple[str, FreeAlgebraElement[_GeneratorCoefficient]]]: ...


class FreeAlgebraFactory(UniqueFactory):
    @overload
    def __call__[
        _FactoryCoefficient: RingElement
    ](
        self,
        base_ring: Rings.ParentMethods[_FactoryCoefficient],
        arg1: FreeAlgebraFactoryArgument = None,
        arg2: FreeAlgebraFactoryArgument = None,
        sparse: bool | None = None,
        order: str | TermOrder | None = None,
        *,
        names: FreeAlgebraNames | None = None,
        name: str | None = None,
        implementation: Literal["generic"] | None = None,
        degrees: FreeAlgebraDegrees | None = None,
    ) -> FreeAlgebra_generic[_FactoryCoefficient]: ...
    @overload
    def __call__[
        _FactoryCoefficient: RingElement
    ](
        self,
        base_ring: Rings.ParentMethods[_FactoryCoefficient],
        arg1: FreeAlgebraFactoryArgument = None,
        arg2: FreeAlgebraFactoryArgument = None,
        sparse: bool | None = None,
        order: str | TermOrder | None = None,
        *,
        names: FreeAlgebraNames | None = None,
        name: str | None = None,
        implementation: Literal["letterplace"],
        degrees: FreeAlgebraDegrees | None = None,
    ) -> FreeAlgebra_letterplace: ...

    def create_key(
        self,
        base_ring: Rings.ParentMethods[RingElement] | Parent,
        arg1: FreeAlgebraFactoryArgument = None,
        arg2: FreeAlgebraFactoryArgument = None,
        sparse: bool | None = None,
        order: str | TermOrder | None = None,
        names: FreeAlgebraNames | None = None,
        name: str | None = None,
        implementation: FreeAlgebraImplementation | None = None,
        degrees: FreeAlgebraDegrees | None = None,
    ) -> FreeAlgebraFactoryKey: ...
    def create_object(
        self,
        version: FactoryVersion | str,
        key: FreeAlgebraFactoryKey,
    ) -> FreeAlgebra_generic[RingElement] | FreeAlgebra_letterplace: ...


FreeAlgebra: FreeAlgebraFactory


class FreeAlgebra_generic(
    CombinatorialFreeModule,
    Generic[_Coefficient],
):
    Element: type[FreeAlgebraElement[_Coefficient]]
    element_class: type[FreeAlgebraElement[_Coefficient]]

    def __init__(
        self,
        R: Rings.ParentMethods[_Coefficient],
        n: int | Integer,
        names: FreeAlgebraNames,
        degrees: Sequence[FreeAlgebraDegree] | None = None,
    ) -> None: ...
    def base_ring(self) -> Rings.ParentMethods[_Coefficient]: ...
    def construction(
        self,
    ) -> tuple[AssociativeFunctor, Rings.ParentMethods[_Coefficient]]: ...
    def one_basis(self) -> FreeMonoidElement: ...
    def is_field(self, proof: bool = True) -> bool: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _element_constructor_(
        self,
        x: FreeAlgebraElementInput[_Coefficient],
    ) -> FreeAlgebraElement[_Coefficient]: ...
    def __call__(
        self,
        x: FreeAlgebraElementInput[_Coefficient] = 0,
    ) -> FreeAlgebraElement[_Coefficient]: ...
    def _coerce_map_from_(self, R: Parent | type) -> bool: ...
    def _is_valid_homomorphism_[TargetElement: Element](
        self,
        other: Parent[TargetElement],
        im_gens: Sequence[TargetElement],
        base_map: Callable[[_Coefficient], TargetElement] | None = None,
    ) -> bool: ...
    def gen(self, i: int | Integer) -> FreeAlgebraElement[_Coefficient]: ...
    def algebra_generators(
        self,
    ) -> FreeAlgebraGeneratorFamily[_Coefficient]: ...
    def gens(self) -> tuple[FreeAlgebraElement[_Coefficient], ...]: ...
    def degree_on_basis(self, m: FreeMonoidElement) -> Integer: ...
    def product_on_basis(
        self,
        x: FreeMonoidElement,
        y: FreeMonoidElement,
    ) -> FreeAlgebraElement[_Coefficient]: ...

    @overload
    def quotient(
        self,
        mons: FreeAlgebraQuotientBasis,
        mats: FreeAlgebraQuotientMatrices[_Coefficient],
        names: FreeAlgebraNames | None = None,
        **args: FreeAlgebraQuotientKwarg,
    ) -> FreeAlgebraQuotient[_Coefficient]: ...
    @overload
    def quotient(
        self,
        mons: FreeAlgebraIdealInput[_Coefficient],
        mats: None = None,
        names: FreeAlgebraNames | None = None,
        **args: FreeAlgebraQuotientKwarg,
    ) -> Parent: ...
    @overload
    def quo(
        self,
        mons: FreeAlgebraQuotientBasis,
        mats: FreeAlgebraQuotientMatrices[_Coefficient],
        names: FreeAlgebraNames | None = None,
        **args: FreeAlgebraQuotientKwarg,
    ) -> FreeAlgebraQuotient[_Coefficient]: ...
    @overload
    def quo(
        self,
        mons: FreeAlgebraIdealInput[_Coefficient],
        mats: None = None,
        names: FreeAlgebraNames | None = None,
        **args: FreeAlgebraQuotientKwarg,
    ) -> Parent: ...

    def ngens(self) -> int: ...
    def monoid(self) -> FreeMonoid: ...
    def g_algebra(
        self,
        relations: FreeAlgebraRelation[_Coefficient],
        names: FreeAlgebraNames | None = None,
        order: str | TermOrder = "degrevlex",
        check: bool = True,
    ) -> NCPolynomialRing_plural: ...
    def poincare_birkhoff_witt_basis(
        self,
    ) -> PBWBasisOfFreeAlgebra[_Coefficient]: ...
    def pbw_basis(self) -> PBWBasisOfFreeAlgebra[_Coefficient]: ...
    def pbw_element(
        self,
        elt: FreeAlgebraElement[_Coefficient],
    ) -> PBWBasisOfFreeAlgebra.Element: ...
    def lie_polynomial(
        self,
        w: FreeMonoidElement | FiniteWord_class | str,
    ) -> FreeAlgebraElement[_Coefficient]: ...


class PBWBasisOfFreeAlgebra(
    CombinatorialFreeModule,
    Generic[_Coefficient],
):
    class Element(CombinatorialFreeModule.Element):
        def parent(self) -> PBWBasisOfFreeAlgebra[RingElement]: ...
        def expand(self) -> FreeAlgebraElement[RingElement]: ...

    element_class: type[Element]

    @staticmethod
    def __classcall_private__(
        cls: type[PBWBasisOfFreeAlgebra[_Coefficient]],
        R: FreeAlgebra_generic[_Coefficient] | Rings.ParentMethods[_Coefficient],
        n: int | Integer | None = None,
        names: FreeAlgebraNames | None = None,
    ) -> PBWBasisOfFreeAlgebra[_Coefficient]: ...
    def __init__(self, alg: FreeAlgebra_generic[_Coefficient]) -> None: ...
    def base_ring(self) -> Rings.ParentMethods[_Coefficient]: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, w: FreeMonoidElement) -> str: ...
    def _element_constructor_(
        self,
        x: FreeAlgebraElement[_Coefficient]
        | FreeMonoidElement
        | Element
        | int
        | Integer,
    ) -> Element: ...
    def __call__(
        self,
        x: FreeAlgebraElement[_Coefficient]
        | FreeMonoidElement
        | Element
        | int
        | Integer = 0,
    ) -> Element: ...
    def _coerce_map_from_(self, R: Parent | type) -> bool: ...
    def one_basis(self) -> FreeMonoidElement: ...
    def algebra_generators(self) -> tuple[Element, ...]: ...
    def gens(self) -> tuple[Element, ...]: ...
    def gen(self, i: int | Integer) -> Element: ...
    def free_algebra(self) -> FreeAlgebra_generic[_Coefficient]: ...
    def product(self, u: Element, v: Element) -> Element: ...
    def expansion(self, t: Element) -> FreeAlgebraElement[_Coefficient]: ...


class AssociativeFunctor(ConstructionFunctor):
    rank: int
    vars: Sequence[str]
    degs: Sequence[FreeAlgebraDegree] | Mapping[str, FreeAlgebraDegree] | None

    def __init__(
        self,
        vars: Sequence[str],
        degs: Sequence[FreeAlgebraDegree]
        | Mapping[str, FreeAlgebraDegree]
        | None = None,
    ) -> None: ...
    def _apply_functor[
        TargetCoefficient: RingElement
    ](
        self,
        R: Rings.ParentMethods[TargetCoefficient],
    ) -> FreeAlgebra_generic[TargetCoefficient]: ...
    def _apply_functor_to_morphism[
        SourceCoefficient: RingElement,
        TargetCoefficient: RingElement,
    ](
        self,
        f: Morphism[SourceCoefficient, TargetCoefficient],
    ) -> Morphism[
        FreeAlgebraElement[SourceCoefficient],
        FreeAlgebraElement[TargetCoefficient],
    ]: ...
    def __eq__(self, other: object) -> bool: ...
    def __mul__(self, other: ConstructionFunctor) -> ConstructionFunctor: ...
    def merge(self, other: ConstructionFunctor) -> Self | None: ...
    def _repr_(self) -> str: ...
