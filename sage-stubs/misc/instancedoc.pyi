from collections.abc import Callable
from typing import TypeVar

_C = TypeVar("_C", bound=type)

class InstanceDocDescriptor:
    def __init__(
        self,
        classdoc: str | None,
        instancedoc: Callable[[object], str],
        attr: str = "__doc__",
    ) -> None: ...
    def __get__(self, obj: object | None, typ: type) -> str: ...
    def __set__(self, obj: object, value: str) -> None: ...
    def __delete__(self, obj: object) -> None: ...

def instancedoc(cls: _C) -> _C: ...
