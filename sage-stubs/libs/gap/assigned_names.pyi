import builtins

class _SageObject: ...

NamesGVars: _SageObject
Filtered: _SageObject
ValueGlobal: _SageObject
IsBoundGlobal: _SageObject
IsFunction: _SageObject
IsDocumentedWord: _SageObject

def load_or_compute(self, function: builtins.object) -> _SageObject: ...
def list_keywords(self) -> _SageObject: ...

KEYWORDS: _SageObject

def list_globals(self) -> _SageObject: ...

GLOBALS: _SageObject

def list_functions(self) -> _SageObject: ...

FUNCTIONS: _SageObject
