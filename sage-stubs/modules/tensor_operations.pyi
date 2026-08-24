from collections.abc import Collection, Iterable, KeysView, Sequence, ValuesView
from typing import Generic, Literal, TypeVar

from sage.modules.free_module import FreeModule_ambient_field
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import FieldElement
from sage.structure.formal_sum import FormalSum
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=FieldElement, default=FieldElement)

type TensorOperationKind = Literal["product", "symmetric", "antisymmetric"]
type VectorInput[_Scalar: FieldElement] = (
    Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar]
)
type TensorMultiIndex = tuple[int | Integer, ...]


def symmetrized_coordinate_sums(
    dim: int | Integer,
    n: int | Integer,
) -> tuple[FormalSum, ...]: ...
def antisymmetrized_coordinate_sums(
    dim: int | Integer,
    n: int | Integer,
) -> tuple[FormalSum, ...]: ...


class VectorCollection(
    FreeModule_ambient_field[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        vector_collection: Collection[VectorInput[_Scalar]],
        base_ring: Parent[_Scalar],
        dim: int | Integer,
    ) -> None: ...
    def vectors(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def n_vectors(self) -> int: ...


class TensorOperation(VectorCollection[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        vector_collections: Sequence[VectorCollection[_Scalar]],
        operation: TensorOperationKind = ...,
    ) -> None: ...
    def _init_product_vectors(
        self,
        indices: Sequence[int | Integer],
    ) -> int: ...
    def _init_power_operation_vectors(
        self,
        indices: Sequence[int | Integer],
        linear_combinations: Iterable[FormalSum],
    ) -> int | None: ...
    def _init_product(self) -> None: ...
    def _init_symmetric(self) -> None: ...
    def _init_antisymmetric(self) -> None: ...
    def index_map(
        self,
        *indices: int | Integer | Sequence[int | Integer],
    ) -> int | None: ...
    def preimage(self) -> KeysView[TensorMultiIndex]: ...
    def codomain(self) -> ValuesView[int | None]: ...
