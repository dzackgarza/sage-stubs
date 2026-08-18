from collections.abc import Callable, Iterable, Sequence
from typing import TypeVar

from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_generic, FreeModule_submodule
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


def span(
    vectors: Iterable[FreeModuleElement[_Scalar] | Sequence[ElementConstructorInput]],
    base_ring: Parent[_Scalar] | None = ...,
    check: bool = ...,
) -> FreeModule_submodule[_Scalar]: ...


def coordinate_vector(
    vector: FreeModuleElement[_Scalar],
    basis: Sequence[FreeModuleElement[_Scalar]],
) -> FreeModuleElement[_Scalar]: ...


def linear_combination(
    coefficients: Iterable[_Scalar],
    vectors: Iterable[FreeModuleElement[_Scalar]],
) -> FreeModuleElement[_Scalar]: ...


def gram_matrix(
    vectors: Sequence[FreeModuleElement[_Scalar]],
    inner_product: Callable[
        [FreeModuleElement[_Scalar], FreeModuleElement[_Scalar]],
        _Scalar,
    ] | None = ...,
) -> Matrix[_Scalar]: ...


def gram_schmidt(
    vectors: Sequence[FreeModuleElement[_Scalar]],
    orthonormal: bool = ...,
) -> tuple[list[FreeModuleElement[_Scalar]], Matrix[_Scalar]]: ...
