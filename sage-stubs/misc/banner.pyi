# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class VersionDict:
    major: _SageObject
    minor: _SageObject
    tiny: _SageObject
    prerelease: _SageObject

def version() -> builtins.str: ...

def banner_text(full: builtins.bool = ...) -> builtins.str: ...

def banner() -> None: ...

def version_dict() -> VersionDict: ...

def require_version(major: builtins.int, minor: builtins.int = ..., tiny: builtins.float = ..., prerelease: builtins.bool = ..., print_message: builtins.bool = ...) -> builtins.bool: ...
