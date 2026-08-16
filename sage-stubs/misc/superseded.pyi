from collections.abc import Callable
from typing import Generic, TypeVar

_R = TypeVar("_R")
_F = TypeVar("_F", bound=Callable[..., object])

def _check_issue_number(self) -> None: ...
def deprecation(self, message: str, stacklevel: int = 4) -> None: ...
def deprecation_cython(self, message: str, stacklevel: int = 3) -> None: ...
def warning(
    self, message: str, warning_class: type[Warning] = ..., stacklevel: int = 3
) -> None: ...
def experimental_warning(self, message: str, stacklevel: int = 4) -> None: ...

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
    def __name__(self) -> str: ...
    def __call__(self, *args: object, **kwds: object) -> DeprecatedFunctionAlias: ...
    def __get__(
        self, inst: object | None, cls: type | None = None
    ) -> (
        DeprecatedFunctionAlias[DeprecatedFunctionAlias]
        | Callable[..., DeprecatedFunctionAlias]
    ): ...

def deprecated_function_alias(
    self,
    func: Callable[..., _R],
    *,
    replacement: str | None = None,
    replacement_rst_doc: str | None = None,
) -> DeprecatedFunctionAlias[_R]: ...
