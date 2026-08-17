from sage.symbolic.function import BuiltinFunction, GinacFunction

class FunctionDiracDelta(BuiltinFunction):
    def __init__(self) -> None: ...

class FunctionHeaviside(GinacFunction):
    def __init__(self) -> None: ...

class FunctionUnitStep(GinacFunction):
    def __init__(self) -> None: ...

class FunctionSignum(BuiltinFunction):
    def __init__(self) -> None: ...

class FunctionKroneckerDelta(BuiltinFunction):
    def __init__(self) -> None: ...

dirac_delta: FunctionDiracDelta
heaviside: FunctionHeaviside
unit_step: FunctionUnitStep
sgn: FunctionSignum
sign: FunctionSignum
kronecker_delta: FunctionKroneckerDelta
