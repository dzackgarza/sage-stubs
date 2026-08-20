from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
from numbers import Real
from typing import NamedTuple, TypeVar

from sage.combinat.finite_state_machine import Automaton, Transducer
from sage.rings.integer import Integer
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent
from sage.symbolic.expression import Expression

_Input = TypeVar("_Input", bound=Hashable)
_Output = TypeVar("_Output")
_Weight = TypeVar("_Weight", Real, RingElement)


type Alphabet[_T: Hashable] = Iterable[_T]
type RecursiveOutput = Element | int | Integer | float


class RecursionRule(NamedTuple):
    K: Integer
    r: RingElement
    k: Integer
    s: RingElement
    t: list[RecursiveOutput]


class AutomatonGenerators:
    def AnyLetter(
        self,
        input_alphabet: Alphabet[_Input],
    ) -> Automaton: ...
    def AnyWord(
        self,
        input_alphabet: Alphabet[_Input],
    ) -> Automaton: ...
    def EmptyWord(
        self,
        input_alphabet: Alphabet[_Input] | None = ...,
    ) -> Automaton: ...
    def Word(
        self,
        word: Iterable[_Input],
        input_alphabet: Alphabet[_Input] | None = ...,
    ) -> Automaton: ...
    def ContainsWord(
        self,
        word: Iterable[_Input],
        input_alphabet: Alphabet[_Input],
    ) -> Automaton: ...


class TransducerGenerators:
    RecursionRule: type[RecursionRule]

    def Identity(
        self,
        input_alphabet: Alphabet[_Input],
    ) -> Transducer: ...
    def CountSubblockOccurrences(
        self,
        block: Iterable[_Input],
        input_alphabet: Alphabet[_Input],
    ) -> Transducer: ...
    def Wait(
        self,
        input_alphabet: Alphabet[_Input],
        threshold: int = ...,
    ) -> Transducer: ...
    def map(
        self,
        f: Callable[[_Input], _Output],
        input_alphabet: Alphabet[_Input],
    ) -> Transducer: ...
    def operator(
        self,
        operator: Callable[..., _Output],
        input_alphabet: Alphabet[_Input],
        number_of_operands: int = ...,
    ) -> Transducer: ...
    def all(
        self,
        input_alphabet: Alphabet[_Input],
        number_of_operands: int = ...,
    ) -> Transducer: ...
    def any(
        self,
        input_alphabet: Alphabet[_Input],
        number_of_operands: int = ...,
    ) -> Transducer: ...
    def add(
        self,
        input_alphabet: Alphabet[_Input],
        number_of_operands: int = ...,
    ) -> Transducer: ...
    def sub(
        self,
        input_alphabet: Alphabet[_Input],
    ) -> Transducer: ...
    def weight(
        self,
        input_alphabet: Alphabet[_Input],
        zero: _Input | int = ...,
    ) -> Transducer: ...
    def abs(
        self,
        input_alphabet: Alphabet[_Input],
    ) -> Transducer: ...
    def GrayCode(self) -> Transducer: ...
    def _parse_recursion_equation_(
        self,
        equation: Expression,
        base: RingElement,
        function: Callable[..., Expression],
        var: Expression,
        word_function: Callable[..., Expression] | None = ...,
        output_rings: Sequence[Parent] = ...,
    ) -> RecursionRule | dict[RingElement, list[RecursiveOutput]]: ...
    def Recursion(
        self,
        recursions: Iterable[
            Expression
            | RecursionRule
            | tuple[RingElement | int | Integer, Sequence[RecursiveOutput]]
        ],
        base: RingElement | int | Integer,
        function: Callable[..., Expression] | None = ...,
        var: Expression | None = ...,
        input_alphabet: Iterable[RingElement | int | Integer] | None = ...,
        word_function: Callable[..., Expression] | None = ...,
        is_zero: Callable[[Sequence[RecursiveOutput]], bool] | None = ...,
        output_rings: Sequence[Parent] = ...,
    ) -> Transducer: ...


automata: AutomatonGenerators
transducers: TransducerGenerators
