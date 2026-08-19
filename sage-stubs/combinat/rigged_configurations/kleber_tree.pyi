from collections.abc import Iterable, Iterator, Sequence
from typing import TypeAlias

from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.graphs.digraph import DiGraph
from sage.plot.graphics import Graphics
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

type KleberRectangle = tuple[int | Integer, int | Integer]
type KleberRectangles = tuple[KleberRectangle, ...]
type CartanTypeInput = CartanType_abstract | Sequence[object] | str
type WeightLatticeElement = CombinatorialFreeModule.Element
type RootLatticeElement = CombinatorialFreeModule.Element

class KleberTreeNode(Element):
    parent_node: KleberTreeNode | None
    children: list[KleberTreeNode]
    weight: WeightLatticeElement
    up_root: RootLatticeElement
    depth: int

    def __init__(
        self,
        parent_obj: KleberTree,
        node_weight: WeightLatticeElement,
        dominant_root: RootLatticeElement,
        parent_node: KleberTreeNode | None = ...,
    ) -> None: ...
    def parent(self) -> KleberTree: ...
    def multiplicity(self) -> Integer: ...
    def __hash__(self) -> int: ...
    def _richcmp_(
        self,
        other: KleberTreeNode,
        op: int,
    ) -> bool: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...

class KleberTree(
    UniqueRepresentation,
    Parent[KleberTreeNode],
):
    Element: type[KleberTreeNode]
    element_class: type[KleberTreeNode]
    B: KleberRectangles
    root: KleberTreeNode

    @staticmethod
    def __classcall_private__(
        cls: type[KleberTree],
        cartan_type: CartanTypeInput,
        B: Iterable[Sequence[int | Integer]],
        classical: CartanTypeInput | None = ...,
    ) -> KleberTree: ...
    def __init__(
        self,
        cartan_type: CartanType_abstract,
        B: KleberRectangles,
        classical_ct: CartanType_abstract,
    ) -> None: ...
    def latex_options(
        self,
        **options: object,
    ) -> dict[str, object] | None: ...
    def _latex_(self) -> str: ...
    def breadth_first_iter(self) -> Iterator[KleberTreeNode]: ...
    def depth_first_iter(self) -> Iterator[KleberTreeNode]: ...
    def __iter__(self) -> Iterator[KleberTreeNode]: ...
    def _repr_(self) -> str: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def digraph(self) -> DiGraph: ...
    def plot(self, **options: object) -> Graphics: ...
    def _element_constructor_(
        self,
        node_weight: WeightLatticeElement,
        dominant_root: RootLatticeElement,
        parent_node: KleberTreeNode | None = ...,
    ) -> KleberTreeNode: ...
    def cardinality(self) -> Integer: ...
    def list(self) -> list[KleberTreeNode]: ...

class VirtualKleberTree(KleberTree):
    @staticmethod
    def __classcall_private__(
        cls: type[VirtualKleberTree],
        cartan_type: CartanTypeInput,
        B: Iterable[Sequence[int | Integer]],
    ) -> VirtualKleberTree | KleberTreeTypeA2Even: ...
    def __init__(
        self,
        cartan_type: CartanType_abstract,
        B: KleberRectangles,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def breadth_first_iter(
        self,
        all_nodes: bool = ...,
    ) -> Iterator[KleberTreeNode]: ...
    def depth_first_iter(
        self,
        all_nodes: bool = ...,
    ) -> Iterator[KleberTreeNode]: ...
    def __iter__(self) -> Iterator[KleberTreeNode]: ...
    def base_tree(self) -> KleberTree: ...

class KleberTreeTypeA2Even(VirtualKleberTree):
    @staticmethod
    def __classcall_private__(
        cls: type[KleberTreeTypeA2Even],
        cartan_type: CartanTypeInput,
        B: Iterable[Sequence[int | Integer]],
    ) -> KleberTreeTypeA2Even: ...
    def __init__(
        self,
        cartan_type: CartanType_abstract,
        B: KleberRectangles,
    ) -> None: ...
    def __iter__(self) -> Iterator[KleberTreeNode]: ...
    def breadth_first_iter(
        self,
        all_nodes: bool = ...,
    ) -> Iterator[KleberTreeNode]: ...
    def depth_first_iter(
        self,
        all_nodes: bool = ...,
    ) -> Iterator[KleberTreeNode]: ...
