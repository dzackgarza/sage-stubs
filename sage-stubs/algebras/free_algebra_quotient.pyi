from collections.abc import Mapping
from typing import Generic, Protocol, Self, TypeVar

from sage.algebras.free_algebra import FreeAlgebra_generic
from sage.algebras.free_algebra_element import FreeAlgebraElement
from sage.algebras.free_algebra_quotient_element import FreeAlgebraQuotientElement
from sage.algebras.letterplace.free_algebra_letterplace import (
    FreeAlgebra_letterplace,
)
from sage.categories.rings import Rings
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.monoids.free_monoid import FreeMonoid
from sage.monoids.free_monoid_element import FreeMonoidElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_AmbientAlgebra = TypeVar("_AmbientAlgebra", covariant=True)
_AmbientParent = TypeVar("_AmbientParent", covariant=True)
_AmbientElement = TypeVar("_AmbientElement", covariant=True)

type FreeAlgebraQuotientSource[_Coefficient: RingElement] = (
    FreeAlgebra_generic[_Coefficient] | FreeAlgebra_letterplace[_Coefficient]
)

class AmbientQuotientParent(Protocol[_AmbientAlgebra]):
    def ambient_algebra(self) -> _AmbientAlgebra: ...

class AmbientQuotientAlgebraElement(Protocol[_AmbientParent, _AmbientElement]):
    def parent(self) -> _AmbientParent: ...
    def ambient_algebra_element(self) -> _AmbientElement: ...

type FreeAlgebraQuotientElementInput[_InputCoefficient: RingElement] = (
    FreeAlgebraQuotientElement[_InputCoefficient]
    | FreeAlgebraElement[_InputCoefficient]
    | FreeMonoidElement
    | FreeModuleElement[_InputCoefficient]
    | _InputCoefficient
    | int
    | Integer
    | list[_InputCoefficient | int | Integer]
    | Mapping[FreeMonoidElement, _InputCoefficient | int | Integer]
    | AmbientQuotientAlgebraElement[
        AmbientQuotientParent[FreeAlgebraQuotient[_InputCoefficient]],
        FreeAlgebraQuotientElement[_InputCoefficient],
    ]
)

class FreeAlgebraQuotient(
    UniqueRepresentation,
    Parent[FreeAlgebraQuotientElement[_Coefficient]],
    Generic[_Coefficient],
):
    @classmethod
    def __classcall__(
        cls: type[Self],
        *args: ElementConstructorInput,
        **kwds: ElementConstructorInput,
    ) -> Self: ...
    def __init__(
        self,
        A: FreeAlgebraQuotientSource[_Coefficient],
        mons: tuple[FreeMonoidElement, ...],
        mats: tuple[Matrix[_Coefficient], ...],
        names: tuple[str, ...],
    ) -> None: ...
    def _element_constructor_(
        self,
        x: FreeAlgebraQuotientElementInput[_Coefficient],
    ) -> FreeAlgebraQuotientElement[_Coefficient]: ...
    def _coerce_map_from_(self, S: Parent | type) -> bool: ...
    def _repr_(self) -> str: ...
    def gen(
        self,
        i: int | Integer,
    ) -> FreeAlgebraQuotientElement[_Coefficient]: ...
    def gens(self) -> tuple[FreeAlgebraQuotientElement[_Coefficient], ...]: ...
    def ngens(self) -> int: ...
    def dimension(self) -> int: ...
    def matrix_action(self) -> tuple[Matrix[_Coefficient], ...]: ...
    def monomial_basis(self) -> tuple[FreeMonoidElement, ...]: ...
    def rank(self) -> int: ...
    def module(self) -> FreeModule_generic[_Coefficient]: ...
    def monoid(self) -> FreeMonoid: ...
    def free_algebra(self) -> FreeAlgebraQuotientSource[_Coefficient]: ...

def hamilton_quatalg[HamiltonCoefficient: RingElement](
    R: Rings.ParentMethods[HamiltonCoefficient],
) -> tuple[
    FreeAlgebraQuotient[HamiltonCoefficient],
    tuple[FreeAlgebraQuotientElement[HamiltonCoefficient], ...],
]: ...
