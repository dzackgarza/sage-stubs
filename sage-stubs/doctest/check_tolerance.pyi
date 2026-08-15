# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

float_without_sign: _SageObject
float_regex: _SageObject
class ToleranceExceededError(Exception):
    ...

def check_tolerance_real_domain(want: builtins.object, got: builtins.str) -> builtins.tuple[builtins.str, builtins.str]: ...

real_plus_optional_imag: _SageObject
only_imag: _SageObject
imaginary_unit: _SageObject
complex_regex: _SageObject
def complex_match_to_real_and_imag(m: builtins.int) -> builtins.tuple[builtins.str, builtins.str]: ...

def complex_star_repl(m: builtins.int) -> _SageObject: ...

def check_tolerance_complex_domain(want: builtins.object, got: builtins.str) -> builtins.tuple[builtins.str, builtins.str]: ...
