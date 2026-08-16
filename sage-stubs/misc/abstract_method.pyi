from collections.abc import Callable
from typing import Generic, ParamSpec, TypeVar, overload

_P = ParamSpec("_P")
_R = TypeVar("_R")
_Class = TypeVar("_Class")

class AbstractMethod(Generic[_P, _R]):
    _f: Callable[_P, _R]

    def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> AbstractMethod: ...

@overload
def abstract_method(
    self=None, /, *, optional: bool = False
) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...
@overload
def abstract_method(
    self, /, *, optional: bool = False
) -> Callable[_P, AbstractMethod]: ...
def abstract_methods_of_class(self) -> dict[str, list[str]]: ...
