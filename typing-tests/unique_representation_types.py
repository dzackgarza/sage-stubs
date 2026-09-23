"""Copies retain the receiver type; unreduce returns its callable's result."""

from typing import assert_type

from sage.rings.integer import Integer
from sage.structure.unique_representation import (
    CachedRepresentation,
    UniqueRepresentation,
    WithPicklingByInitArgs,
    unreduce,
)


class Labelled(UniqueRepresentation):
    def __init__(self, label: str) -> None:
        self.label = label


def stringify(value: int) -> str:
    return str(value)


def reconstruction(
    plain: WithPicklingByInitArgs,
    cached: CachedRepresentation,
    unique: UniqueRepresentation,
    labelled: Labelled,
) -> None:
    assert_type(plain.__copy__(), WithPicklingByInitArgs)
    assert_type(cached.__copy__(), CachedRepresentation)
    assert_type(unique.__copy__(), UniqueRepresentation)
    assert_type(labelled.__copy__(), Labelled)
    assert_type(labelled.__deepcopy__({}), Labelled)
    assert_type(unreduce(Labelled, ("a",), {}), Labelled)
    assert_type(unreduce(Integer, (3,), {}), Integer)
    assert_type(unreduce(int, (3,), {}), int)
    assert_type(unreduce(stringify, (3,), {}), str)
