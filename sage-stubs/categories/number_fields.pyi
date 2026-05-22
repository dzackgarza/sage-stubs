from typing import TYPE_CHECKING

from sage.categories.category_singleton import Category_singleton
from sage.categories.category import Category

if TYPE_CHECKING:
    from sage.rings.number_field.number_field_base import NumberField
    from sage.structure.sage_object import SageObject

class NumberFields(Category_singleton):
    def super_categories(self) -> list[Category]: ...
    def _call_(self, x: object) -> NumberField: ...

    class ParentMethods:
        def zeta_function(self, prec: int = ..., max_imaginary_part: float = ..., algorithm: str = ...) -> SageObject: ...
        def _test_absolute_disc(self, **options: object) -> None: ...

    class ElementMethods: ...
