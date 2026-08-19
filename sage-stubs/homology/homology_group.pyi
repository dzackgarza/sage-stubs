from collections.abc import Sequence
from typing import TypeVar, overload

from sage.groups.additive_abelian.additive_abelian_group import (
    AdditiveAbelianGroup_fixed_gens,
)
from sage.modules.free_module import FreeModule_ambient_field
from sage.rings.integer import Integer
from sage.rings.integer_ring import IntegerRing_class
from sage.structure.element import FieldElement
from sage.structure.parent import Parent

_FieldScalar = TypeVar(
    "_FieldScalar",
    bound=FieldElement,
    default=FieldElement,
)

type HomologyRank = int | Integer
type InvariantFactors = Sequence[int | Integer]


class HomologyGroup_class(AdditiveAbelianGroup_fixed_gens):
    def __init__(
        self,
        n: HomologyRank,
        invfac: InvariantFactors,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...


@overload
def HomologyGroup(
    n: HomologyRank | InvariantFactors,
    base_ring: IntegerRing_class,
    invfac: InvariantFactors | None = ...,
) -> HomologyGroup_class: ...
@overload
def HomologyGroup(
    n: HomologyRank,
    base_ring: Parent[_FieldScalar],
    invfac: InvariantFactors | None = ...,
) -> FreeModule_ambient_field[_FieldScalar] | HomologyGroup_class: ...
