from collections.abc import Iterable

from sage.categories.algebras import Algebras
from sage.categories.category_types import Category_over_base_ring
from sage.categories.covariant_functorial_construction import (
    CovariantConstructionCategory,
    CovariantFunctorialConstruction,
)
from sage.categories.pushout import ConstructionFunctor
from sage.categories.tensor import TensorProductOfAlgebras
from sage.groups.group import Group
from sage.rings.ring import Ring
from sage.structure.sage_object import SageObject

class AlgebraFunctor(CovariantFunctorialConstruction):
    def __init__(self, base_ring: Ring) -> None: ...
    def base_ring(self) -> Ring: ...
    def __call__(
        self, G: Group | Iterable[SageObject], category: object | None = ...
    ) -> Algebras: ...

class GroupAlgebraFunctor(ConstructionFunctor):
    def __init__(self, group: Group) -> None: ...
    def group(self) -> Group: ...

class AlgebrasCategory(CovariantConstructionCategory, Category_over_base_ring):
    class ParentMethods:
        def coproduct_on_basis(self, g: object) -> TensorProductOfAlgebras: ...
