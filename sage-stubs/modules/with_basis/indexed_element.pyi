from collections.abc import Callable, Hashable, Iterator, Mapping, Sequence
from typing import Generic, Self, TypeVar, overload

from sage.combinat.free_module import CombinatorialFreeModule
from sage.interfaces.expect import Expect
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import Element, ModuleElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.typeset.ascii_art import AsciiArt
from sage.typeset.unicode_art import UnicodeArt

_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)

type IndexedElementStateValue[_Index: Hashable, _Scalar: RingElement] = (
    Mapping[_Index, _Scalar] | bool | int
)


class IndexedFreeModuleElement(
    ModuleElement,
    Generic[_Index, _Scalar],
):
    def __init__(
        self,
        M: CombinatorialFreeModule,
        x: Mapping[_Index, _Scalar],
    ) -> None: ...
    def parent(self) -> CombinatorialFreeModule: ...
    def __iter__(self) -> Iterator[tuple[_Index, _Scalar]]: ...
    def __contains__(self, x: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[
            [CombinatorialFreeModule, Mapping[_Index, _Scalar]],
            IndexedFreeModuleElement[_Index, _Scalar],
        ],
        tuple[CombinatorialFreeModule, Mapping[_Index, _Scalar]],
    ]: ...
    def __setstate__(
        self,
        state: tuple[
            Parent[Self],
            Mapping[str, IndexedElementStateValue[_Index, _Scalar]],
        ],
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: dict[int, Self] | None = ...) -> Self: ...
    def monomial_coefficients(
        self,
        copy: bool = ...,
    ) -> dict[_Index, _Scalar]: ...
    def _sorted_items_for_printing(self) -> list[tuple[_Index, _Scalar]]: ...
    def _repr_(self) -> str: ...
    def _ascii_art_(self) -> AsciiArt: ...
    def _unicode_art_(self) -> UnicodeArt: ...
    def _latex_(self) -> str: ...
    def _richcmp_(
        self,
        other: IndexedFreeModuleElement[_Index, _Scalar],
        op: int,
    ) -> bool: ...
    def _add_(self, other: IndexedFreeModuleElement[_Index, _Scalar]) -> Self: ...
    def _neg_(self) -> Self: ...
    def _sub_(self, other: IndexedFreeModuleElement[_Index, _Scalar]) -> Self: ...
    def __getitem__(self, m: _Index) -> _Scalar: ...
    @overload
    def _vector_(
        self,
        new_base_ring: None = ...,
        order: Sequence[_Index] | Mapping[_Index, int] | None = ...,
        sparse: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    @overload
    def _vector_(
        self,
        new_base_ring: Parent[_NewScalar],
        order: Sequence[_Index] | Mapping[_Index, int] | None = ...,
        sparse: bool = ...,
    ) -> FreeModuleElement[_NewScalar]: ...
    @overload
    def to_vector(
        self,
        new_base_ring: None = ...,
        order: Sequence[_Index] | Mapping[_Index, int] | None = ...,
        sparse: bool = ...,
    ) -> FreeModuleElement[_Scalar]: ...
    @overload
    def to_vector(
        self,
        new_base_ring: Parent[_NewScalar],
        order: Sequence[_Index] | Mapping[_Index, int] | None = ...,
        sparse: bool = ...,
    ) -> FreeModuleElement[_NewScalar]: ...
    def _acted_upon_(
        self,
        scalar: ElementConstructorInput,
        self_on_left: bool,
    ) -> Self | None: ...
    def _lmul_(self, right: Element) -> Self: ...
    def _rmul_(self, left: Element) -> Self: ...
    def __truediv__(self, x: ElementConstructorInput) -> Self: ...
    def _magma_init_(self, magma: Expect) -> str: ...


def _unpickle_element(
    C: CombinatorialFreeModule,
    d: Mapping[_Index, _Scalar],
) -> IndexedFreeModuleElement[_Index, _Scalar]: ...
