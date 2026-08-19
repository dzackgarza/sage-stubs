from collections.abc import Iterable, Iterator
from typing import Protocol

from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.root_system.weyl_group import WeylGroup_gens, WeylGroupElement
from sage.rings.integer import Integer
from sage.rings.ring import Ring

class AffineNilTemperleyLiebGeneratorFamily(Protocol):

    def __getitem__(self, i: int | Integer) -> CombinatorialFreeModule.Element: ...
    def __iter__(self) -> Iterator[CombinatorialFreeModule.Element]: ...
    def keys(self) -> Iterable[int]: ...
    def values(self) -> Iterable[CombinatorialFreeModule.Element]: ...


class AffineNilTemperleyLiebTypeA(CombinatorialFreeModule):

    Element: type[CombinatorialFreeModule.Element]

    def __init__(
        self,
        n: int | Integer,
        R: Ring = ...,
        prefix: str = "a",
    ) -> None: ...
    def _element_constructor_(
        self,
        w: WeylGroupElement,
    ) -> CombinatorialFreeModule.Element: ...
    def one_basis(self) -> WeylGroupElement: ...
    def _repr_(self) -> str: ...
    def weyl_group(self) -> WeylGroup_gens: ...
    def index_set(self) -> tuple[int, ...]: ...
    def algebra_generators(self) -> AffineNilTemperleyLiebGeneratorFamily: ...
    def algebra_generator(
        self,
        i: int | Integer,
    ) -> CombinatorialFreeModule.Element: ...
    def product_on_basis(
        self,
        w: WeylGroupElement,
        w1: WeylGroupElement,
    ) -> CombinatorialFreeModule.Element: ...
    def has_no_braid_relation(
        self,
        w: WeylGroupElement,
        i: int | Integer,
    ) -> bool: ...
    def _repr_term(
        self,
        t: WeylGroupElement,
        short_display: bool = True,
    ) -> str: ...
