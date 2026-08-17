from collections.abc import Sequence
from types import TracebackType
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.expression import Expression, SymbolicSubstitution


type AssumptionFeature = str
type Assumption = Expression | GenericDeclaration
type AssumptionInput = Assumption | tuple[Expression, ..., AssumptionFeature] | list[Expression | AssumptionFeature]


class GenericDeclaration(UniqueRepresentation):
    def __init__(self, var: Expression, assumption: AssumptionFeature) -> None: ...
    def __repr__(self) -> str: ...
    def has(self, arg: Expression) -> bool: ...
    def assume(self) -> None: ...
    def forget(self) -> None: ...
    def contradicts(
        self, soln: SymbolicSubstitution | Expression
    ) -> bool: ...


def preprocess_assumptions(
    args: Sequence[Assumption | AssumptionFeature | Sequence[Expression | AssumptionFeature]],
) -> Sequence[Assumption | list[Expression | AssumptionFeature]]: ...
def assume(*args: Assumption | AssumptionFeature | Sequence[Expression | AssumptionFeature]) -> None: ...
def forget(*args: Assumption | AssumptionFeature | Sequence[Expression | AssumptionFeature]) -> None: ...
def assumptions(*args: Expression) -> list[Assumption]: ...


class assuming:
    Ass: tuple[Assumption | AssumptionFeature | Sequence[Expression | AssumptionFeature], ...]
    replace: bool
    def __init__(
        self,
        *args: Assumption | AssumptionFeature | Sequence[Expression | AssumptionFeature],
        replace: bool = False,
    ) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ) -> None: ...
