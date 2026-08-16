from collections.abc import Callable
from typing import Generic, TypeVar

from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.structure.element import Element
from sage.structure.parent import Parent

_DomainElement = TypeVar("_DomainElement", default=Element)
_CodomainElement = TypeVar("_CodomainElement", default=Element)

class DefaultConvertMap(
    Map[_DomainElement, _CodomainElement], Generic[_DomainElement, _CodomainElement]
):
    def __init__(
        self,
        domain: Parent[_DomainElement]
        | Homset[
            Map[_DomainElement, _CodomainElement], _DomainElement, _CodomainElement
        ],
        codomain: Parent[_CodomainElement] | None,
        category: object | None = ...,
    ) -> None: ...
    def domain(self) -> Parent[DefaultConvertMap]: ...
    def codomain(self) -> Parent[DefaultConvertMap]: ...
    def _repr_type(self) -> str: ...
    def _call_(self, x: _DomainElement) -> DefaultConvertMap: ...
    def _call_with_args(
        self,
        x: _DomainElement,
        args: tuple[_DomainElement, ...] = ...,
        kwds: dict[str, _DomainElement] = ...,
    ) -> DefaultConvertMap: ...

class DefaultConvertMap_unique(DefaultConvertMap[_DomainElement, _CodomainElement]): ...

class NamedConvertMap(DefaultConvertMap[_DomainElement, _CodomainElement]):
    def __init__(
        self,
        domain: Parent[_DomainElement],
        codomain: Parent[_CodomainElement],
        method_name: str,
    ) -> None: ...

class CallableConvertMap(DefaultConvertMap[_DomainElement, _CodomainElement]):
    def __init__(
        self,
        domain: Parent[_DomainElement],
        codomain: Parent[_CodomainElement],
        func: Callable[[_DomainElement], _CodomainElement],
        parent_as_first_arg: bool | None = ...,
    ) -> None: ...

class CCallableConvertMap_class(
    DefaultConvertMap[_DomainElement, _CodomainElement]
): ...

def CCallableConvertMap(
    domain: Parent[_DomainElement],
    codomain: Parent[_CodomainElement],
    func: Callable[[_DomainElement], _CodomainElement],
    name: str | None,
) -> CCallableConvertMap_class[_DomainElement, _CodomainElement]: ...

class ListMorphism(DefaultConvertMap[list[_DomainElement], list[_CodomainElement]]):
    def __init__(
        self,
        domain: Parent[list[_DomainElement]] | Parent[_DomainElement],
        real_morphism: Map[_DomainElement, _CodomainElement] | Parent[_CodomainElement],
    ) -> None: ...

class TryMap(DefaultConvertMap[_DomainElement, _CodomainElement]):
    def __init__(
        self,
        morphism_preferred: Map[_DomainElement, _CodomainElement]
        | Parent[_DomainElement],
        morphism_backup: Map[_DomainElement, _CodomainElement]
        | Parent[_CodomainElement],
        error_types: tuple[type[Exception], ...] | None = ...,
    ) -> None: ...
