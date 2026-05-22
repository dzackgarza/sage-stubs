from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.category_with_axiom import CategoryWithAxiom
    from sage.categories.graded_modules import GradedModulesCategory
else:
    CategoryWithAxiom = object
    GradedModulesCategory = object

class LambdaBracketAlgebrasWithBasis(CategoryWithAxiom):
    class ElementMethods:
        def index(self) -> tuple[str, int] | None: ...
        
    class FinitelyGeneratedAsLambdaBracketAlgebra(CategoryWithAxiom):
        class Graded(GradedModulesCategory):
            class ParentMethods:
                def degree_on_basis(self, m: object) -> int: ...
