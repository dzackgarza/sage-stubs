from collections.abc import Sequence
from typing import Self

from numpy import ndarray

from sage.modules.vector_numpy_dense import Vector_numpy_dense
from sage.rings.integer import Integer
from sage.structure.parent import ElementConstructorInput


class Vector_numpy_integer_dense(Vector_numpy_dense[Integer]):
    def __init__(
        self,
        parent: object,
        entries: ndarray | Sequence[int | Integer | ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def list(self, copy: bool = ...) -> list[Integer]: ...
    def dot_product(self, right: Vector_numpy_integer_dense) -> Integer: ...
    inner_product = dot_product
    def gcd(self) -> Integer: ...
    content = gcd
