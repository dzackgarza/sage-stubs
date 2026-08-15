# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class DifferentiableManifoldHomset:
    Element: _SageObject
    def __init__(self, domain: builtins.object, codomain: builtins.object, name: builtins.str = ..., latex_name: builtins.str = ...) -> None: ...

class DifferentiableCurveSet:
    Element: _SageObject
    def __init__(self, domain: builtins.object, codomain: builtins.object, name: builtins.str = ..., latex_name: builtins.str = ...) -> None: ...

class IntegratedCurveSet:
    Element: _SageObject
    def __init__(self, domain: builtins.object, codomain: builtins.object, name: builtins.str = ..., latex_name: builtins.str = ...) -> None: ...
    def one(self) -> _SageObject: ...

class IntegratedAutoparallelCurveSet:
    Element: _SageObject
    def __init__(self, domain: builtins.object, codomain: builtins.object, name: builtins.str = ..., latex_name: builtins.str = ...) -> None: ...

class IntegratedGeodesicSet:
    Element: _SageObject
    def __init__(self, domain: builtins.object, codomain: builtins.object, name: builtins.str = ..., latex_name: builtins.str = ...) -> None: ...
