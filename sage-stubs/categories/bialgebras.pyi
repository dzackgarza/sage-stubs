from sage.categories.category_types import Category_over_base_ring
from sage.categories.category import Category
from sage.categories.super_modules import SuperModulesCategory
from sage.misc.lazy_import import LazyImport

class Bialgebras(Category_over_base_ring): # type: ignore[misc]
    def super_categories(self) -> list[Category]: ...
    def additional_structure(self) -> None: ...

    class ElementMethods:
        def is_primitive(self) -> bool: ...
        def is_grouplike(self) -> bool: ...

    class Super(SuperModulesCategory): ... # type: ignore[misc]

    WithBasis: LazyImport
