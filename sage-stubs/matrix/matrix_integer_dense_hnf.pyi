from collections.abc import Iterator, Sequence
from typing import Self, TypeVar
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_double import RealDoubleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

import builtins

class _SageObject: ...

def max_det_prime(n: builtins.int) -> ElementConstructorInput: ...
def det_from_modp_and_divisor(
    A: builtins.object,
    d: builtins.object,
    p: builtins.int,
    z_mod: builtins.object,
    moduli: builtins.object,
    z_so_far: builtins.object = ...,
    N_so_far: builtins.object = ...,
) -> ElementConstructorInput: ...
def det_given_divisor(
    A: builtins.object,
    d: builtins.object,
    proof: builtins.bool = ...,
    stabilize: builtins.int = ...,
) -> ElementConstructorInput: ...
def det_padic(
    A: builtins.object, proof: builtins.bool = ..., stabilize: builtins.int = ...
) -> ElementConstructorInput: ...
def double_det(
    A: builtins.object, b: builtins.object, c: builtins.object, proof: builtins.bool
) -> ElementConstructorInput: ...
def add_column_fallback(
    B: builtins.object, a: builtins.object, proof: builtins.bool
) -> ElementConstructorInput: ...
def solve_system_with_difficult_last_row(
    B: builtins.object, a: builtins.object
) -> ElementConstructorInput: ...
def add_column(
    B: builtins.object, H_B: builtins.object, a: builtins.object, proof: builtins.bool
) -> ElementConstructorInput: ...
def add_row(
    A: builtins.object,
    b: builtins.object,
    pivots: builtins.object,
    include_zero_rows: builtins.object,
) -> ElementConstructorInput: ...
def pivots_of_hnf_matrix(H: builtins.object) -> builtins.list[builtins.int]: ...
def hnf_square(A: builtins.object, proof: builtins.bool) -> ElementConstructorInput: ...
def interleave_matrices(
    A: builtins.object,
    B: builtins.object,
    cols1: builtins.object,
    cols2: builtins.object,
) -> ElementConstructorInput: ...
def probable_pivot_rows(A: builtins.object) -> ElementConstructorInput: ...
def probable_pivot_columns(A: builtins.object) -> ElementConstructorInput: ...
def ones(H: builtins.object, pivots: builtins.object) -> ElementConstructorInput: ...
def extract_ones_data(
    H: builtins.object, pivots: builtins.object
) -> ElementConstructorInput: ...
def is_in_hnf_form(H: builtins.object, pivots: builtins.object) -> builtins.bool: ...
def probable_hnf(
    A: builtins.object, include_zero_rows: builtins.object, proof: builtins.bool
) -> ElementConstructorInput: ...
def pad_zeros(
    A: builtins.object, nrows: builtins.object
) -> ElementConstructorInput: ...
def hnf(
    A: builtins.object,
    include_zero_rows: builtins.bool = ...,
    proof: builtins.bool = ...,
) -> ElementConstructorInput: ...
def hnf_with_transformation(
    A: builtins.object, proof: builtins.bool = ...
) -> ElementConstructorInput: ...
def hnf_with_transformation_tests(
    n: builtins.int = ..., m: builtins.int = ..., trials: builtins.int = ...
) -> ElementConstructorInput: ...
def benchmark_hnf(
    nrange: builtins.object, bits: builtins.int = ...
) -> ElementConstructorInput: ...
def benchmark_magma_hnf(
    nrange: builtins.object, bits: builtins.int = ...
) -> ElementConstructorInput: ...
def sanity_checks(
    times: builtins.int = ...,
    n: builtins.int = ...,
    m: builtins.int = ...,
    proof: builtins.bool = ...,
    stabilize: builtins.int = ...,
    check_using_magma: builtins.bool = ...,
) -> ElementConstructorInput: ...
