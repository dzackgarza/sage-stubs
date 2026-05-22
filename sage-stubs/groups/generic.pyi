from typing import TypeVar
from sage.rings.integer import Integer

_T = TypeVar('_T')

def multiple(
    a: _T,
    n: object,
    operation: str = '*',
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> _T: ...
def bsgs(
    a: object,
    b: object,
    bounds: object,
    operation: str = '*',
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> Integer: ...
def discrete_log_rho(
    a: object,
    base: object,
    ord: object = None,
    operation: str = '*',
    identity: object = None,
    inverse: object = None,
    op: object = None,
    hash_function: object = ...,
) -> Integer: ...
def discrete_log(
    a: object,
    base: object,
    ord: object = None,
    bounds: object = None,
    operation: str = '*',
    identity: object = None,
    inverse: object = None,
    op: object = None,
    algorithm: str = 'bsgs',
    *,
    verify: bool = True,
) -> Integer: ...
def discrete_log_generic(
    a: object,
    base: object,
    ord: object = None,
    bounds: object = None,
    operation: str = '*',
    identity: object = None,
    inverse: object = None,
    op: object = None,
    algorithm: str = 'bsgs',
) -> Integer: ...
def discrete_log_lambda(
    a: object,
    base: object,
    bounds: object,
    operation: str = '*',
    identity: object = None,
    inverse: object = None,
    op: object = None,
    hash_function: object = ...,
) -> Integer: ...
def linear_relation(
    P: object,
    Q: object,
    operation: str = '+',
    identity: object = None,
    inverse: object = None,
    op: object = None,
    *,
    ord_p: object = None,
    ord_q: object = None,
) -> tuple[object, ...]: ...
def order_from_multiple(
    P: object,
    m: object,
    plist: object = None,
    factorization: object = None,
    check: bool = True,
    operation: str = '+',
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> Integer: ...
def order_from_bounds(
    P: object,
    bounds: object,
    d: object = None,
    operation: str = '+',
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> Integer: ...
def has_order(P: object, n: object, operation: str = '+') -> bool: ...
def merge_points(
    P1: object,
    P2: object,
    operation: str = '+',
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> tuple[object, ...]: ...
def structure_description(G: object, latex: bool = False) -> str: ...
