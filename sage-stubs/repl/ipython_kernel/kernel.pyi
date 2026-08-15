# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class SageZMQInteractiveShell:
    ...

class SageKernel:
    implementation: _SageObject
    implementation_version: _SageObject
    shell_class: _SageObject
    def __init__(self, **kwds: builtins.object) -> None: ...
    @property
    def banner(self) -> _SageObject: ...
    @property
    def help_links(self) -> _SageObject: ...
    def pre_handler_hook(self) -> _SageObject: ...
