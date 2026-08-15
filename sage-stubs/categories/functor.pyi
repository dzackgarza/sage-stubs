from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent

class Functor:
    def __call__(self, x: Parent | Morphism) -> Parent | Morphism: ...
