from functools import partial
from typing import TypeVar

from sage.misc.classcall_metaclass import ClasscallMetaclass
from sage.misc.nested_class import NestedClassMetaclass

_T = TypeVar("_T", bound=type)

class BindableClass(metaclass=ClasscallMetaclass):
    @staticmethod
    def __classget__(cls: type[_T], instance: object | None, owner: type) -> _T | type[_T]: ...

class BoundClass(partial[BindableClass]):
    __doc__: str | None
    def __init__(self, *args: object) -> None: ...

class Inner2(BindableClass): ...

class Outer(metaclass=NestedClassMetaclass):
    class Inner(BindableClass): ...
    Inner2: type[Inner2]
