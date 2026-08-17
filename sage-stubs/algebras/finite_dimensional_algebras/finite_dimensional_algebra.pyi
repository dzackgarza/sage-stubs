from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Generic, Literal, Protocol, TypeVar

from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_element import (
    FiniteDimensionalAlgebraElement,
)
from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_ideal import (
    FiniteDimensionalAlgebraIdeal,
)
from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra_morphism import (
    FiniteDimensionalAlgebraHomset,
    FiniteDimensionalAlgebraMorphism,
)
from sage.categories.category import Category
from sage.categories.fields import Fields
from sage.categories.homset import Homset
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import FieldElement, Vector
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar(
    "_Scalar",
    bound=FieldElement,
    default=FieldElement,
)
_ExtendedScalar = TypeVar("_ExtendedScalar", bound=FieldElement)

type FiniteDimensionalAlgebraElementInput[_Scalar: FieldElement] = (
    FiniteDimensionalAlgebraElement[_Scalar]
    | _Scalar
    | int
    | Sequence[_Scalar | int]
    | Vector[_Scalar]
    | Matrix[_Scalar]
    | None
)
type FiniteDimensionalIdealGenerator[_Scalar: FieldElement] = (
    FiniteDimensionalAlgebraElement[_Scalar]
    | Vector[_Scalar]
    | Matrix[_Scalar]
)
type FiniteDimensionalIdealInput[_Scalar: FieldElement] = (
    FiniteDimensionalIdealGenerator[_Scalar]
    | Sequence[FiniteDimensionalIdealGenerator[_Scalar]]
    | None
)

class FiniteAlgebraBasis(Protocol[_Scalar]):
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[FiniteDimensionalAlgebraElement[_Scalar]]: ...
    def __getitem__(
        self,
        index: int,
    ) -> FiniteDimensionalAlgebraElement[_Scalar]: ...
    def keys(self) -> Iterable[int]: ...
    def values(
        self,
    ) -> Iterable[FiniteDimensionalAlgebraElement[_Scalar]]: ...

class FiniteDimensionalAlgebra(
    UniqueRepresentation,
    Parent[FiniteDimensionalAlgebraElement[_Scalar]],
    Generic[_Scalar],
):
    Element: type[FiniteDimensionalAlgebraElement[_Scalar]]
    element_class: type[FiniteDimensionalAlgebraElement[_Scalar]]

    @staticmethod
    def __classcall_private__(
        cls: type[FiniteDimensionalAlgebra[_Scalar]],
        k: Fields.ParentMethods[_Scalar],
        table: Sequence[Matrix[_Scalar]],
        names: str | Sequence[str] = "e",
        assume_associative: bool = False,
        assume_unital: bool = False,
        category: Category | None = None,
    ) -> FiniteDimensionalAlgebra[_Scalar]: ...
    def __init__(
        self,
        k: Fields.ParentMethods[_Scalar],
        table: Sequence[Matrix[_Scalar]],
        names: str | Sequence[str] = "e",
        category: Category | None = None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def base_ring(self) -> Fields.ParentMethods[_Scalar]: ...
    def _coerce_map_from_(self, S: Parent) -> bool: ...
    def _element_constructor_(
        self,
        x: FiniteDimensionalAlgebraElementInput[_Scalar],
    ) -> FiniteDimensionalAlgebraElement[_Scalar]: ...
    def from_base_ring(
        self,
        x: FiniteDimensionalAlgebraElementInput[_Scalar],
    ) -> FiniteDimensionalAlgebraElement[_Scalar]: ...
    def _Hom_(
        self,
        B: FiniteDimensionalAlgebra[_Scalar],
        category: Category,
    ) -> FiniteDimensionalAlgebraHomset[_Scalar] | Homset: ...
    def ngens(self) -> int: ...
    def degree(self) -> int: ...
    def gen(self, i: int) -> FiniteDimensionalAlgebraElement[_Scalar]: ...
    def basis(self) -> FiniteAlgebraBasis[_Scalar]: ...
    def __iter__(self) -> Iterator[FiniteDimensionalAlgebraElement[_Scalar]]: ...
    def _ideal_class_(
        self,
        n: int = 0,
    ) -> type[FiniteDimensionalAlgebraIdeal[_Scalar]]: ...
    def table(self) -> tuple[Matrix[_Scalar], ...]: ...
    def left_table(self) -> tuple[Matrix[_Scalar], ...]: ...
    def base_extend(
        self,
        F: Fields.ParentMethods[_ExtendedScalar],
    ) -> FiniteDimensionalAlgebra[_ExtendedScalar]: ...
    def cardinality(self) -> Integer | PlusInfinity: ...
    def ideal(
        self,
        gens: FiniteDimensionalIdealInput[_Scalar] = None,
        given_by_matrix: bool = False,
        side: Literal["left", "right", "twosided"] | None = None,
    ) -> FiniteDimensionalAlgebraIdeal[_Scalar]: ...
    def is_associative(self) -> bool: ...
    def is_commutative(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def is_unitary(self) -> bool: ...
    def is_zero(self) -> bool: ...
    def one(self) -> FiniteDimensionalAlgebraElement[_Scalar]: ...
    def zero(self) -> FiniteDimensionalAlgebraElement[_Scalar]: ...
    def random_element(
        self,
        *args: int | Integer,
        **kwargs: int | Integer | bool | str,
    ) -> FiniteDimensionalAlgebraElement[_Scalar]: ...
    def _is_valid_homomorphism_(
        self,
        other: FiniteDimensionalAlgebra[_Scalar],
        im_gens: Sequence[
            FiniteDimensionalAlgebraElement[_Scalar]
            | FreeModuleElement[_Scalar]
            | Vector[_Scalar]
        ],
        base_map: Callable[[_Scalar], _Scalar] | None = None,
    ) -> bool: ...
    def quotient_map(
        self,
        ideal: FiniteDimensionalAlgebraIdeal[_Scalar],
    ) -> FiniteDimensionalAlgebraMorphism[_Scalar]: ...
    def maximal_ideal(self) -> FiniteDimensionalAlgebraIdeal[_Scalar]: ...
    def primary_decomposition(
        self,
    ) -> list[FiniteDimensionalAlgebraMorphism[_Scalar]]: ...
    def maximal_ideals(
        self,
    ) -> list[FiniteDimensionalAlgebraIdeal[_Scalar]]: ...
