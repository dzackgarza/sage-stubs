from typing import TypeVar

from sage.rings.integer import Integer

_T = TypeVar("_T")

def multiple(
    self,
    n: object,
    operation: str = "*",
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> _T: ...
def bsgs(
    self,
    b: object,
    bounds: object,
    operation: str = "*",
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> Integer: ...
def discrete_log_rho(
    self,
    base: object,
    ord: object = None,
    operation: str = "*",
    identity: object = None,
    inverse: object = None,
    op: object = None,
    hash_function: object = ...,
) -> Integer: ...
def discrete_log(
    self,
    base: object,
    ord: object = None,
    bounds: object = None,
    operation: str = "*",
    identity: object = None,
    inverse: object = None,
    op: object = None,
    algorithm: str = "bsgs",
    *,
    verify: bool = True,
) -> Integer: ...
def discrete_log_generic(
    self,
    base: object,
    ord: object = None,
    bounds: object = None,
    operation: str = "*",
    identity: object = None,
    inverse: object = None,
    op: object = None,
    algorithm: str = "bsgs",
) -> Integer: ...
def discrete_log_lambda(
    self,
    base: object,
    bounds: object,
    operation: str = "*",
    identity: object = None,
    inverse: object = None,
    op: object = None,
    hash_function: object = ...,
) -> Integer: ...
def linear_relation(
    self,
    Q: object,
    operation: str = "+",
    identity: object = None,
    inverse: object = None,
    op: object = None,
    *,
    ord_p: object = None,
    ord_q: object = None,
) -> tuple[object, ...]: ...
def order_from_multiple(
    self,
    m: object,
    plist: object = None,
    factorization: object = None,
    check: bool = True,
    operation: str = "+",
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> Integer: ...
def order_from_bounds(
    self,
    bounds: object,
    d: object = None,
    operation: str = "+",
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> Integer: ...
def has_order(self, n: object, operation: str = "+") -> bool: ...
def merge_points(
    self,
    P2: object,
    operation: str = "+",
    identity: object = None,
    inverse: object = None,
    op: object = None,
) -> tuple[object, ...]: ...
def structure_description(self, latex: bool = False) -> str: ...
