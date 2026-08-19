from collections.abc import Hashable, Iterable
from typing import Generic, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.words.finite_word import FiniteWord_class
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type ShuffleElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    FiniteWord_class,
    _Scalar,
]
type ShuffleTensorElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    tuple[FiniteWord_class, FiniteWord_class],
    _Scalar,
]
type AlphabetInput = str | Iterable[Hashable]

class ShuffleAlgebra(
    CombinatorialFreeModule,
    Generic[_Scalar],
):
    Element: type[ShuffleElement[_Scalar]]
    element_class: type[ShuffleElement[_Scalar]]

    @staticmethod
    def __classcall_private__(
        cls: type[ShuffleAlgebra[_Scalar]],
        R: Ring,
        names: AlphabetInput,
        prefix: str | None = ...,
    ) -> ShuffleAlgebra[_Scalar]: ...
    def __init__(
        self,
        R: Ring,
        names: tuple[str, ...],
        prefix: str,
    ) -> None: ...
    def base_ring(self) -> Ring: ...
    def variable_names(self) -> tuple[str, ...]: ...
    def _repr_term(self, t: FiniteWord_class) -> str: ...
    def _repr_(self) -> str: ...
    def one_basis(self) -> FiniteWord_class: ...
    def one(self) -> ShuffleElement[_Scalar]: ...
    def zero(self) -> ShuffleElement[_Scalar]: ...
    def monomial(
        self,
        index: FiniteWord_class,
    ) -> ShuffleElement[_Scalar]: ...
    def term(
        self,
        index: FiniteWord_class,
        coeff: _Scalar,
    ) -> ShuffleElement[_Scalar]: ...
    def product_on_basis(
        self,
        w1: FiniteWord_class,
        w2: FiniteWord_class,
    ) -> ShuffleElement[_Scalar]: ...
    def antipode_on_basis(
        self,
        w: FiniteWord_class,
    ) -> ShuffleElement[_Scalar]: ...
    def gen(self, i: int | Integer) -> ShuffleElement[_Scalar]: ...
    def some_elements(self) -> list[ShuffleElement[_Scalar]]: ...
    def coproduct_on_basis(
        self,
        w: FiniteWord_class,
    ) -> ShuffleTensorElement[_Scalar]: ...
    def counit(self, S: ShuffleElement[_Scalar]) -> _Scalar: ...
    def degree_on_basis(self, w: FiniteWord_class) -> Integer: ...
    def algebra_generators(self) -> AbstractFamily: ...
    gens = algebra_generators
    def _element_constructor_(
        self,
        x: ShuffleElement[_Scalar]
        | DualPBWElement[_Scalar]
        | FiniteWord_class
        | str
        | Element,
    ) -> ShuffleElement[_Scalar]: ...
    def _coerce_map_from_(self, R: Parent) -> bool: ...
    def dual_pbw_basis(self) -> DualPBWBasis[_Scalar]: ...
    def to_dual_pbw_element(
        self,
        w: ShuffleElement[_Scalar],
    ) -> DualPBWElement[_Scalar]: ...

class DualPBWElement(
    IndexedFreeModuleElement[FiniteWord_class, _Scalar],
    Generic[_Scalar],
):
    def parent(self) -> DualPBWBasis[_Scalar]: ...
    def expand(self) -> ShuffleElement[_Scalar]: ...

class DualPBWBasis(
    CombinatorialFreeModule,
    Generic[_Scalar],
):
    Element: type[DualPBWElement[_Scalar]]
    element_class: type[DualPBWElement[_Scalar]]
    expansion: ModuleMorphism[
        FiniteWord_class,
        FiniteWord_class,
        _Scalar,
    ]

    @staticmethod
    def __classcall_private__(
        cls: type[DualPBWBasis[_Scalar]],
        R: Ring,
        names: AlphabetInput,
    ) -> DualPBWBasis[_Scalar]: ...
    def __init__(self, R: Ring, names: tuple[str, ...]) -> None: ...
    def base_ring(self) -> Ring: ...
    def _repr_term(self, t: FiniteWord_class) -> str: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: DualPBWElement[_Scalar]
        | ShuffleElement[_Scalar]
        | FiniteWord_class
        | str
        | Element,
    ) -> DualPBWElement[_Scalar]: ...
    def _coerce_map_from_(self, R: Parent) -> bool: ...
    def one_basis(self) -> FiniteWord_class: ...
    def one(self) -> DualPBWElement[_Scalar]: ...
    def zero(self) -> DualPBWElement[_Scalar]: ...
    def monomial(
        self,
        index: FiniteWord_class,
    ) -> DualPBWElement[_Scalar]: ...
    def counit(self, S: DualPBWElement[_Scalar]) -> _Scalar: ...
    def algebra_generators(self) -> tuple[DualPBWElement[_Scalar], ...]: ...
    gens = algebra_generators
    def gen(self, i: int | Integer) -> DualPBWElement[_Scalar]: ...
    def some_elements(self) -> list[DualPBWElement[_Scalar]]: ...
    def shuffle_algebra(self) -> ShuffleAlgebra[_Scalar]: ...
    def product(
        self,
        u: DualPBWElement[_Scalar],
        v: DualPBWElement[_Scalar],
    ) -> DualPBWElement[_Scalar]: ...
    def antipode(
        self,
        elt: DualPBWElement[_Scalar],
    ) -> DualPBWElement[_Scalar]: ...
    def coproduct(
        self,
        elt: DualPBWElement[_Scalar],
    ) -> ShuffleTensorElement[_Scalar]: ...
    def degree_on_basis(self, w: FiniteWord_class) -> Integer: ...
    def expansion_on_basis(
        self,
        w: FiniteWord_class,
    ) -> ShuffleElement[_Scalar]: ...
