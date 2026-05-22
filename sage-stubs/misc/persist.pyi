import io
import pickle
from collections.abc import Callable
from os import PathLike
from typing import TypeVar, overload

already_pickled: dict[int, bool]
already_unpickled: dict[int, object]
unpickle_override: dict[tuple[str, str], tuple[Callable[..., object] | type, str | None]]

_T = TypeVar("_T")

@overload
def load(
    filename: str | PathLike[str],
    /,
    compress: bool = ...,
    verbose: bool = ...,
    **kwargs: object,
) -> object | None: ...
@overload
def load(
    *filename: str | PathLike[str],
    compress: bool = ...,
    verbose: bool = ...,
    **kwargs: object,
) -> list[object] | None: ...

def _base_save(obj: object, filename: str | PathLike[str], compress: bool = ...) -> str: ...
def save(
    obj: object,
    filename: str | PathLike[str],
    compress: bool = ...,
    **kwargs: object,
) -> None: ...
def _base_dumps(obj: object, compress: bool = ...) -> bytes: ...
def dumps(obj: object, compress: bool = ...) -> bytes: ...
def register_unpickle_override(
    module: str,
    name: str,
    unpickler: Callable[..., object] | type,
    call_name: str | None = ...,
) -> None: ...
def unpickle_global(module: str, name: str) -> Callable[..., object] | type: ...

class _BasePickler(pickle.Pickler):
    def __init__(
        self,
        file_obj: io.BufferedIOBase,
        protocol: int | None = ...,
        persistent_id: Callable[[object], object] | None = ...,
        *,
        fix_imports: bool = ...,
    ) -> None: ...

class _BaseUnpickler(pickle.Unpickler):
    def __init__(
        self,
        file_obj: io.BufferedIOBase,
        persistent_load: Callable[[object], object] | None = ...,
        **kwargs: object,
    ) -> None: ...
    def persistent_load(self, pid: object) -> object | None: ...
    def find_class(self, module: str, name: str) -> Callable[..., object] | type: ...

class SagePickler(_BasePickler):
    def __init__(
        self,
        file_obj: io.BufferedIOBase,
        persistent_id: Callable[[object], object] | None = ...,
        py2compat: bool = ...,
    ) -> None: ...
    @classmethod
    def dumps(cls, obj: object, **kwargs: object) -> bytes: ...

class SageUnpickler(_BaseUnpickler):
    @classmethod
    def loads(cls, data: bytes, **kwargs: object) -> object | None: ...

def loads(
    s: bytes,
    compress: bool = ...,
    **kwargs: object,
) -> object | None: ...
def picklejar(obj: object, dir: str | None = ...) -> None: ...
def unpickle_all(
    target: str,
    debug: bool = ...,
    run_test_suite: bool = ...,
) -> list[tuple[type[BaseException], BaseException, object]] | None: ...
def make_None(*args: object, **kwds: object) -> None: ...
def load_sage_object(cls: type[_T], dic: dict[str, object]) -> _T: ...
def load_sage_element(
    cls: type[_T],
    parent: object,
    dic_pic: bytes,
) -> _T: ...
def db(name: str) -> object | None: ...
def db_save(x: object, name: str | None = ...) -> None: ...
