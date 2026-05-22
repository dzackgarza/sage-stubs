import io
import pickle
from collections.abc import Callable
from os import PathLike
from typing import TypeVar, overload

already_pickled: dict[int, bool]
already_unpickled: dict[int, object]
unpickle_override: dict[tuple[str, str], tuple[Callable[..., object] | type, str | None]]

_LoadedT = TypeVar("_LoadedT")

@overload
def load(
    *filename: str | PathLike[str],
    compress: bool = True,
    verbose: bool = True,
    **kwargs: object,
) -> None: ...
@overload
def load(
    filename: str | PathLike[str],
    /,
    compress: bool = True,
    verbose: bool = True,
    **kwargs: object,
) -> _LoadedT: ...
def load(
    *filename: str | PathLike[str],
    compress: bool = True,
    verbose: bool = True,
    **kwargs: object,
) -> _LoadedT | list[_LoadedT] | None: ...

def _base_save(obj: object, filename: str | PathLike[str], compress: bool = True) -> str: ...
def save(
    obj: object,
    filename: str | PathLike[str],
    compress: bool = True,
    **kwargs: object,
) -> None: ...
def _base_dumps(obj: object, compress: bool = True) -> bytes: ...
def dumps(obj: object, compress: bool = True) -> bytes: ...
def register_unpickle_override(
    module: str,
    name: str,
    unpickler: Callable[..., object] | type,
    call_name: str | None = None,
) -> None: ...
def unpickle_global(module: str, name: str) -> Callable[..., object] | type: ...

class _BasePickler(pickle.Pickler):
    def __init__(
        self,
        file_obj: io.BufferedIOBase,
        protocol: int | None = None,
        persistent_id: Callable[[object], object] | None = None,
        *,
        fix_imports: bool = True,
    ) -> None: ...

class _BaseUnpickler(pickle.Unpickler):
    def __init__(
        self,
        file_obj: io.BufferedIOBase,
        persistent_load: Callable[[object], object] | None = None,
        **kwargs: object,
    ) -> None: ...
    def persistent_load(self, pid: object) -> object | None: ...
    def find_class(self, module: str, name: str) -> Callable[..., object] | type: ...

class SagePickler(_BasePickler):
    def __init__(
        self,
        file_obj: io.BufferedIOBase,
        persistent_id: Callable[[object], object] | None = None,
        py2compat: bool = True,
    ) -> None: ...
    @classmethod
    def dumps(cls, obj: object, **kwargs: object) -> bytes: ...

class SageUnpickler(_BaseUnpickler):
    @classmethod
    def loads(cls, data: bytes, **kwargs: object) -> _LoadedT: ...

def loads(
    s: bytes,
    compress: bool = True,
    **kwargs: object,
) -> _LoadedT: ...
def picklejar(obj: object, dir: str | None = None) -> None: ...
def unpickle_all(
    target: str,
    debug: bool = False,
    run_test_suite: bool = False,
) -> list[tuple[type[BaseException], BaseException, object]] | None: ...
def make_None(*args: object, **kwds: object) -> None: ...
def load_sage_object(_LoadedT: type[_LoadedT], dic: dict[str, object]) -> _LoadedT: ...
def load_sage_element(
    cls: type,
    parent: object,
    dic_pic: bytes,
) -> _LoadedT: ...
def db(name: str) -> _LoadedT: ...
def db_save(x: object, name: str | None = None) -> None: ...
