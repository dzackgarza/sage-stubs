from collections.abc import Iterable, Sequence
from typing import Literal, overload

from sage.geometry.polyhedron.base import Polyhedron_base
from sage.matrix.matrix0 import Matrix
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.modules.free_module import (
    FreeModule_ambient_pid,
    FreeModule_submodule_with_basis_pid,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.number_field.number_field_element import OrderElement_absolute
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.element import RingElement
from sage.symbolic.expression import Expression

type IntegerLatticeVector = Sequence[int | Integer] | FreeModuleElement[Integer]
type IntegerLatticeBasis = (
    Matrix[Integer]
    | Iterable[IntegerLatticeVector]
    | FreeModule_ambient_pid[Integer]
    | OrderElement_absolute
)
type ClosestVectorTarget = (
    Sequence[RingElement | int]
    | FreeModuleElement[RingElement]
)
type LatticeReductionAlgorithm = Literal["fplll", "pari"]
type ApproximationAlgorithm = Literal[
    "embedding",
    "nearest_plane",
    "rounding_off",
]


def IntegerLattice(
    basis: IntegerLatticeBasis,
    lll_reduce: bool = ...,
) -> FreeModule_submodule_with_basis_integer: ...


class FreeModule_submodule_with_basis_integer(
    FreeModule_submodule_with_basis_pid[Integer],
):
    def __init__(
        self,
        ambient: FreeModule_ambient_pid[Integer],
        basis: Matrix[Integer] | Iterable[IntegerLatticeVector],
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: Matrix[Integer] | None = ...,
        already_echelonized: bool = ...,
        lll_reduce: bool = ...,
    ) -> None: ...

    @property
    def reduced_basis(self) -> Matrix_integer_dense: ...

    def LLL(self, *args: object, **kwds: object) -> Matrix_integer_dense: ...
    def BKZ(self, *args: object, **kwds: object) -> Matrix_integer_dense: ...
    def HKZ(self, *args: object, **kwds: object) -> Matrix_integer_dense: ...
    def volume(self) -> Integer | Expression: ...
    def discriminant(self) -> Integer: ...
    def is_unimodular(self) -> bool: ...
    def shortest_vector(
        self,
        update_reduced_basis: bool = ...,
        algorithm: LatticeReductionAlgorithm = ...,
        *args: object,
        **kwds: object,
    ) -> FreeModuleElement[Integer]: ...
    def update_reduced_basis(
        self,
        w: IntegerLatticeVector,
    ) -> None: ...
    def voronoi_cell(
        self,
        radius: RingElement | int | float | None = ...,
    ) -> Polyhedron_base: ...
    def voronoi_relevant_vectors(
        self,
    ) -> list[FreeModuleElement[Rational]]: ...
    def closest_vector(
        self,
        t: ClosestVectorTarget,
    ) -> FreeModuleElement[Integer]: ...
    def approximate_closest_vector(
        self,
        t: ClosestVectorTarget,
        delta: Rational | float | None = ...,
        algorithm: ApproximationAlgorithm = ...,
        *args: object,
        **kwargs: object,
    ) -> FreeModuleElement[Integer]: ...
    def babai(
        self,
        t: ClosestVectorTarget,
        delta: Rational | float | None = ...,
        algorithm: ApproximationAlgorithm = ...,
        *args: object,
        **kwargs: object,
    ) -> FreeModuleElement[Integer]: ...
    def hadamard_ratio(
        self,
        use_reduced_basis: bool = ...,
    ) -> RingElement: ...

    @overload
    def gaussian_heuristic(
        self,
        exact_form: Literal[False] = ...,
    ) -> RealNumber: ...
    @overload
    def gaussian_heuristic(
        self,
        exact_form: Literal[True],
    ) -> Expression: ...
    @overload
    def gaussian_heuristic(
        self,
        exact_form: bool = ...,
    ) -> RealNumber | Expression: ...
