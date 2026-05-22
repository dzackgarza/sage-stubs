from collections.abc import Callable
from types import (
    BuiltinFunctionType,
    FunctionType,
    MethodDescriptorType,
    MethodType,
    WrapperDescriptorType,
)
from typing import TypeAlias

from sage.structure.sage_object import SageObject

AttributeValue: TypeAlias = (
    property
    | Callable[..., object]
    | FunctionType
    | MethodType
    | MethodDescriptorType
    | WrapperDescriptorType
    | BuiltinFunctionType
    | str
    | int
    | float
    | bool
    | type
    | SageObject
)

class AttributeErrorMessage:
    def __init__(self, obj: object | None = None, name: str = "") -> None: ...

def raw_getattr(obj: object, name: str) -> AttributeValue: ...
def getattr_from_other_class(
    self: object, cls: type, name: str | None
) -> AttributeValue: ...
def dir_with_other_class(self: object, *cls: type) -> list[str]: ...
