from typing import Self
from sage.rings.integer import Integer
from sage.rings.infinity import PlusInfinity
from sage.rings.continued_fraction import ContinuedFraction_base

class gosper_iterator:
    a: Integer | int | PlusInfinity
    b: Integer | int | PlusInfinity
    c: Integer | int | PlusInfinity
    d: Integer | int | PlusInfinity
    x: object
    states: set[tuple[Integer | int | PlusInfinity, Integer | int | PlusInfinity, Integer | int | PlusInfinity, Integer | int | PlusInfinity, int]]
    states_to_currently_emitted: dict[tuple[Integer | int | PlusInfinity, Integer | int | PlusInfinity, Integer | int | PlusInfinity, Integer | int | PlusInfinity, int], int]
    currently_emitted: int
    currently_read: int
    input_preperiod_length: int | PlusInfinity
    input_period_length: int
    output_preperiod_length: int

    def __init__(self, a: Integer | int, b: Integer | int, c: Integer | int, d: Integer | int, x: ContinuedFraction_base) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> Integer: ...
    def emit(self, q: Integer | int) -> None: ...
    def ingest(self) -> None: ...
    @staticmethod
    def bound(n: Integer | int | PlusInfinity, d: Integer | int | PlusInfinity) -> int | PlusInfinity: ...
