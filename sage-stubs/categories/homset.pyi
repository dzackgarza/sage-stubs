from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism

class Homset:
    def __call__(self, *args: Any, **kwargs: Any) -> Morphism: ...
