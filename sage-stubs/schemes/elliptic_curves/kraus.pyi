import builtins

class _SageObject: ...

def c4c6_nonsingular(self, c6: builtins.object) -> _SageObject: ...
def c4c6_model(
    self, c6: builtins.object, assume_nonsingular: builtins.bool = ...
) -> _SageObject: ...
def make_integral(self, P: builtins.int, e: builtins.object) -> _SageObject: ...
def sqrt_mod_4(self, P: builtins.int) -> _SageObject: ...
def check_b2_local(
    self,
    c6: builtins.object,
    P: builtins.int,
    b2: builtins.object,
    debug: builtins.bool = ...,
) -> _SageObject: ...
def check_b2_global(
    self, c6: builtins.object, b2: builtins.object, debug: builtins.bool = ...
) -> _SageObject: ...
def check_Kraus_local_3(
    self,
    c6: builtins.object,
    P: builtins.int,
    assume_nonsingular: builtins.bool = ...,
    debug: builtins.bool = ...,
) -> _SageObject: ...
def check_a1a3_local(
    self,
    c6: builtins.object,
    P: builtins.int,
    a1: builtins.object,
    a3: builtins.object,
    debug: builtins.bool = ...,
) -> _SageObject: ...
def check_a1a3_global(
    self,
    c6: builtins.object,
    a1: builtins.object,
    a3: builtins.object,
    debug: builtins.bool = ...,
) -> _SageObject: ...
def check_rst_global(
    self,
    c6: builtins.object,
    r: builtins.int,
    s: builtins.object,
    t: builtins.object,
    debug: builtins.bool = ...,
) -> _SageObject: ...
def check_Kraus_local_2(
    self,
    c6: builtins.object,
    P: builtins.int,
    a1: builtins.object = ...,
    assume_nonsingular: builtins.bool = ...,
) -> _SageObject: ...
def check_Kraus_local(
    self, c6: builtins.object, P: builtins.int, assume_nonsingular: builtins.bool = ...
) -> _SageObject: ...
def check_Kraus_global(
    self,
    c6: builtins.object,
    assume_nonsingular: builtins.bool = ...,
    debug: builtins.bool = ...,
) -> _SageObject: ...
def semi_global_minimal_model(self, debug: builtins.bool = ...) -> _SageObject: ...
