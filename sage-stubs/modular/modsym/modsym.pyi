from typing import TYPE_CHECKING

from sage.rings.commutative_ring import CommutativeRing
from sage.rings.integer import Integer
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from sage.modular.arithgroup.congruence_subgroup import CongruenceSubgroup
    from sage.modular.dirichlet import DirichletCharacter
    from sage.modular.modsym.ambient import ModularSymbolsAmbient

def canonical_parameters(
    group: int | CongruenceSubgroup | DirichletCharacter,
    weight: int | Integer,
    sign: int | Integer,
    base_ring: CommutativeRing | None,
) -> tuple[CongruenceSubgroup | tuple[DirichletCharacter, Parent], Integer, Integer, CommutativeRing]:
    """
    Return canonically normalized parameters for modular symbols.
    """
    ...

def ModularSymbols_clear_cache() -> None:
    """
    Clear the global cache of modular symbols spaces.
    """
    ...

def ModularSymbols(
    group: int | CongruenceSubgroup | DirichletCharacter = 1,
    weight: int | Integer = 2,
    sign: int | Integer = 0,
    base_ring: CommutativeRing | None = None,
    use_cache: bool = True,
    custom_init: callable | None = None,
) -> ModularSymbolsAmbient:
    """
    Create an ambient space of modular symbols.
    """
    ...
