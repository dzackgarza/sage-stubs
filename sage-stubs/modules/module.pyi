from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.structure.element import ModuleElement, RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)
_Element = TypeVar("_Element", bound=ModuleElement, default=ModuleElement)
_SourceElement = TypeVar("_SourceElement", bound=ModuleElement)


class Module(Parent[_Element], Generic[_Scalar, _Element]):
    Element: type[_Element]

    def __init__(
        self,
        base: Parent[_Scalar],
        category: Category | None = ...,
        names: str | tuple[str, ...] | None = ...,
    ) -> None: ...
    def _coerce_map_from_(
        self,
        M: Module[RingElement, _SourceElement],
    ) -> Morphism[_SourceElement, _Element] | None: ...
    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> Module[_NewScalar, ModuleElement]: ...
    def base_extend(
        self,
        R: Parent[_NewScalar],
    ) -> Module[_NewScalar, ModuleElement]: ...
    def endomorphism_ring(
        self,
    ) -> Homset[Map, _Element, _Element]: ...


def is_Module(x: object) -> bool: ...
def is_VectorSpace(x: object) -> bool: ...
