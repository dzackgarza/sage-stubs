from collections.abc import Hashable, Iterable, Sequence
from typing import Never

from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.combinat.root_system.coxeter_type import CoxeterType, CoxeterTypeData
from sage.groups.finitely_presented import (
    FinitelyPresentedGroup,
    FinitelyPresentedGroupElement,
)
from sage.matrix.matrix import Matrix
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation


type ArtinGeneratorNames = str | Iterable[str] | None
type ArtinInput = (
    Sequence[int | Integer]
    | FinitelyPresentedGroupElement
    | Element
)
type CoxeterGroupElement = Element
type CoxeterGroupParent = Parent[CoxeterGroupElement]


class ArtinGroupElement(FinitelyPresentedGroupElement):
    def parent(self) -> ArtinGroup: ...
    def _latex_(self) -> str: ...
    def exponent_sum(self) -> Integer: ...
    def coxeter_group_element(
        self,
        W: CoxeterGroupParent | None = ...,
    ) -> CoxeterGroupElement: ...
    def burau_matrix(self, var: str = ...) -> Matrix[RingElement]: ...


class FiniteTypeArtinGroupElement(ArtinGroupElement):
    def parent(self) -> FiniteTypeArtinGroup: ...
    def __hash__(self) -> int: ...
    def left_normal_form(self) -> tuple[FiniteTypeArtinGroupElement, ...]: ...
    def _left_normal_form_coxeter(
        self,
    ) -> tuple[int | Integer | CoxeterGroupElement, ...]: ...


class ArtinGroup(
    UniqueRepresentation,
    FinitelyPresentedGroup,
):
    Element: type[ArtinGroupElement]
    element_class: type[ArtinGroupElement]

    @staticmethod
    def __classcall_private__(
        cls: type[ArtinGroup],
        coxeter_data: CoxeterTypeData | CoxeterMatrix | Sequence[Sequence[object]],
        names: ArtinGeneratorNames = ...,
    ) -> FinitelyPresentedGroup: ...
    def __init__(
        self,
        coxeter_matrix: CoxeterMatrix,
        names: tuple[str, ...],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def cardinality(self) -> PlusInfinity: ...
    order = cardinality
    def as_permutation_group(self) -> Never: ...
    def coxeter_type(self) -> CoxeterType: ...
    def coxeter_matrix(self) -> CoxeterMatrix: ...
    def coxeter_group(self) -> CoxeterGroupParent: ...
    def index_set(self) -> tuple[Hashable, ...]: ...
    def _element_constructor_(self, x: ArtinInput) -> ArtinGroupElement: ...
    def _an_element_(self) -> ArtinGroupElement: ...
    def some_elements(self) -> list[ArtinGroupElement]: ...
    def _standard_lift_Tietze(
        self,
        w: CoxeterGroupElement,
    ) -> list[int | Integer]: ...
    def _standard_lift(
        self,
        w: CoxeterGroupElement,
    ) -> ArtinGroupElement: ...


class FiniteTypeArtinGroup(ArtinGroup):
    Element: type[FiniteTypeArtinGroupElement]
    element_class: type[FiniteTypeArtinGroupElement]

    def _element_constructor_(
        self,
        x: ArtinInput,
    ) -> FiniteTypeArtinGroupElement: ...
    def _an_element_(self) -> FiniteTypeArtinGroupElement: ...
    def some_elements(self) -> list[FiniteTypeArtinGroupElement]: ...
    def _standard_lift(
        self,
        w: CoxeterGroupElement,
    ) -> FiniteTypeArtinGroupElement: ...
    def delta(self) -> FiniteTypeArtinGroupElement: ...
