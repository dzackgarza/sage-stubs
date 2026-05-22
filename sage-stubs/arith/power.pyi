from typing import TypeVar
from sage.rings.integer import Integer

_T = TypeVar('_T')

def generic_power(a: _T, n: int | Integer) -> _T: ...
