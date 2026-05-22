from collections.abc import Callable
from functools import partial
from inspect import FullArgSpec
from typing import TypeVar

from sage.structure.sage_object import SageObject

_F = TypeVar("_F", bound=Callable[..., SageObject])

def sage_wraps(
    wrapped: Callable[..., SageObject],
    assigned: tuple[str, ...] | set[str] = ...,
    updated: tuple[str, ...] | set[str] = ...,
) -> Callable[[_F], _F]: ...

class infix_operator:
    operators: dict[str, dict[str, str]]
    precedence: str
    def __init__(self, precedence: str) -> None: ...
    def __call__(self, func: Callable[[SageObject, SageObject], SageObject]) -> _infix_wrapper: ...

class _infix_wrapper:
    function: Callable[..., SageObject] | None
    left: SageObject | None
    right: SageObject | None
    def __init__(self, left: SageObject | None = None, right: SageObject | None = None) -> None: ...
    def __call__(self, *args: object, **kwds: object) -> SageObject: ...
    def _left(self, right: SageObject) -> SageObject: ...
    def _right(self, left: SageObject) -> SageObject: ...

def decorator_defaults(func: _F) -> _F: ...

class suboptions:
    name: str
    options: dict[str, object]
    def __init__(self, name: str, **options: object) -> None: ...
    def __call__(self, func: _F) -> _F: ...

class options:
    options: dict[str, object]
    original_opts: bool
    def __init__(self, **options: object) -> None: ...
    def __call__(self, func: _F) -> _F: ...

class rename_keyword:
    renames: dict[str, str]
    deprecation: int | None
    def __init__(self, deprecated: None = None, deprecation: int | None = None, **renames: str) -> None: ...
    def __call__(self, func: _F) -> _F: ...

class specialize:
    args: tuple[object, ...]
    kwargs: dict[str, object]
    def __init__(self, *args: object, **kwargs: object) -> None: ...
    def __call__(self, f: Callable[..., SageObject]) -> partial[SageObject]: ...

def decorator_keywords(func: _F) -> _F: ...
