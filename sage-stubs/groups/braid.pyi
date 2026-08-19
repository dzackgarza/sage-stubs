from collections.abc import Iterable, Mapping, Sequence
from typing import Literal, Never, overload

from sage.algebras.free_algebra_element import FreeAlgebraElement
from sage.categories.action import Action
from sage.combinat.permutation import Permutation
from sage.groups.artin import FiniteTypeArtinGroup, FiniteTypeArtinGroupElement
from sage.groups.finitely_presented import (
    FinitelyPresentedGroup,
    GroupMorphismWithGensImages,
)
from sage.groups.free_group import FreeGroupElement, FreeGroup_class
from sage.groups.group import Group
from sage.groups.perm_gps.permgroup_element import SymmetricGroupElement
from sage.homology.chain_complex import ChainComplex_class
from sage.homology.homology_group import HomologyGroup_class
from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.plot.graphics import Graphics
from sage.plot.plot3d.base import Graphics3d
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.rings.ring import Ring
from sage.rings.semirings.tropical_semiring import TropicalSemiringElement
from sage.structure.element import Element, RingElement
from sage.symbolic.expression import Expression


type TietzeWord = Sequence[int | Integer]
type BraidInput = TietzeWord | Permutation | SymmetricGroupElement | Braid
type BurauReduction = bool | Literal["increasing", "simple", "unitary"]
type LaurentMatrix = Matrix[LaurentPolynomial]
type BraidMatrix = Matrix[RingElement]
type AnnularGrading = tuple[int | Integer, int | Integer]
type AnnularHomologyGroup = HomologyGroup_class | FreeModule_generic
type AnnularHomology = dict[int | Integer, AnnularHomologyGroup]
type RightQuantumExponentTuple = tuple[int, ...]


class Braid(FiniteTypeArtinGroupElement):
    def parent(self) -> BraidGroup_class: ...
    def __hash__(self) -> int: ...
    def strands(self) -> Integer: ...
    def components_in_closure(self) -> Integer: ...

    @overload
    def burau_matrix(
        self,
        var: str = ...,
        reduced: Literal["unitary"] = ...,
    ) -> tuple[LaurentMatrix, LaurentMatrix, LaurentMatrix]: ...
    @overload
    def burau_matrix(
        self,
        var: str = ...,
        reduced: bool | Literal["increasing", "simple"] = ...,
    ) -> LaurentMatrix: ...

    def alexander_polynomial(
        self,
        var: str = ...,
        normalized: bool = ...,
    ) -> LaurentPolynomial: ...
    def permutation(
        self,
        W: Group | None = ...,
    ) -> Permutation | SymmetricGroupElement: ...
    def plot(
        self,
        color: str | Sequence[str] = ...,
        orientation: Literal["bottom-top", "top-bottom"] = ...,
        gap: float = ...,
        aspect_ratio: int | float = ...,
        axes: bool = ...,
        **kwds: Element | int | float | bool | str,
    ) -> Graphics: ...
    def plot3d(
        self,
        color: str | Sequence[str] = ...,
    ) -> Graphics3d: ...
    def LKB_matrix(self, variables: str = ...) -> LaurentMatrix: ...
    def TL_matrix(
        self,
        drain_size: int | Integer,
        variab: str | Element | None = ...,
        sparse: bool = ...,
    ) -> BraidMatrix: ...
    def links_gould_matrix(self, symbolics: bool = ...) -> BraidMatrix: ...
    def links_gould_polynomial(
        self,
        varnames: str | None = ...,
        use_symbolics: bool = ...,
    ) -> LaurentPolynomial | Expression: ...
    def tropical_coordinates(
        self,
    ) -> list[TropicalSemiringElement[Integer]]: ...
    def markov_trace(
        self,
        variab: str | Element | None = ...,
        normalized: bool = ...,
    ) -> LaurentPolynomial | Expression: ...
    def jones_polynomial(
        self,
        variab: str | Element | None = ...,
        skein_normalization: bool = ...,
    ) -> LaurentPolynomial | Expression: ...

    @overload
    def annular_khovanov_complex(
        self,
        qagrad: None = ...,
        ring: Ring | None = ...,
    ) -> dict[AnnularGrading, ChainComplex_class]: ...
    @overload
    def annular_khovanov_complex(
        self,
        qagrad: AnnularGrading,
        ring: Ring | None = ...,
    ) -> ChainComplex_class: ...

    @overload
    def annular_khovanov_homology(
        self,
        qagrad: None = ...,
        ring: Ring = ...,
    ) -> dict[AnnularGrading, AnnularHomology]: ...
    @overload
    def annular_khovanov_homology(
        self,
        qagrad: AnnularGrading,
        ring: Ring = ...,
    ) -> AnnularHomology: ...

    def left_normal_form(
        self,
        algorithm: Literal["artin", "libbraiding"] = ...,
    ) -> tuple[Braid, ...]: ...
    def right_normal_form(self) -> tuple[Braid, ...]: ...
    def centralizer(self) -> list[Braid]: ...
    def super_summit_set(self) -> list[Braid]: ...
    def gcd(self, other: Braid) -> Braid: ...
    def lcm(self, other: Braid) -> Braid: ...
    def conjugating_braid(self, other: Braid) -> Braid | None: ...
    def is_conjugated(self, other: Braid) -> bool: ...
    def pure_conjugating_braid(self, other: Braid) -> Braid | None: ...
    def ultra_summit_set(self) -> list[Braid]: ...
    def thurston_type(
        self,
    ) -> Literal["periodic", "reducible", "pseudo-Anosov"]: ...
    def is_reducible(self) -> bool: ...
    def is_periodic(self) -> bool: ...
    def is_pseudoanosov(self) -> bool: ...
    def rigidity(self) -> Integer: ...
    def sliding_circuits(self) -> list[list[Braid]]: ...
    def mirror_image(self) -> Braid: ...
    def reverse(self) -> Braid: ...
    def deformed_burau_matrix(
        self,
        variab: str = ...,
    ) -> Matrix[FreeAlgebraElement]: ...

    @overload
    def colored_jones_polynomial(
        self,
        N: int | Integer,
        variab: str | None = ...,
        try_inverse: bool = ...,
    ) -> LaurentPolynomial: ...
    @overload
    def colored_jones_polynomial(
        self,
        N: int | Integer,
        variab: Element,
        try_inverse: bool = ...,
    ) -> Element: ...

    def super_summit_set_element(self) -> tuple[Braid, Braid]: ...
    def ultra_summit_set_element(self) -> tuple[Braid, Braid]: ...
    def sliding_circuits_element(self) -> tuple[Braid, Braid]: ...
    def trajectory(self) -> list[Braid]: ...
    def cyclic_slidings(self) -> list[list[Braid]]: ...


class RightQuantumWord:
    tuples: Mapping[RightQuantumExponentTuple, LaurentPolynomial]

    def __init__(self, words: FreeAlgebraElement) -> None: ...
    def reduced_word(self) -> FreeAlgebraElement: ...
    def eps(self, N: int | Integer) -> LaurentPolynomial: ...
    def __repr__(self) -> str: ...


class BraidGroup_class(FiniteTypeArtinGroup):
    Element: type[Braid]
    element_class: type[Braid]

    def __init__(self, names: tuple[str, ...]) -> None: ...
    def __reduce__(
        self,
    ) -> tuple[type[BraidGroup_class], tuple[tuple[str, ...]]]: ...
    def _repr_(self) -> str: ...
    def cardinality(self) -> PlusInfinity: ...
    order = cardinality
    def as_permutation_group(self) -> Never: ...
    def strands(self) -> Integer: ...
    def _element_constructor_(self, x: BraidInput) -> Braid: ...
    def _an_element_(self) -> Braid: ...
    def some_elements(self) -> list[Braid]: ...
    def dimension_of_TL_space(
        self,
        drain_size: int | Integer,
    ) -> Integer: ...
    def TL_basis_with_drain(
        self,
        drain_size: int | Integer,
    ) -> tuple[tuple[int, ...], ...]: ...
    def TL_representation(
        self,
        drain_size: int | Integer,
        variab: str | Element | None = ...,
    ) -> tuple[BraidMatrix, ...]: ...
    def mapping_class_action(
        self,
        F: FreeGroup_class,
    ) -> MappingClassGroupAction: ...
    def mirror_involution(self) -> GroupMorphismWithGensImages: ...

    @overload
    def presentation_two_generators(
        self,
        isomorphisms: Literal[False] = ...,
    ) -> FinitelyPresentedGroup: ...
    @overload
    def presentation_two_generators(
        self,
        isomorphisms: Literal[True],
    ) -> tuple[
        FinitelyPresentedGroup,
        GroupMorphismWithGensImages,
        GroupMorphismWithGensImages,
    ]: ...

    def epimorphisms(self, H: Group) -> list[GroupMorphismWithGensImages]: ...


@overload
def BraidGroup(
    n: int | Integer,
    names: str | Iterable[str] = ...,
) -> BraidGroup_class: ...
@overload
def BraidGroup(
    n: str | Iterable[str] | None = ...,
    names: str | Iterable[str] = ...,
) -> BraidGroup_class: ...


class MappingClassGroupAction(Action):
    def __init__(
        self,
        G: FreeGroup_class,
        M: BraidGroup_class,
    ) -> None: ...
    def _act_(
        self,
        b: FreeGroupElement,
        x: Braid,
    ) -> FreeGroupElement: ...
