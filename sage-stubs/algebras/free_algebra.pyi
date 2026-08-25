from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Generic, Literal, Protocol, TypeVar, overload

from sage.algebras.free_algebra_element import FreeAlgebraElement
from sage.algebras.free_algebra_quotient import FreeAlgebraQuotient
from sage.algebras.letterplace.free_algebra_letterplace import (
    FreeAlgebra_letterplace,
)
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.pushout import ConstructionFunctor
from sage.categories.rings import Rings
from sage.combinat.free_module import (
    CombinatorialCoercionResult,
    CombinatorialFreeModule,
)
from sage.combinat.words.finite_word import FiniteWord_class
from sage.matrix.matrix0 import Matrix
from sage.monoids.free_monoid import FreeMonoid
from sage.monoids.free_monoid_element import FreeMonoidElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.plural import NCPolynomialRing_plural
from sage.rings.polynomial.term_order import TermOrder
from sage.structure.element import Element, RingElement
from sage.structure.factorization import Factorization
from sage.structure.factory import (
    FactoryArgument,
    FactoryCacheKey,
    FactoryVersion,
    UniqueFactory,
)
from sage.structure.parent import ElementConstructorInput, Parent

type FreeAlgebraNames = str | Sequence[str]
type FreeAlgebraDegree = int | Integer
type FreeAlgebraDegrees = FreeAlgebraDegree | Sequence[FreeAlgebraDegree]
type FreeAlgebraImplementation = Literal["generic", "letterplace"]
type FreeAlgebraFactoryArgument = int | Integer | FreeAlgebraNames | None
type FreeAlgebraElementInput[_Coefficient: RingElement] = (
    FreeAlgebraElement[_Coefficient]
    | FreeMonoidElement
    | Factorization
    | ElementConstructorInput
    | str
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
)
_FactoryCoefficient = TypeVar("_FactoryCoefficient", bound=RingElement)
_TargetElement = TypeVar("_TargetElement", bound=Element)
_TargetCoefficient = TypeVar("_TargetCoefficient", bound=RingElement)
_SourceCoefficient = TypeVar("_SourceCoefficient", bound=RingElement)

class FreeAlgebraGeneratorFamily(Protocol[_GeneratorCoefficient]):
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[FreeAlgebraElement[_GeneratorCoefficient]]: ...
    def __getitem__(
        self,
        name: str,
    ) -> FreeAlgebraElement[_GeneratorCoefficient]: ...
    def keys(self) -> Iterable[str]: ...
    def values(self) -> Iterable[FreeAlgebraElement[_GeneratorCoefficient]]: ...
    def items(
        self,
    ) -> Iterable[tuple[str, FreeAlgebraElement[_GeneratorCoefficient]]]: ...

class FreeAlgebraConstructor(Protocol):
    @overload
    def __call__(
        self,
        base_ring: Rings.ParentMethods[_FactoryCoefficient],
        arg1: FreeAlgebraFactoryArgument = ...,
        arg2: FreeAlgebraFactoryArgument = ...,
        sparse: bool | None = ...,
        order: str | TermOrder | None = ...,
        *,
        names: FreeAlgebraNames | None = ...,
        name: str | None = ...,
        implementation: Literal["generic"] | None = ...,
        degrees: FreeAlgebraDegrees | None = ...,
    ) -> FreeAlgebra_generic[_FactoryCoefficient]: ...
    @overload
    def __call__(
        self,
        base_ring: Rings.ParentMethods[_FactoryCoefficient],
        arg1: FreeAlgebraFactoryArgument = ...,
        arg2: FreeAlgebraFactoryArgument = ...,
        sparse: bool | None = ...,
        order: str | TermOrder | None = ...,
        *,
        names: FreeAlgebraNames | None = ...,
        name: str | None = ...,
        implementation: Literal["letterplace"],
        degrees: FreeAlgebraDegrees | None = ...,
    ) -> FreeAlgebra_letterplace[_FactoryCoefficient]: ...
    @overload
    def __call__(
        self,
        base_ring: Rings.ParentMethods[_FactoryCoefficient],
        arg1: FreeAlgebraFactoryArgument = ...,
        arg2: FreeAlgebraFactoryArgument = ...,
        sparse: bool | None = ...,
        order: str | TermOrder | None = ...,
        *,
        names: FreeAlgebraNames | None = ...,
        name: str | None = ...,
        implementation: FreeAlgebraImplementation | None = ...,
        degrees: FreeAlgebraDegrees | None = ...,
    ) -> (
        FreeAlgebra_generic[_FactoryCoefficient]
        | FreeAlgebra_letterplace[_FactoryCoefficient]
    ): ...

class FreeAlgebraFactory(UniqueFactory):
    def create_key(
        self,
        *args: FactoryArgument,
        **kwds: FactoryArgument,
    ) -> FactoryCacheKey: ...
    def create_object(
        self,
        version: FactoryVersion,
        key: FactoryCacheKey,
        **extra_args: FactoryArgument,
    ) -> FreeAlgebra_generic[RingElement] | FreeAlgebra_letterplace[RingElement]: ...

FreeAlgebra: FreeAlgebraConstructor

class FreeAlgebra_generic(
    CombinatorialFreeModule,
    Generic[_Coefficient],
):
    def __init__(
        self,
        R: Rings.ParentMethods[_Coefficient],
        n: int | Integer,
        names: FreeAlgebraNames,
        degrees: Sequence[FreeAlgebraDegree] | None = ...,
    ) -> None: ...
    def construction(
        self,
    ) -> tuple[AssociativeFunctor, Rings.ParentMethods[_Coefficient]]: ...
    def one_basis(self) -> FreeMonoidElement: ...
    def is_field(self, proof: bool = ...) -> bool: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _element_constructor_(
        self,
        x: FreeAlgebraElementInput[_Coefficient],
    ) -> FreeAlgebraElement[_Coefficient]: ...
    def _coerce_map_from_(
        self,
        R: Parent | type,
        /,
    ) -> CombinatorialCoercionResult: ...
    def _is_valid_homomorphism_(
        self,
        other: Parent[_TargetElement],
        im_gens: Sequence[_TargetElement],
        base_map: Callable[[_Coefficient], _TargetElement] | None = ...,
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
        names: FreeAlgebraNames | None = ...,
        **args: FreeAlgebraQuotientKwarg,
    ) -> FreeAlgebraQuotient[_Coefficient]: ...
    @overload
    def quotient(
        self,
        mons: FreeAlgebraIdealInput[_Coefficient],
        mats: None = ...,
        names: FreeAlgebraNames | None = ...,
        **args: FreeAlgebraQuotientKwarg,
    ) -> Parent: ...
    @overload
    def quo(
        self,
        mons: FreeAlgebraQuotientBasis,
        mats: FreeAlgebraQuotientMatrices[_Coefficient],
        names: FreeAlgebraNames | None = ...,
        **args: FreeAlgebraQuotientKwarg,
    ) -> FreeAlgebraQuotient[_Coefficient]: ...
    @overload
    def quo(
        self,
        mons: FreeAlgebraIdealInput[_Coefficient],
        mats: None = ...,
        names: FreeAlgebraNames | None = ...,
        **args: FreeAlgebraQuotientKwarg,
    ) -> Parent: ...
    def ngens(self) -> int: ...
    def monoid(self) -> FreeMonoid: ...
    def g_algebra(
        self,
        relations: FreeAlgebraRelation[_Coefficient],
        names: FreeAlgebraNames | None = ...,
        order: str | TermOrder = ...,
        check: bool = ...,
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
        def expand(self) -> FreeAlgebraElement[RingElement]: ...

    @staticmethod
    def __classcall_private__(
        class_: type[PBWBasisOfFreeAlgebra[_Coefficient]],
        R: FreeAlgebra_generic[_Coefficient] | Rings.ParentMethods[_Coefficient],
        n: int | Integer | None = ...,
        names: FreeAlgebraNames | None = ...,
    ) -> PBWBasisOfFreeAlgebra[_Coefficient]: ...
    def __init__(self, alg: FreeAlgebra_generic[_Coefficient]) -> None: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, w: FreeMonoidElement) -> str: ...
    def _element_constructor_(
        self,
        x: FreeAlgebraElement[_Coefficient] | ElementConstructorInput,
    ) -> PBWBasisOfFreeAlgebra.Element: ...
    def _coerce_map_from_(
        self,
        R: Parent | type,
        /,
    ) -> CombinatorialCoercionResult: ...
    def one_basis(self) -> FreeMonoidElement: ...
    def algebra_generators(
        self,
    ) -> tuple[PBWBasisOfFreeAlgebra.Element, ...]: ...
    def gens(self) -> tuple[PBWBasisOfFreeAlgebra.Element, ...]: ...
    def gen(self, i: int | Integer) -> PBWBasisOfFreeAlgebra.Element: ...
    def free_algebra(self) -> FreeAlgebra_generic[_Coefficient]: ...
    def product(
        self,
        u: PBWBasisOfFreeAlgebra.Element,
        v: PBWBasisOfFreeAlgebra.Element,
    ) -> PBWBasisOfFreeAlgebra.Element: ...
    def expansion(
        self,
        t: PBWBasisOfFreeAlgebra.Element,
    ) -> FreeAlgebraElement[_Coefficient]: ...

class AssociativeFunctor(ConstructionFunctor):
    rank: int
    vars: Sequence[str]
    degs: Sequence[FreeAlgebraDegree] | Mapping[str, FreeAlgebraDegree] | None

    def __init__(
        self,
        vars: Sequence[str],
        degs: Sequence[FreeAlgebraDegree]
        | Mapping[str, FreeAlgebraDegree]
        | None = ...,
    ) -> None: ...
    def _apply_functor(
        self,
        R: Rings.ParentMethods[_TargetCoefficient],
    ) -> FreeAlgebra_generic[_TargetCoefficient]: ...
    @overload
    def _apply_functor_to_morphism(
        self,
        f: Morphism[Element, Element],
    ) -> Morphism[Element, Element]: ...
    @overload
    def _apply_functor_to_morphism(
        self,
        f: Morphism[_SourceCoefficient, _TargetCoefficient],
    ) -> Morphism[
        FreeAlgebraElement[_SourceCoefficient],
        FreeAlgebraElement[_TargetCoefficient],
    ]: ...
    def __eq__(self, other: object) -> bool: ...
    def __mul__(self, other: ConstructionFunctor) -> ConstructionFunctor: ...
    def merge(
        self,
        other: ConstructionFunctor,
    ) -> AssociativeFunctor | None: ...
    def _repr_(self) -> str: ...
