"""Source-owned fraction-ring methods preserve rings and generic substitutions."""

from typing import assert_type

from sage.categories.rings import Rings
from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import (
    FractionWithFactoredDenominatorRing,
    FractionWithFactoredDenominatorSum,
    diff_seq,
    subs_all,
)
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element, RingElement
from sage.symbolic.expression import Expression


def fraction_ring_types(
    parent: FractionWithFactoredDenominatorRing,
    terms: FractionWithFactoredDenominatorSum,
    variables: tuple[Expression, ...],
    substitutions: dict[Expression, Expression],
    expression: Expression,
    named: dict[str, Expression],
    polynomial: Polynomial,
    polynomial_substitutions: dict[Polynomial, Integer],
    element: Element,
) -> None:
    assert_type(parent.base_ring(), Rings.ParentMethods[RingElement])
    assert_type(terms.__repr__(), str)
    assert_type(subs_all(variables, substitutions), list[Expression])
    assert_type(subs_all(expression, substitutions), Expression)
    assert_type(subs_all(expression, None), Expression)
    assert_type(subs_all(element, None), Element)
    assert_type(subs_all(polynomial, polynomial_substitutions), Element)
    assert_type(subs_all(named, substitutions), dict[str, Expression])
    assert_type(subs_all((named,), substitutions), list[dict[str, Expression]])
    mixed: tuple[Expression | dict[str, Expression], ...] = (expression, named)
    assert_type(
        subs_all(mixed, substitutions),
        list[Expression]
        | list[dict[str, Expression]]
        | list[Expression | dict[str, Expression]],
    )
    ordered = [substitutions, substitutions]
    assert_type(subs_all(expression, ordered), Expression)
    assert_type(subs_all(expression, tuple(ordered), simplify=True), Expression)
    assert_type(diff_seq(variables, ((0, 1),)), tuple[Expression, ...])
