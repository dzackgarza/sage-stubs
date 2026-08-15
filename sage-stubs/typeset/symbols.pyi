# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class CompoundSymbol:
    def __init__(self, character: builtins.object, top: builtins.object, extension: builtins.object, bottom: builtins.object, middle: builtins.object = ..., middle_top: builtins.object = ..., middle_bottom: builtins.object = ..., top_2: builtins.object = ..., bottom_2: builtins.object = ...) -> None: ...
    def __call__(self, num_lines: builtins.object) -> _SageObject: ...
    def print_to_stdout(self, num_lines: builtins.object) -> _SageObject: ...

class CompoundAsciiSymbol:
    def character_art(self, num_lines: builtins.object) -> _SageObject: ...

class CompoundUnicodeSymbol:
    def character_art(self, num_lines: builtins.object) -> _SageObject: ...

ascii_integral: _SageObject
unicode_integral: _SageObject
ascii_left_parenthesis: _SageObject
ascii_right_parenthesis: _SageObject
unicode_left_parenthesis: _SageObject
unicode_right_parenthesis: _SageObject
ascii_left_square_bracket: _SageObject
ascii_right_square_bracket: _SageObject
unicode_left_square_bracket: _SageObject
unicode_right_square_bracket: _SageObject
ascii_left_curly_brace: _SageObject
ascii_right_curly_brace: _SageObject
unicode_left_curly_brace: _SageObject
unicode_right_curly_brace: _SageObject
