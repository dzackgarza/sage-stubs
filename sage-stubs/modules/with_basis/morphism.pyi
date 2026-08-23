from collections.abc import Callable, Hashable
from types import NotImplementedType
from typing import Generic, Literal, TypeVar, overload

from sage.categories.category import Category
from sage.categories.morphism import Morphism, SetMorphism
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

_DomainIndex = TypeVar("_DomainIndex", bound=Hashable, default=Hashable)
_CodomainIndex = TypeVar("_CodomainIndex", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_Value = TypeVar("_Value", bound=RingElement, default=RingElement)

type ModuleSide = Literal["left", "right"]
type TriangularDirection = Literal["upper", "lower"]
type DomainElement[_DomainIndex: Hashable, _Scalar: RingElement] = IndexedFreeModuleElement[_DomainIndex, _Scalar]
type CodomainElement[_CodomainIndex: Hashable, _Scalar: RingElement] = IndexedFreeModuleElement[_CodomainIndex, _Scalar]

class ModuleMorphism(
    Morphism[
        DomainElement[_DomainIndex, _Scalar],
        CodomainElement[_CodomainIndex, _Scalar],
    ],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        domain: CombinatorialFreeModule,
        codomain: Parent[CodomainElement[_CodomainIndex, _Scalar]] | None = ...,
        category: Category | None = ...,
        affine: bool = ...,
    ) -> None: ...

class ModuleMorphismFromFunction(
    ModuleMorphism[_DomainIndex, _CodomainIndex, _Scalar],
    SetMorphism[
        DomainElement[_DomainIndex, _Scalar],
        CodomainElement[_CodomainIndex, _Scalar],
    ],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        domain: CombinatorialFreeModule,
        function: Callable[
            [DomainElement[_DomainIndex, _Scalar]],
            CodomainElement[_CodomainIndex, _Scalar],
        ],
        codomain: Parent[CodomainElement[_CodomainIndex, _Scalar]] | None = ...,
        category: Category | None = ...,
    ) -> None: ...

class ModuleMorphismByLinearity(
    ModuleMorphism[_DomainIndex, _CodomainIndex, _Scalar],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        domain: CombinatorialFreeModule,
        on_basis: Callable[..., CodomainElement[_CodomainIndex, _Scalar]] | None = ...,
        codomain: Parent[CodomainElement[_CodomainIndex, _Scalar]] | None = ...,
        category: Category | None = ...,
        position: int = ...,
        zero: CodomainElement[_CodomainIndex, _Scalar] | None = ...,
    ) -> None: ...
    def _richcmp_(
        self,
        other: object,
        op: int,
    ) -> bool | NotImplementedType: ...
    def on_basis(
        self,
    ) -> Callable[..., CodomainElement[_CodomainIndex, _Scalar]]: ...
    def __call__(
        self,
        *args: object,
    ) -> CodomainElement[_CodomainIndex, _Scalar]: ...
    _call_ = __call__

class TriangularModuleMorphism(
    ModuleMorphism[_DomainIndex, _CodomainIndex, _Scalar],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        triangular: TriangularDirection = ...,
        unitriangular: bool = ...,
        key: Callable[[_CodomainIndex], object] | None = ...,
        inverse: ModuleMorphism[_CodomainIndex, _DomainIndex, _Scalar] | None = ...,
        inverse_on_support: Callable[[_CodomainIndex], _DomainIndex | None]
        | Literal["compute"] = ...,
        invertible: bool | None = ...,
    ) -> None: ...
    def _richcmp_(
        self,
        other: object,
        op: int,
    ) -> bool | NotImplementedType: ...
    def _test_triangular(self, **options: object) -> None: ...
    def __invert__(
        self,
    ) -> ModuleMorphism[_CodomainIndex, _DomainIndex, _Scalar]: ...
    def section(
        self,
    ) -> ModuleMorphism[_CodomainIndex, _DomainIndex, _Scalar] | SetMorphism[
        CodomainElement[_CodomainIndex, _Scalar],
        DomainElement[_DomainIndex, _Scalar],
    ]: ...
    def _invert_on_basis(
        self,
        i: _CodomainIndex,
    ) -> DomainElement[_DomainIndex, _Scalar]: ...
    def preimage(
        self,
        f: CodomainElement[_CodomainIndex, _Scalar],
    ) -> DomainElement[_DomainIndex, _Scalar]: ...
    def coreduced(
        self,
        y: CodomainElement[_CodomainIndex, _Scalar],
    ) -> CodomainElement[_CodomainIndex, _Scalar]: ...
    def cokernel_basis_indices(self) -> list[_CodomainIndex]: ...
    def cokernel_projection(
        self,
        category: Category | None = ...,
    ) -> ModuleMorphism[_CodomainIndex, _CodomainIndex, _Scalar]: ...

class TriangularModuleMorphismByLinearity(
    ModuleMorphismByLinearity[_DomainIndex, _CodomainIndex, _Scalar],
    TriangularModuleMorphism[_DomainIndex, _CodomainIndex, _Scalar],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        domain: CombinatorialFreeModule,
        on_basis: Callable[..., CodomainElement[_CodomainIndex, _Scalar]],
        codomain: CombinatorialFreeModule | None = ...,
        category: Category | None = ...,
        **keywords: object,
    ) -> None: ...
    def _richcmp_(
        self,
        other: object,
        op: int,
    ) -> bool | NotImplementedType: ...

class TriangularModuleMorphismFromFunction(
    ModuleMorphismFromFunction[_DomainIndex, _CodomainIndex, _Scalar],
    TriangularModuleMorphism[_DomainIndex, _CodomainIndex, _Scalar],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        domain: CombinatorialFreeModule,
        function: Callable[
            [DomainElement[_DomainIndex, _Scalar]],
            CodomainElement[_CodomainIndex, _Scalar],
        ],
        codomain: CombinatorialFreeModule | None = ...,
        category: Category | None = ...,
        **keywords: object,
    ) -> None: ...

class ModuleMorphismFromMatrix(
    ModuleMorphismByLinearity[_DomainIndex, _CodomainIndex, _Scalar],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        domain: CombinatorialFreeModule,
        matrix: Matrix[_Scalar],
        codomain: CombinatorialFreeModule | None = ...,
        category: Category | None = ...,
        side: ModuleSide = ...,
    ) -> None: ...
    def _richcmp_(
        self,
        other: object,
        op: int,
    ) -> bool | NotImplementedType: ...

class DiagonalModuleMorphism(
    ModuleMorphismByLinearity[_DomainIndex, _DomainIndex, _Scalar],
    Generic[_DomainIndex, _Scalar],
):
    def __init__(
        self,
        domain: CombinatorialFreeModule,
        diagonal: Callable[[_DomainIndex], _Scalar],
        codomain: CombinatorialFreeModule | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def _richcmp_(
        self,
        other: object,
        op: int,
    ) -> bool | NotImplementedType: ...
    def _on_basis(
        self,
        i: _DomainIndex,
    ) -> CodomainElement[_DomainIndex, _Scalar]: ...
    def __invert__(
        self,
    ) -> ModuleMorphism[_DomainIndex, _DomainIndex, _Scalar]: ...

@overload
def pointwise_inverse_function(
    f: PointwiseInverseFunction[_Value],
) -> Callable[..., _Value]: ...
@overload
def pointwise_inverse_function(
    f: Callable[..., _Value],
) -> PointwiseInverseFunction[_Value]: ...

class PointwiseInverseFunction(SageObject, Generic[_Value]):
    def __init__(self, f: Callable[..., _Value]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __call__(self, *args: object) -> RingElement: ...
    def pointwise_inverse(self) -> Callable[..., _Value]: ...
