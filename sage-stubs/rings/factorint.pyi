from sage.rings.integer import Integer
from sage.structure.factorization_integer import IntegerFactorization

def aurifeuillian(
    n: Integer | int,
    m: Integer | int,
    F: Integer | int | None = None,
    check: bool = True,
) -> list[Integer]: ...

def factor_aurifeuillian(n: Integer | int, check: bool = True) -> list[Integer]: ...

def factor_cunningham(m: Integer | int, proof: bool | None = None) -> IntegerFactorization: ...

def factor_trial_division(m: Integer | int, limit: int = ...) -> IntegerFactorization: ...
