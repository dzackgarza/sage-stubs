from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sage.structure.element import Element

class Morphism:
    def __call__(self, *args: Any, **kwargs: Any) -> Element: ...
    def is_invertible(self) -> bool: ...
