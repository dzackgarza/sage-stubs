from collections.abc import Callable, Sequence
from typing import Generic, Literal, TypeVar, overload

from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import VectorSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.structure.element import ElementConstructorInput, FieldElement, RingElement

_Scalar = TypeVar("_Scalar", bound=FieldElement, default=FieldElement)
_RingScalar = TypeVar("_RingScalar", bound=RingElement)

type MatrixSide = Literal["left", "right"]
type LinearTransformationRule[_Scalar: FieldElement] = (
    Matrix[_Scalar]
    | Sequence[
        FreeModuleElement[_Scalar]
        | Sequence[ElementConstructorInput]
    ]
    | Callable[
        [FreeModuleElement[_Scalar]],
        FreeModuleElement[_Scalar]
        | Sequence[ElementConstructorInput],
    ]
)

@overload
def linear_transformation(
    arg0: Matrix[_RingScalar],
    arg1: None = ...,
    arg2: None = ...,
    side: MatrixSide = ...,
) -> VectorSpaceMorphism[FieldElement]: ...
@overload
def linear_transformation(
    arg0: VectorSpace[_Scalar],
    arg1: VectorSpace[_Scalar],
    arg2: LinearTransformationRule[_Scalar],
    side: MatrixSide = ...,
) -> VectorSpaceMorphism[_Scalar]: ...

class VectorSpaceMorphism(
    FreeModuleMorphism[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        homspace: VectorSpaceHomspace[_Scalar],
        A: Matrix[_Scalar],
        side: MatrixSide = ...,
    ) -> None: ...
    def parent(self) -> VectorSpaceHomspace[_Scalar]: ...
    def domain(self) -> VectorSpace[_Scalar]: ...
    def codomain(self) -> VectorSpace[_Scalar]: ...
    def is_invertible(self) -> bool: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...

from sage.modules.vector_space_homspace import VectorSpaceHomspace
