from collections.abc import Callable
from typing import TypeVar

from sage.structure.sage_object import SageObject

_C = TypeVar("_C", bound=type)

class InstanceDocDescriptor:
    def __init__(
        self,
        classdoc: str | None,
        instancedoc: Callable[[object], str],
        attr: str = "__doc__",
    ) -> None: ...
    def __get__(self, obj: object | None, typ: type[SageObject]) -> str: ...
    def __set__(self, obj: object, value: str) -> None: ...
    def __delete__(self, obj: object) -> None: ...

def instancedoc(cls) -> type[SageObject]: ...
