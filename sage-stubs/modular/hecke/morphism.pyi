
from typing import TYPE_CHECKING

from sage.matrix.matrix_dense import Matrix
from sage.categories.morphism import Morphism
from sage.modules.matrix_morphism import MatrixMorphism
class HeckeModuleMorphism(Morphism):
    ...


class HeckeModuleMorphism_matrix(MatrixMorphism, HeckeModuleMorphism):
    

    def __init__(self, parent, A: Matrix, name: str = '', side: str = 'left') -> None: ...
    def name(self, new: str | None = None) -> str: ...
