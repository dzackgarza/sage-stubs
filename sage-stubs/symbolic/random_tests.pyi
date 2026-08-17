from collections.abc import Callable, Sequence

from sage.structure.element import Element
from sage.symbolic.expression import Expression, SymbolicInput
from sage.symbolic.function import Function


type ProbabilityWeight = int | float
type ProbabilityMetadata = int | str
type RandomExpressionOperator = Callable[..., SymbolicInput]
type RandomExpressionValue = Expression | Element | int | float | complex
type ProbabilityEntry[T] = tuple[
    ProbabilityWeight,
    T,
    *tuple[ProbabilityMetadata, ...],
]
type NormalizedProbabilityEntry[T] = tuple[
    float,
    T,
    *tuple[ProbabilityMetadata, ...],
]
type ProbabilityList[T] = list[ProbabilityEntry[T]]
type NormalizedProbabilityList[T] = list[NormalizedProbabilityEntry[T]]
type UnaryOperatorChoice = ProbabilityEntry[Callable[[SymbolicInput], SymbolicInput]]
type BinaryOperatorChoice = ProbabilityEntry[
    Callable[[SymbolicInput, SymbolicInput], SymbolicInput]
]
type FunctionChoice = tuple[ProbabilityWeight, Function, int]
type OperatorChoice = tuple[ProbabilityWeight, RandomExpressionOperator, int]
type LeafChoice = ProbabilityEntry[RandomExpressionValue]
type NestedOperatorChoice = ProbabilityEntry[
    Sequence[OperatorChoice | FunctionChoice | UnaryOperatorChoice | BinaryOperatorChoice]
]
type InternalProbabilityList = list[
    OperatorChoice | NestedOperatorChoice | FunctionChoice
]


fast_binary: list[BinaryOperatorChoice]
fast_unary: list[UnaryOperatorChoice]
fast_nodes: InternalProbabilityList
full_binary: list[BinaryOperatorChoice]
full_unary: list[UnaryOperatorChoice]
full_functions: list[FunctionChoice]
full_nullary: ProbabilityList[RandomExpressionValue]
full_internal: InternalProbabilityList


def normalize_prob_list[T](
    pl: Sequence[ProbabilityEntry[T] | ProbabilityEntry[Sequence[ProbabilityEntry[T]]]],
    extra: tuple[ProbabilityMetadata, ...] = (),
) -> NormalizedProbabilityList[T]: ...

def choose_from_prob_list[T](
    lst: Sequence[NormalizedProbabilityEntry[T] | ProbabilityEntry[T]],
) -> NormalizedProbabilityEntry[T] | ProbabilityEntry[T]: ...

def random_integer_vector(n: int, length: int) -> list[int]: ...

def random_expr_helper(
    n_nodes: int,
    internal: Sequence[OperatorChoice],
    leaves: Sequence[ProbabilityEntry[RandomExpressionValue]],
    verbose: bool,
) -> SymbolicInput: ...

def random_expr(
    size: int,
    nvars: int = 1,
    ncoeffs: int | None = None,
    var_frac: float = 0.5,
    internal: InternalProbabilityList = full_internal,
    nullary: ProbabilityList[RandomExpressionValue] = full_nullary,
    nullary_frac: float = 0.2,
    coeff_generator: Callable[[], RandomExpressionValue] = ...,
    verbose: bool = False,
) -> SymbolicInput: ...

def assert_strict_weak_order[T](
    a: T,
    b: T,
    c: T,
    cmp_func: Callable[[T, T], bool],
) -> None: ...

def check_symbolic_expression_order(repetitions: int = 1000) -> None: ...
