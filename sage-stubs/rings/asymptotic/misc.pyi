from sage.categories.category import Category
from sage.rings.asymptotic.asymptotic_ring import AsymptoticExpansion
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject

def repr_short_to_parent(
    s: AsymptoticExpansion | ElementConstructorInput,
) -> AsymptoticExpansion: ...
def parent_to_repr_short(P: int | Integer) -> AsymptoticExpansion: ...
def split_str_by_op(
    string: Ring, op: Ring, strip_parentheses: Ring = ...
) -> AsymptoticExpansion: ...
def repr_op(
    left: AsymptoticExpansion | ElementConstructorInput,
    op: Ring,
    right: AsymptoticExpansion | ElementConstructorInput = ...,
    latex: Ring = ...,
) -> AsymptoticExpansion: ...
def combine_exceptions(
    e: int | Integer | Rational, *f: ElementConstructorInput
) -> AsymptoticExpansion: ...
def substitute_raise_exception(
    element: AsymptoticExpansion | ElementConstructorInput, e: int | Integer | Rational
) -> AsymptoticExpansion: ...
def bidirectional_merge_overlapping(
    A: AsymptoticExpansion | ElementConstructorInput,
    B: AsymptoticExpansion | ElementConstructorInput,
    key: tuple[ElementConstructorInput, ...] = ...,
) -> AsymptoticExpansion: ...
def bidirectional_merge_sorted(
    A: AsymptoticExpansion | ElementConstructorInput,
    B: AsymptoticExpansion | ElementConstructorInput,
    key: tuple[ElementConstructorInput, ...] = ...,
) -> AsymptoticExpansion: ...
def log_string(
    element: AsymptoticExpansion | ElementConstructorInput, base: Ring = ...
) -> AsymptoticExpansion: ...
def strip_symbolic(expression: int | Integer) -> AsymptoticExpansion: ...

class NotImplementedOZero(NotImplementedError):
    def __init__(
        self, asymptotic_ring: Ring = ..., var: Ring = ..., exact_part: Ring = ...
    ) -> None: ...

class NotImplementedBZero(NotImplementedError):
    def __init__(
        self, asymptotic_ring: Ring = ..., var: Ring = ..., exact_part: Ring = ...
    ) -> None: ...

def transform_category(
    category: Category,
    subcategory_mapping: Ring,
    axiom_mapping: Ring,
    initial_category: Ring = ...,
) -> AsymptoticExpansion: ...

class Locals(dict):
    def __getitem__(
        self, key: tuple[ElementConstructorInput, ...]
    ) -> AsymptoticExpansion: ...
    def __setitem__(
        self,
        key: tuple[ElementConstructorInput, ...],
        value: RingElement | int | Integer | Rational,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def default_locals(self) -> AsymptoticExpansion: ...

class WithLocals(SageObject):
    def locals(self, locals: Ring = ...) -> AsymptoticExpansion: ...
