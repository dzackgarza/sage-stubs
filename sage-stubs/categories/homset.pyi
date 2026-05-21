from typing import Any
from sage.categories.morphism import Morphism

class Homset:
    def __call__(self, *args: Any, **kwargs: Any) -> Morphism: ...
