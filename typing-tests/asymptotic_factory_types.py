"""Factory calls retain their key producer's defaults, keywords, and product."""

from typing import assert_type

from sage.categories.category import Category
from sage.rings.asymptotic.growth_group import GenericGrowthGroup
from sage.rings.asymptotic.term_monoid import (
    BTermMonoid,
    ExactTermMonoid,
    GenericTermMonoid,
    OTermMonoid,
    TermConstructionValue,
    TermMonoidFactory,
    TermMonoidKey,
)
from sage.structure.element import RingElement
from sage.structure.factory import UniqueFactory
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation, unreduce


def term_factory_types(
    factory: TermMonoidFactory,
    growth: GenericGrowthGroup,
    coefficients: Parent[RingElement],
    category: Category,
    existing: GenericTermMonoid,
    exact: ExactTermMonoid,
    asymptotic_ring: Parent,
) -> None:
    assert_type(factory("O", growth, coefficients), GenericTermMonoid)
    assert_type(
        factory(term_monoid="exact", growth_group=growth, coefficient_ring=coefficients),
        GenericTermMonoid,
    )
    assert_type(factory("B", growth, coefficients, category=category), GenericTermMonoid)
    assert_type(factory(existing, asymptotic_ring=asymptotic_ring), GenericTermMonoid)
    key, extra = factory.create_key_and_extra_args("O", growth, coefficients)
    assert_type(key, TermMonoidKey)
    assert_type(extra, dict[str, TermConstructionValue])
    assert_type(factory.get_object((10, 9), key, extra), GenericTermMonoid)
    assert_type(factory.create_object(0, key, category=category), GenericTermMonoid)
    assert_type(factory.other_keys(key, existing), list[TermMonoidKey])
    assert_type(
        GenericTermMonoid.__classcall__(GenericTermMonoid, factory, growth, coefficients),
        GenericTermMonoid,
    )
    assert_type(
        OTermMonoid.__classcall__(OTermMonoid, factory, growth, coefficients),
        OTermMonoid,
    )
    assert_type(exact.__copy__(), ExactTermMonoid)
    assert_type(exact.__deepcopy__({}), ExactTermMonoid)
    assert_type(unreduce(ExactTermMonoid, (factory, growth, coefficients), {}), ExactTermMonoid)
    assert_type(UniqueRepresentation.__classcall__(UniqueRepresentation), UniqueRepresentation)
    assert_type(
        TermMonoidFactory("typed-custom", ExactTermMonoid, OTermMonoid, BTermMonoid),
        TermMonoidFactory,
    )


class Product:
    def __init__(self, number: int, label: str) -> None:
        self.number = number
        self.label = label


class ProductFactory(UniqueFactory[tuple[int, str], Product, bool, [int, str]]):
    def create_key_and_extra_args(
        self, number: int, label: str = ""
    ) -> tuple[tuple[int, str], dict[str, bool]]:
        return (number, label), {}

    def create_object(
        self, version: tuple[int, ...], key: tuple[int, str], **extra: bool
    ) -> Product:
        return Product(*key)


def independent_factory_types(factory: ProductFactory) -> None:
    assert_type(factory(3), Product)
    assert_type(factory(number=3, label="three"), Product)
    assert_type(factory.get_object((10, 9), (3, "three"), {}), Product)
    assert_type(factory.other_keys((3, "three"), factory(3)), list[tuple[int, str]])
