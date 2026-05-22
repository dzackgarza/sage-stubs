from sage.categories.category import Category
from sage.categories.modules import Modules
from sage.categories.with_realizations import WithRealizationsCategory

class ModulesWithSeveralRealizations(Modules, WithRealizationsCategory):
    def super_categories(self) -> list[Category]: ...
