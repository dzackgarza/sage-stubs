from typing import Any, TypeVar
from collections.abc import Callable

_F = TypeVar('_F', bound=Callable[..., Any])

def cached_method(func: _F) -> _F: ...
