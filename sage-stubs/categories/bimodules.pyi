from sage.categories.category import Category, CategoryWithParameters
from sage.structure.parent import Parent

class Bimodules(CategoryWithParameters):
    def __init__(
        self,
        left_base: Parent | Category,
        right_base: Parent | Category,
        name: str | None = None,
    ) -> None: ...
    class ElementMethods:
        ...
    class ParentMethods:
        ...
