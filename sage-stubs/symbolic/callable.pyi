from collections.abc import Callable

from sage.categories.pushout import ConstructionFunctor
from sage.structure.element import Element
from sage.structure.factory import (
    FactoryArgument,
    FactoryCacheKey,
    FactoryVersion,
    UniqueFactory,
)
from sage.structure.parent import Parent
from sage.structure.sage_object import SageCoercionAtom
from sage.symbolic.expression import Expression
from sage.symbolic.ring import SymbolicRing

type CallableArguments = tuple[Expression, ...]

class CallableSymbolicExpressionFunctor(ConstructionFunctor):
    rank: int

    def __init__(self, arguments: CallableArguments) -> None: ...
    def merge(
        self, other: ConstructionFunctor
    ) -> CallableSymbolicExpressionFunctor | None: ...
    def __call__(self, R: SymbolicRing) -> CallableSymbolicExpressionRing_class: ...
    def arguments(self) -> CallableArguments: ...
    def unify_arguments(
        self, x: CallableSymbolicExpressionFunctor
    ) -> CallableArguments: ...

class CallableSymbolicExpressionRing_class(SymbolicRing):
    def __init__(self, arguments: CallableArguments | Parent | None) -> None: ...
    def _coerce_map_from_(self, R: Parent) -> bool: ...
    def construction(
        self,
    ) -> tuple[CallableSymbolicExpressionFunctor, tuple[SymbolicRing]]: ...
    def _element_constructor_(self, x: SageCoercionAtom) -> Element: ...
    def _repr_(self) -> str: ...
    def arguments(self) -> CallableArguments: ...
    args: Callable[[], CallableArguments]

    def _repr_element_(self, x: Element) -> str: ...
    def _latex_element_(self, x: Element) -> str: ...
    def _call_element_(
        self, element: Element, *args: Element, **kwds: Element
    ) -> Element: ...

class CallableSymbolicExpressionRingFactory(UniqueFactory):
    def create_key(
        self, *args: FactoryArgument, **kwds: FactoryArgument
    ) -> FactoryCacheKey: ...
    def create_object(
        self,
        version: FactoryVersion,
        key: FactoryCacheKey,
        **extra_args: FactoryArgument,
    ) -> CallableSymbolicExpressionRing_class: ...

CallableSymbolicExpressionRing: CallableSymbolicExpressionRingFactory
