from collections.abc import Iterable, Iterator, Sequence
from typing import Generic, TypeVar

from sage.matrix.matrix import Matrix
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.free_module import FreeModule_generic, FreeModule_submodule
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


def FGP_Module(
    V: FreeModule_generic[_Scalar],
    W: FreeModule_submodule[_Scalar] | None = ...,
    check: bool = ...,
) -> FGP_Module_class[_Scalar]: ...


class FGP_Module_class(
    Parent[FGP_Element[_Scalar]],
    Generic[_Scalar],
):
    Element: type[FGP_Element[_Scalar]]
    def __init__(
        self,
        V: FreeModule_generic[_Scalar],
        W: FreeModule_submodule[_Scalar],
        check: bool = ...,
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def V(self) -> FreeModule_generic[_Scalar]: ...
    cover = V
    def W(self) -> FreeModule_submodule[_Scalar]: ...
    relations = W
    def ngens(self) -> int: ...
    def gen(self, i: int | Integer) -> FGP_Element[_Scalar]: ...
    def gens(self) -> tuple[FGP_Element[_Scalar], ...]: ...
    def basis(self) -> AbstractFamily: ...
    def zero(self) -> FGP_Element[_Scalar]: ...
    def an_element(self) -> FGP_Element[_Scalar]: ...
    def random_element(self, *args: object, **kwds: object) -> FGP_Element[_Scalar]: ...
    def __iter__(self) -> Iterator[FGP_Element[_Scalar]]: ...
    def _element_constructor_(
        self,
        x: FGP_Element[_Scalar]
        | FreeModuleElement[_Scalar]
        | Iterable[ElementConstructorInput],
    ) -> FGP_Element[_Scalar]: ...
    def invariants(self, include_ones: bool = ...) -> tuple[Integer, ...]: ...
    elementary_divisors = invariants
    def smith_form_gens(self) -> tuple[FGP_Element[_Scalar], ...]: ...
    def smith_form(self) -> Matrix[_Scalar]: ...
    def rank(self) -> int: ...
    def is_finite(self) -> bool: ...
    def cardinality(self) -> Integer | PlusInfinity: ...
    order = cardinality
    def exponent(self) -> Integer | PlusInfinity: ...
    def quotient(
        self,
        submodule: FGP_Module_class[_Scalar]
        | Sequence[FGP_Element[_Scalar]],
    ) -> FGP_Module_class[_Scalar]: ...
    def submodule(
        self,
        generators: Iterable[FGP_Element[_Scalar]],
    ) -> FGP_Module_class[_Scalar]: ...
    def hom(
        self,
        images: Matrix[_Scalar]
        | Sequence[FGP_Element[_Scalar]],
        codomain: FGP_Module_class[_Scalar] | None = ...,
    ) -> FGP_Morphism[_Scalar]: ...
    def Hom(
        self,
        codomain: FGP_Module_class[_Scalar],
    ) -> FGP_Homset[_Scalar]: ...


from sage.modules.fg_pid.fgp_morphism import FGP_Homset, FGP_Morphism
