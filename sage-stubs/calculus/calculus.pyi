from collections.abc import Callable, Mapping

from sage.interfaces.maxima import Maxima
from sage.misc.parser import LookupNameMaker, Parser
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element
from sage.symbolic.expression import Expression, SymbolicInput, SymbolicSubstitution
from sage.symbolic.function import Function


type SymbolicAlgorithm = str
type LimitDirection = str | None
type SymbolicParseAtom = Expression | Element | int | float | complex | bool | str

type SymbolicParseResult = (
    SymbolicParseAtom
    | list[SymbolicParseResult]
    | tuple[SymbolicParseResult, ...]
)
type SymbolTableValue = Expression | Function | Callable[..., Expression]
type SymbolTable = Mapping[tuple[str, int], SymbolTableValue]
type MaximaOption = str | bool | int | float | Expression


def symbolic_sum(
    expression: SymbolicInput,
    v: Expression,
    a: SymbolicInput,
    b: SymbolicInput,
    algorithm: SymbolicAlgorithm = "maxima",
    hold: bool = False,
) -> Expression: ...
def nintegral(
    ex: SymbolicInput,
    x: Expression,
    a: SymbolicInput,
    b: SymbolicInput,
    desired_relative_error: str | float = "1e-8",
    maximum_num_subintervals: int = 200,
) -> tuple[float, float, Integer, Integer]: ...
nintegrate = nintegral
def symbolic_product(
    expression: SymbolicInput,
    v: Expression,
    a: SymbolicInput,
    b: SymbolicInput,
    algorithm: SymbolicAlgorithm = "maxima",
    hold: bool = False,
) -> Expression: ...
def minpoly(
    ex: SymbolicInput,
    var: str = "x",
    algorithm: str | None = None,
    bits: int | None = None,
    degree: int | None = None,
    epsilon: SymbolicInput = 0,
) -> Polynomial: ...
def limit(
    ex: SymbolicInput,
    *args: SymbolicInput,
    dir: LimitDirection = None,
    taylor: bool = False,
    algorithm: SymbolicAlgorithm = "maxima",
    **kwargs: SymbolicInput,
) -> Expression: ...
lim = limit
def mma_free_limit(
    expression: SymbolicInput,
    v: Expression,
    a: SymbolicInput,
    dir: LimitDirection = None,
) -> Expression: ...
def laplace(
    ex: SymbolicInput,
    t: Expression,
    s: Expression,
    algorithm: SymbolicAlgorithm = "maxima",
) -> Expression: ...
def inverse_laplace(
    ex: SymbolicInput,
    s: Expression,
    t: Expression,
    algorithm: SymbolicAlgorithm = "maxima",
) -> Expression: ...
def at(
    ex: Expression,
    *args: SymbolicSubstitution,
    **kwds: SymbolicInput,
) -> Expression: ...
def dummy_diff(*args: SymbolicInput) -> Expression: ...
def dummy_integrate(*args: SymbolicInput) -> Expression: ...
def dummy_laplace(*args: SymbolicInput) -> Expression: ...
def dummy_inverse_laplace(*args: SymbolicInput) -> Expression: ...
def dummy_pochhammer(*args: SymbolicInput) -> Expression: ...
def symbolic_expression_from_maxima_string(
    x: str | Expression,
    equals_sub: bool = False,
    maxima: Maxima = ...,
) -> SymbolicParseResult: ...
def mapped_opts(v: MaximaOption) -> str: ...
def maxima_options(**kwds: MaximaOption) -> str: ...
def symbolic_expression_from_string(
    s: str,
    syms: SymbolTable | None = None,
    accept_sequence: bool = False,
    *,
    parser: Parser | None = None,
) -> SymbolicParseResult: ...


syms_cur: dict[str, SymbolTableValue]
syms_default: dict[str, SymbolTableValue]
parser_make_var: LookupNameMaker
parser_make_function: LookupNameMaker
SR_parser: Parser
parser_make_Mvar: LookupNameMaker
SRM_parser: Parser
SR_parser_giac: Parser
