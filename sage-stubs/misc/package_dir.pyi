import pkgutil
from collections.abc import Callable, Iterator
from pathlib import Path

def is_package_or_sage_namespace_package_dir(path: str | Path) -> bool: ...
def cython_namespace_package_support() -> None: ...
def walk_packages(
    path: list[str] | None = ...,
    prefix: str = ...,
    onerror: Callable[[str], None] | None = ...,
) -> Iterator[pkgutil.ModuleInfo]: ...
