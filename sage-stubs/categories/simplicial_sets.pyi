from collections.abc import Iterable, Mapping

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.homsets import HomsetsCategory
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.homology.chain_complex import ChainComplex_class
from sage.modules.quotient_module import QuotientModule_free_ambient
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element, RingElement
from sage.topology.simplicial_set import (
    AbstractSimplex_class,
    SimplicialSet_arbitrary,
    SimplicialSet_finite,
)
from sage.topology.simplicial_set_constructions import (
    SmashProductOfSimplicialSets_finite,
)
from sage.topology.simplicial_set_morphism import SimplicialSetMorphism

type CoverCharacter = Mapping[AbstractSimplex_class, Element]
type TwistingOperator = Mapping[AbstractSimplex_class, RingElement]
type ChainDimensions = int | Integer | Iterable[int | Integer] | None


class SimplicialSets(Category_singleton):
    def super_categories(self) -> list[Category]: ...

    class ParentMethods:
        def is_finite(self) -> bool: ...
        def is_pointed(self) -> bool: ...
        def set_base_point(
            self,
            point: AbstractSimplex_class,
        ) -> SimplicialSet_finite: ...

    class Homsets(HomsetsCategory):
        class Endset(CategoryWithAxiom):
            class ParentMethods:
                def one(self) -> SimplicialSetMorphism: ...

    class Finite(CategoryWithAxiom):
        pass

    class SubcategoryMethods:
        def Pointed(self) -> CategoryWithAxiom: ...

    class Pointed(CategoryWithAxiom):
        class ParentMethods:
            def base_point(self) -> AbstractSimplex_class: ...
            def base_point_map(
                self,
                domain: SimplicialSet_arbitrary | None = ...,
            ) -> SimplicialSetMorphism: ...
            def fundamental_group(
                self,
                simplify: bool = ...,
            ) -> FinitelyPresentedGroup: ...
            def universal_cover_map(self) -> SimplicialSetMorphism: ...
            def covering_map(
                self,
                character: CoverCharacter,
            ) -> SimplicialSetMorphism: ...
            def cover(
                self,
                character: CoverCharacter,
            ) -> SimplicialSet_finite: ...
            def universal_cover(self) -> SimplicialSet_finite: ...
            def twisted_chain_complex(
                self,
                twisting_operator: TwistingOperator | None = ...,
                dimensions: ChainDimensions = ...,
                augmented: bool = ...,
                cochain: bool = ...,
                verbose: bool = ...,
                subcomplex: SimplicialSet_arbitrary | None = ...,
                check: bool = ...,
            ) -> ChainComplex_class[Integer, RingElement]: ...
            def twisted_homology(
                self,
                n: int,
                reduced: bool = ...,
            ) -> QuotientModule_free_ambient[RingElement]: ...
            def is_simply_connected(self) -> bool: ...
            def connectivity(
                self,
                max_dim: int | Integer | None = ...,
            ) -> Integer | PlusInfinity: ...

        class Finite(CategoryWithAxiom):
            class ParentMethods:
                def unset_base_point(self) -> SimplicialSet_finite: ...
                def fat_wedge(self, n: int) -> SimplicialSet_finite: ...
                def smash_product(
                    self,
                    *others: SimplicialSet_arbitrary,
                ) -> SmashProductOfSimplicialSets_finite: ...
