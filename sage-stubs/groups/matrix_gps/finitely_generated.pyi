from sage.categories.category import Category
from sage.categories.groups import Groups
from sage.groups.matrix_gps.finitely_generated_gap import FinitelyGeneratedMatrixGroup_gap
from sage.groups.matrix_gps.group_element import MatrixGroupElement_base
from sage.groups.matrix_gps.matrix_group import MatrixGroup_generic
from sage.structure.element import Matrix
from sage.structure.parent import ElementConstructorInput

type MatrixGroupGeneratorInput = Matrix | int | ElementConstructorInput

class FinitelyGeneratedMatrixGroup_generic(
    MatrixGroup_generic,
    Groups.ParentMethods[MatrixGroupElement_base],
):
    def gens(self) -> tuple[MatrixGroupElement_base, ...]: ...
    def ngens(self) -> int: ...

def MatrixGroup(
    *group_generators: MatrixGroupGeneratorInput,
    check: bool = ...,
    category: Category | None = ...,
) -> FinitelyGeneratedMatrixGroup_gap | FinitelyGeneratedMatrixGroup_generic: ...
