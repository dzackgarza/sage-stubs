from sage.categories.super_modules import SuperModulesCategory
from sage.categories.morphism import Morphism

class SuperHopfAlgebrasWithBasis(SuperModulesCategory):
    class ParentMethods:
        @property
        def antipode(self) -> Morphism: ...
        def _test_antipode(self, **options: object) -> None: ...
