from sage.categories.algebras import Algebras
from sage.categories.category import Category
from sage.categories.with_realizations import WithRealizationsCategory

class AlgebrasWithSeveralRealizations(Algebras, WithRealizationsCategory):
    def super_categories(self) -> list[Category]: ...
