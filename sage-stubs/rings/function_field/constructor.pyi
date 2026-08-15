# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class FunctionFieldFactory:
    def create_key(self, F: builtins.object, names: builtins.object) -> _SageObject: ...
    def create_object(self, version: builtins.object, key: builtins.object, **extra_args: builtins.object) -> _SageObject: ...

FunctionField: _SageObject
class FunctionFieldExtensionFactory:
    def create_key(self, polynomial: builtins.object, names: builtins.object) -> _SageObject: ...
    def create_object(self, version: builtins.object, key: builtins.object, **extra_args: builtins.object) -> _SageObject: ...

FunctionFieldExtension: _SageObject
