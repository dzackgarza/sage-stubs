from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.lie_conformal_algebras import LieConformalAlgebras
from sage.categories.super_modules import SuperModulesCategory
from sage.structure.element import Element


class FinitelyGeneratedLieConformalAlgebras(
    CategoryWithAxiom_over_base_ring,
):
    _base_category_class_and_axiom: tuple[
        type[LieConformalAlgebras],
        str,
    ]

    class ParentMethods:
        def some_elements(self) -> list[Element]: ...

    class Super(SuperModulesCategory):
        class Graded(GradedModulesCategory):
            def _repr_object_names(self) -> str: ...

    class Graded(GradedModulesCategory):
        def _repr_object_names(self) -> str: ...
