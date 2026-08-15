from collections.abc import Callable
from typing import Generic, TypeVar

from sage.categories.map import Map
from sage.structure.parent import Parent
from sage.structure.element import Element

_DomainElement = TypeVar("_DomainElement", default=Element)
_CodomainElement = TypeVar("_CodomainElement", default=Element)

class DefaultConvertMap(Map[_DomainElement, _CodomainElement], Generic[_DomainElement, _CodomainElement]):
    def __init__(self, domain: Parent[_DomainElement], codomain: Parent[_CodomainElement], category: object | None = ...) -> None: ...
    def domain(self) -> Parent[_DomainElement]: ...
    def codomain(self) -> Parent[_CodomainElement]: ...
    def _repr_type(self) -> str: ...
    def _call_(self, x: _DomainElement) -> _CodomainElement: ...
    def _call_with_args(self, x: _DomainElement, args: tuple[_DomainElement, ...] = ..., kwds: dict[str, _DomainElement] = ...) -> _CodomainElement: ...

class DefaultConvertMap_unique(DefaultConvertMap[_DomainElement, _CodomainElement]): ...

class NamedConvertMap(DefaultConvertMap[_DomainElement, _CodomainElement]):
    def __init__(self, domain: Parent[_DomainElement], codomain: Parent[_CodomainElement], method_name: str) -> None: ...

class CallableConvertMap(DefaultConvertMap[_DomainElement, _CodomainElement]):
    def __init__(
        self,
        domain: Parent[_DomainElement],
        codomain: Parent[_CodomainElement],
        func: Callable[[_DomainElement], _CodomainElement],
        parent_as_first_arg: bool | None = ...,
    ) -> None: ...

class CCallableConvertMap_class(DefaultConvertMap[_DomainElement, _CodomainElement]): ...

def CCallableConvertMap(
    domain: Parent[_DomainElement],
    codomain: Parent[_CodomainElement],
    func: Callable[[_DomainElement], _CodomainElement],
    name: str | None,
) -> CCallableConvertMap_class[_DomainElement, _CodomainElement]: ...

class ListMorphism(DefaultConvertMap[list[_DomainElement], list[_CodomainElement]]):
    def __init__(self, domain: Parent[list[_DomainElement]], real_morphism: Map[_DomainElement, _CodomainElement]) -> None: ...

class TryMap(DefaultConvertMap[_DomainElement, _CodomainElement]):
    def __init__(
        self,
        morphism_preferred: Map[_DomainElement, _CodomainElement],
        morphism_backup: Map[_DomainElement, _CodomainElement],
        error_types: tuple[type[Exception], ...] | None = ...,
    ) -> None: ...
