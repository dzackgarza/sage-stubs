from sage.categories.category import Category, CategoryWithParameters, JoinCategory
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.bimodules import Bimodules
from sage.categories.schemes import Schemes
from sage.misc.unknown import Unknown


class Category_over_base(CategoryWithParameters):
    r"""
    A base class for categories over some base object.
    """

    def __init__(self, base: Category | object, name: str | None = None) -> None: ...

    def _make_named_class_key(self, name: str) -> Category | type | tuple[object, ...]: ...

    def base(self) -> Category | object: ...

    def _repr_object_names(self) -> str: ...

    def _latex_(self) -> str: ...


class Category_module(AbelianCategory, Category_over_base_ring):
    pass
