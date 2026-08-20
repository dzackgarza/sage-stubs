from collections import defaultdict
from collections.abc import Hashable, Iterable, Mapping
from numbers import Real
from typing import Generic, TypeVar

from sage.graphs.digraph import DiGraph
from sage.structure.sage_object import SageObject

_Symbol = TypeVar("_Symbol", bound=Hashable, default=str)

type HuffmanTree = int | tuple[HuffmanTree, HuffmanTree]
type HuffmanEdge = tuple[str, str]
type WeightTable[_T: Hashable] = Mapping[_T, Real]


def frequency_table(
    string: Iterable[_Symbol],
) -> defaultdict[_Symbol, int]: ...


class Huffman(SageObject, Generic[_Symbol]):
    def __init__(
        self,
        source: str | WeightTable[_Symbol],
    ) -> None: ...
    def _build_code_from_tree(
        self,
        tree: HuffmanTree,
        code_by_index: dict[int, str],
        prefix: str,
    ) -> None: ...
    def _build_code(
        self,
        weights: WeightTable[_Symbol],
    ) -> None: ...
    def encode(
        self,
        string: Iterable[_Symbol],
    ) -> str: ...
    def decode(self, string: str) -> str: ...
    def encoding_table(self) -> dict[_Symbol, str]: ...
    def tree(self) -> DiGraph: ...
    def _generate_edges(
        self,
        tree: HuffmanTree,
        parent: str = ...,
        bit: str = ...,
    ) -> list[HuffmanEdge]: ...
