from collections.abc import Callable
from typing import Generic, TypeVar, overload

_Owner = TypeVar("_Owner")
_Value = TypeVar("_Value")

class _lazy_attribute(Generic[_Owner, _Value]):
    f: Callable[[_Owner], _Value]
    __name__: str
    __doc__: str | None
    __module__: str
    def __init__(self, f: Callable[[_Owner], _Value]) -> None: ...
    def _sage_src_lines_(self) -> tuple[list[str], int]: ...
    @overload
    def __get__(self, instance: None, owner: type[_Owner]) -> _lazy_attribute[_Owner, _Value]: ...
    @overload
    def __get__(self, instance: _Owner, owner: type[_Owner]) -> _Value: ...

class lazy_attribute(_lazy_attribute[_Owner, _Value]):
    def __init__(self, f: Callable[[_Owner], _Value]) -> None: ...

class lazy_class_attribute(_lazy_attribute[_Owner, _Value]):
    @overload
    def __get__(self, instance: None, owner: type[_Owner]) -> lazy_class_attribute[_Owner, _Value]: ...
    @overload
    def __get__(self, instance: _Owner, owner: type[_Owner]) -> _Value: ...
