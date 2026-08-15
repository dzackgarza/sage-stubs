from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.category import Category
from sage.misc.lazy_import import LazyImport

class AssociativeAlgebras(CategoryWithAxiom_over_base_ring):
    Unital: LazyImport
    def WithBasis(self) -> Category: ...
    def FiniteDimensional(self) -> Category: ...
