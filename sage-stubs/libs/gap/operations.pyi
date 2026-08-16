import builtins

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
    flags: FlagsType

    def __init__(self, libgap_element: builtins.object) -> None: ...
    @property
    def obj(self) -> _SageObject: ...
    def operations(self) -> _SageObject: ...
    def op_names(self) -> _SageObject: ...
