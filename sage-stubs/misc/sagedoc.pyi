import builtins

class _SageObject: ...

math_substitutes: _SageObject
nonmath_substitutes: _SageObject
itempattern: _SageObject
itemreplace: _SageObject

def detex(self, embedded: builtins.bool = ...) -> _SageObject: ...
def skip_TESTS_block(self) -> _SageObject: ...
def process_dollars(self) -> _SageObject: ...

pythonversion: _SageObject
extlinks: _SageObject

def process_extlinks(self, embedded: builtins.bool = ...) -> _SageObject: ...
def process_mathtt(self) -> _SageObject: ...
def process_optional_doctest_tags(self) -> _SageObject: ...
def format(self, embedded: builtins.bool = ...) -> _SageObject: ...
def format_src(self) -> _SageObject: ...
def search_src(
    self,
    extra1: builtins.str = ...,
    extra2: builtins.str = ...,
    extra3: builtins.str = ...,
    extra4: builtins.str = ...,
    extra5: builtins.str = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def search_doc(
    self,
    extra1: builtins.str = ...,
    extra2: builtins.str = ...,
    extra3: builtins.str = ...,
    extra4: builtins.str = ...,
    extra5: builtins.str = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def search_def(
    self,
    extra1: builtins.str = ...,
    extra2: builtins.str = ...,
    extra3: builtins.str = ...,
    extra4: builtins.str = ...,
    extra5: builtins.str = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def format_search_as_html(
    self, results: builtins.object, search: builtins.object
) -> _SageObject: ...
def my_getsource(self, oname: builtins.str = ...) -> _SageObject: ...

browse_sage_doc: _SageObject
tutorial: _SageObject
reference: _SageObject
manual: _SageObject
developer: _SageObject
constructions: _SageObject
python_help: _SageObject

def help(self=...) -> _SageObject: ...
