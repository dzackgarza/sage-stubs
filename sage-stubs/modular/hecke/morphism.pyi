from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.matrix.matrix_dense import Matrix
    from sage.categories.morphism import Morphism
    from sage.modules.matrix_morphism import MatrixMorphism

class HeckeModuleMorphism(Morphism):
    """Abstract base class for morphisms of Hecke modules."""

    pass

class HeckeModuleMorphism_matrix(MatrixMorphism, HeckeModuleMorphism):
    """Morphisms of Hecke modules when the morphism is given by a matrix."""

    def __init__(self, parent, A: Matrix, name: str = '', side: str = 'left') -> None: ...
    def name(self, new: str | None = None) -> str: ...
