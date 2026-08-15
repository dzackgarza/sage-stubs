# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class PackageSystem:
    def spkg_installation_hint(self, spkgs: builtins.object, *, prompt: builtins.str = ..., feature: builtins.object = ...) -> _SageObject: ...

class SagePackageSystem:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class PipPackageSystem:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...
