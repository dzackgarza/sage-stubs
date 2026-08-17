from collections.abc import Iterable
from typing import ClassVar, Literal

from sage.categories.pushout import ConstructionFunctor
from sage.structure.factory import FactoryArgument, FactoryVersion, UniqueFactory
from sage.symbolic.expression import Expression
from sage.symbolic.ring import SymbolicRing


type SymbolicVariableCollection = Iterable[Expression | str]
type SymbolicVariableSet = frozenset[Expression]
type SymbolicSubringClass = type[GenericSymbolicSubring]
type SymbolicSubringKey = tuple[SymbolicSubringClass, tuple[Expression | str, ...]]


class SymbolicSubringFactory(UniqueFactory):
    def create_key_and_extra_args(
        self,
        accepting_variables: SymbolicVariableCollection | None = None,
        rejecting_variables: SymbolicVariableCollection | None = None,
        no_variables: bool = False,
        **kwds: FactoryArgument,
    ) -> tuple[SymbolicSubringKey, dict[str, FactoryArgument]]: ...
    def create_object(
        self,
        version: FactoryVersion,
        key: SymbolicSubringKey,
        **kwds: FactoryArgument,
    ) -> SymbolicRing: ...


SymbolicSubring: SymbolicSubringFactory


class GenericSymbolicSubring(SymbolicRing):
    def __init__(self, vars: SymbolicVariableCollection) -> None: ...
    def has_valid_variable(self, variable: Expression | str) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...


class GenericSymbolicSubringFunctor(ConstructionFunctor):
    rank: ClassVar[int]
    coercion_reversed: ClassVar[bool]
    vars: SymbolicVariableSet
    def __init__(self, vars: SymbolicVariableCollection) -> None: ...
    def merge(
        self,
        other: GenericSymbolicSubringFunctor,
    ) -> GenericSymbolicSubringFunctor | None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...


class SymbolicSubringAcceptingVars(GenericSymbolicSubring):
    def has_valid_variable(self, variable: Expression | str) -> bool: ...
    def construction(
        self,
    ) -> tuple[SymbolicSubringAcceptingVarsFunctor, SymbolicRing]: ...


class SymbolicSubringAcceptingVarsFunctor(GenericSymbolicSubringFunctor):
    def merge(
        self,
        other: GenericSymbolicSubringFunctor,
    ) -> GenericSymbolicSubringFunctor | None: ...


class SymbolicSubringRejectingVars(GenericSymbolicSubring):
    def has_valid_variable(self, variable: Expression | str) -> bool: ...
    def construction(
        self,
    ) -> tuple[SymbolicSubringRejectingVarsFunctor, SymbolicRing]: ...


class SymbolicSubringRejectingVarsFunctor(GenericSymbolicSubringFunctor):
    def merge(
        self,
        other: GenericSymbolicSubringFunctor,
    ) -> GenericSymbolicSubringFunctor | None: ...


class SymbolicConstantsSubring(SymbolicSubringAcceptingVars):
    def has_valid_variable(self, variable: Expression | str) -> Literal[False]: ...
