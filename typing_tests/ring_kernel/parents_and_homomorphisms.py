from typing import assert_type

from sage.rings.commutative_ring import CommutativeRing
from sage.rings.field import Field
from sage.rings.homset import RingHomset_generic
from sage.rings.integral_domain import IntegralDomain
from sage.rings.morphism import RingHomomorphism
from sage.rings.principal_ideal_domain import PrincipalIdealDomain
from sage.rings.ring import Ring
from sage.structure.element import CommutativeRingElement, FieldElement, RingElement


class RElement(RingElement): ...


class CElement(CommutativeRingElement): ...


class KElement(FieldElement): ...


def check_ring_parent(parent: Ring[RElement]) -> None:
    assert_type(parent.an_element(), RElement)
    assert_type(parent(0), RElement)


def check_commutative_tower(
    commutative_ring: CommutativeRing[CElement],
    domain: IntegralDomain[CElement],
    pid: PrincipalIdealDomain[CElement],
) -> None:
    assert_type(commutative_ring.an_element(), CElement)
    assert_type(domain.an_element(), CElement)
    assert_type(pid.an_element(), CElement)


def check_field_parent(field: Field[KElement]) -> None:
    assert_type(field.an_element(), KElement)
    assert_type(field(1), KElement)


def check_ring_homset(
    homset: RingHomset_generic[RElement, CElement],
) -> None:
    assert_type(homset.domain().an_element(), RElement)
    assert_type(homset.codomain().an_element(), CElement)
    assert_type(homset.an_element(), RingHomomorphism[RElement, CElement])
