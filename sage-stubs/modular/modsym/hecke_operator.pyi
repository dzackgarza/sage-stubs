
from sage.rings.integer import Integer
from sage.matrix.matrix import Matrix
from sage.structure.element import Element
class HeckeOperator:
    def apply_sparse(self, x: Element) -> Element: ...
