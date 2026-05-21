from typing import Any
from sage.structure.parent import Parent

class Functor:
    def __call__(self, *args: Any, **kwargs: Any) -> Parent: ...
