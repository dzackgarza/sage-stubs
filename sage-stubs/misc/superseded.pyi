from collections.abc import Callable
from typing import Generic, TypeVar

_R = TypeVar("_R")
_F = TypeVar("_F", bound=Callable[..., object])

def _check_issue_number(issue_number: int) -> None: ...
def deprecation(issue_number: int, message: str, stacklevel: int = 4) -> None: ...
def deprecation_cython(issue_number: int, message: str, stacklevel: int = 3) -> None: ...
def warning(
    issue_number: int,
    message: str,
    warning_class: type[Warning] = ...,
    stacklevel: int = 3,
) -> None: ...
def experimental_warning(
    issue_number: int,
    message: str,
    stacklevel: int = 4,
) -> None: ...

class experimental:
    issue_number: int
    stacklevel: int
    def __init__(self, issue_number: int, stacklevel: int = 4) -> None: ...
    def __call__(self, func: _F) -> _F: ...

class __experimental_self_test:
    def __init__(self, x: str) -> None: ...

class DeprecatedFunctionAlias(Generic[_R]):
    func: Callable[..., _R]
    issue_number: int
    instance: object | None
    unbound: DeprecatedFunctionAlias[_R] | None
    __module__: str
    __doc__: str
    def __init__(
        self,
        issue_number: int,
        func: Callable[..., _R],
        module: str,
        instance: object | None = None,
        unbound: DeprecatedFunctionAlias[_R] | None = None,
        *,
        replacement: str | None = None,
        replacement_rst_doc: str | None = None,
    ) -> None: ...
    @property
    def __name__(self) -> str: ...
    def __call__(self, *args: object, **kwds: object) -> _R: ...
    def __get__(
        self,
        inst: object | None,
        cls: type | None = None,
    ) -> DeprecatedFunctionAlias[_R] | Callable[..., _R]: ...

def deprecated_function_alias(
    issue_number: int,
    func: Callable[..., _R],
    *,
    replacement: str | None = None,
    replacement_rst_doc: str | None = None,
) -> DeprecatedFunctionAlias[_R]: ...
