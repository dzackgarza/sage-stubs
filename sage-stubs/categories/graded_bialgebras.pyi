from sage.categories.bialgebras import Bialgebras
from sage.categories.category import Category
from sage.categories.graded_algebras import GradedAlgebras
from sage.categories.graded_coalgebras import GradedCoalgebras

class GradedBialgebras(GradedAlgebras, Bialgebras, GradedCoalgebras):
    def super_categories(self) -> list[Category]: ...
