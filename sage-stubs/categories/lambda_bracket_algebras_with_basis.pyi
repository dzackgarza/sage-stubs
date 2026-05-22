from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.graded_modules import GradedModulesCategory

class LambdaBracketAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    class ElementMethods:
        def index(self) -> tuple[str, int] | None: ...
        
    class FinitelyGeneratedAsLambdaBracketAlgebra(CategoryWithAxiom_over_base_ring):
        class Graded(GradedModulesCategory):
            class ParentMethods:
                def degree_on_basis(self, m: object) -> int: ...
