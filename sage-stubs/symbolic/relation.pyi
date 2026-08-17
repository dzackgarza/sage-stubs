from collections.abc import Sequence
from typing import Literal, overload

from sage.rings.integer import Integer
from sage.structure.sequence import Sequence_generic
from sage.symbolic.expression import Expression, SymbolicDomain


type Equation = Expression
type Variable = Expression
type Solution = Expression | dict[Expression, Expression]
type ModularSolution = tuple[Integer, ...] | dict[Expression, Integer]
type InequalitySolution = list[Expression] | tuple[Expression, Expression] | list[tuple[Expression, Expression]]


def check_relation_maxima(relation: Equation) -> bool | Equation: ...
def check_relation_maxima_neq_as_not_eq(relation: Equation) -> bool: ...
def string_to_list_of_solutions(s: str) -> Sequence_generic: ...


@overload
def solve(
    f: Equation | Sequence[Equation],
    *args: Variable | Sequence[Variable],
    explicit_solutions: bool | None = None,
    multiplicities: Literal[True],
    to_poly_solve: bool | Literal["force"] | None = None,
    solution_dict: bool = False,
    algorithm: str | None = None,
    domain: SymbolicDomain | None = None,
) -> tuple[list[Expression], list[Integer]]: ...
@overload
def solve(
    f: Equation | Sequence[Equation],
    *args: Variable | Sequence[Variable],
    explicit_solutions: bool | None = None,
    multiplicities: Literal[False] | None = None,
    to_poly_solve: bool | Literal["force"] | None = None,
    solution_dict: Literal[True],
    algorithm: str | None = None,
    domain: SymbolicDomain | None = None,
) -> list[dict[Expression, Expression]]: ...
@overload
def solve(
    f: Equation | Sequence[Equation],
    *args: Variable | Sequence[Variable],
    explicit_solutions: bool | None = None,
    multiplicities: Literal[False] | None = None,
    to_poly_solve: bool | Literal["force"] | None = None,
    solution_dict: Literal[False] = False,
    algorithm: str | None = None,
    domain: SymbolicDomain | None = None,
) -> list[Expression] | list[list[Expression]]: ...


@overload
def solve_mod(
    eqns: Equation | Sequence[Equation],
    modulus: int | Integer,
    solution_dict: Literal[False] = False,
) -> list[tuple[Integer, ...]]: ...
@overload
def solve_mod(
    eqns: Equation | Sequence[Equation],
    modulus: int | Integer,
    solution_dict: Literal[True],
) -> list[dict[Expression, Integer]]: ...


def solve_ineq_univar(ineq: Equation) -> InequalitySolution: ...
def solve_ineq_fourier(
    ineq: Equation | Sequence[Equation],
    vars: Sequence[Variable] | None = None,
) -> InequalitySolution: ...
def solve_ineq(
    ineq: Equation | Sequence[Equation],
    vars: Sequence[Variable] | None = None,
) -> InequalitySolution: ...
