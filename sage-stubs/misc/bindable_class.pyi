from functools import partial
from typing import TypeVar, Generic

_T = TypeVar('_T')

class BindableClass:
    @staticmethod
    def __classget__(cls: type[_T], instance: object, owner: type) -> _T | type[_T]: ...

class BoundClass(partial[object]):
    __doc__: str | None
    def __init__(self, *args: object) -> None: ...

class Inner2(BindableClass): ...

class Outer:
    class Inner(BindableClass): ...
    Inner2: type[Inner2]
