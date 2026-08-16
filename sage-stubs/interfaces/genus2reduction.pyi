import builtins

class _SageObject: ...

roman_numeral: _SageObject

class ReductionData:
    Q: builtins.int
    P: builtins.int

    def __init__(
        self,
        pari_result: builtins.object,
        P: builtins.int,
        Q: builtins.int,
        Pmin: builtins.object,
        Qmin: builtins.object,
        minimal_disc: builtins.object,
        local_data: builtins.object,
        conductor: builtins.object,
    ) -> None: ...

def divisors_to_string(self) -> _SageObject: ...

class Genus2reduction:
    def __init__(self) -> None: ...
    def __call__(self, Q: builtins.int, P: builtins.int) -> _SageObject: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...

genus2reduction: _SageObject
