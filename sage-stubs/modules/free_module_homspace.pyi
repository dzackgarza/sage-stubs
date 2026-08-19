from collections.abc import Callable, Sequence
from typing import Generic, Literal, TypeVar

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.matrix.matrix0 import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

_DomainScalar = TypeVar(
    "_DomainScalar",
    bound=RingElement,
    default=RingElement,
)
_CodomainScalar = TypeVar(
    "_CodomainScalar",
    bound=RingElement,
    default=RingElement,
)

type MatrixSide = Literal["left", "right"]
type FreeModuleMorphismRule[
    _DomainScalar: RingElement,
    _CodomainScalar: RingElement,
] = (
    Matrix[_CodomainScalar]
    | Sequence[
        FreeModuleElement[_CodomainScalar]
        | Sequence[ElementConstructorInput]
    ]
    | Callable[
        [FreeModuleElement[_DomainScalar]],
        FreeModuleElement[_CodomainScalar]
        | Sequence[ElementConstructorInput],
    ]
)

class FreeModuleHomspace(
    Homset[
        FreeModuleMorphism[_DomainScalar, _CodomainScalar],
        FreeModuleElement[_DomainScalar],
        FreeModuleElement[_CodomainScalar],
    ],
    Generic[_DomainScalar, _CodomainScalar],
):
    element_class: type[
        FreeModuleMorphism[_DomainScalar, _CodomainScalar]
    ]

    def __init__(
        self,
        domain: FreeModule_generic[_DomainScalar],
        codomain: FreeModule_generic[_CodomainScalar],
        category: Category | None = ...,
    ) -> None: ...
    def domain(self) -> FreeModule_generic[_DomainScalar]: ...
    def codomain(self) -> FreeModule_generic[_CodomainScalar]: ...
    def __call__(
        self,
        A: FreeModuleMorphism[
            _DomainScalar,
            _CodomainScalar,
        ] | FreeModuleMorphismRule[
            _DomainScalar,
            _CodomainScalar,
        ],
        **kwds: object,
    ) -> FreeModuleMorphism[_DomainScalar, _CodomainScalar]: ...
    def zero(
        self,
        side: MatrixSide = ...,
    ) -> FreeModuleMorphism[_DomainScalar, _CodomainScalar]: ...
    def _matrix_space(
        self,
        side: MatrixSide = ...,
    ) -> MatrixSpace[_CodomainScalar]: ...
    def basis(
        self,
        side: MatrixSide = ...,
    ) -> tuple[
        FreeModuleMorphism[_DomainScalar, _CodomainScalar],
        ...,
    ]: ...
    def identity(
        self,
        side: MatrixSide = ...,
    ) -> FreeModuleMorphism[_DomainScalar, _CodomainScalar]: ...
    one = identity
    def natural_map(
        self,
    ) -> FreeModuleMorphism[_DomainScalar, _CodomainScalar]: ...
