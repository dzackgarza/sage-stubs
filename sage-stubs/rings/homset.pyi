from collections.abc import Callable, Sequence
from typing import Generic, TypeVar, overload

from sage.categories.category import Category
from sage.categories.homset import HomsetWithBase
from sage.rings.morphism import RingHomomorphism, RingHomomorphism_im_gens
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_DomainElement = TypeVar(
    "_DomainElement",
    bound=RingElement,
    default=RingElement,
)
_CodomainElement = TypeVar(
    "_CodomainElement",
    bound=RingElement,
    default=RingElement,
)

def RingHomset(
    R: Parent[_DomainElement],
    S: Parent[_CodomainElement],
    category: Category | None = None,
) -> RingHomset_generic[_DomainElement, _CodomainElement]: ...

class RingHomset_generic(
    HomsetWithBase[
        RingHomomorphism,
        _DomainElement,
        _CodomainElement,
    ],
    Generic[_DomainElement, _CodomainElement],
):
    def __init__(
        self,
        R: Parent[_DomainElement],
        S: Parent[_CodomainElement],
        category: Category | None = None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def has_coerce_map_from(self, x: object) -> bool: ...
    @overload
    def __call__(
        self,
        x: RingHomomorphism,
        check: bool = True,
        base_map: RingHomomorphism | None = None,
    ) -> RingHomomorphism: ...
    @overload
    def __call__(
        self,
        x: Sequence[_CodomainElement]
        | Callable[[_DomainElement], _CodomainElement],
        check: bool = True,
        base_map: RingHomomorphism | None = None,
    ) -> RingHomomorphism_im_gens: ...
    def _element_constructor_(
        self,
        x: RingHomomorphism
        | Sequence[_CodomainElement]
        | Callable[[_DomainElement], _CodomainElement],
        check: bool = True,
        base_map: RingHomomorphism | None = None,
    ) -> RingHomomorphism: ...
    def natural_map(self) -> RingHomomorphism: ...
    def zero(self) -> RingHomomorphism: ...
    def domain(self) -> Parent[_DomainElement]: ...
    def codomain(self) -> Parent[_CodomainElement]: ...

class RingHomset_quo_ring(
    RingHomset_generic[_DomainElement, _CodomainElement],
):
    def _element_constructor_(
        self,
        x: RingHomomorphism
        | Sequence[_CodomainElement]
        | Callable[[_DomainElement], _CodomainElement],
        base_map: RingHomomorphism | None = None,
        check: bool = True,
    ) -> RingHomomorphism: ...
