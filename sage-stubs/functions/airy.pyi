from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionKeyword, FunctionResult

class FunctionAiryAiGeneral(BuiltinFunction):
    def __init__(self) -> None: ...

class FunctionAiryAiSimple(BuiltinFunction):
    def __init__(self) -> None: ...

class FunctionAiryAiPrime(BuiltinFunction):
    def __init__(self) -> None: ...

class FunctionAiryBiGeneral(BuiltinFunction):
    def __init__(self) -> None: ...

class FunctionAiryBiSimple(BuiltinFunction):
    def __init__(self) -> None: ...

class FunctionAiryBiPrime(BuiltinFunction):
    def __init__(self) -> None: ...

airy_ai_general: FunctionAiryAiGeneral
airy_ai_simple: FunctionAiryAiSimple
airy_ai_prime: FunctionAiryAiPrime
airy_bi_general: FunctionAiryBiGeneral
airy_bi_simple: FunctionAiryBiSimple
airy_bi_prime: FunctionAiryBiPrime

def airy_ai(
    alpha: FunctionArgument,
    x: FunctionArgument | None = None,
    hold_derivative: bool = True,
    **kwds: FunctionKeyword,
) -> FunctionResult: ...
def airy_bi(
    alpha: FunctionArgument,
    x: FunctionArgument | None = None,
    hold_derivative: bool = True,
    **kwds: FunctionKeyword,
) -> FunctionResult: ...
