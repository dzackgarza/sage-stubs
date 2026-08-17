from collections.abc import Sequence

from sage.categories.pushout import ConstructionFunctor
from sage.structure.parent import Parent
from sage.structure.factory import UniqueFactory
from sage.symbolic.expression import Expression, SymbolicInput
from sage.symbolic.ring import SymbolicRing


type CallableArguments = tuple[Expression, ...]
type CallableArgumentInput = Sequence[Expression] | tuple[Sequence[Expression]]


class CallableSymbolicExpressionFunctor(ConstructionFunctor):
    rank: int

    def __init__(self, arguments: CallableArguments) -> None: ...
    def __repr__(self) -> str: ...
    def merge(
        self,
        other: CallableSymbolicExpressionFunctor,
    ) -> CallableSymbolicExpressionFunctor: ...
    def __call__(self, R: SymbolicRing) -> CallableSymbolicExpressionRing_class: ...
    def arguments(self) -> CallableArguments: ...
    def unify_arguments(
        self,
        x: CallableSymbolicExpressionFunctor,
    ) -> CallableArguments: ...


class CallableSymbolicExpressionRing_class(SymbolicRing):
    symbols: Parent

    def __init__(self, arguments: CallableArguments) -> None: ...
    def _coerce_map_from_(self, R: Parent) -> bool: ...
    def construction(
        self,
    ) -> tuple[CallableSymbolicExpressionFunctor, SymbolicRing]: ...
    def _element_constructor_(self, x: SymbolicInput) -> Expression: ...
    def _repr_(self) -> str: ...
    def arguments(self) -> CallableArguments: ...
    def args(self) -> CallableArguments: ...
    def _repr_element_(self, x: Expression) -> str: ...
    def _latex_element_(self, x: Expression) -> str: ...
    def _call_element_(
        self,
        element: Expression,
        *args: SymbolicInput,
        **kwds: SymbolicInput,
    ) -> Expression: ...


class CallableSymbolicExpressionRingFactory(UniqueFactory):
    def create_key(
        self,
        args: CallableArgumentInput,
        check: bool = True,
    ) -> CallableArguments: ...
    def create_object(
        self,
        version: int,
        key: CallableArguments,
        **extra_args: SymbolicInput,
    ) -> CallableSymbolicExpressionRing_class: ...


CallableSymbolicExpressionRing: CallableSymbolicExpressionRingFactory
