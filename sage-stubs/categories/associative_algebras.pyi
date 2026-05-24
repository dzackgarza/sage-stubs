from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.category import Category
from sage.misc.lazy_import import LazyImport
from sage.structure.parent import Parent

class AssociativeAlgebras(CategoryWithAxiom_over_base_ring):
    Unital: LazyImport
    def __init__(self, base: Parent | Category, name: str | None = None) -> None: ...
    def WithBasis(self) -> Category: ...
    def FiniteDimensional(self) -> Category: ...
