from sage.categories.category import Category
from sage.structure.element import Element
from sage.structure.parent import Parent

class SemisimpleAlgebras:
    def __init__(self, base: Parent | Category, name: str | None = None) -> None: ...
    class ParentMethods:
        def radical_basis(self) -> tuple[Element, ...]: ...
    class FiniteDimensional:
        ...
