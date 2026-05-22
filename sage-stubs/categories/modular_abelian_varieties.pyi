from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.category_with_axiom import CategoryWithAxiom
    from sage.categories.homset import HomsetsCategory
    from sage.categories.category import Category
    from sage.rings.ring import Field
else:
    CategoryWithAxiom = object
    HomsetsCategory = object
    Category = object
    Field = object

class ModularAbelianVarieties(Category):
    def __init__(self, Y: object) -> None: ...
    def base_field(self) -> 'Field': ...
    def super_categories(self) -> list['Category']: ...
    
    class Homsets(HomsetsCategory):
        class Endset(CategoryWithAxiom):
            def extra_super_categories(self) -> list['Category']: ...
