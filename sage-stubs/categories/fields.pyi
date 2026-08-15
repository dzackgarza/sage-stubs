from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.rings import Rings
from sage.structure.element import FieldElement

_CategoryElement = TypeVar(
    "_CategoryElement",
    bound=FieldElement,
    default=FieldElement,
    covariant=True,
)
_ParentElement = TypeVar(
    "_ParentElement",
    bound=FieldElement,
    default=FieldElement,
    covariant=True,
)

class Fields(Category, Generic[_CategoryElement]):
    def __init__(self) -> None: ...
    def __contains__(self, x: object) -> bool: ...
    class ElementMethods:
        ...
    class ParentMethods(Rings.ParentMethods[_ParentElement], Generic[_ParentElement]):
        def fraction_field(self) -> Fields.ParentMethods[_ParentElement]: ...
