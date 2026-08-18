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

from sage.groups.matrix_gps.isometries import GroupOfIsometries
from sage.matrix.matrix2 import Matrix
from sage.modules.free_quadratic_module import (
    FreeQuadraticModule_generic,
    FreeQuadraticModule_submodule_with_basis_pid,
)
from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
from sage.quadratic_forms.quadratic_form import QuadraticForm

type _BasisVector = FreeModuleElement | Iterable[Element | int | Integer]
type _BasisData = Matrix | Iterable[_BasisVector]
type _CartanData = str | list[str | int | Integer] | tuple[str | int | Integer, ...]
type _Scalar = Element | int | Integer
type _GlueData = Iterable[Element | int | Integer | tuple[int | Integer, int | Integer]]

def IntegralLattice(
    data: ElementConstructorInput, basis: _BasisData | None = ...
) -> FreeQuadraticModule_integer_symmetric: ...
def IntegralLatticeDirectSum(
    Lattices: Iterable[FreeQuadraticModule_integer_symmetric],
    return_embeddings: bool = ...,
) -> ElementConstructorInput: ...
def IntegralLatticeGluing(
    Lattices: Iterable[FreeQuadraticModule_integer_symmetric],
    glue: _GlueData,
    return_embeddings: bool = ...,
) -> ElementConstructorInput: ...

class FreeQuadraticModule_integer_symmetric(
    FreeQuadraticModule_submodule_with_basis_pid
):
    def __init__(
        self,
        ambient: FreeQuadraticModule_generic,
        basis: _BasisData,
        inner_product_matrix: ElementConstructorInput,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...
    def is_even(self) -> bool: ...
    def dual_lattice(self) -> FreeQuadraticModule_generic: ...
    def gram_matrix(self) -> Matrix[Integer]: ...
    def discriminant_group(self, s: int | Integer = ...) -> TorsionQuadraticModule: ...
    def signature(self) -> Integer: ...
    def signature_pair(self) -> tuple[int, int]: ...
    def direct_sum(
        self, M: FreeModule_generic
    ) -> FreeQuadraticModule_integer_symmetric: ...
    def is_primitive(self, M: FreeQuadraticModule_generic) -> bool: ...
    def orthogonal_complement(
        self, M: FreeQuadraticModule_generic | _BasisData
    ) -> FreeQuadraticModule_integer_symmetric: ...
    def sublattice(
        self, basis: _BasisData
    ) -> FreeQuadraticModule_integer_symmetric: ...
    def overlattice(
        self, gens: _BasisData
    ) -> FreeQuadraticModule_integer_symmetric: ...
    def maximal_overlattice(
        self, p: int | Integer | None = ...
    ) -> FreeQuadraticModule_integer_symmetric: ...
    def orthogonal_group(
        self, gens: ElementConstructorInput = ..., is_finite: bool | None = ...
    ) -> GroupOfIsometries: ...
    automorphisms = orthogonal_group

    def genus(self) -> FreeQuadraticModule_integer_symmetric: ...
    def tensor_product(
        self, other: FreeQuadraticModule_integer_symmetric, discard_basis: bool = ...
    ) -> FreeQuadraticModule_integer_symmetric: ...
    def quadratic_form(self) -> QuadraticForm: ...
    def minimum(self) -> FreeQuadraticModule_integer_symmetric: ...
    def maximum(self) -> FreeQuadraticModule_integer_symmetric: ...
    min = minimum
    max = maximum

    def LLL(self) -> FreeQuadraticModule_integer_symmetric: ...
    lll = LLL

    def short_vectors(
        self, n: int | Integer, **kwargs: bool | int | Integer
    ) -> FreeQuadraticModule_integer_symmetric: ...
    def enumerate_short_vectors(self) -> FreeQuadraticModule_integer_symmetric: ...
    def enumerate_close_vectors(
        self, target: FreeModule_generic
    ) -> FreeQuadraticModule_integer_symmetric: ...
    def twist(
        self, s: _Scalar, discard_basis: bool = ...
    ) -> FreeQuadraticModule_integer_symmetric: ...

def local_modification(
    M: FreeQuadraticModule_integer_symmetric,
    G: ElementConstructorInput,
    p: int | Integer,
    check: bool = ...,
) -> FreeQuadraticModule_integer_symmetric: ...
