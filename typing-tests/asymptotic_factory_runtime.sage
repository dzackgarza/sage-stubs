"""Complete native consumers for classcall, unique factories, and pickling."""

from copy import copy, deepcopy
from sage.rings.asymptotic.growth_group import GrowthGroup
from sage.rings.asymptotic.term_monoid import (
    BTermMonoid, DefaultTermMonoidFactory, ExactTermMonoid,
    GenericTermMonoid, OTermMonoid, TermMonoidFactory,
)
from sage.structure.factory import UniqueFactory
from sage.structure.unique_representation import UniqueRepresentation, unreduce

factory = DefaultTermMonoidFactory
growth = GrowthGroup("x^ZZ")
category = Monoids() & Posets()

for kind, term_class in (("O", OTermMonoid), ("exact", ExactTermMonoid), ("B", BTermMonoid)):
    monoid = factory(kind, growth, QQ)
    assert isinstance(monoid, term_class)
    assert factory(term_monoid=kind, growth_group=growth, coefficient_ring=QQ) is monoid
    assert factory(kind, growth, QQ, category=category) is monoid
    assert factory(monoid, growth, QQ) is monoid
    key, extra = factory.create_key_and_extra_args(kind, growth, QQ, category=category)
    assert key == (term_class, growth, QQ)
    assert extra == {"category": category}
    assert factory.create_object(0, key, **extra) is monoid
    assert factory.get_object((10, 9), key, extra) is monoid
    assert factory.other_keys(key, monoid) == []
    assert term_class.__classcall__(term_class, factory, growth, QQ) is monoid
    assert copy(monoid) is monoid
    assert deepcopy(monoid) is monoid
    assert loads(dumps(monoid)) is monoid
    assert unreduce(term_class, (factory, growth, QQ), {}) is monoid

assert copy(factory) is factory
assert deepcopy(factory) is factory
assert loads(dumps(factory)) is factory
assert UniqueRepresentation.__classcall__(UniqueRepresentation) is UniqueRepresentation()

asymptotic_ring = AsymptoticRing(growth_group=growth, coefficient_ring=QQ)
assert factory("O", asymptotic_ring=asymptotic_ring) is factory("O", growth, QQ)

class CustomExactMonoid(ExactTermMonoid):
    pass

custom = TermMonoidFactory("native-custom", exact_term_monoid_class=CustomExactMonoid)
assert isinstance(custom("exact", growth, QQ), CustomExactMonoid)
assert type(custom("exact", growth, QQ)) is not type(factory("exact", growth, QQ))

# A factory product need not inherit SageObject. Its actual class and key
# remain correlated through the same inherited call and cache pipeline.
class Product:
    def __init__(self, number, label):
        self.number = number
        self.label = label

class ProductFactory(UniqueFactory):
    def create_key_and_extra_args(self, number, label=""):
        return (number, label), {}

    def create_object(self, version, key, **extra):
        return Product(*key)

products = ProductFactory("native-products")
first = products(3)
assert isinstance(first, Product)
assert first.number == 3 and first.label == ""
assert products(number=3) is first
assert products(3, "three") is not first
named = products(number=3, label="three")
assert named.number == 3 and named.label == "three"
assert products(number=3, label="three") is named
assert products.other_keys((3, "three"), named) == []
print("PASS: native classcall, term factory families, cache identity, and pickling")
