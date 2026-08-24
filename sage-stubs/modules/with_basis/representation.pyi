from collections.abc import Callable, Hashable, Iterable, Sequence
from typing import Generic, Literal, Self, TypeVar

from sage.algebras.clifford_algebra_element import ExteriorAlgebraElement
from sage.categories.category import Category
from sage.combinat.free_module import (
    CombinatorialFreeModule,
    CombinatorialFreeModule_Tensor,
)
from sage.combinat.integer_vector import IntegerVector
from sage.combinat.partition import Partition
from sage.data_structures.bitset import FrozenBitset
from sage.groups.class_function import ClassFunction
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.subquotient import (
    QuotientModuleWithBasis,
    SubmoduleWithBasis,
)
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import Element, RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.typeset.ascii_art import AsciiArt
from sage.typeset.unicode_art import UnicodeArt

_Actor = TypeVar("_Actor", bound=Element, default=Element)
_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type RepresentationSide = Literal["left", "right", "twosided"]
type ActionSide = Literal["left", "right"]
type RepresentationElement[_Index: Hashable, _Scalar: RingElement] = IndexedFreeModuleElement[_Index, _Scalar]
type CharacterInput[_Actor: Element, _Scalar: RingElement] = (
    Sequence[_Scalar]
    | Callable[[_Actor], RingElement]
)
type RepresentationAction[_Actor: Element, _Index: Hashable, _Scalar: RingElement] = Callable[
    [_Actor, _Index],
    RepresentationElement[_Index, _Scalar],
]
type SchurShape = Partition | Sequence[int | Integer]


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
        g: _Actor | CombinatorialFreeModule.Element,
        side: ActionSide | None = ...,
        sparse: bool = ...,
    ) -> Matrix[_Scalar]: ...
    def character(self) -> ClassFunction | FreeModuleElement[RingElement]: ...
    def brauer_character(self) -> FreeModuleElement[RingElement]: ...
    def exterior_power(
        self,
        degree: int | Integer | None = ...,
    ) -> Representation_Exterior[_Actor, _Index, _Scalar] | Representation_ExteriorAlgebra[_Actor, _Index, _Scalar]: ...
    def symmetric_power(
        self,
        degree: int | Integer | None = ...,
    ) -> Representation_Symmetric[_Actor, _Index, _Scalar]: ...
    def schur_functor(
        self,
        la: SchurShape,
    ) -> SchurFunctorRepresentation[_Actor, Hashable, _Scalar]: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[_Index, _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[_Index, _Scalar]: ...
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
    def _composition_series_data(
        self,
    ) -> tuple[
        tuple[Representation_abstract[_Actor, Hashable, _Scalar], ...],
        tuple[Representation_abstract[_Actor, Hashable, _Scalar], ...],
    ]: ...
    def composition_series(
        self,
    ) -> tuple[Representation_abstract[_Actor, Hashable, _Scalar], ...]: ...
    def composition_factors(
        self,
    ) -> tuple[Representation_abstract[_Actor, Hashable, _Scalar], ...]: ...

    class Element(CombinatorialFreeModule.Element):
        def _acted_upon_(
            self,
            scalar: ElementConstructorInput,
            self_on_left: bool = ...,
        ) -> Self | None: ...


class Representation(
    Representation_abstract[_Actor, _Index, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        semigroup: Parent[_Actor],
        module: CombinatorialFreeModule,
        on_basis: RepresentationAction[_Actor, _Index, _Scalar] | None,
        side: ActionSide = ...,
        **kwargs: object,
    ) -> None: ...
    def _test_representation(self, **options: object) -> None: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, b: _Index) -> str: ...
    def _latex_term(self, b: _Index) -> str: ...
    def _element_constructor_(
        self,
        x: ElementConstructorInput | RepresentationElement[_Index, _Scalar],
    ) -> RepresentationElement[_Index, _Scalar]: ...
    def product_by_coercion(
        self,
        left: RepresentationElement[_Index, _Scalar],
        right: RepresentationElement[_Index, _Scalar],
    ) -> RepresentationElement[_Index, _Scalar]: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[_Index, _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[_Index, _Scalar]: ...


class Subrepresentation(
    Representation_abstract[_Actor, _Index, _Scalar],
    SubmoduleWithBasis[_Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        basis: AbstractFamily,
        support_order: tuple[Hashable, ...],
        ambient: Representation_abstract[_Actor, Hashable, _Scalar],
        *args: object,
        **opts: object,
    ) -> None: ...
    def _repr_(self) -> str: ...

    class Element(Representation_abstract.Element):
        def _acted_upon_(
            self,
            scalar: ElementConstructorInput,
            self_on_left: bool = ...,
        ) -> Self | None: ...


class QuotientRepresentation(
    Representation_abstract[_Actor, _Index, _Scalar],
    QuotientModuleWithBasis[_Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(self, *args: object, **kwds: object) -> None: ...
    def _repr_(self) -> str: ...
    class Element(Subrepresentation.Element): ...


class Representation_Tensor(
    Representation_abstract[_Actor, tuple[Hashable, ...], _Scalar],
    CombinatorialFreeModule_Tensor,
    Generic[_Actor, _Scalar],
):
    def __init__(
        self,
        reps: tuple[Representation_abstract[_Actor, Hashable, _Scalar], ...],
        **options: object,
    ) -> None: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[tuple[Hashable, ...], _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[tuple[Hashable, ...], _Scalar]: ...

    class Element(Representation_abstract.Element): ...


class Representation_Exterior(
    Representation_abstract[_Actor, FrozenBitset, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        rep: Representation_abstract[_Actor, _Index, _Scalar],
        degree: int | Integer | None = ...,
        category: Category | None = ...,
        **options: object,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _repr_term(self, m: FrozenBitset) -> str: ...
    def _ascii_art_term(self, m: FrozenBitset) -> AsciiArt: ...
    def _unicode_art_term(self, m: FrozenBitset) -> UnicodeArt: ...
    def _latex_term(self, m: FrozenBitset) -> str: ...
    def _from_repr_to_ext(
        self,
        elt: RepresentationElement[_Index, _Scalar],
    ) -> ExteriorAlgebraElement: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[FrozenBitset, _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[FrozenBitset, _Scalar]: ...
    def _action_on_basis(
        self,
        g: _Actor,
        b: FrozenBitset,
        vec_on_left: bool,
    ) -> RepresentationElement[FrozenBitset, _Scalar]: ...


class Representation_ExteriorAlgebra(
    Representation_Exterior[_Actor, _Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        rep: Representation_abstract[_Actor, _Index, _Scalar],
        degree: int | Integer | None = ...,
        category: Category | None = ...,
        **options: object,
    ) -> None: ...
    def one_basis(self) -> FrozenBitset: ...
    def product_on_basis(
        self,
        x: FrozenBitset,
        y: FrozenBitset,
    ) -> RepresentationElement[FrozenBitset, _Scalar]: ...


class Representation_Symmetric(
    Representation_abstract[_Actor, IntegerVector, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        rep: Representation_abstract[_Actor, _Index, _Scalar],
        degree: int | Integer,
        **options: object,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _repr_term(self, m: IntegerVector) -> str: ...
    def _ascii_art_term(self, m: IntegerVector) -> AsciiArt: ...
    def _unicode_art_term(self, m: IntegerVector) -> UnicodeArt: ...
    def _latex_term(self, m: IntegerVector) -> str: ...
    def _from_repr_to_sym(
        self,
        elt: RepresentationElement[_Index, _Scalar],
    ) -> RingElement: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[IntegerVector, _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[IntegerVector, _Scalar]: ...
    def _action_on_basis(
        self,
        g: _Actor,
        b: IntegerVector,
        vec_on_left: bool,
    ) -> RepresentationElement[IntegerVector, _Scalar]: ...


class RegularRepresentation(
    Representation[_Actor, _Actor, _Scalar],
    Generic[_Actor, _Scalar],
):
    def __init__(
        self,
        semigroup: Parent[_Actor],
        base_ring: Parent[_Scalar],
        side: ActionSide = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _left_on_basis(
        self,
        g: _Actor,
        m: _Actor,
    ) -> RepresentationElement[_Actor, _Scalar]: ...
    def _right_on_basis(
        self,
        g: _Actor,
        m: _Actor,
    ) -> RepresentationElement[_Actor, _Scalar]: ...


class TrivialRepresentation(
    Representation_abstract[_Actor, str, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Scalar],
):
    def __init__(
        self,
        semigroup: Parent[_Actor],
        base_ring: Parent[_Scalar],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[str, _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[str, _Scalar]: ...

    class Element(Representation_abstract.Element):
        def _acted_upon_(
            self,
            scalar: ElementConstructorInput,
            self_on_left: bool = ...,
        ) -> Self | None: ...


class SignRepresentation_abstract(
    Representation_abstract[_Actor, str, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Scalar],
):
    sign_function: Callable[[_Actor], int]

    def __init__(
        self,
        group: Parent[_Actor],
        base_ring: Parent[_Scalar],
        sign_function: Callable[[_Actor], int] | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[str, _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[str, _Scalar]: ...


class SignRepresentationPermgroup(
    SignRepresentation_abstract[_Actor, _Scalar],
    Generic[_Actor, _Scalar],
):
    def _default_sign(self, elem: _Actor) -> int: ...


class SignRepresentationMatrixGroup(
    SignRepresentation_abstract[_Actor, _Scalar],
    Generic[_Actor, _Scalar],
):
    def _default_sign(self, elem: _Actor) -> int: ...


class SignRepresentationCoxeterGroup(
    SignRepresentation_abstract[_Actor, _Scalar],
    Generic[_Actor, _Scalar],
):
    def _default_sign(self, elem: _Actor) -> int: ...


class ReflectionRepresentation(
    Representation_abstract[_Actor, int, _Scalar],
    CombinatorialFreeModule,
    Generic[_Actor, _Scalar],
):
    @staticmethod
    def __classcall_private__(
        class_: type[ReflectionRepresentation[_Actor, _Scalar]],
        W: Parent[_Actor],
        base_ring: Parent[_Scalar] | None = ...,
    ) -> ReflectionRepresentation[_Actor, _Scalar]: ...
    def __init__(
        self,
        W: Parent[_Actor],
        base_ring: Parent[_Scalar],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[int, _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[int, _Scalar]: ...


class NaturalMatrixRepresentation(
    Representation[_Actor, int, _Scalar],
    Generic[_Actor, _Scalar],
):
    @staticmethod
    def __classcall_private__(
        class_: type[NaturalMatrixRepresentation[_Actor, _Scalar]],
        semigroup: Parent[_Actor],
        base_ring: Parent[_Scalar] | None = ...,
    ) -> NaturalMatrixRepresentation[_Actor, _Scalar]: ...
    def __init__(
        self,
        semigroup: Parent[_Actor],
        base_ring: Parent[_Scalar],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _semigroup_action(
        self,
        g: _Actor,
        vec: RepresentationElement[int, _Scalar],
        vec_on_left: bool,
    ) -> RepresentationElement[int, _Scalar]: ...


class SchurFunctorRepresentation(
    Subrepresentation[_Actor, _Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    @staticmethod
    def __classcall_private__(
        class_: type[SchurFunctorRepresentation[_Actor, _Index, _Scalar]],
        V: Representation_abstract[_Actor, _Index, _Scalar],
        shape: SchurShape,
    ) -> SchurFunctorRepresentation[_Actor, _Index, _Scalar]: ...
    def __init__(
        self,
        V: Representation_abstract[_Actor, _Index, _Scalar],
        shape: Partition,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...


from sage.modules.with_basis.invariant import (
    FiniteDimensionalInvariantModule,
    FiniteDimensionalTwistedInvariantModule,
)
