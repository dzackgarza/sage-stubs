from collections.abc import Sequence

from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
from sage.rings.finite_rings.hom_prime_finite_field import FiniteFieldHomomorphism_prime
from sage.rings.homset import RingHomset_generic
from sage.rings.integer import Integer
from sage.rings.morphism import RingHomomorphism_im_gens
from sage.structure.parent import ElementConstructorInput

class FiniteFieldHomset(RingHomset_generic):
    def _repr_(self) -> str: ...
    def is_aut(self) -> bool: ...
    def order(self) -> Integer: ...
    def __len__(self) -> int: ...
    def list(self) -> list[FiniteFieldHomomorphism_generic]: ...
    def __getitem__(self, n: int) -> FiniteFieldHomomorphism_generic: ...
    def index(self, item: FiniteFieldHomomorphism_generic) -> int: ...
    def _an_element_(self) -> FiniteFieldHomomorphism_generic: ...
    def __call__(
        self,
        im_gens: Sequence[ElementConstructorInput],
        base_map: Map | Morphism | None = ...,
        check: bool = ...,
    ) -> (
        RingHomomorphism_im_gens
        | FiniteFieldHomomorphism_prime
        | FiniteFieldHomomorphism_generic
        | Sequence[ElementConstructorInput]
    ): ...
