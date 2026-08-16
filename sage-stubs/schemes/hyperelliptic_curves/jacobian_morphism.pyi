import builtins
from collections.abc import (
    Iterator,
)

from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element

class _SageObject: ...

class MumfordDivisorClassField:
    def __init__(
        self,
        parent: builtins.object,
        u: builtins.object,
        v: builtins.object,
        check: builtins.bool = ...,
    ) -> None: ...
    def scheme(self) -> _SageObject: ...
    def uv(self) -> tuple[Polynomial, Polynomial]: ...
    def __iter__(self) -> Iterator[Polynomial]: ...
    def __getitem__(self, n: builtins.int) -> Polynomial: ...
    def __hash__(self) -> int: ...
    def __reduce__(self) -> tuple[Element, ...]: ...
    def __bool__(self) -> bool: ...
    def order(self) -> Integer: ...
    def degree(self) -> Integer: ...

class MumfordDivisorClassFieldRamified:
    def __init__(
        self,
        parent: builtins.object,
        u: builtins.object,
        v: builtins.object,
        check: builtins.bool = ...,
    ) -> None: ...

class MumfordDivisorClassFieldInert:
    def __init__(
        self,
        parent: builtins.object,
        u: builtins.object,
        v: builtins.object,
        check: builtins.bool = ...,
    ) -> None: ...

class MumfordDivisorClassFieldSplit:
    def __init__(
        self,
        parent: builtins.object,
        u: builtins.object,
        v: builtins.object,
        n: builtins.int = ...,
        check: builtins.bool = ...,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __iter__(self) -> Iterator[Polynomial]: ...
    def __hash__(self) -> int: ...
