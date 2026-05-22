from typing import TYPE_CHECKING, Callable
from sage.structure.sage_object import SageObject
from sage.combinat.root_system.cartan_type import CartanType

if TYPE_CHECKING:
    from sage.combinat.root_system.weyl_characters import WeylCharacter
    from sage.modules.free_module_element import vector as FreeModuleElement

class BranchingRule(SageObject):
    _R: CartanType
    _S: CartanType
    _f: Callable[[list[int]], list[int] | tuple[int, ...]]
    _name: str
    _intermediate_types: list[CartanType]
    _intermediate_names: list[str]

    def __init__(
        self,
        R: CartanType | str,
        S: CartanType | str,
        f: Callable[[list[int]], list[int] | tuple[int, ...]],
        name: str = ...,
        intermediate_types: list[CartanType] | None = ...,
        intermediate_names: list[str] | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __call__(self, x: list[int] | FreeModuleElement) -> list[int] | tuple[int, ...]: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: BranchingRule) -> bool: ...
    def __mul__(self, other: BranchingRule) -> BranchingRule: ...
    def Rtype(self) -> CartanType: ...
    def Stype(self) -> CartanType: ...
    def describe(
        self, verbose: bool = ..., debug: bool = ..., no_r: bool = ...
    ) -> None: ...
    def branch(self, chi: WeylCharacter, style: str | None = ...) -> WeylCharacter: ...

def branch_weyl_character(
    chi: WeylCharacter,
    R: CartanType | str,
    S: CartanType | str,
    rule: str | BranchingRule = ...,
) -> WeylCharacter: ...

def branching_rule(
    Rtype: CartanType | str,
    Stype: CartanType | str,
    rule: str | BranchingRule | list[BranchingRule | str] = ...,
) -> BranchingRule: ...

def branching_rule_from_plethysm(
    chi: WeylCharacter,
    Rtype: CartanType | str,
) -> BranchingRule: ...
