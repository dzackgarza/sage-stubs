from typing import assert_type

from sage.categories.homset import Homset
from sage.categories.morphism import Morphism, SetMorphism
from sage.structure.element import Element
from sage.structure.parent import Parent


class DomainElement(Element): ...


class CodomainElement(Element): ...


def check_general_homset(
    homset: Homset[Morphism, DomainElement, CodomainElement],
) -> None:
    assert_type(homset.domain(), Parent[DomainElement])
    assert_type(homset.codomain(), Parent[CodomainElement])
    assert_type(homset.an_element(), Morphism)
    assert_type(homset.identity(), Morphism)


def check_set_homset(
    homset: Homset[
        SetMorphism[DomainElement, CodomainElement],
        DomainElement,
        CodomainElement,
    ],
) -> None:
    assert_type(homset.domain(), Parent[DomainElement])
    assert_type(homset.codomain(), Parent[CodomainElement])
    assert_type(
        homset.an_element(), SetMorphism[DomainElement, CodomainElement]
    )
