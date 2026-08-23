from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Generic, Self, TypeVar, overload

from sage.matrix.matrix import Matrix
from sage.rings.integer import Integer
from sage.structure.element import RingElement, Vector
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.sequence import Sequence_generic

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)

type VectorEntries = (
    Iterable[ElementConstructorInput]
    | Mapping[int | Integer, ElementConstructorInput]
)


@overload
def vector(
    arg0: FreeModuleElement[_Scalar],
    arg1: None = ...,
    arg2: None = ...,
    sparse: bool | None = ...,
    immutable: bool = ...,
) -> FreeModuleElement[_Scalar]: ...
@overload
def vector(
    arg0: Parent[_Scalar],
    arg1: VectorEntries | FreeModuleElement[_Scalar],
    arg2: None = ...,
    sparse: bool | None = ...,
    immutable: bool = ...,
) -> FreeModuleElement[_Scalar]: ...
@overload
def vector(
    arg0: VectorEntries | FreeModuleElement[RingElement],
    arg1: Parent[_Scalar],
    arg2: None = ...,
    sparse: bool | None = ...,
    immutable: bool = ...,
) -> FreeModuleElement[_Scalar]: ...
@overload
def vector(
    arg0: Parent[_Scalar],
    arg1: int | Integer,
    arg2: VectorEntries | FreeModuleElement[_Scalar] | None = ...,
    sparse: bool | None = ...,
    immutable: bool = ...,
) -> FreeModuleElement[_Scalar]: ...
@overload
def vector(
    arg0: VectorEntries,
    arg1: None = ...,
    arg2: None = ...,
    sparse: bool | None = ...,
    immutable: bool = ...,
) -> FreeModuleElement[RingElement]: ...

free_module_element = vector

@overload
def prepare(
    v: VectorEntries,
    R: Parent[_Scalar],
    degree: int | Integer | None = ...,
) -> tuple[Sequence_generic, Parent[_Scalar]]: ...
@overload
def prepare(
    v: VectorEntries,
    R: None,
    degree: int | Integer | None = ...,
) -> tuple[Sequence_generic, Parent[RingElement]]: ...

@overload
def zero_vector(
    arg0: int | Integer,
    arg1: None = ...,
) -> FreeModuleElement[Integer]: ...
@overload
def zero_vector(
    arg0: Parent[_Scalar],
    arg1: int | Integer,
) -> FreeModuleElement[_Scalar]: ...

@overload
def random_vector(
    ring: int | Integer,
    degree: int | Integer | None = ...,
    *args: object,
    **kwds: object,
) -> FreeModuleElement[Integer]: ...
@overload
def random_vector(
    ring: Parent[_Scalar],
    degree: int | Integer,
    *args: object,
    **kwds: object,
) -> FreeModuleElement[_Scalar]: ...


def make_FreeModuleElement_generic_dense(
    parent: FreeModule_generic[_Scalar],
    entries: Sequence[ElementConstructorInput],
    degree: int | Integer,
) -> FreeModuleElement_generic_dense[_Scalar]: ...

def make_FreeModuleElement_generic_dense_v1(
    parent: FreeModule_generic[_Scalar],
    entries: Sequence[ElementConstructorInput],
    degree: int | Integer,
    immutable: bool,
) -> FreeModuleElement_generic_dense[_Scalar]: ...

def make_FreeModuleElement_generic_sparse(
    parent: FreeModule_generic[_Scalar],
    entries: Mapping[int | Integer, ElementConstructorInput],
    degree: int | Integer,
) -> FreeModuleElement_generic_sparse[_Scalar]: ...

def make_FreeModuleElement_generic_sparse_v1(
    parent: FreeModule_generic[_Scalar],
    entries: Mapping[int | Integer, ElementConstructorInput],
    degree: int | Integer,
    immutable: bool,
) -> FreeModuleElement_generic_sparse[_Scalar]: ...


class FreeModuleElement(Vector[_Scalar], Generic[_Scalar]):
    def __init__(self, parent: Parent[Self]) -> None: ...
    def parent(self) -> FreeModule_generic[_Scalar]: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def degree(self) -> int: ...
    def dimension(self) -> int: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_Scalar]: ...
    @overload
    def __getitem__(self, i: int | Integer) -> _Scalar: ...
    @overload
    def __getitem__(self, i: slice) -> list[_Scalar]: ...
    def __setitem__(
        self,
        i: int | Integer | slice,
        value: ElementConstructorInput | Sequence[ElementConstructorInput],
    ) -> None: ...
    def list(self, copy: bool = ...) -> list[_Scalar]: ...
    def dict(self, copy: bool = ...) -> dict[int, _Scalar]: ...
    def vector(self) -> Self: ...
    def row(self) -> Matrix[_Scalar]: ...
    def column(self) -> Matrix[_Scalar]: ...
    def support(self) -> list[int]: ...
    def hamming_weight(self) -> int: ...
    def denominator(self) -> Integer: ...
    def numerator(self) -> FreeModuleElement[RingElement]: ...
    def dot_product(self, right: FreeModuleElement[_Scalar]) -> _Scalar: ...
    inner_product = dot_product
    def pairwise_product(self, right: FreeModuleElement[_Scalar]) -> Self: ...
    def norm(self, p: int | float | None = ...) -> RingElement: ...
    def change_ring(self, ring: Parent[_NewScalar]) -> FreeModuleElement[_NewScalar]: ...
    def apply_map(
        self,
        function: Callable[[_Scalar], _NewScalar],
        ring: Parent[_NewScalar] | None = ...,
    ) -> FreeModuleElement[_NewScalar]: ...
    def __neg__(self) -> Self: ...
    def __add__(self, right: FreeModuleElement[_Scalar]) -> Self: ...
    def __sub__(self, right: FreeModuleElement[_Scalar]) -> Self: ...
    @overload
    def __mul__(self, right: FreeModuleElement[_Scalar]) -> _Scalar: ...
    @overload
    def __mul__(self, right: Matrix[_Scalar]) -> Self: ...
    @overload
    def __mul__(self, right: _Scalar | int | Integer) -> Self: ...
    def __rmul__(self, left: _Scalar | int | Integer) -> Self: ...


class FreeModuleElement_generic_dense(FreeModuleElement[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        parent: FreeModule_generic[_Scalar],
        entries: Sequence[ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def list(self, copy: bool = ...) -> list[_Scalar]: ...


class FreeModuleElement_generic_sparse(FreeModuleElement[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        parent: FreeModule_generic[_Scalar],
        entries: dict[int, ElementConstructorInput] | Sequence[ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def dict(self, copy: bool = ...) -> dict[int, _Scalar]: ...


from sage.modules.free_module import FreeModule_generic
