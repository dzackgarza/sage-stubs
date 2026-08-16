from collections.abc import Callable

from sage.modular.arithgroup.congruence_subgroup import CongruenceSubgroup
from sage.modular.dirichlet import DirichletCharacter
from sage.modular.modsym.ambient import ModularSymbolsAmbient
from sage.rings.commutative_ring import CommutativeRing
from sage.rings.integer import Integer
from sage.structure.parent import Parent

def canonical_parameters(
    self, weight: int | Integer, sign: int | Integer, base_ring: CommutativeRing | None
) -> tuple[
    CongruenceSubgroup | tuple[DirichletCharacter, Parent],
    Integer,
    Integer,
    CommutativeRing,
]: ...
def ModularSymbols_clear_cache(self) -> None: ...
def ModularSymbols(
    self=1,
    weight: int | Integer = 2,
    sign: int | Integer = 0,
    base_ring: CommutativeRing | None = None,
    use_cache: bool = True,
    custom_init: Callable[[ModularSymbolsAmbient], None] | None = None,
) -> ModularSymbolsAmbient: ...
