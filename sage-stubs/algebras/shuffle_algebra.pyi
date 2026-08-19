from collections.abc import Hashable, Iterable, Sequence
from typing import Generic, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.words.finite_word import FiniteWord_class
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Letter = TypeVar("_Letter", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type ShuffleElement[
    _Letter: Hashable,
    _Scalar: RingElement,
] = IndexedFreeModuleElement[FiniteWord_class[_Letter], _Scalar]
type ShuffleTensorElement[
    _Letter: Hashable,
    _Scalar: RingElement,
] = IndexedFreeModuleElement[
    tuple[FiniteWord_class[_Letter], FiniteWord_class[_Letter]],
    _Scalar,
]
type AlphabetInput[_Letter: Hashable] = (
    str
    | Iterable[_Letter]
    | Parent[_Letter]
)


class ShuffleAlgebra(
    CombinatorialFreeModule,
    Generic[_Letter, _Scalar],
):
    Element: type[ShuffleElement[_Letter, _Scalar]]
    element_class: type[ShuffleElement[_Letter, _Scalar]]

    @staticmethod
    def __classcall_private__(
        cls: type[ShuffleAlgebra[_Letter, _Scalar]],
        R: Ring,
        names: AlphabetInput[_Letter],
        prefix: str | None = ...,
    ) -> ShuffleAlgebra[_Letter, _Scalar]: ...
    def __init__(
        self,
        R: Ring,
        names: Parent[_Letter],
        prefix: str,
    ) -> None: ...
    def base_ring(self) -> Ring: ...
    def variable_names(self) -> Parent[_Letter]: ...
    def _repr_term(self, t: FiniteWord_class[_Letter]) -> str: ...
    def _repr_(self) -> str: ...
    def one_basis(self) -> FiniteWord_class[_Letter]: ...
    def one(self) -> ShuffleElement[_Letter, _Scalar]: ...
    def zero(self) -> ShuffleElement[_Letter, _Scalar]: ...
    def monomial(
        self,
        index: FiniteWord_class[_Letter],
    ) -> ShuffleElement[_Letter, _Scalar]: ...
    def term(
        self,
        index: FiniteWord_class[_Letter],
        coeff: _Scalar,
    ) -> ShuffleElement[_Letter, _Scalar]: ...
    def product_on_basis(
        self,
        w1: FiniteWord_class[_Letter],
        w2: FiniteWord_class[_Letter],
    ) -> ShuffleElement[_Letter, _Scalar]: ...
    def antipode_on_basis(
        self,
        w: FiniteWord_class[_Letter],
    ) -> ShuffleElement[_Letter, _Scalar]: ...
    def gen(self, i: int | Integer) -> ShuffleElement[_Letter, _Scalar]: ...
    def some_elements(self) -> list[ShuffleElement[_Letter, _Scalar]]: ...
    def coproduct_on_basis(
        self,
        w: FiniteWord_class[_Letter],
    ) -> ShuffleTensorElement[_Letter, _Scalar]: ...
    def counit(self, S: ShuffleElement[_Letter, _Scalar]) -> _Scalar: ...
    def degree_on_basis(self, w: FiniteWord_class[_Letter]) -> Integer: ...
    def algebra_generators(self) -> AbstractFamily: ...
    gens = algebra_generators
    def _element_constructor_(
        self,
        x: ShuffleElement[_Letter, _Scalar]
        | DualPBWElement[_Letter, _Scalar]
        | FiniteWord_class[_Letter]
        | Iterable[_Letter]
        | _Scalar
        | ElementConstructorInput,
    ) -> ShuffleElement[_Letter, _Scalar]: ...
    def _coerce_map_from_(
        self,
        R: Ring | ShuffleAlgebra | DualPBWBasis,
    ) -> bool: ...
    def dual_pbw_basis(self) -> DualPBWBasis[_Letter, _Scalar]: ...
    def to_dual_pbw_element(
        self,
        w: ShuffleElement[_Letter, _Scalar],
    ) -> DualPBWElement[_Letter, _Scalar]: ...


class DualPBWElement(
    IndexedFreeModuleElement[FiniteWord_class[_Letter], _Scalar],
    Generic[_Letter, _Scalar],
):
    def parent(self) -> DualPBWBasis[_Letter, _Scalar]: ...
    def expand(self) -> ShuffleElement[_Letter, _Scalar]: ...


class DualPBWBasis(
    CombinatorialFreeModule,
    Generic[_Letter, _Scalar],
):
    Element: type[DualPBWElement[_Letter, _Scalar]]
    element_class: type[DualPBWElement[_Letter, _Scalar]]
    expansion: ModuleMorphism[
        FiniteWord_class[_Letter],
        FiniteWord_class[_Letter],
        _Scalar,
    ]

    @staticmethod
    def __classcall_private__(
        cls: type[DualPBWBasis[_Letter, _Scalar]],
        R: Ring,
        names: AlphabetInput[_Letter],
    ) -> DualPBWBasis[_Letter, _Scalar]: ...
    def __init__(self, R: Ring, names: Parent[_Letter]) -> None: ...
    def base_ring(self) -> Ring: ...
    def variable_names(self) -> Parent[_Letter]: ...
    def _repr_term(self, t: FiniteWord_class[_Letter]) -> str: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: DualPBWElement[_Letter, _Scalar]
        | ShuffleElement[_Letter, _Scalar]
        | FiniteWord_class[_Letter]
        | Iterable[_Letter]
        | _Scalar
        | ElementConstructorInput,
    ) -> DualPBWElement[_Letter, _Scalar]: ...
    def _coerce_map_from_(
        self,
        R: Ring | ShuffleAlgebra | DualPBWBasis,
    ) -> bool: ...
    def one_basis(self) -> FiniteWord_class[_Letter]: ...
    def one(self) -> DualPBWElement[_Letter, _Scalar]: ...
    def zero(self) -> DualPBWElement[_Letter, _Scalar]: ...
    def monomial(
        self,
        index: FiniteWord_class[_Letter],
    ) -> DualPBWElement[_Letter, _Scalar]: ...
    def counit(self, S: DualPBWElement[_Letter, _Scalar]) -> _Scalar: ...
    def algebra_generators(
        self,
    ) -> tuple[DualPBWElement[_Letter, _Scalar], ...]: ...
    gens = algebra_generators
    def gen(self, i: int | Integer) -> DualPBWElement[_Letter, _Scalar]: ...
    def some_elements(self) -> list[DualPBWElement[_Letter, _Scalar]]: ...
    def shuffle_algebra(self) -> ShuffleAlgebra[_Letter, _Scalar]: ...
    def product(
        self,
        u: DualPBWElement[_Letter, _Scalar],
        v: DualPBWElement[_Letter, _Scalar],
    ) -> DualPBWElement[_Letter, _Scalar]: ...
    def antipode(
        self,
        elt: DualPBWElement[_Letter, _Scalar],
    ) -> DualPBWElement[_Letter, _Scalar]: ...
    def coproduct(
        self,
        elt: DualPBWElement[_Letter, _Scalar],
    ) -> ShuffleTensorElement[_Letter, _Scalar]: ...
    def degree_on_basis(self, w: FiniteWord_class[_Letter]) -> Integer: ...
    def expansion_on_basis(
        self,
        w: FiniteWord_class[_Letter],
    ) -> ShuffleElement[_Letter, _Scalar]: ...
