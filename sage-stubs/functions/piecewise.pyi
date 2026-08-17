from collections.abc import Callable, Iterable, Sequence
from sage.ext.fast_callable import Expression as FastExpression
from sage.ext.fast_callable import ExpressionTreeBuilder
from sage.sets.real_set import RealSet
from sage.structure.element import Element
from sage.symbolic.expression import Expression, SymbolicInput
from sage.symbolic.function import BuiltinFunction, FunctionKeyword
from sympy.functions.elementary.piecewise import Piecewise as SympyPiecewise


type PieceExpression = Expression | Callable[[Expression], SymbolicInput]
type Piece = tuple[RealSet, PieceExpression]
type PieceParameters = Sequence[Expression]


class PiecewiseFunction(BuiltinFunction):
    def __init__(self) -> None: ...
    def __call__(
        self,
        function_pieces: Iterable[Piece],
        **kwds: FunctionKeyword,
    ) -> Expression: ...
    @staticmethod
    def in_operands(ex: Expression) -> bool: ...
    @staticmethod
    def simplify(ex: Expression) -> Expression: ...

    class EvaluationMethods:
        def __pow__(
            self,
            parameters: PieceParameters,
            variable: Expression,
            n: SymbolicInput,
        ) -> Expression: ...
        def expression_at(
            self,
            parameters: PieceParameters,
            variable: Expression,
            point: SymbolicInput,
        ) -> Expression: ...
        def domains(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> list[RealSet]: ...
        def domain(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> RealSet: ...
        def __len__(self, parameters: PieceParameters, variable: Expression) -> int: ...
        def expressions(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> list[Expression]: ...
        def items(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> list[tuple[RealSet, Expression]]: ...
        def __call__(
            self,
            parameters: PieceParameters,
            variable: Expression,
            value: SymbolicInput | None = None,
            **kwds: FunctionKeyword,
        ) -> Expression: ...
        def _fast_callable_(
            self,
            parameters: PieceParameters,
            variable: Expression,
            etb: ExpressionTreeBuilder,
        ) -> FastExpression: ...
        def restriction(
            self,
            parameters: PieceParameters,
            variable: Expression,
            restricted_domain: RealSet,
        ) -> Expression: ...
        def extension(
            self,
            parameters: PieceParameters,
            variable: Expression,
            extension: PieceExpression,
            extension_domain: RealSet | None = None,
        ) -> Expression: ...
        def unextend_zero(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> Expression: ...
        def pieces(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> list[Expression]: ...
        def end_points(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> list[Element]: ...
        def piecewise_add(
            self,
            parameters: PieceParameters,
            variable: Expression,
            other: Expression,
        ) -> Expression: ...
        def integral(
            self,
            parameters: PieceParameters,
            variable: Expression,
            x: Expression | None = None,
            a: SymbolicInput | None = None,
            b: SymbolicInput | None = None,
            definite: bool = False,
            **kwds: FunctionKeyword,
        ) -> Expression: ...
        def critical_points(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> list[Expression]: ...
        def convolution(
            self,
            parameters: PieceParameters,
            variable: Expression,
            other: Expression,
        ) -> Expression: ...
        def trapezoid(
            self,
            parameters: PieceParameters,
            variable: Expression,
            N: int,
        ) -> Expression: ...
        def laplace(
            self,
            parameters: PieceParameters,
            variable: Expression,
            x: Expression | str = "x",
            s: Expression | str = "t",
        ) -> Expression: ...
        def fourier_series_cosine_coefficient(
            self,
            parameters: PieceParameters,
            variable: Expression,
            n: int,
            L: SymbolicInput | None = None,
        ) -> Expression: ...
        def fourier_series_sine_coefficient(
            self,
            parameters: PieceParameters,
            variable: Expression,
            n: int,
            L: SymbolicInput | None = None,
        ) -> Expression: ...
        def fourier_series_partial_sum(
            self,
            parameters: PieceParameters,
            variable: Expression,
            N: int,
            L: SymbolicInput | None = None,
        ) -> Expression: ...
        def _sympy_(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> SympyPiecewise: ...
        def _giac_init_(
            self,
            parameters: PieceParameters,
            variable: Expression,
        ) -> str: ...


piecewise: PiecewiseFunction
