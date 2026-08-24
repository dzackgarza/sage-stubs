from collections.abc import Callable, Sequence
from typing import Self

from sage.interfaces.singular import Singular, SingularElement
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.parent import ElementConstructorInput


class Vector_integer_dense(FreeModuleElement[Integer]):
    def __init__(
        self,
        parent: FreeModule_generic[Integer],
        x: Sequence[ElementConstructorInput] | int | Integer,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _richcmp_(
        self,
        right: FreeModuleElement[Integer],
        op: int,
    ) -> bool: ...
    def list(self, copy: bool = ...) -> list[Integer]: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., Vector_integer_dense],
        tuple[
            FreeModule_generic[Integer],
            list[Integer],
            int,
            bool,
        ],
    ]: ...
    def _add_(self, right: Vector_integer_dense) -> Self: ...
    def _sub_(self, right: Vector_integer_dense) -> Self: ...
    def _dot_product_(self, right: Vector_integer_dense) -> Integer: ...
    def _pairwise_product_(self, right: Vector_integer_dense) -> Self: ...
    def _rmul_(self, left: Integer) -> Self: ...
    def _lmul_(self, right: Integer) -> Self: ...
    def _neg_(self) -> Self: ...
    def _singular_(self, singular: Singular | None = ...) -> SingularElement: ...


def unpickle_v0(
    parent: FreeModule_generic[Integer],
    entries: Sequence[ElementConstructorInput],
    degree: int,
) -> Vector_integer_dense: ...
def unpickle_v1(
    parent: FreeModule_generic[Integer],
    entries: Sequence[ElementConstructorInput],
    degree: int,
    immutable: bool,
) -> Vector_integer_dense: ...
