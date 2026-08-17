from collections.abc import Iterator, Sequence

from sage.rings.integer import Integer
from sage.symbolic.expression import Expression
from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionKeyword, FunctionResult


type HypergeometricParameter = FunctionArgument
type HypergeometricParameters = Sequence[HypergeometricParameter]
type RationalParameter = HypergeometricParameter | tuple[int, int]


def rational_param_as_tuple(x: HypergeometricParameter) -> RationalParameter: ...


class Hypergeometric(BuiltinFunction):
    def __init__(self) -> None: ...
    def __call__(
        self,
        a: HypergeometricParameters,
        b: HypergeometricParameters,
        z: FunctionArgument,
        **kwargs: FunctionKeyword,
    ) -> FunctionResult: ...

    class EvaluationMethods:
        def sorted_parameters(
            self,
            a: tuple[Expression, ...],
            b: tuple[Expression, ...],
            z: Expression,
        ) -> Expression: ...
        def eliminate_parameters(
            self,
            a: tuple[Expression, ...],
            b: tuple[Expression, ...],
            z: Expression,
        ) -> Expression: ...
        def is_termwise_finite(
            self,
            a: tuple[Expression, ...],
            b: tuple[Expression, ...],
            z: Expression,
        ) -> bool: ...
        def is_terminating(
            self,
            a: tuple[Expression, ...],
            b: tuple[Expression, ...],
            z: Expression,
        ) -> bool: ...
        def is_absolutely_convergent(
            self,
            a: tuple[Expression, ...],
            b: tuple[Expression, ...],
            z: Expression,
        ) -> bool: ...
        def terms(
            self,
            a: tuple[Expression, ...],
            b: tuple[Expression, ...],
            z: Expression,
            n: int | Integer | None = None,
        ) -> Iterator[Expression]: ...
        def deflated(
            self,
            a: tuple[Expression, ...],
            b: tuple[Expression, ...],
            z: Expression,
        ) -> Expression: ...


hypergeometric: Hypergeometric


def closed_form(hyp: Expression) -> Expression: ...


class Hypergeometric_M(BuiltinFunction):
    def __init__(self) -> None: ...

    class EvaluationMethods:
        def generalized(
            self,
            a: Expression,
            b: Expression,
            z: Expression,
        ) -> Expression: ...


hypergeometric_M: Hypergeometric_M


class Hypergeometric_U(BuiltinFunction):
    def __init__(self) -> None: ...

    class EvaluationMethods:
        def generalized(
            self,
            a: Expression,
            b: Expression,
            z: Expression,
        ) -> Expression: ...


hypergeometric_U: Hypergeometric_U
