from typing import Protocol, Self, TypeVar

from sage.symbolic.expression import Expression, SymbolicInput


class Simplifiable(Protocol):
    def simplify(self, *args: SymbolicInput, **kwds: SymbolicInput) -> Self: ...


class Differentiable(Protocol):
    def derivative(self, *args: SymbolicInput, **kwds: SymbolicInput) -> Self: ...


class Integrable(Protocol):
    def integral(self, *args: SymbolicInput, **kwds: SymbolicInput) -> Self: ...


class Expandable(Protocol):
    def expand(self, *args: SymbolicInput, **kwds: SymbolicInput) -> Self: ...


_SimplifiableT = TypeVar("_SimplifiableT", bound=Simplifiable)
_DifferentiableT = TypeVar("_DifferentiableT", bound=Differentiable)
_IntegrableT = TypeVar("_IntegrableT", bound=Integrable)
_ExpandableT = TypeVar("_ExpandableT", bound=Expandable)


def simplify(
    f: _SimplifiableT,
    algorithm: str = "maxima",
    **kwds: SymbolicInput,
) -> _SimplifiableT: ...
def derivative(
    f: _DifferentiableT | SymbolicInput,
    *args: SymbolicInput,
    **kwds: SymbolicInput,
) -> _DifferentiableT | Expression: ...
diff = derivative
def integral(
    f: _IntegrableT | SymbolicInput,
    *args: SymbolicInput,
    **kwds: SymbolicInput,
) -> _IntegrableT | Expression: ...
integrate = integral
def limit(
    f: SymbolicInput,
    dir: str | None = None,
    taylor: bool = False,
    **argv: SymbolicInput,
) -> Expression: ...
lim = limit
def taylor(f: SymbolicInput, *args: SymbolicInput) -> Expression: ...
def expand(
    x: _ExpandableT | SymbolicInput,
    *args: SymbolicInput,
    **kwds: SymbolicInput,
) -> _ExpandableT | Expression: ...
