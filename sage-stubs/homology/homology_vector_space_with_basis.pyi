from typing import Generic, Literal, TypeVar

from sage.algebras.steenrod.steenrod_algebra import SteenrodAlgebra_generic
from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.homology.chain_homotopy import ChainContraction
from sage.homology.chains import Chains, Cochains
from sage.matrix.matrix import Matrix
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import FieldElement
from sage.structure.parent import Parent
from sage.topology.cell_complex import GenericCellComplex

_FieldScalar = TypeVar(
    "_FieldScalar",
    bound=FieldElement,
    default=FieldElement,
)

type HomologyBasisIndex = tuple[int | Integer, int]
type HomogeneousCycle = Chains.Element | Cochains.Element


class HomologyVectorSpaceWithBasis(
    CombinatorialFreeModule,
    Generic[_FieldScalar],
):
    class Element(
        IndexedFreeModuleElement[HomologyBasisIndex, _FieldScalar]
    ):
        def parent(self) -> HomologyVectorSpaceWithBasis[_FieldScalar]: ...
        def to_cycle(self) -> HomogeneousCycle: ...
        to_cocycle = to_cycle
        def eval(
            self,
            other: HomologyVectorSpaceWithBasis.Element,
        ) -> _FieldScalar: ...

    element_class: type[Element]

    def __init__(
        self,
        base_ring: Parent[_FieldScalar],
        cell_complex: GenericCellComplex,
        cohomology: bool = ...,
        category: Category | None = ...,
    ) -> None: ...
    def base_ring(self) -> Parent[_FieldScalar]: ...
    def basis(
        self,
        d: int | Integer | None = ...,
    ) -> AbstractFamily: ...
    def degree_on_basis(
        self,
        i: HomologyBasisIndex,
    ) -> int | Integer: ...
    def contraction(self) -> ChainContraction[Integer, _FieldScalar]: ...
    def complex(self) -> GenericCellComplex: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, i: HomologyBasisIndex) -> str: ...
    _latex_term = _repr_term
    def _to_cycle_on_basis(
        self,
        i: HomologyBasisIndex,
    ) -> HomogeneousCycle: ...
    def dual(
        self,
    ) -> HomologyVectorSpaceWithBasis[_FieldScalar] | CohomologyRing[_FieldScalar]: ...


class HomologyVectorSpaceWithBasis_mod2(
    HomologyVectorSpaceWithBasis[_FieldScalar],
    Generic[_FieldScalar],
):
    class Element(HomologyVectorSpaceWithBasis.Element):
        def _acted_upon_(
            self,
            a: SteenrodAlgebra_generic.Element | _FieldScalar,
            self_on_left: bool,
        ) -> HomologyVectorSpaceWithBasis_mod2.Element: ...

    element_class: type[Element]

    def __init__(
        self,
        base_ring: Parent[_FieldScalar],
        cell_complex: GenericCellComplex,
        category: Category | None = ...,
    ) -> None: ...


class CohomologyRing(
    HomologyVectorSpaceWithBasis[_FieldScalar],
    Generic[_FieldScalar],
):
    class Element(HomologyVectorSpaceWithBasis.Element):
        def parent(self) -> CohomologyRing[_FieldScalar]: ...
        def cup_product(
            self,
            other: CohomologyRing.Element,
        ) -> CohomologyRing.Element: ...

    element_class: type[Element]

    def __init__(
        self,
        base_ring: Parent[_FieldScalar],
        cell_complex: GenericCellComplex,
        category: Category | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def one(self) -> CohomologyRing.Element: ...
    def product_on_basis(
        self,
        li: HomologyBasisIndex,
        ri: HomologyBasisIndex,
    ) -> CohomologyRing.Element: ...


class CohomologyRing_mod2(
    CohomologyRing[_FieldScalar],
    Generic[_FieldScalar],
):
    class Element(CohomologyRing.Element):
        def parent(self) -> CohomologyRing_mod2[_FieldScalar]: ...
        def Sq(
            self,
            i: int | Integer,
        ) -> CohomologyRing_mod2.Element: ...
        def _acted_upon_(
            self,
            a: SteenrodAlgebra_generic.Element | _FieldScalar,
            self_on_left: bool,
        ) -> CohomologyRing_mod2.Element: ...

    element_class: type[Element]

    def __init__(
        self,
        base_ring: Parent[_FieldScalar],
        cell_complex: GenericCellComplex,
    ) -> None: ...
    def steenrod_module_map(
        self,
        deg_domain: int | Integer,
        deg_codomain: int | Integer,
        side: Literal["left", "right"] = ...,
    ) -> Matrix[_FieldScalar]: ...


def sum_indices(
    k: int | Integer,
    i_k_plus_one: int | Integer,
    S_k_plus_one: int | Integer,
) -> list[list[int]]: ...


def is_GF2(R: Parent[FieldElement]) -> bool: ...
