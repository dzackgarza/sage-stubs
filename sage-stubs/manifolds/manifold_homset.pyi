from collections.abc import Callable
from typing import Literal, overload

from sage.categories.category import Category
from sage.categories.homset import Homset, HomsetCallInput
from sage.categories.morphism import Morphism
from sage.matrix.matrix2 import Matrix
from sage.manifolds.continuous_map import (
    _CoordinateFunctions,
    ContinuousMap,
)
from sage.manifolds.manifold import TopologicalManifold
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent, ParentCallInput
from sage.structure.unique_representation import UniqueRepresentation

class TopologicalManifoldHomset(
    UniqueRepresentation, Homset[TopologicalManifold, TopologicalManifold]
):
    Element = ContinuousMap
    element_class: type[ContinuousMap]

    def __init__(
        self,
        domain: TopologicalManifold,
        codomain: TopologicalManifold,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...
    def _latex_(self) -> str: ...
    def _element_constructor_(
        self,
        coord_functions: _CoordinateFunctions,
        name: str | None = None,
        latex_name: str | None = None,
        is_isomorphism: bool = False,
        is_identity: bool = False,
    ) -> ContinuousMap: ...
    def _an_element_(self) -> ContinuousMap: ...
    def _coerce_map_from_(self, other: ParentCallInput) -> bool: ...
    @overload
    def __call__(self, x: HomsetCallInput = ..., check: bool | None = None) -> ContinuousMap: ...
    @overload
    def __call__(
        self,
        coord_functions: _CoordinateFunctions,
        name: str | None = None,
        latex_name: str | None = None,
        is_isomorphism: bool = False,
        is_identity: bool = False,
    ) -> ContinuousMap: ...
    @overload
    def __call__(
        self,
        *,
        on_basis: Callable[..., SageElement],
        codomain: Parent | None = None,
        category: Category | None = None,
        zero: SageElement | None = None,
        position: int = 0,
        triangular: Literal["upper", "lower"] | None = None,
        unitriangular: bool = False,
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        function: Callable[..., SageElement],
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
        diagonal: Callable[..., SageElement],
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
    def one(self) -> ContinuousMap: ...
