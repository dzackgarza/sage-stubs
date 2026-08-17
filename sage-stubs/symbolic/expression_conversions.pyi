from collections.abc import Mapping, Sequence
from typing import Generic, Protocol, TypeVar, overload

from sage.ext.fast_callable import Expression as FastExpression
from sage.ext.fast_callable import ExpressionTreeBuilder
from sage.interfaces.expect import Expect
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.ring import Ring
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.symbolic.constants import Constant
from sage.symbolic.expression import (
    Expression,
    SymbolicInput,
    SymbolicOperator,
)
from sage.symbolic.function import Function


_Result = TypeVar("_Result")
_RingElement = TypeVar("_RingElement", bound=Element)
type SymbolicPyObject = (
    Element
    | Constant
    | int
    | float
    | complex
    | bool
    | str
    | tuple[SymbolicPyObject, ...]
)
type FakeOperand = Expression | FakeExpression | SymbolicPyObject


class SymbolicRelationOperator(Protocol):
    def __call__(
        self,
        left: SymbolicInput,
        right: SymbolicInput,
    ) -> bool | Expression: ...


class SymbolicDerivativeOperator(SymbolicOperator, Protocol):
    _parameter_set: Sequence[int]

    def function(self) -> Function: ...
    def parameter_set(self) -> Sequence[int]: ...
    def change_function(self, function: Function) -> SymbolicDerivativeOperator: ...


class FakeExpression:
    def __init__(
        self,
        operands: Sequence[FakeOperand],
        operator: SymbolicOperator,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def pyobject(self) -> None: ...
    def operands(self) -> list[FakeOperand]: ...
    def __getitem__(self, i: int) -> FakeOperand: ...
    def operator(self) -> SymbolicOperator: ...
    def _fast_callable_(self, etb: ExpressionTreeBuilder) -> FastExpression: ...


class Converter(Generic[_Result]):
    use_fake_div: bool
    ex: Expression

    def __init__(self, use_fake_div: bool = False) -> None: ...
    def __call__(self, ex: Expression | None = None) -> _Result: ...
    def get_fake_div(self, ex: Expression) -> FakeExpression | Expression: ...
    def pyobject(self, ex: Expression, obj: SymbolicPyObject) -> _Result: ...
    def symbol(self, ex: Expression) -> _Result: ...
    def relation(
        self,
        ex: Expression,
        operator: SymbolicRelationOperator,
    ) -> _Result: ...
    def derivative(
        self,
        ex: Expression,
        operator: SymbolicDerivativeOperator,
    ) -> _Result: ...
    def arithmetic(self, ex: Expression, operator: SymbolicOperator) -> _Result: ...
    def composition(self, ex: Expression, operator: SymbolicOperator) -> _Result: ...


class InterfaceInit(Converter[str]):
    name_init: str
    interface: Expect
    relation_symbols: Mapping[SymbolicRelationOperator, str]

    def __init__(self, interface: Expect) -> None: ...
    def symbol(self, ex: Expression) -> str: ...
    def pyobject(self, ex: Expression, obj: SymbolicPyObject) -> str: ...
    def relation(
        self,
        ex: Expression,
        operator: SymbolicRelationOperator,
    ) -> str: ...
    def tuple(self, ex: Expression) -> str: ...
    def derivative(
        self,
        ex: Expression,
        operator: SymbolicDerivativeOperator,
    ) -> str: ...
    def arithmetic(self, ex: Expression, operator: SymbolicOperator) -> str: ...
    def composition(self, ex: Expression, operator: SymbolicOperator) -> str: ...


class FriCASConverter(InterfaceInit):
    def __init__(self) -> None: ...
    def pyobject(self, ex: Expression, obj: SymbolicPyObject) -> str: ...
    def symbol(self, ex: Expression) -> str: ...
    def derivative(
        self,
        ex: Expression,
        operator: SymbolicDerivativeOperator,
    ) -> str: ...


fricas_converter: FriCASConverter


class PolynomialConverter(Converter[Element]):
    ring: Parent[Element]
    base_ring: Parent[Element]

    def __init__(
        self,
        ex: Expression,
        base_ring: Ring | None = None,
        ring: MPolynomialRing_base | None = None,
    ) -> None: ...
    def symbol(self, ex: Expression) -> Element: ...
    def pyobject(self, ex: Expression, obj: SymbolicPyObject) -> Element: ...
    def composition(self, ex: Expression, operator: SymbolicOperator) -> Element: ...
    def relation(
        self,
        ex: Expression,
        op: SymbolicRelationOperator,
    ) -> Element: ...
    def arithmetic(self, ex: Expression, operator: SymbolicOperator) -> Element: ...


def polynomial(
    ex: Expression,
    base_ring: Ring | None = None,
    ring: MPolynomialRing_base | None = None,
) -> Element: ...


class LaurentPolynomialConverter(PolynomialConverter):
    def __init__(
        self,
        ex: Expression,
        base_ring: Ring | None = None,
        ring: MPolynomialRing_base | None = None,
    ) -> None: ...


def laurent_polynomial(
    ex: Expression,
    base_ring: Ring | None = None,
    ring: MPolynomialRing_base | None = None,
) -> LaurentPolynomial: ...


class FastCallableConverter(Converter[FastExpression]):
    def __init__(self, ex: Expression, etb: ExpressionTreeBuilder) -> None: ...
    def pyobject(
        self,
        ex: Expression,
        obj: SymbolicPyObject,
    ) -> FastExpression: ...
    def relation(
        self,
        ex: Expression,
        operator: SymbolicRelationOperator,
    ) -> FastExpression: ...
    def arithmetic(
        self,
        ex: Expression,
        operator: SymbolicOperator,
    ) -> FastExpression: ...
    def symbol(self, ex: Expression) -> FastExpression: ...
    def composition(
        self,
        ex: Expression,
        function: SymbolicOperator,
    ) -> FastExpression: ...
    def tuple(self, ex: Expression) -> list[Expression]: ...


def fast_callable(ex: Expression, etb: ExpressionTreeBuilder) -> FastExpression: ...


class RingConverter(Converter[_RingElement], Generic[_RingElement]):
    def __init__(
        self,
        R: Parent[_RingElement],
        subs_dict: Mapping[Expression, _RingElement] | None = None,
    ) -> None: ...
    def symbol(self, ex: Expression) -> _RingElement: ...
    def pyobject(self, ex: Expression, obj: SymbolicPyObject) -> _RingElement: ...
    def arithmetic(
        self,
        ex: Expression,
        operator: SymbolicOperator,
    ) -> _RingElement: ...
    def composition(
        self,
        ex: Expression,
        operator: SymbolicOperator,
    ) -> _RingElement: ...


class ExpressionTreeWalker(Converter[Expression]):
    def __init__(self, ex: Expression) -> None: ...
    def symbol(self, ex: Expression) -> Expression: ...
    def pyobject(self, ex: Expression, obj: SymbolicPyObject) -> Expression: ...
    def relation(
        self,
        ex: Expression,
        operator: SymbolicRelationOperator,
    ) -> Expression: ...
    def arithmetic(
        self,
        ex: Expression,
        operator: SymbolicOperator,
    ) -> Expression: ...
    def composition(
        self,
        ex: Expression,
        operator: SymbolicOperator,
    ) -> Expression: ...
    def derivative(
        self,
        ex: Expression,
        operator: SymbolicDerivativeOperator,
    ) -> Expression: ...
    def tuple(self, ex: Expression) -> list[Expression]: ...


class SubstituteFunction(ExpressionTreeWalker):
    substitutions: Mapping[Function, Function]

    @overload
    def __init__(
        self,
        ex: Expression,
        substitutions: Mapping[Function, Function],
    ) -> None: ...
    @overload
    def __init__(
        self,
        ex: Expression,
        old: Function,
        new: Function,
    ) -> None: ...
    def composition(
        self,
        ex: Expression,
        operator: SymbolicOperator,
    ) -> Expression: ...
    def derivative(
        self,
        ex: Expression,
        operator: SymbolicDerivativeOperator,
    ) -> Expression: ...


class Exponentialize(ExpressionTreeWalker):
    CircDict: Mapping[Function, SymbolicOperator]
    Circs: Sequence[Function]

    def __init__(self, ex: Expression) -> None: ...
    def composition(
        self,
        ex: Expression,
        op: SymbolicOperator,
    ) -> Expression: ...


class DeMoivre(ExpressionTreeWalker):
    def __init__(self, ex: Expression, force: bool = False) -> None: ...
    def composition(
        self,
        ex: Expression,
        op: SymbolicOperator,
    ) -> Expression: ...


class HalfAngle(ExpressionTreeWalker):
    HalvesDict: Mapping[Function, SymbolicOperator]
    Halves: Sequence[Function]

    def __init__(self, ex: Expression) -> None: ...
    def composition(
        self,
        ex: Expression,
        op: SymbolicOperator,
    ) -> Expression: ...


class HoldRemover(ExpressionTreeWalker):
    def __init__(
        self,
        ex: Expression,
        exclude: Sequence[SymbolicOperator] | None = None,
    ) -> None: ...
    def composition(
        self,
        ex: Expression,
        operator: SymbolicOperator,
    ) -> Expression: ...
