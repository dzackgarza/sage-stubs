from typing import TypeAlias

from sage.structure.sage_object import SageObject

_LazyImportArg: TypeAlias = SageObject | bool | int | str | type | None
_LazyImportReturn: TypeAlias = SageObject | bool | int | str | type | None

class LazyImport:
    def __init__(
        self,
        module: str,
        name: str,
        as_name: str | None = None,
        at_startup: bool = False,
        namespace: dict[str, LazyImport | _LazyImportReturn] | None = None,
        deprecation: int | tuple[int, str] | None = None,
        feature: _LazyImportArg = None,
    ) -> None: ...
    def __call__(self, *args: _LazyImportArg, **kwds: _LazyImportArg) -> _LazyImportReturn: ...
