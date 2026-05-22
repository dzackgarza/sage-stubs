from collections.abc import Callable
from typing import TypeVar

from sage.misc.classcall_metaclass import ClasscallMetaclass

_T = TypeVar("_T")

class CmpKey:
    count: int
    def __init__(self) -> None: ...
    def __get__(self, inst: object, cls: type) -> tuple[int, int]: ...

class CmpKeyNamed:
    def __get__(self, inst: object, cls: type) -> tuple[int, int]: ...

_cmp_key: CmpKey
_cmp_key_named: CmpKeyNamed

def C3_merge(lists: list[list[object]]) -> list[object]: ...
def identity(x: _T) -> _T: ...
def C3_sorted_merge(
    lists: list[list[object]],
    key: Callable[[object], object] = ...,
) -> tuple[list[object], list[object]]: ...

class HierarchyElement(object, metaclass=ClasscallMetaclass):
    value: object
    _bases: list[HierarchyElement]
    _key: Callable[[object], object]
    _from_value: Callable[[object], HierarchyElement]

    @staticmethod
    def __classcall__(
        cls: type,
        value: object,
        succ: object,
        key: Callable[[object], object] | None = None,
    ) -> HierarchyElement: ...
    def __init__(
        self,
        value: object,
        bases: list[HierarchyElement],
        key: Callable[[object], object],
        from_value: Callable[[object], HierarchyElement],
    ) -> None: ...
    @property
    def bases(self) -> list[HierarchyElement]: ...
    @property
    def mro(self) -> list[object]: ...
    @property
    def _bases_controlled(self) -> list[object]: ...
    @property
    def mro_standard(self) -> list[object]: ...
    @property
    def mro_controlled(self) -> list[object]: ...
    def _test_mro(self) -> None: ...
    @property
    def cls(self) -> type: ...
    def all_bases(self) -> set[HierarchyElement]: ...
    def all_bases_len(self) -> int: ...
    def all_bases_controlled_len(self) -> int: ...
