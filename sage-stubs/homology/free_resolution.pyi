from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.categories.morphism import Morphism
from sage.homology.chain_complex import ChainComplex_class
from sage.matrix.matrix import Matrix
from sage.misc.classcall_metaclass import ClasscallMetaclass
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type ResolutionModule[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | FreeModule_generic[_Scalar]
    | Ideal_generic
)
type ResolutionDifferential[_Scalar: RingElement] = (
    FreeModuleMorphism[_Scalar, _Scalar]
    | Morphism[FreeModuleElement[_Scalar], Element]
)
type ResolutionDegree = (
    int
    | Integer
    | FreeModuleElement[Integer]
    | tuple[int | Integer, ...]
)
type ResolutionDegrees = Sequence[ResolutionDegree]


class FreeResolution(
    SageObject,
    Generic[_Scalar],
    metaclass=ClasscallMetaclass,
):
    @staticmethod
    def __classcall_private__(
        cls: type[FreeResolution[_Scalar]],
        module: ResolutionModule[_Scalar],
        *args: Element | int | str | bool,
        graded: bool = ...,
        degrees: ResolutionDegrees | None = ...,
        shifts: ResolutionDegrees | None = ...,
        **kwds: Element | int | str | bool | None,
    ) -> FreeResolution[_Scalar]: ...
    def __init__(
        self,
        module: ResolutionModule[_Scalar],
        name: str = ...,
        **kwds: Element | int | str | bool | None,
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _repr_module(self, i: int | Integer) -> str: ...
    def differential(
        self,
        i: int | Integer,
    ) -> ResolutionDifferential[_Scalar]: ...
    def target(self) -> Parent[Element]: ...


class FiniteFreeResolution(
    FreeResolution[_Scalar],
    Generic[_Scalar],
):
    def __len__(self) -> int: ...
    def __getitem__(
        self,
        i: int | Integer,
    ) -> FreeModule_generic[_Scalar]: ...
    def differential(
        self,
        i: int | Integer,
    ) -> ResolutionDifferential[_Scalar]: ...
    def matrix(self, i: int | Integer) -> Matrix[_Scalar]: ...
    def chain_complex(self) -> ChainComplex_class[Integer, _Scalar]: ...
    def _m(self) -> Matrix[_Scalar] | Ideal_generic: ...


class FiniteFreeResolution_free_module(
    FiniteFreeResolution[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        module: ResolutionModule[_Scalar],
        *args: Element | int | str | bool,
        **kwds: Element | int | str | bool | None,
    ) -> None: ...


class FiniteFreeResolution_singular(
    FiniteFreeResolution[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        module: ResolutionModule[_Scalar],
        name: str = ...,
        algorithm: str = ...,
        **kwds: Element | int | str | bool | None,
    ) -> None: ...
