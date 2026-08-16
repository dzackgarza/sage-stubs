from typing import Literal, overload

from sage.matrix.matrix import Matrix

@overload
def is_triangular_number(
    n: int, return_value: Literal[True]
) -> tuple[bool, object]: ...
@overload
def is_triangular_number(
    self, return_value: Literal[False] = False
) -> bool | tuple: ...
@overload
def extend_to_primitive(A_input: list[object]) -> list[object]: ...
@overload
def extend_to_primitive(self) -> Matrix: ...
def least_quadratic_nonresidue(self) -> int: ...
