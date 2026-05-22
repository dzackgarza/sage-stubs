from collections.abc import Callable
from types import (
    BuiltinFunctionType,
    FunctionType,
    MethodDescriptorType,
    MethodType,
    WrapperDescriptorType,
)
from typing import TypeAlias, TypeVar, overload

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

_D = TypeVar("_D")

def shortrepr(obj: object, max: int = 50) -> str: ...
@overload
def getattr_debug(obj: object, name: str) -> AttributeValue: ...
@overload
def getattr_debug(obj: object, name: str, default: _D) -> AttributeValue | _D: ...
def type_debug(cls: type) -> None: ...
