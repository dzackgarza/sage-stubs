from collections.abc import Callable, Hashable, Iterable, Sequence
from typing import Generic, Literal, TypeVar

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.subquotient import (
    QuotientModuleWithBasis,
    SubmoduleWithBasis,
)
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent

_Actor = TypeVar("_Actor", bound=Element, default=Element)
_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_OtherIndex = TypeVar("_OtherIndex", bound=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type RepresentationSide = Literal["left", "right", "twosided"]
type ActionSide = Literal["left", "right"]
type RepresentationElement[_Index: Hashable, _Scalar: RingElement] = IndexedFreeModuleElement[_Index, _Scalar]
type CharacterInput[_Actor: Element, _Scalar: RingElement] = (
    Sequence[_Scalar]
    | Callable[[_Actor], RingElement]
)

class Representation_abstract(Generic[_Actor, _Index, _Scalar]):
    def __init__(
        self,
        semigroup: Parent[_Actor],
        side: RepresentationSide,
        algebra: CombinatorialFreeModule | None = ...,
    ) -> None: ...
    def semigroup(self) -> Parent[_Actor]: ...
    def semigroup_algebra(self) -> CombinatorialFreeModule: ...
    def side(self) -> RepresentationSide: ...
    def invariant_module(
        self,
        S: Parent[_Actor] | None = ...,
        **kwargs: object,
    ) -> FiniteDimensionalInvariantModule[_Actor, _Index, _Scalar]: ...
    def twisted_invariant_module(
        self,
        chi: CharacterInput[_Actor, _Scalar] | Parent[_Actor],
        G: Parent[_Actor] | CharacterInput[_Actor, _Scalar] | None = ...,
        **kwargs: object,
    ) -> FiniteDimensionalInvariantModule[_Actor, _Index, _Scalar] | FiniteDimensionalTwistedInvariantModule[_Actor, _Index, _Scalar]: ...
    def representation_matrix(
        self,
        g: _Actor | IndexedFreeModuleElement[Hashable, _Scalar],
        side: ActionSide | None = ...,
        sparse: bool = ...,
    ) -> Matrix[_Scalar]: ...
    def character(self) -> FreeModuleElement[RingElement]: ...
    def brauer_character(self) -> FreeModuleElement[RingElement]: ...
    def exterior_power(
        self,
        degree: int | None = ...,
    ) -> Representation_Exterior[_Actor, _Index, _Scalar] | Representation_ExteriorAlgebra[_Actor, _Index, _Scalar]: ...
    def symmetric_power(
        self,
        degree: int,
    ) -> Representation_Symmetric[_Actor, _Index, _Scalar]: ...
    def schur_functor(
        self,
        shape: Sequence[int],
    ) -> SchurFunctorRepresentation[_Actor, Hashable, _Scalar]: ...
    def is_irreducible(self) -> bool: ...
    def find_subrepresentation(
        self,
    ) -> Subrepresentation[_Actor, Hashable, _Scalar] | None: ...
    def subrepresentation(
        self,
        gens: Iterable[RepresentationElement[_Index, _Scalar]],
        check: bool = ...,
        already_echelonized: bool = ...,
        *args: object,
        is_closed: bool = ...,
        **opts: object,
    ) -> Subrepresentation[_Actor, Hashable, _Scalar]: ...
    def quotient_representation(
        self,
        subrepr: Subrepresentation[_Actor, Hashable, _Scalar]
        | Iterable[RepresentationElement[_Index, _Scalar]],
        already_echelonized: bool = ...,
        **kwds: object,
    ) -> QuotientRepresentation[_Actor, Hashable, _Scalar]: ...
    def composition_series(
        self,
    ) -> list[Subrepresentation[_Actor, Hashable, _Scalar]]: ...
    def composition_factors(
        self,
    ) -> list[QuotientRepresentation[_Actor, Hashable, _Scalar]]: ...
    def tensor_product(
        self,
        other: Representation_abstract[_Actor, _OtherIndex, _Scalar],
    ) -> Representation_Tensor[
        _Actor,
        tuple[_Index, _OtherIndex],
        _Scalar,
    ]: ...

class Representation(
    Representation_abstract[_Actor, _Index, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        semigroup: Parent[_Actor],
        module: CombinatorialFreeModule,
        on_basis: Callable[
            [_Actor, _Index],
            RepresentationElement[_Index, _Scalar],
        ] | None,
        side: ActionSide = ...,
        **kwargs: object,
    ) -> None: ...
    def _element_constructor_(
        self,
        x: RepresentationElement[_Index, _Scalar],
    ) -> RepresentationElement[_Index, _Scalar]: ...
    def product_by_coercion(
        self,
        left: RepresentationElement[_Index, _Scalar],
        right: RepresentationElement[_Index, _Scalar],
    ) -> RepresentationElement[_Index, _Scalar]: ...

class Subrepresentation(
    Representation_abstract[_Actor, _Index, _Scalar],
    SubmoduleWithBasis[_Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
): ...

class QuotientRepresentation(
    Representation_abstract[_Actor, _Index, _Scalar],
    QuotientModuleWithBasis[_Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
): ...

class Representation_Tensor(
    Representation_abstract[_Actor, _Index, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        reps: Sequence[Representation_abstract[_Actor, Hashable, _Scalar]],
        **options: object,
    ) -> None: ...

class Representation_Exterior(
    Representation_abstract[_Actor, tuple[_Index, ...], _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        rep: Representation_abstract[_Actor, _Index, _Scalar],
        degree: int | None = ...,
        category: Category | None = ...,
        **options: object,
    ) -> None: ...
    def degree(self) -> int | None: ...
    def characteristic_polynomial(
        self,
        g: _Actor,
        var: str = ...,
    ) -> Polynomial: ...

class Representation_ExteriorAlgebra(
    Representation_Exterior[_Actor, _Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
): ...

class Representation_Symmetric(
    Representation_abstract[_Actor, tuple[int, ...], _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        rep: Representation_abstract[_Actor, _Index, _Scalar],
        degree: int,
        **options: object,
    ) -> None: ...
    def degree(self) -> int: ...

class RegularRepresentation(
    Representation[_Actor, _Actor, _Scalar],
    Generic[_Actor, _Scalar],
): ...

class TrivialRepresentation(
    Representation_abstract[_Actor, str, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Scalar],
): ...

class SignRepresentation_abstract(
    Representation_abstract[_Actor, str, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Scalar],
):
    def sign_function(self, elem: _Actor) -> int: ...

class SignRepresentationPermgroup(
    SignRepresentation_abstract[_Actor, _Scalar],
    Generic[_Actor, _Scalar],
): ...

class SignRepresentationMatrixGroup(
    SignRepresentation_abstract[_Actor, _Scalar],
    Generic[_Actor, _Scalar],
): ...

class SignRepresentationCoxeterGroup(
    SignRepresentation_abstract[_Actor, _Scalar],
    Generic[_Actor, _Scalar],
): ...

class ReflectionRepresentation(
    Representation_abstract[_Actor, int, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Scalar],
): ...

class NaturalMatrixRepresentation(
    Representation[_Actor, int, _Scalar],
    Generic[_Actor, _Scalar],
): ...

class SchurFunctorRepresentation(
    Subrepresentation[_Actor, _Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        V: Representation_abstract[_Actor, Hashable, _Scalar],
        shape: Sequence[int],
    ) -> None: ...

from sage.modules.with_basis.invariant import (
    FiniteDimensionalInvariantModule,
    FiniteDimensionalTwistedInvariantModule,
)
