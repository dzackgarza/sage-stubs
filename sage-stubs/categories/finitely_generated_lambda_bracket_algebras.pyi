from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.lambda_bracket_algebras import LambdaBracketAlgebras
from sage.structure.element import Element


class FinitelyGeneratedLambdaBracketAlgebras(
    CategoryWithAxiom_over_base_ring,
):
    _base_category_class_and_axiom: tuple[
        type[LambdaBracketAlgebras],
        str,
    ]

    class ParentMethods:
        def ngens(self) -> int: ...
        def gen(self, i: int) -> Element: ...
        def some_elements(self) -> list[Element]: ...

    class Graded(GradedModulesCategory):
        def _repr_object_names(self) -> str: ...
