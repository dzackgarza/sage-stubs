
from sage.categories.homset import HomsetWithBase
from sage.categories.morphism import Morphism
from sage.matrix.matrix import Matrix
from sage.modular.hecke.module import HeckeModule_generic
from sage.modules.matrix_morphism import MatrixMorphism


class HeckeModuleMorphism(Morphism):
    ...


class HeckeModuleMorphism_matrix(MatrixMorphism, HeckeModuleMorphism):
    def __init__(
        self,
        parent: HomsetWithBase[HeckeModule_generic, HeckeModule_generic],
        A: Matrix | MatrixMorphism,
        name: str = "",
        side: str = "left",
    ) -> None: ...
    def name(self, new: str | None = None) -> str: ...
