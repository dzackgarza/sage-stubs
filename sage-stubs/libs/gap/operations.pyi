# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

Length: _SageObject
FlagsType: _SageObject
TypeObj: _SageObject
IS_SUBSET_FLAGS: _SageObject
GET_OPER_FLAGS: _SageObject
OPERATIONS: _SageObject
NameFunction: _SageObject
NAME_RE: _SageObject
class OperationInspector:
    def __init__(self, libgap_element: builtins.object) -> None: ...
    @property
    def obj(self) -> _SageObject: ...
    def operations(self) -> _SageObject: ...
    def op_names(self) -> _SageObject: ...
