from collections.abc import Sequence
from types import TracebackType

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.rings.ring import Ring
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.parent_base import ParentWithBase
from typing import TypeAlias

ParentWithGensState: TypeAlias = dict[
    str,
    Ring | tuple[Element, ...] | tuple[str, ...] | list[Element] | str | None,
]

class ParentWithGens(ParentWithBase):
    def __init__(
        self,
        base: Ring,
        names: str | tuple[str, ...] | None = None,
        normalize: bool = True,
        category: Category | None = None,
    ) -> None: ...
    def ngens(self) -> int: ...
    def gen(self, i: int = 0) -> Element: ...
    def gens(self) -> tuple[Element, ...]: ...
    def _assign_names(
        self,
        names: str | tuple[str, ...] | None = None,
        normalize: bool = True,
    ) -> None: ...
    def __getstate__(self) -> ParentWithGensState: ...
    def __setstate__(self, d: ParentWithGensState) -> None: ...
    def hom(
        self,
        im_gens: Parent | Sequence[Element],
        codomain: Parent | None = None,
        base_map: Morphism | None = None,
        category: Category | None = None,
        check: bool = True,
    ) -> Morphism: ...

class localvars:
    def __init__(
        self,
        obj: ParentWithGens,
        names: str | tuple[str, ...],
        latex_names: str | tuple[str, ...] | None = None,
        normalize: bool = True,
    ) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
