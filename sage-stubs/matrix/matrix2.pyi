from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Generic, Literal, TypeVar, overload

from sage.categories.morphism import Morphism
from sage.combinat.free_module import CombinatorialFreeModule
from sage.geometry.abc import ConvexRationalPolyhedralCone
from sage.graphs.graph import Graph
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.matrix.matrix1 import Matrix as Matrix1
from sage.matrix.matrix_window import MatrixWindow
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.plot.graphics import Graphics
from sage.repl.image import Image
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.element import Element, RingElement
from sage.structure.factorization import Factorization
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_OtherScalar = TypeVar("_OtherScalar", bound=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)

type _PermutationPair = tuple[
    PermutationGroupElement,
    PermutationGroupElement,
]
type _Eigenspace = tuple[
    RingElement,
    FreeModule_generic[RingElement],
]
type _EigenspaceWithMultiplicity = tuple[
    RingElement,
    FreeModule_generic[RingElement],
    int,
]
type _EigenvectorData = tuple[
    RingElement,
    list[FreeModuleElement[RingElement]],
    int,
]
type _DecompositionFactor[_T: RingElement] = tuple[
    FreeModule_generic[_T],
    bool,
]
type _KrylovRow = tuple[int, int, int]
type _MatrixOption = Element | str | int | float | bool | None


class Matrix(
    Matrix1[_Scalar],
    Generic[_Scalar],
):
    # Entrywise maps and linear equations
    def subs(
        self,
        *args: Element | int | float | Mapping[Element, Element | int | float],
        **kwds: Element | int | float,
    ) -> Matrix[RingElement]: ...

    @overload
    def solve_left(
        self,
        B: Matrix[_OtherScalar],
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> Matrix[RingElement]: ...
    @overload
    def solve_left(
        self,
        B: FreeModuleElement[_OtherScalar],
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> FreeModuleElement[RingElement]: ...

    @overload
    def solve_right(
        self,
        B: Matrix[_OtherScalar],
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> Matrix[RingElement]: ...
    @overload
    def solve_right(
        self,
        B: FreeModuleElement[_OtherScalar],
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> FreeModuleElement[RingElement]: ...

    def pivot_rows(self) -> tuple[int, ...]: ...
    def prod_of_row_sums(
        self,
        cols: Iterable[int | Integer],
    ) -> _Scalar: ...
    def elementwise_product(
        self,
        right: Matrix[_OtherScalar],
    ) -> Matrix[RingElement]: ...

    # Permanents, determinants, Pfaffians, and minors
    def permanent(self, algorithm: str = ...) -> _Scalar: ...
    def permanental_minor(
        self,
        k: int | Integer,
        algorithm: str = ...,
    ) -> _Scalar: ...
    def pseudoinverse(
        self,
        *,
        algorithm: str | None = ...,
    ) -> Matrix[RingElement]: ...
    def rook_vector(
        self,
        algorithm: str | None = ...,
        complement: bool = ...,
        use_complement: bool | None = ...,
    ) -> list[_Scalar]: ...
    def minors(self, k: int | Integer) -> list[_Scalar]: ...
    def minor(
        self,
        rows: Sequence[int | Integer],
        columns: Sequence[int | Integer],
    ) -> _Scalar: ...
    def determinant(
        self,
        algorithm: str | None = ...,
        **kwds: _MatrixOption,
    ) -> _Scalar: ...
    det = determinant
    def quantum_determinant(
        self,
        q: RingElement | None = ...,
    ) -> RingElement: ...
    qdet = quantum_determinant
    def pfaffian(
        self,
        algorithm: str | None = ...,
        check: bool = ...,
    ) -> _Scalar: ...

    # Coefficient maps and polynomial invariants
    def apply_morphism(
        self,
        phi: Morphism[_Scalar, _NewScalar],
    ) -> Matrix[_NewScalar]: ...

    @overload
    def apply_map(
        self,
        phi: Callable[[_Scalar], _NewScalar],
        R: None = ...,
        sparse: bool | None = ...,
    ) -> Matrix[_NewScalar]: ...
    @overload
    def apply_map(
        self,
        phi: Callable[[_Scalar], Element],
        R: Parent[_NewScalar],
        sparse: bool | None = ...,
    ) -> Matrix[_NewScalar]: ...
    @overload
    def apply_map(
        self,
        phi: Callable[[_Scalar], Element],
        R: None = ...,
        sparse: bool | None = ...,
    ) -> Matrix[RingElement]: ...

    def characteristic_polynomial(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    charpoly = characteristic_polynomial
    def minimal_polynomial(
        self,
        var: str = ...,
        **kwds: _MatrixOption,
    ) -> Polynomial: ...
    minpoly = minimal_polynomial
    def fcp(self, var: str = ...) -> Factorization: ...
    def denominator(self) -> RingElement: ...
    def diagonal(
        self,
        offset: int | Integer = ...,
    ) -> list[_Scalar]: ...
    def trace(self) -> _Scalar: ...
    def trace_of_product(
        self,
        other: Matrix[_Scalar],
    ) -> _Scalar: ...
    def get_bandwidth(self) -> Integer: ...
    def hessenberg_form(self) -> Matrix[RingElement]: ...
    def hessenbergize(self) -> None: ...

    # Kernels, images, invariant subspaces, and decompositions
    def rank(
        self,
        algorithm: str | None = ...,
        **kwds: _MatrixOption,
    ) -> int: ...
    def left_nullity(self) -> int: ...
    nullity = left_nullity
    def right_nullity(self) -> int: ...
    def right_kernel_matrix(
        self,
        *args: _MatrixOption,
        **kwds: _MatrixOption,
    ) -> Matrix[_Scalar]: ...
    def left_kernel_matrix(
        self,
        *args: _MatrixOption,
        **kwds: _MatrixOption,
    ) -> Matrix[_Scalar]: ...
    def right_kernel(
        self,
        *args: _MatrixOption,
        **kwds: _MatrixOption,
    ) -> FreeModule_generic[_Scalar]: ...
    def left_kernel(
        self,
        *args: _MatrixOption,
        **kwds: _MatrixOption,
    ) -> FreeModule_generic[_Scalar]: ...
    kernel = left_kernel
    def kernel_on(
        self,
        V: FreeModule_generic[_Scalar],
        poly: Polynomial | None = ...,
        check: bool = ...,
    ) -> FreeModule_generic[_Scalar]: ...
    def integer_kernel(
        self,
        ring: Parent[_NewScalar] = ...,
    ) -> FreeModule_generic[_NewScalar]: ...
    def image(self) -> FreeModule_generic[_Scalar]: ...

    @overload
    def row_module(
        self,
        base_ring: None = ...,
    ) -> FreeModule_generic[_Scalar]: ...
    @overload
    def row_module(
        self,
        base_ring: Parent[_NewScalar],
    ) -> FreeModule_generic[_NewScalar]: ...
    row_space = row_module

    @overload
    def column_module(
        self,
        base_ring: None = ...,
    ) -> FreeModule_generic[_Scalar]: ...
    @overload
    def column_module(
        self,
        base_ring: Parent[_NewScalar],
    ) -> FreeModule_generic[_NewScalar]: ...
    column_space = column_module

    @overload
    def decomposition(
        self,
        algorithm: str = ...,
        is_diagonalizable: bool = ...,
        dual: Literal[False] = ...,
    ) -> Sequence[_DecompositionFactor[_Scalar]]: ...
    @overload
    def decomposition(
        self,
        algorithm: str,
        is_diagonalizable: bool,
        dual: Literal[True],
    ) -> tuple[
        Sequence[_DecompositionFactor[_Scalar]],
        Sequence[_DecompositionFactor[_Scalar]],
    ]: ...
    def decomposition_of_subspace(
        self,
        M: FreeModule_generic[_Scalar],
        check_restrict: bool = ...,
        **kwds: _MatrixOption,
    ) -> Sequence[_DecompositionFactor[_Scalar]]: ...
    def restrict(
        self,
        V: FreeModule_generic[_Scalar],
        check: bool = ...,
    ) -> Matrix[_Scalar]: ...
    def restrict_domain(
        self,
        V: FreeModule_generic[_Scalar],
    ) -> Matrix[_Scalar]: ...
    def restrict_codomain(
        self,
        V: FreeModule_generic[_Scalar],
    ) -> Matrix[RingElement]: ...
    def maxspin(
        self,
        v: FreeModuleElement[_Scalar],
    ) -> list[FreeModuleElement[_Scalar]]: ...
    def wiedemann(
        self,
        i: int | Integer,
        t: int | Integer = ...,
    ) -> Polynomial: ...

    @overload
    def cyclic_subspace(
        self,
        v: FreeModuleElement[_Scalar],
        var: None = ...,
        basis: Literal["echelon", "iterates"] = ...,
    ) -> FreeModule_generic[RingElement]: ...
    @overload
    def cyclic_subspace(
        self,
        v: FreeModuleElement[_Scalar],
        var: str | Polynomial,
        basis: Literal["echelon", "iterates"] = ...,
    ) -> tuple[Polynomial, FreeModule_generic[RingElement]]: ...

    # Eigenvalue and singular-value data
    @overload
    def eigenspaces_left(
        self,
        format: str = ...,
        var: str = ...,
        algebraic_multiplicity: Literal[False] = ...,
    ) -> Sequence[_Eigenspace]: ...
    @overload
    def eigenspaces_left(
        self,
        format: str,
        var: str,
        algebraic_multiplicity: Literal[True],
    ) -> Sequence[_EigenspaceWithMultiplicity]: ...
    left_eigenspaces = eigenspaces_left

    @overload
    def eigenspaces_right(
        self,
        format: str = ...,
        var: str = ...,
        algebraic_multiplicity: Literal[False] = ...,
    ) -> Sequence[_Eigenspace]: ...
    @overload
    def eigenspaces_right(
        self,
        format: str,
        var: str,
        algebraic_multiplicity: Literal[True],
    ) -> Sequence[_EigenspaceWithMultiplicity]: ...
    right_eigenspaces = eigenspaces_right

    def eigenvalues(
        self,
        extend: bool = ...,
        algorithm: str | None = ...,
    ) -> Sequence[RingElement]: ...
    def singular_values(self) -> Sequence[RingElement]: ...
    def eigenvectors_left(
        self,
        other: Matrix | None = ...,
        *,
        extend: bool = ...,
        algorithm: str | None = ...,
    ) -> list[_EigenvectorData]: ...
    left_eigenvectors = eigenvectors_left
    def eigenvectors_right(
        self,
        other: Matrix | None = ...,
        *,
        extend: bool = ...,
    ) -> list[_EigenvectorData]: ...
    right_eigenvectors = eigenvectors_right
    def eigenmatrix_left(
        self,
        other: Matrix | None = ...,
    ) -> tuple[Matrix[RingElement], Matrix[RingElement]]: ...
    left_eigenmatrix = eigenmatrix_left
    def eigenmatrix_right(
        self,
        other: Matrix | None = ...,
    ) -> tuple[Matrix[RingElement], Matrix[RingElement]]: ...
    right_eigenmatrix = eigenmatrix_right
    def eigenvalue_multiplicity(
        self,
        eigenvalue: RingElement,
    ) -> Integer: ...

    # Echelon and canonical forms
    def rref(
        self,
        *args: _MatrixOption,
        **kwds: _MatrixOption,
    ) -> Matrix[RingElement]: ...
    def echelonize(
        self,
        algorithm: str = ...,
        cutoff: int = ...,
        **kwds: _MatrixOption,
    ) -> None: ...
    def echelon_form(
        self,
        algorithm: str = ...,
        cutoff: int = ...,
        **kwds: _MatrixOption,
    ) -> Matrix[_Scalar]: ...
    def extended_echelon_form(
        self,
        subdivide: bool = ...,
        **kwds: _MatrixOption,
    ) -> Matrix[_Scalar]: ...

    @overload
    def smith_form(
        self,
        transformation: Literal[True] = ...,
        integral: Parent | bool | None = ...,
        exact: bool = ...,
    ) -> tuple[
        Matrix[_Scalar],
        Matrix[RingElement],
        Matrix[RingElement],
    ]: ...
    @overload
    def smith_form(
        self,
        transformation: Literal[False],
        integral: Parent | bool | None = ...,
        exact: bool = ...,
    ) -> Matrix[_Scalar]: ...
    @overload
    def smith_form(
        self,
        transformation: bool,
        integral: Parent | bool | None = ...,
        exact: bool = ...,
    ) -> (
        Matrix[_Scalar]
        | tuple[
            Matrix[_Scalar],
            Matrix[RingElement],
            Matrix[RingElement],
        ]
    ): ...

    @overload
    def hermite_form(
        self,
        include_zero_rows: bool = ...,
        transformation: Literal[False] = ...,
    ) -> Matrix[_Scalar]: ...
    @overload
    def hermite_form(
        self,
        include_zero_rows: bool,
        transformation: Literal[True],
    ) -> tuple[Matrix[_Scalar], Matrix[_Scalar]]: ...

    @overload
    def zigzag_form(
        self,
        subdivide: bool = ...,
        transformation: Literal[False] = ...,
    ) -> Matrix[_Scalar]: ...
    @overload
    def zigzag_form(
        self,
        subdivide: bool,
        transformation: Literal[True],
    ) -> tuple[Matrix[_Scalar], Matrix[RingElement]]: ...

    def rational_form(
        self,
        format: str = ...,
        subdivide: bool = ...,
    ) -> Matrix[_Scalar]: ...

    @overload
    def jordan_form(
        self,
        base_ring: Parent[_NewScalar] | None = ...,
        sparse: bool = ...,
        subdivide: bool = ...,
        transformation: Literal[False] = ...,
        eigenvalues: Sequence[RingElement] | None = ...,
        check_input: bool = ...,
    ) -> Matrix[RingElement]: ...
    @overload
    def jordan_form(
        self,
        base_ring: Parent[_NewScalar] | None,
        sparse: bool,
        subdivide: bool,
        transformation: Literal[True],
        eigenvalues: Sequence[RingElement] | None = ...,
        check_input: bool = ...,
    ) -> tuple[Matrix[RingElement], Matrix[RingElement]]: ...

    def jordan_decomposition(
        self,
    ) -> tuple[Matrix[RingElement], Matrix[RingElement]]: ...
    def diagonalization(
        self,
        base_field: Parent[_NewScalar] | None = ...,
    ) -> tuple[Matrix[RingElement], Matrix[RingElement]]: ...
    def is_diagonalizable(
        self,
        base_field: Parent | None = ...,
    ) -> bool: ...

    @overload
    def is_similar(
        self,
        other: Matrix,
        transformation: Literal[False] = ...,
    ) -> bool: ...
    @overload
    def is_similar(
        self,
        other: Matrix,
        transformation: Literal[True],
    ) -> bool | tuple[bool, Matrix[RingElement]]: ...

    # Row/column symmetry, windows, and blocks
    def as_bipartite_graph(self) -> Graph: ...
    def automorphisms_of_rows_and_columns(
        self,
    ) -> list[_PermutationPair]: ...

    @overload
    def permutation_normal_form(
        self,
        check: Literal[False] = ...,
    ) -> Matrix[_Scalar]: ...
    @overload
    def permutation_normal_form(
        self,
        check: Literal[True],
    ) -> tuple[Matrix[_Scalar], _PermutationPair]: ...

    @overload
    def is_permutation_of(
        self,
        N: Matrix[_Scalar],
        check: Literal[False] = ...,
    ) -> bool: ...
    @overload
    def is_permutation_of(
        self,
        N: Matrix[_Scalar],
        check: Literal[True],
    ) -> tuple[bool, _PermutationPair | None]: ...

    def matrix_window(
        self,
        row: int = ...,
        col: int = ...,
        nrows: int = ...,
        ncols: int = ...,
        check: bool = ...,
    ) -> MatrixWindow[_Scalar]: ...
    def set_block(
        self,
        row: int,
        col: int,
        block: Matrix[_OtherScalar],
    ) -> None: ...
    def subdivide(
        self,
        row_lines: Iterable[int | Integer] | None = ...,
        col_lines: Iterable[int | Integer] | None = ...,
    ) -> None: ...
    def subdivision(
        self,
        i: int,
        j: int,
    ) -> Matrix[_Scalar]: ...
    def subdivision_entry(
        self,
        i: int,
        j: int,
        x: int,
        y: int,
    ) -> _Scalar: ...
    def subdivisions(self) -> tuple[list[int], list[int]]: ...
    get_subdivisions = subdivisions
    def tensor_product(
        self,
        A: Matrix[_OtherScalar],
        subdivide: bool = ...,
    ) -> Matrix[RingElement]: ...
    def randomize(
        self,
        density: float = ...,
        nonzero: bool = ...,
        *args: _MatrixOption,
        **kwds: _MatrixOption,
    ) -> None: ...

    # Structural predicates and elementary operations
    def is_one(self) -> bool: ...
    def is_scalar(
        self,
        a: _Scalar | int | Integer | None = ...,
    ) -> bool: ...
    def is_diagonal(self) -> bool: ...
    def is_triangular(
        self,
        side: Literal["lower", "upper"] = ...,
    ) -> bool: ...
    def is_unitary(self) -> bool: ...
    def is_bistochastic(self, normalized: bool = ...) -> bool: ...
    def is_normal(self) -> bool: ...
    def is_nilpotent(self) -> bool: ...
    def is_semisimple(self) -> bool: ...
    def as_sum_of_permutations(self) -> CombinatorialFreeModule.Element: ...
    def visualize_structure(
        self,
        maxsize: int | Integer | None = ...,
    ) -> Image: ...
    def is_positive_semidefinite(self) -> bool: ...
    def is_positive_definite(self) -> bool: ...
    def principal_square_root(
        self,
        check_positivity: bool = ...,
    ) -> Matrix[RingElement]: ...
    def density(self) -> Rational | int: ...
    def inverse(self) -> Matrix[RingElement]: ...
    def adjugate(self) -> Matrix[_Scalar]: ...
    adjoint_classical = adjugate
    def conjugate(self) -> Matrix[RingElement]: ...
    def conjugate_transpose(self) -> Matrix[RingElement]: ...
    def norm(
        self,
        p: int | float | str = ...,
    ) -> Element: ...
    def numerical_approx(
        self,
        prec: int | None = ...,
        digits: int | None = ...,
        algorithm: str | None = ...,
    ) -> Matrix[RingElement]: ...
    n = numerical_approx
    def plot(
        self,
        *args: _MatrixOption,
        **kwds: _MatrixOption,
    ) -> Graphics: ...
    def derivative(
        self,
        *args: _MatrixOption,
    ) -> Matrix[RingElement]: ...
    def exp(self) -> Matrix[RingElement]: ...

    # Orthogonal, unitary, and triangular factorizations
    def QR(
        self,
        full: bool = ...,
    ) -> tuple[Matrix[RingElement], Matrix[RingElement]]: ...
    def gram_schmidt(
        self,
        orthonormal: bool = ...,
    ) -> tuple[Matrix[RingElement], Matrix[RingElement]]: ...
    def cholesky(
        self,
        extended: bool = ...,
    ) -> Matrix[RingElement]: ...
    def inverse_positive_definite(self) -> Matrix[RingElement]: ...

    @overload
    def LU(
        self,
        pivot: str | None = ...,
        format: Literal["plu"] = ...,
    ) -> tuple[
        Matrix[RingElement],
        Matrix[RingElement],
        Matrix[RingElement],
    ]: ...
    @overload
    def LU(
        self,
        pivot: str | None,
        format: Literal["compact"],
    ) -> tuple[tuple[int, ...], Matrix[RingElement]]: ...
    @overload
    def LU(
        self,
        pivot: str | None = ...,
        format: str = ...,
    ) -> (
        tuple[
            Matrix[RingElement],
            Matrix[RingElement],
            Matrix[RingElement],
        ]
        | tuple[tuple[int, ...], Matrix[RingElement]]
    ): ...

    def indefinite_factorization(
        self,
        algorithm: str = ...,
        check: bool = ...,
    ) -> tuple[
        Matrix[RingElement],
        FreeModuleElement[RingElement],
    ]: ...
    def block_ldlt(
        self,
        classical: bool = ...,
    ) -> tuple[
        Matrix[RingElement],
        Matrix[RingElement],
        Matrix[RingElement],
    ]: ...
    def symplectic_form(
        self,
    ) -> tuple[Matrix[_Scalar], Matrix[_Scalar]]: ...

    # Ideals, divisors, cones, and lattice reduction
    def elementary_divisors(
        self,
        algorithm: str | None = ...,
    ) -> list[_Scalar]: ...
    def fitting_ideal(
        self,
        i: int | Integer,
    ) -> Ideal_generic: ...
    def is_positive_operator_on(
        self,
        K1: ConvexRationalPolyhedralCone,
        K2: ConvexRationalPolyhedralCone | None = ...,
    ) -> bool: ...
    def is_cross_positive_on(
        self,
        K: ConvexRationalPolyhedralCone,
    ) -> bool: ...
    def is_Z_operator_on(
        self,
        K: ConvexRationalPolyhedralCone,
    ) -> bool: ...
    def is_lyapunov_like_on(
        self,
        K: ConvexRationalPolyhedralCone,
    ) -> bool: ...
    def LLL_gram(
        self,
        flag: int = ...,
    ) -> Matrix[Integer]: ...

    @overload
    def find(
        self,
        f: Callable[[_Scalar], bool],
        indices: Literal[False] = ...,
    ) -> Matrix[IntegerMod_abstract]: ...
    @overload
    def find(
        self,
        f: Callable[[_Scalar], bool],
        indices: Literal[True],
    ) -> dict[tuple[int, int], _Scalar]: ...
    @overload
    def find(
        self,
        f: Callable[[_Scalar], bool],
        indices: bool,
    ) -> Matrix[IntegerMod_abstract] | dict[tuple[int, int], _Scalar]: ...
    def hadamard_bound(self) -> Integer: ...

    # Krylov matrices and polynomial-kernel bases
    def krylov_matrix(
        self,
        M: Matrix[_Scalar],
        shifts: Sequence[int | Integer] | FreeModuleElement[Integer] | None = ...,
        degrees: int | Integer | Sequence[int | Integer] | FreeModuleElement[Integer] | None = ...,
    ) -> Matrix[_Scalar]: ...

    @overload
    def krylov_basis(
        self,
        M: Matrix[_Scalar],
        shifts: Sequence[int | Integer] | FreeModuleElement[Integer] | None = ...,
        degrees: int | Integer | Sequence[int | Integer] | FreeModuleElement[Integer] | None = ...,
        output_rows: Literal[True] = ...,
        algorithm: str | None = ...,
    ) -> tuple[Matrix[_Scalar], tuple[_KrylovRow, ...]]: ...
    @overload
    def krylov_basis(
        self,
        M: Matrix[_Scalar],
        shifts: Sequence[int | Integer] | FreeModuleElement[Integer] | None,
        degrees: int | Integer | Sequence[int | Integer] | FreeModuleElement[Integer] | None,
        output_rows: Literal[False],
        algorithm: str | None = ...,
    ) -> Matrix[_Scalar]: ...

    @overload
    def krylov_kernel_basis(
        self,
        M: Matrix[_Scalar],
        shifts: Sequence[int | Integer] | FreeModuleElement[Integer] | None = ...,
        degrees: int | Integer | Sequence[int | Integer] | FreeModuleElement[Integer] | None = ...,
        output_rows: Literal[True] = ...,
        var: str | None = ...,
        basis_algorithm: str | None = ...,
    ) -> tuple[Matrix[Polynomial], tuple[_KrylovRow, ...]]: ...
    @overload
    def krylov_kernel_basis(
        self,
        M: Matrix[_Scalar],
        shifts: Sequence[int | Integer] | FreeModuleElement[Integer] | None,
        degrees: int | Integer | Sequence[int | Integer] | FreeModuleElement[Integer] | None,
        output_rows: Literal[False],
        var: str | None = ...,
        basis_algorithm: str | None = ...,
    ) -> Matrix[Polynomial]: ...

    @property
    def T(self) -> Matrix[_Scalar]: ...
    @property
    def C(self) -> Matrix[RingElement]: ...
    @property
    def H(self) -> Matrix[RingElement]: ...
