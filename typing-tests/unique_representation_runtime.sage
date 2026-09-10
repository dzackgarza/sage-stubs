"""Inherited unique representation preserves copies and pickle reconstruction."""

from copy import copy, deepcopy

from sage.structure.unique_representation import (
    UniqueRepresentation,
    WithPicklingByInitArgs,
    unreduce,
)


class Labelled(UniqueRepresentation):
    def __init__(self, label):
        self.label = label


labelled = Labelled("a")
assert Labelled("a") is labelled
assert Labelled("b") is not labelled
assert copy(labelled) is labelled
assert deepcopy(labelled) is labelled
assert labelled.__copy__().label == "a"
assert labelled.__deepcopy__({}).label == "a"
assert unreduce(Labelled, ("a",), {}) is labelled

# The inherited reduction contains a reconstruction function, not a type
# object. Reconstruct from its actual arguments, retaining the cached object.
reconstructor, arguments = labelled.__reduce__()
assert reconstructor(*arguments) is labelled

plain = WithPicklingByInitArgs()
assert copy(plain) is plain
assert deepcopy(plain) is plain
assert WithPicklingByInitArgs() is not plain

# unreduce is not specific to UniqueRepresentation subclasses.
integer = unreduce(Integer, (3,), {})
assert integer.parent() is ZZ
assert integer == 3
assert type(unreduce(int, (3,), {})) is int

# unreduce forwards to its supplied callable rather than imposing a class or
# a unique-representation result. Preserve this directly implemented case.
def stringify(value):
    return str(value)


assert unreduce(stringify, (3,), {}) == "3"
