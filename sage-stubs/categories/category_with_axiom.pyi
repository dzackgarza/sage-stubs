from sage.categories.category_cy_helper import AxiomContainer
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_types import Category_over_base_ring

from .category import Category

class CategoryWithAxiom(Category):
    _base_category_class_and_axiom: tuple[type[Category], str]
    def __init__(self, base_category: Category) -> None: ...
    def base_category(self) -> Category: ...

class CategoryWithAxiom_over_base_ring(CategoryWithAxiom, Category_over_base_ring):
    def __init__(self, base_category: Category) -> None: ...

class CategoryWithAxiom_singleton(Category_singleton, CategoryWithAxiom): ...

all_axioms: AxiomContainer

def uncamelcase(s: str, separator: str = " ") -> str: ...
def base_category_class_and_axiom(cls: type[Category]) -> tuple[type[Category], str]: ...
