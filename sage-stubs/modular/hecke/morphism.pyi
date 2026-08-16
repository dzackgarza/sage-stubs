from sage.categories.homset import Homset, HomsetWithBase
from sage.categories.morphism import Morphism
from sage.matrix.matrix import Matrix
from sage.modular.hecke.module import HeckeModule_generic
from sage.modules.matrix_morphism import MatrixMorphism, MatrixMorphism_abstract
from sage.structure.parent import Parent

class HeckeModuleMorphism(Morphism): ...

class HeckeModuleMorphism_matrix(MatrixMorphism, HeckeModuleMorphism):
    def __init__(
        self,
        parent: HomsetWithBase[HeckeModule_generic, HeckeModule_generic]
        | Homset[Parent, Parent],
        A: Matrix | MatrixMorphism | MatrixMorphism_abstract,
        name: str | bool = "",
        side: str | Literal[left, right] = "left",
    ) -> None: ...
    def name(self, new: str | None = None) -> str: ...
