from sage.libs.gap.element import GapElement
from sage.groups.matrix_gps.finitely_generated_gap import FinitelyGeneratedMatrixGroup_gap
from sage.structure.element import Matrix, MultiplicativeGroupElement

class MatrixGroupElement_base(MultiplicativeGroupElement):
    def matrix(self) -> Matrix: ...

class MatrixGroupElement_gap(MatrixGroupElement_base):
    def parent(self, x: None = None) -> FinitelyGeneratedMatrixGroup_gap: ...
    def gap(self) -> GapElement: ...
