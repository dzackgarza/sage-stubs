import builtins

class _SageObject: ...

def canonical_parameters(
    self, level: builtins.object, weight: builtins.object, base_ring: builtins.object
) -> _SageObject: ...
def ModularForms_clear_cache(self) -> _SageObject: ...
def ModularForms(
    self=...,
    weight: builtins.int = ...,
    base_ring: builtins.object = ...,
    eis_only: builtins.bool = ...,
    use_cache: builtins.bool = ...,
    prec: builtins.int = ...,
) -> _SageObject: ...
def CuspForms(
    self=...,
    weight: builtins.int = ...,
    base_ring: builtins.object = ...,
    use_cache: builtins.bool = ...,
    prec: builtins.int = ...,
) -> _SageObject: ...
def EisensteinForms(
    self=...,
    weight: builtins.int = ...,
    base_ring: builtins.object = ...,
    use_cache: builtins.bool = ...,
    prec: builtins.int = ...,
) -> _SageObject: ...
def Newforms(
    self,
    weight: builtins.int = ...,
    base_ring: builtins.object = ...,
    names: builtins.object = ...,
) -> _SageObject: ...
def Newform(
    self,
    group: builtins.object = ...,
    weight: builtins.int = ...,
    base_ring: builtins.object = ...,
    names: builtins.object = ...,
) -> _SageObject: ...
def parse_label(self) -> _SageObject: ...
