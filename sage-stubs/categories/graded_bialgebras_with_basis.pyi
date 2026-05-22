from sage.categories.bialgebras_with_basis import BialgebrasWithBasis
from sage.categories.category import Category
from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis
from sage.categories.graded_coalgebras_with_basis import GradedCoalgebrasWithBasis

class GradedBialgebrasWithBasis(GradedAlgebrasWithBasis, BialgebrasWithBasis, GradedCoalgebrasWithBasis):
    def super_categories(self) -> list[Category]: ...
