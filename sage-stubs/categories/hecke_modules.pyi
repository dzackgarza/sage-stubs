from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.category import Category
    from sage.categories.algebras import Algebras
    from sage.categories.homset import HomsetsCategory
else:
    Category = object
    Algebras = object
    HomsetsCategory = object

class HeckeModules(Category):
    def __init__(self, R: object) -> None: ...
    def super_categories(self) -> list['Category']: ...
    def _repr_object_names(self) -> str: ...
    
    class ParentMethods:
        def Endomorphism_algebra(self) -> 'Algebras': ...
        
    class Homsets(HomsetsCategory):
        def extra_super_categories(self) -> list['Category']: ...
