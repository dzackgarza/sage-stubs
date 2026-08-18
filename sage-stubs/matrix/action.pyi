from typing import Generic, TypeVar

from sage.categories.action import Action
from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_TargetScalar = TypeVar("_TargetScalar", bound=RingElement)


class MatrixAction(Action, Generic[_Scalar]):
    def matrix_space(self) -> MatrixSpace[_Scalar]: ...


class MatrixMatrixAction(MatrixAction[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        left: MatrixSpace[_Scalar],
        right: MatrixSpace[_Scalar],
    ) -> None: ...
    def _act_(
        self,
        left: Matrix[_Scalar],
        right: Matrix[_Scalar],
    ) -> Matrix[_Scalar]: ...
    def codomain(self) -> MatrixSpace[_Scalar]: ...


class MatrixVectorAction(MatrixAction[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        matrix_space: MatrixSpace[_Scalar],
        vector_space: FreeModule_generic[_Scalar],
    ) -> None: ...
    def _act_(
        self,
        matrix: Matrix[_Scalar],
        vector: FreeModuleElement[_Scalar],
    ) -> FreeModuleElement[_Scalar]: ...
    def codomain(self) -> FreeModule_generic[_Scalar]: ...


class VectorMatrixAction(MatrixAction[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        vector_space: FreeModule_generic[_Scalar],
        matrix_space: MatrixSpace[_Scalar],
    ) -> None: ...
    def _act_(
        self,
        vector: FreeModuleElement[_Scalar],
        matrix: Matrix[_Scalar],
    ) -> FreeModuleElement[_Scalar]: ...
    def codomain(self) -> FreeModule_generic[_Scalar]: ...


class MatrixScalarAction(
    MatrixAction[_Scalar],
    Generic[_Scalar, _TargetScalar],
):
    def __init__(
        self,
        scalar_parent: Parent[_TargetScalar],
        matrix_space: MatrixSpace[_Scalar],
        is_left: bool,
    ) -> None: ...
    def _act_(
        self,
        scalar: _TargetScalar,
        matrix: Matrix[_Scalar],
    ) -> Matrix[_TargetScalar]: ...
    def codomain(self) -> MatrixSpace[_TargetScalar]: ...
