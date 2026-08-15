from collections.abc import Callable
from typing import Generic, Literal, TypeVar, overload

from sage.matrix.matrix2 import Matrix
from sage.categories.morphism import Morphism
from sage.categories.category import Category
from sage.rings.ring import Ring
from sage.structure.element import Element
from sage.structure.parent import Parent, ParentCallInput

_DomainElementT = TypeVar("_DomainElementT", bound=Parent)
_CodomainElementT = TypeVar("_CodomainElementT", bound=Parent)
type HomsetCallInput = Morphism | Callable[..., Element] | ParentCallInput

def Hom(
    X: _DomainElementT,
    Y: _CodomainElementT,
    category: Category | None = None,
    check: bool = True,
) -> Homset[_DomainElementT, _CodomainElementT]: ...

def hom(X: Parent, Y: Parent, f: HomsetCallInput) -> Morphism: ...

def End(X: Parent, category: Category | None = None) -> Homset[Parent, Parent]: ...

def end(X: Parent, f: HomsetCallInput) -> Morphism: ...

class Homset(Generic[_DomainElementT, _CodomainElementT]):
    def __init__(
        self,
        X: _DomainElementT,
        Y: _CodomainElementT,
        category: Category | None = None,
        base: Ring | None = None,
        check: bool = True,
    ) -> None: ...
    @overload
    def __call__(self, x: HomsetCallInput = ..., check: bool | None = None) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        on_basis: Callable[..., Element],
        codomain: Parent | None = None,
        category: Category | None = None,
        zero: Element | None = None,
        position: int = 0,
        triangular: Literal["upper", "lower"] | None = None,
        unitriangular: bool = False,
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        function: Callable[..., Element],
        codomain: Parent | None = None,
        category: Category | None = None,
        triangular: Literal["upper", "lower"] | None = None,
        unitriangular: bool = False,
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        diagonal: Callable[..., Element],
        codomain: Parent | None = None,
        category: Category | None = None,
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        matrix: Matrix,
        codomain: Parent | None = None,
        category: Category | None = None,
        side: Literal["left", "right"] = "left",
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    def _repr_(self) -> str: ...
    def __hash__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def homset_category(self) -> Category: ...
    def domain(self) -> _DomainElementT: ...
    def codomain(self) -> _CodomainElementT: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __contains__(self, x: object) -> bool: ...
    def natural_map(self) -> Morphism: ...
    def identity(self) -> Morphism: ...
    def one(self) -> Morphism: ...

class HomsetWithBase(Homset[_DomainElementT, _CodomainElementT]):
    ...
