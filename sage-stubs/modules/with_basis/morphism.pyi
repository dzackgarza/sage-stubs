from collections.abc import Callable, Hashable
from typing import Generic, Literal, TypeVar

from sage.categories.category import Category
from sage.categories.morphism import Morphism, SetMorphism
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_DomainIndex = TypeVar("_DomainIndex", bound=Hashable, default=Hashable)
_CodomainIndex = TypeVar("_CodomainIndex", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

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
        on_basis: Callable[[_DomainIndex], CodomainElement[_CodomainIndex, _Scalar]] | None = ...,
        codomain: Parent[CodomainElement[_CodomainIndex, _Scalar]] | None = ...,
        category: Category | None = ...,
        position: int = ...,
        zero: CodomainElement[_CodomainIndex, _Scalar] | None = ...,
    ) -> None: ...
    def on_basis(
        self,
    ) -> Callable[[_DomainIndex], CodomainElement[_CodomainIndex, _Scalar]]: ...

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
    def matrix(self, side: ModuleSide | None = ...) -> Matrix[_Scalar]: ...

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
        inverse_on_support: Callable[[_CodomainIndex], _DomainIndex | None] | Literal["compute"] = ...,
        invertible: bool | None = ...,
    ) -> None: ...
    def preimage(
        self,
        x: CodomainElement[_CodomainIndex, _Scalar],
    ) -> DomainElement[_DomainIndex, _Scalar]: ...
    def section(
        self,
    ) -> ModuleMorphism[_CodomainIndex, _DomainIndex, _Scalar] | SetMorphism[
        CodomainElement[_CodomainIndex, _Scalar],
        DomainElement[_DomainIndex, _Scalar],
    ]: ...
    def __invert__(
        self,
    ) -> ModuleMorphism[_CodomainIndex, _DomainIndex, _Scalar]: ...
    def reduced(
        self,
        x: CodomainElement[_CodomainIndex, _Scalar],
    ) -> CodomainElement[_CodomainIndex, _Scalar]: ...
    def coreduced(
        self,
        x: CodomainElement[_CodomainIndex, _Scalar],
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
        on_basis: Callable[[_DomainIndex], CodomainElement[_CodomainIndex, _Scalar]],
        codomain: CombinatorialFreeModule | None = ...,
        category: Category | None = ...,
        **keywords: object,
    ) -> None: ...

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

class DiagonalModuleMorphism(
    TriangularModuleMorphismByLinearity[_DomainIndex, _DomainIndex, _Scalar],
    Generic[_DomainIndex, _Scalar],
):
    def __init__(
        self,
        domain: CombinatorialFreeModule,
        diagonal: Callable[[_DomainIndex], _Scalar],
        codomain: CombinatorialFreeModule | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def diagonal(self, index: _DomainIndex) -> _Scalar: ...

class PointwiseInverseFunction:
    def __init__(self, pointwise_inverse: Callable[..., RingElement]) -> None: ...
    def __call__(self, *args: object) -> RingElement: ...
    def pointwise_inverse(self) -> Callable[..., RingElement]: ...
