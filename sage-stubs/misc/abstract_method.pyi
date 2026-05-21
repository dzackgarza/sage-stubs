from typing import Any, TypeVar
from collections.abc import Callable

_F = TypeVar('_F', bound=Callable[..., Any])

class AbstractMethod: ...

def abstract_method(func: _F, /, **kwargs: Any) -> _F: ...
