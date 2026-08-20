from typing import Literal, overload

from sage.libs.ntl.ntl_mat_ZZ import ntl_mat_ZZ
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.modules.free_module_integer import (
    FreeModule_submodule_with_basis_integer,
)
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial


type CryptographicLatticeType = Literal[
    "modular",
    "random",
    "ideal",
    "cyclotomic",
]


@overload
def gen_lattice(
    type: CryptographicLatticeType = ...,
    n: int | Integer = ...,
    m: int | Integer = ...,
    q: int | Integer = ...,
    seed: int | Integer | None = ...,
    quotient: Polynomial | None = ...,
    dual: bool = ...,
    ntl: Literal[False] = ...,
    lattice: Literal[False] = ...,
) -> Matrix_integer_dense: ...


@overload
def gen_lattice(
    type: CryptographicLatticeType = ...,
    n: int | Integer = ...,
    m: int | Integer = ...,
    q: int | Integer = ...,
    seed: int | Integer | None = ...,
    quotient: Polynomial | None = ...,
    dual: bool = ...,
    ntl: Literal[True] = ...,
    lattice: Literal[False] = ...,
) -> ntl_mat_ZZ: ...


@overload
def gen_lattice(
    type: CryptographicLatticeType = ...,
    n: int | Integer = ...,
    m: int | Integer = ...,
    q: int | Integer = ...,
    seed: int | Integer | None = ...,
    quotient: Polynomial | None = ...,
    dual: bool = ...,
    ntl: Literal[False] = ...,
    lattice: Literal[True] = ...,
) -> FreeModule_submodule_with_basis_integer: ...


@overload
def gen_lattice(
    type: CryptographicLatticeType = ...,
    n: int | Integer = ...,
    m: int | Integer = ...,
    q: int | Integer = ...,
    seed: int | Integer | None = ...,
    quotient: Polynomial | None = ...,
    dual: bool = ...,
    ntl: bool = ...,
    lattice: bool = ...,
) -> Matrix_integer_dense | ntl_mat_ZZ | FreeModule_submodule_with_basis_integer: ...
