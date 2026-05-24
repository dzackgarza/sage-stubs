from typing import Protocol

from sage.manifolds.subset import ManifoldSubset
from sage.structure.parent import Parent

class _SubsetPointLike(Protocol):
    def parent(self) -> Parent: ...

class _ManifoldPointLike(Protocol):
    def parent(self) -> ManifoldSubset: ...

class _ImageMap(Protocol):
    _name: str | None
    _latex_name: str | None

    def domain(self) -> ManifoldSubset: ...
    def codomain(self) -> ManifoldSubset: ...
    def __call__(self, point: _ManifoldPointLike) -> _ManifoldPointLike: ...

class ImageManifoldSubset(ManifoldSubset):
    _map: _ImageMap
    _inverse: _ImageMap | None
    _domain_subset: ManifoldSubset

    def __init__(
        self,
        map: _ImageMap,
        inverse: _ImageMap | None = None,
        name: str | None = None,
        latex_name: str | None = None,
        domain_subset: ManifoldSubset | None = None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _an_element_(self) -> _ManifoldPointLike: ...
    def __contains__(self, point: _SubsetPointLike) -> bool: ...
