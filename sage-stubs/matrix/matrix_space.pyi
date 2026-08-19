from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping, Sequence
from typing import Generic, TypeVar, overload

from sage.categories.action import Action
from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.pushout import MatrixFunctor
from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.with_basis.subquotient import SubmoduleWithBasis
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import Element, RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)
_Entry = TypeVar("_Entry")

type MatrixIndexKeys = Iterable[Hashable] | Parent
type MatrixData[_T: RingElement] = (
    Matrix[_T]
    | FreeModuleElement[_T]
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
    | ElementConstructorInput
    | None
)


def get_matrix_class(
    R: Parent[_Scalar],
    nrows: int | Integer,
    ncols: int | Integer,
    sparse: bool,
    implementation: str | type[Matrix[_Scalar]] | None,
) -> type[Matrix[_Scalar]]: ...


def dict_to_list(
    entries: Mapping[tuple[int, int], _Entry],
    nrows: int | Integer,
    ncols: int | Integer,
) -> list[_Entry | int]: ...


class MatrixSpace(
    UniqueRepresentation,
    Parent[Matrix[_Scalar]],
    Generic[_Scalar],
):
    Element: type[Matrix[_Scalar]]
    transposed: MatrixSpace[_Scalar]
    _copy_zero: bool

    @staticmethod
    def __classcall__(
        class_: type[MatrixSpace[_Scalar]],
        base_ring: Parent[_Scalar],
        nrows_or_row_keys: int | Integer | MatrixIndexKeys | None = ...,
        ncols_or_column_keys: int | Integer | MatrixIndexKeys | None = ...,
        sparse: bool = ...,
        implementation: str | type[Matrix[_Scalar]] | None = ...,
        *,
        nrows: int | Integer | None = ...,
        ncols: int | Integer | None = ...,
        row_keys: MatrixIndexKeys | None = ...,
        column_keys: MatrixIndexKeys | None = ...,
        **kwds: object,
    ) -> MatrixSpace[_Scalar] | Homset: ...

    def __init__(
        self,
        base_ring: Parent[_Scalar],
        nrows: int | Integer,
        ncols: int | Integer | None = ...,
        sparse: bool = ...,
        implementation: str | type[Matrix[_Scalar]] | None = ...,
    ) -> None: ...

    def base_ring(self) -> Parent[_Scalar]: ...
    def cardinality(self) -> Integer | PlusInfinity: ...
    def characteristic(self) -> Integer: ...
    def is_exact(self) -> bool: ...
    def _has_default_implementation(self) -> bool: ...

    def _element_constructor_(
        self,
        entries: MatrixData[_Scalar] = ...,
        **kwds: object,
    ) -> Matrix[_Scalar]: ...

    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> MatrixSpace[_NewScalar]: ...

    def base_extend(
        self,
        R: Parent[_NewScalar],
    ) -> MatrixSpace[_NewScalar]: ...

    def construction(
        self,
    ) -> tuple[MatrixFunctor, Parent[_Scalar]]: ...

    def _get_action_(
        self,
        S: Parent,
        op: Callable[[Element, Element], Element],
        self_on_left: bool,
    ) -> Action | None: ...

    def _coerce_map_from_base_ring(self) -> Map: ...
    def _coerce_map_from_(self, S: Parent) -> bool | Map | None: ...
    def _repr_(self) -> str: ...
    def _repr_option(self, key: str) -> bool: ...
    def _latex_(self) -> str: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Matrix[_Scalar]]: ...

    @overload
    def __getitem__(
        self,
        x: int | Integer,
    ) -> Matrix[_Scalar]: ...
    @overload
    def __getitem__(
        self,
        x: str | tuple[str, ...],
    ) -> Parent: ...

    def basis(self) -> AbstractFamily: ...
    def dimension(self) -> int: ...
    def dims(self) -> tuple[int, int]: ...

    def submodule(
        self,
        gens: Iterable[Matrix[_Scalar]],
        check: bool = ...,
        already_echelonized: bool = ...,
        unitriangular: bool = ...,
        support_order: Sequence[tuple[int, int]]
        | Callable[[tuple[int, int]], Hashable]
        | None = ...,
        category: Category | None = ...,
        *args: object,
        **opts: object,
    ) -> SubmoduleWithBasis[Hashable, _Scalar]: ...

    def identity_matrix(self) -> Matrix[_Scalar]: ...
    one = identity_matrix

    def diagonal_matrix(
        self,
        entries: Sequence[ElementConstructorInput],
    ) -> Matrix[_Scalar]: ...

    def is_dense(self) -> bool: ...
    def is_sparse(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def gen(self, n: int | Integer) -> Matrix[_Scalar]: ...
    def zero_matrix(self) -> Matrix[_Scalar]: ...
    zero = zero_matrix
    def ngens(self) -> int: ...

    def matrix(
        self,
        x: MatrixData[_Scalar] = ...,
        **kwds: object,
    ) -> Matrix[_Scalar]: ...

    def matrix_space(
        self,
        nrows: int | Integer | None = ...,
        ncols: int | Integer | None = ...,
        sparse: bool = ...,
    ) -> MatrixSpace[_Scalar]: ...

    def ncols(self) -> int: ...
    def nrows(self) -> int: ...
    def row_space(self) -> FreeModule_generic[_Scalar]: ...
    def column_space(self) -> FreeModule_generic[_Scalar]: ...

    def random_element(
        self,
        density: float | None = ...,
        *args: object,
        **kwds: object,
    ) -> Matrix[_Scalar]: ...

    def _an_element_(self) -> Matrix[_Scalar]: ...
    def some_elements(self) -> Iterator[Matrix[_Scalar]]: ...

    def _random_nonzero_element(
        self,
        *args: object,
        **kwds: object,
    ) -> Matrix[_Scalar]: ...

    def from_vector(
        self,
        vector: FreeModuleElement[_Scalar],
        order: Sequence[tuple[int, int]] | None = ...,
        coerce: bool = ...,
    ) -> Matrix[_Scalar]: ...

    def _from_dict(
        self,
        d: Mapping[tuple[int, int], ElementConstructorInput],
        coerce: bool = ...,
        remove_zeros: bool = ...,
    ) -> Matrix[_Scalar]: ...
