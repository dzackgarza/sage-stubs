from collections.abc import Callable
from types import ModuleType

sequence_number: dict[str, int]

def _standard_libs_libdirs_incdirs_aliases() -> tuple[list[str], list[str], list[str], dict[str, object]]: ...
def _webbrowser_open_file(path: str) -> None: ...
def cython(
    filename: str,
    verbose: int = ...,
    compile_message: bool = ...,
    use_cache: bool = ...,
    create_local_c_file: bool = ...,
    annotate: bool = ...,
    view_annotate: bool = ...,
    view_annotate_callback: Callable[[str], None] | None = ...,
    sage_namespace: bool = ...,
    create_local_so_file: bool = ...,
) -> tuple[str, str]: ...
def cython_lambda(
    vars: str | list[tuple[str, str]],
    expr: str,
    verbose: int = ...,
    **kwds: object,
) -> Callable[..., float]: ...
def cython_import(filename: str, **kwds: object) -> ModuleType: ...
def cython_import_all(filename: str, globals: dict[str, object], **kwds: object) -> None: ...
def sanitize(f: str) -> str: ...
def compile_and_load(code: str, **kwds: object) -> ModuleType: ...
def cython_compile(code: str, **kwds: object) -> None: ...
