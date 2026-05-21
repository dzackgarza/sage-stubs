from collections.abc import Callable
from typing import TypeVar, overload

_F = TypeVar("_F", bound=Callable[..., object])

class AbstractMethod: ...

@overload
def abstract_method(func: None = None, /, *, optional: bool = False) -> Callable[[_F], _F]: ...
@overload
def abstract_method(func: _F, /, *, optional: bool = False) -> _F: ...
