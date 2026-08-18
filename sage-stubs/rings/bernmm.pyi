from sage.rings.integer import Integer
from sage.rings.rational import Rational

def bernmm_bern_rat(
    k: int | Integer,
    num_threads: int = ...,
) -> Rational: ...
def bernmm_bern_modp(
    p: int | Integer,
    k: int | Integer,
) -> int: ...
