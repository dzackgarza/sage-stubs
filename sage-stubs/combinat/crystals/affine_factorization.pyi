from collections.abc import Iterable, Iterator, Sequence
from typing import Self

from sage.categories.morphism import Morphism
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.combinat.root_system.weyl_group import WeylGroupElement
from sage.combinat.tableau import Tableau
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

type Factorization = tuple[WeylGroupElement, ...]
type FactorizationInput = Iterable[WeylGroupElement]
type FactorizationWeight = Sequence[int | Integer]
type SkewShapeInput = Sequence[Sequence[int | Integer] | object]
type FactorizationSource = WeylGroupElement | SkewShapeInput

class AffineFactorizationCrystal(
    UniqueRepresentation,
    Parent[AffineFactorizationCrystal.Element],
):
    n: int
    k: int
    x: int
    w: WeylGroupElement
    module_generators: list[AffineFactorizationCrystal.Element]

    class Element(ElementWrapper):
        value: Factorization
        def parent(self) -> AffineFactorizationCrystal: ...
        def e(self, i: int | Integer) -> Self | None: ...
        def f(self, i: int | Integer) -> Self | None: ...
        def bracketing(
            self,
            i: int | Integer,
        ) -> list[list[int]]: ...
        def to_tableau(self) -> Tableau: ...

    Element: type[Element]
    element_class: type[Element]

    @staticmethod
    def __classcall_private__(
        cls: type[AffineFactorizationCrystal],
        w: FactorizationSource,
        n: int | Integer,
        x: int | Integer | None = ...,
        k: int | Integer | None = ...,
    ) -> AffineFactorizationCrystal: ...
    def __init__(
        self,
        w: WeylGroupElement,
        n: int | Integer,
        x: int | Integer | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        value: FactorizationInput | Element,
    ) -> Element: ...
    def __iter__(self) -> Iterator[Element]: ...
    def list(self) -> list[Element]: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def index_set(self) -> tuple[int, ...]: ...
    def highest_weight_vectors(self) -> tuple[Element, ...]: ...
    @property
    def _tableaux_isomorphism(self) -> FactorizationToTableaux: ...


def affine_factorizations(
    w: WeylGroupElement,
    l: int | Integer,
    weight: FactorizationWeight | None = ...,
) -> list[list[WeylGroupElement]]: ...

class FactorizationToTableaux(
    Morphism[AffineFactorizationCrystal.Element, Element],
):
    def _call_(
        self,
        x: AffineFactorizationCrystal.Element,
    ) -> Element: ...
    def is_isomorphism(self) -> bool: ...
    is_embedding = is_isomorphism
    is_surjective = is_isomorphism
