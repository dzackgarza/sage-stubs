from collections.abc import Callable
from typing import Generic, ParamSpec, TypeVar, overload

_P = ParamSpec("_P")
_R = TypeVar("_R")
_Class = TypeVar("_Class")

class AbstractMethod(Generic[_P, _R]):
    _f: Callable[_P, _R]
    def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _R: ...

@overload
def abstract_method(
    func: None = None,
    /,
    *,
    optional: bool = False,
) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...
@overload
def abstract_method(
    func: Callable[_P, _R],
    /,
    *,
    optional: bool = False,
) -> Callable[_P, _R]: ...

def abstract_methods_of_class(cls: type[_Class]) -> dict[str, list[str]]: ...
