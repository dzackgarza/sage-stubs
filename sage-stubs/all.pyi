from collections.abc import Callable
from copy import copy as copy, deepcopy as deepcopy
from time import sleep as sleep

from sage.arith.misc import (
    euler_phi as euler_phi,
    factor as factor,
    gcd as gcd,
    is_prime as is_prime,
    lcm as lcm,
    moebius as moebius,
    next_prime as next_prime,
    previous_prime as previous_prime,
    prime_pi as prime_pi,
    prime_range as prime_range,
)
from sage.graphs.graph import Graph as Graph
from sage.matrix.constructor import (
    diagonal_matrix as diagonal_matrix,
    identity_matrix as identity_matrix,
    matrix as matrix,
    zero_matrix as zero_matrix,
)
from sage.modules.free_module import FreeModule as FreeModule
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing_class, ZZ as ZZ
from sage.rings.rational import Rational as Rational
from sage.rings.rational_field import QQ as QQ, RationalField
from sage.rings.real_mpfr import RealField_class
from sage.rings.complex_mpfr import ComplexField_class
from sage.rings.infinity import infinity as oo
from sage.rings.imaginary_unit import I as I
from sage.structure.element import Element
from sage.structure.parent import Parent

type SageGlobal = (
    Parent | Element | bool | Callable[..., Parent | Element | bool | None]
)

deprecationWarning: Callable[[int, str], None]
true: bool
false: bool
CC: ComplexField_class
RR: RealField_class
i: Element
copying: Callable[[], None]
copyright: Callable[[], None]

def sage_globals() -> dict[str, SageGlobal]: ...
