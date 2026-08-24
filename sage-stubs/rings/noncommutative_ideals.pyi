from collections.abc import Sequence
from typing import Literal, TypeAlias

from sage.rings.ideal import Ideal_generic
from sage.rings.ideal_monoid import IdealMonoid_c
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.parent import Parent

IdealSide: TypeAlias = Literal["left", "right", "twosided"]
IdealGeneratorInput: TypeAlias = Sequence[RingElement]

class IdealMonoid_nc(IdealMonoid_c):
    def __init__(self, R: Ring) -> None: ...
    def _element_constructor_(
        self,
        x: object,
    ) -> Ideal_nc: ...

class Ideal_nc(Ideal_generic):
    def __init__(
        self,
        ring: Ring,
        gens: IdealGeneratorInput,
        coerce: bool = ...,
        side: IdealSide = ...,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, right: object) -> bool: ...
    def __ne__(self, right: object) -> bool: ...
    def __hash__(self) -> int: ...
    def side(self) -> IdealSide: ...
    def __mul__(self, other: Ideal_nc | Ring) -> Ideal_nc | Parent: ...
