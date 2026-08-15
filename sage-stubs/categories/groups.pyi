from collections.abc import Iterable
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.structure.element import MultiplicativeGroupElement
from sage.structure.parent import Parent

_E = TypeVar(
    "_E",
    bound=MultiplicativeGroupElement,
    default=MultiplicativeGroupElement,
    covariant=True,
)

class Groups(Category):
    def __init__(self) -> None: ...
    def Commutative(self) -> Category: ...
    def Topological(self) -> Category: ...
    def FinitelyGenerated(self) -> CategoryWithAxiom: ...

    class ElementMethods:
        ...
    class ParentMethods(Parent[_E], Generic[_E]):
        def group_generators(self) -> Iterable[_E]: ...
        def one(self) -> _E: ...

Group = Groups.ParentMethods
GroupElement = MultiplicativeGroupElement
