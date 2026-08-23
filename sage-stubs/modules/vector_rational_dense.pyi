from collections.abc import Callable, Sequence
from typing import Self

from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.parent import ElementConstructorInput


class Vector_rational_dense(FreeModuleElement[Rational]):
    def __init__(
        self,
        parent: FreeModule_generic[Rational],
        x: Sequence[ElementConstructorInput] | int | Integer | Rational,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _richcmp_(
        self,
        right: Vector_rational_dense,
        op: int,
    ) -> bool: ...
    def list(self, copy: bool = ...) -> list[Rational]: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., Vector_rational_dense],
        tuple[
            FreeModule_generic[Rational],
            list[Rational],
            int,
            bool,
        ],
    ]: ...
    def _add_(self, right: Vector_rational_dense) -> Self: ...
    def _sub_(self, right: Vector_rational_dense) -> Self: ...
    def _dot_product_(self, right: Vector_rational_dense) -> Rational: ...
    def _pairwise_product_(self, right: Vector_rational_dense) -> Self: ...
    def _rmul_(self, left: Integer | Rational) -> Self: ...
    def _lmul_(self, right: Integer | Rational) -> Self: ...
    def _neg_(self) -> Self: ...


def unpickle_v0(
    parent: FreeModule_generic[Rational],
    entries: Sequence[ElementConstructorInput],
    degree: int,
) -> Vector_rational_dense: ...
def unpickle_v1(
    parent: FreeModule_generic[Rational],
    entries: Sequence[ElementConstructorInput],
    degree: int,
    immutable: bool,
) -> Vector_rational_dense: ...
