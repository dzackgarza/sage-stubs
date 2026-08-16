from collections.abc import Callable
from typing import TypeVar

_F = TypeVar("_F", bound=Callable[..., object])

def gen_rest_table_index(
    self,
    names: dict[object, str] | None = ...,
    sort: bool = ...,
    only_local_functions: bool = ...,
    root: object = ...,
) -> str: ...
def list_of_subfunctions(
    self, only_local_functions: bool = ...
) -> tuple[list[object], dict[object, str]]: ...
def gen_thematic_rest_table_index(
    self,
    additional_categories: dict[str, str] | None = ...,
    only_local_functions: bool = ...,
) -> str: ...
def doc_index(self) -> Callable[[Callable[..., object]], Callable[..., object]]: ...
