from collections.abc import Iterable, Iterator, Mapping, Sequence
from typing import Generic, TypeVar

from sage.combinat.diagram_algebras import (
    TemperleyLiebDiagram,
    TemperleyLiebDiagrams,
)
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.typeset.ascii_art import AsciiArt
from sage.typeset.unicode_art import UnicodeArt

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type DiagramVertex = int | Integer
type DiagramPair = tuple[DiagramVertex, DiagramVertex]
type DiagramPairs = Iterable[Sequence[DiagramVertex]]
type BlobDiagramData = tuple[DiagramPairs, DiagramPairs]
type BlobAlgebraElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    BlobDiagram,
    _Scalar,
]

class BlobDiagram(Element):
    marked: tuple[DiagramPair, ...]
    unmarked: tuple[DiagramPair, ...]

    def __init__(
        self,
        parent: BlobDiagrams,
        marked: DiagramPairs,
        unmarked: DiagramPairs,
    ) -> None: ...
    def parent(self) -> BlobDiagrams: ...
    def _repr_(self) -> str: ...
    def __hash__(self) -> int: ...
    def _richcmp_(
        self,
        other: BlobDiagram,
        op: int,
    ) -> bool: ...
    def temperley_lieb_diagram(self) -> TemperleyLiebDiagram: ...

class BlobDiagrams(
    Parent[BlobDiagram],
    UniqueRepresentation,
):
    Element: type[BlobDiagram]
    element_class: type[BlobDiagram]

    def __init__(self, n: int | Integer) -> None: ...
    def _repr_(self) -> str: ...
    def cardinality(self) -> Integer: ...
    def order(self) -> Integer: ...
    def base_set(self) -> frozenset[int]: ...
    def _element_constructor_(
        self,
        marked: BlobDiagramData | DiagramPairs,
        unmarked: DiagramPairs | None = ...,
    ) -> BlobDiagram: ...
    def __contains__(self, X: object) -> bool: ...
    def __iter__(self) -> Iterator[BlobDiagram]: ...

class BlobAlgebra(
    CombinatorialFreeModule,
    Generic[_Scalar],
):
    Element: type[BlobAlgebraElement[_Scalar]]
    element_class: type[BlobAlgebraElement[_Scalar]]

    @staticmethod
    def __classcall_private__(
        cls: type[BlobAlgebra[_Scalar]],
        k: int | Integer,
        q1: _Scalar,
        q2: _Scalar,
        q3: _Scalar,
        base_ring: Ring | None = ...,
        prefix: str = ...,
    ) -> BlobAlgebra[_Scalar]: ...
    def __init__(
        self,
        k: int | Integer,
        q1: _Scalar,
        q2: _Scalar,
        q3: _Scalar,
        base_ring: Ring,
        prefix: str,
    ) -> None: ...
    def base_ring(self) -> Ring: ...
    def _ascii_art_term(self, diagram: BlobDiagram) -> AsciiArt: ...
    def _unicode_art_term(self, diagram: BlobDiagram) -> UnicodeArt: ...
    def _latex_term(self, diagram: BlobDiagram) -> str: ...
    def order(self) -> Integer: ...
    def one_basis(self) -> BlobDiagram: ...
    def one(self) -> BlobAlgebraElement[_Scalar]: ...
    def zero(self) -> BlobAlgebraElement[_Scalar]: ...
    def monomial(
        self,
        index: BlobDiagram,
    ) -> BlobAlgebraElement[_Scalar]: ...
    def term(
        self,
        index: BlobDiagram,
        coeff: _Scalar,
    ) -> BlobAlgebraElement[_Scalar]: ...
    def _from_dict(
        self,
        d: Mapping[BlobDiagram, _Scalar],
        coerce: bool = ...,
        remove_zeros: bool = ...,
    ) -> BlobAlgebraElement[_Scalar]: ...
    def product_on_basis(
        self,
        top: BlobDiagram,
        bot: BlobDiagram,
    ) -> BlobAlgebraElement[_Scalar]: ...
