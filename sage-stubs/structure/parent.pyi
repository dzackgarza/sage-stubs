from collections.abc import Callable, Hashable, Sequence

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.rings.ring import Ring
from sage.structure.element import Element
from sage.structure.sage_object import SageCoercionAtom

from .category_object import CategoryObject

type ParentCallAtom = Element | SageCoercionAtom
type ParentCallInput = ParentCallAtom | Sequence[ParentCallAtom]
type AlgebraPrintOption = (
    str
    | bool
    | tuple[str, str]
    | list[str]
    | dict[Hashable, str]
    | Sequence[str]
    | Callable[[Element], Hashable]
    | None
)

class Parent(CategoryObject):
    def __init__(self, category: Category | None = ...) -> None: ...
    def Hom(self, codomain: Parent, category: Category | None = ...) -> Homset[Parent, Parent]: ...
    def _refine_category_(self, category: Category | Sequence[Category]) -> None: ...
    def _test_not_implemented_methods(self, **options: bool | int | str | None) -> None: ...
    def __call__(self, x: ParentCallInput = ..., *args: ParentCallInput, **kwds: ParentCallInput) -> Element | Parent: ...
    def structure_morphism(self) -> Morphism: ...
    def zero(self) -> Element: ...
    def base_ring(self) -> Ring: ...
    def quotient_module(self, sub: Parent, **kwargs: bool | int | str) -> Parent: ...
    def algebra(
        self,
        base_ring: Ring | None = ...,
        category: Category | None = ...,
        **kwds: AlgebraPrintOption,
    ) -> Parent: ...
