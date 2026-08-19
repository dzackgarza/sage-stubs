from collections.abc import Hashable, Iterable, Mapping, Sequence
from typing import Generic, Literal, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.rooted_tree import LabelledRootedTree, RootedTree
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import RingElement

ROOT: Literal["#"]

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type GrossmanLarsonTree = RootedTree | LabelledRootedTree
type GrossmanLarsonElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    GrossmanLarsonTree,
    _Scalar,
]
type GrossmanLarsonTensorElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    tuple[GrossmanLarsonTree, GrossmanLarsonTree],
    _Scalar,
]
type GrossmanLarsonNames = str | Sequence[Hashable] | int | Integer | object | None

class GrossmanLarsonAlgebra(
    CombinatorialFreeModule,
    Generic[_Scalar],
):
    Element: type[GrossmanLarsonElement[_Scalar]]
    element_class: type[GrossmanLarsonElement[_Scalar]]

    @staticmethod
    def __classcall_private__(
        cls: type[GrossmanLarsonAlgebra[_Scalar]],
        R: Ring,
        names: GrossmanLarsonNames = ...,
    ) -> GrossmanLarsonAlgebra[_Scalar]: ...
    def __init__(
        self,
        R: Ring,
        names: object | None = ...,
    ) -> None: ...
    def base_ring(self) -> Ring: ...
    def variable_names(self) -> object: ...
    def _repr_(self) -> str: ...
    def single_vertex(
        self,
        i: int | Integer,
    ) -> GrossmanLarsonElement[_Scalar]: ...
    def single_vertex_all(
        self,
    ) -> tuple[GrossmanLarsonElement[_Scalar], ...]: ...
    def _first_ngens(
        self,
        n: int,
    ) -> tuple[GrossmanLarsonElement[_Scalar], ...]: ...
    def change_ring(
        self,
        R: Ring,
    ) -> GrossmanLarsonAlgebra[RingElement]: ...
    def degree_on_basis(self, t: GrossmanLarsonTree) -> int: ...
    def _an_element_(self) -> GrossmanLarsonElement[_Scalar]: ...
    def some_elements(self) -> list[GrossmanLarsonElement[_Scalar]]: ...
    def one_basis(self) -> GrossmanLarsonTree: ...
    def one(self) -> GrossmanLarsonElement[_Scalar]: ...
    def zero(self) -> GrossmanLarsonElement[_Scalar]: ...
    def monomial(
        self,
        index: GrossmanLarsonTree,
    ) -> GrossmanLarsonElement[_Scalar]: ...
    def _from_dict(
        self,
        d: Mapping[GrossmanLarsonTree, _Scalar],
        coerce: bool = ...,
        remove_zeros: bool = ...,
    ) -> GrossmanLarsonElement[_Scalar]: ...
    def product_on_basis(
        self,
        x: GrossmanLarsonTree,
        y: GrossmanLarsonTree,
    ) -> GrossmanLarsonElement[_Scalar]: ...
    def coproduct_on_basis(
        self,
        x: GrossmanLarsonTree,
    ) -> GrossmanLarsonTensorElement[_Scalar]: ...
    def counit_on_basis(self, x: GrossmanLarsonTree) -> _Scalar: ...
    def antipode_on_basis(
        self,
        x: GrossmanLarsonTree,
    ) -> GrossmanLarsonElement[_Scalar]: ...
    def _element_constructor_(
        self,
        x: GrossmanLarsonElement[_Scalar]
        | GrossmanLarsonTree
        | object,
    ) -> GrossmanLarsonElement[_Scalar]: ...
    def _coerce_map_from_(self, R: object) -> bool: ...
