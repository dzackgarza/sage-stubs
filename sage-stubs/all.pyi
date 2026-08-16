from collections.abc import Callable
from copy import copy as copy
from copy import deepcopy as deepcopy
from time import sleep as sleep

from sage.arith.misc import (
    euler_phi as euler_phi,
)
from sage.arith.misc import (
    factor as factor,
)
from sage.arith.misc import (
    gcd as gcd,
)
from sage.arith.misc import (
    is_prime as is_prime,
)
from sage.arith.misc import (
    lcm as lcm,
)
from sage.arith.misc import (
    moebius as moebius,
)
from sage.arith.misc import (
    next_prime as next_prime,
)
from sage.arith.misc import (
    previous_prime as previous_prime,
)
from sage.arith.misc import (
    prime_pi as prime_pi,
)
from sage.arith.misc import (
    prime_range as prime_range,
)
from sage.graphs.graph import Graph as Graph
from sage.matrix.constructor import (
    diagonal_matrix as diagonal_matrix,
)
from sage.matrix.constructor import (
    identity_matrix as identity_matrix,
)
from sage.matrix.constructor import (
    matrix as matrix,
)
from sage.matrix.constructor import (
    zero_matrix as zero_matrix,
)
from sage.modules.free_module import FreeModule as FreeModule
from sage.rings.complex_mpfr import ComplexField_class
from sage.rings.imaginary_unit import I as I
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational import Rational as Rational
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealField_class
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

def sage_globals(self) -> dict[str, SageGlobal]: ...
