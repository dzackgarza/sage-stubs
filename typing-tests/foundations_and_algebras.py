from typing import TypeVar, assert_type

from sage.algebras.affine_nil_temperley_lieb import (
    AffineNilTemperleyLiebGenerators,
    AffineNilTemperleyLiebTypeA,
)
from sage.algebras.down_up_algebra import (
    DownUpAlgebra,
    DownUpAlgebraGenerators,
    DownUpBasisIndex,
    VermaModule,
    VermaWeightFamily,
)
from sage.categories.homset import End, Hom, Homset
from sage.categories.morphism import Morphism
from sage.combinat.free_module import CombinatorialFreeModuleElement
from sage.combinat.root_system.weyl_group import WeylGroupElement, WeylGroup_gens
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent

_DomainElement = TypeVar("_DomainElement", bound=Element)
_CodomainElement = TypeVar("_CodomainElement", bound=Element)
_EndElement = TypeVar("_EndElement", bound=Element)


def check_homset(
    X: Parent[_DomainElement], Y: Parent[_CodomainElement]
) -> None:
    H = Hom(X, Y)
    assert_type(
        H,
        Homset[
            Morphism[_DomainElement, _CodomainElement],
            _DomainElement,
            _CodomainElement,
        ],
    )
    assert_type(H.domain(), Parent[_DomainElement])
    assert_type(H.codomain(), Parent[_CodomainElement])
    assert_type(H.an_element(), Morphism[_DomainElement, _CodomainElement])


def check_endomorphisms(X: Parent[_EndElement]) -> None:
    E = End(X)
    assert_type(
        E,
        Homset[Morphism[_EndElement, _EndElement], _EndElement, _EndElement],
    )
    assert_type(E.identity(), Morphism[_EndElement, _EndElement])


def check_affine_nil_temperley_lieb(
    A: AffineNilTemperleyLiebTypeA,
    w: WeylGroupElement,
    i: int,
) -> None:
    assert_type(A.weyl_group(), WeylGroup_gens)
    assert_type(A.one_basis(), WeylGroupElement)
    assert_type(A.index_set(), tuple[int, ...])
    assert_type(A.algebra_generators(), AffineNilTemperleyLiebGenerators)
    assert_type(A.algebra_generator(i), CombinatorialFreeModuleElement)
    assert_type(A.product_on_basis(w, w), CombinatorialFreeModuleElement)


def check_down_up_algebra(
    A: DownUpAlgebra,
    index: DownUpBasisIndex,
    highest_weight: RingElement,
) -> None:
    assert_type(A.algebra_generators(), DownUpAlgebraGenerators)
    assert_type(A.one_basis(), DownUpBasisIndex)
    assert_type(A.product_on_basis(index, index), CombinatorialFreeModuleElement)
    M = A.verma_module(highest_weight)
    assert_type(M, VermaModule)
    assert_type(M.highest_weight_vector(), CombinatorialFreeModuleElement)
    assert_type(M.weights(), VermaWeightFamily)
