from collections.abc import Callable
from copy import copy as copy
from copy import deepcopy as deepcopy
from time import sleep as sleep

from sage.arith.misc import (
    binomial as binomial,
)
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
from sage.categories.category_with_axiom import uncamelcase as uncamelcase
from sage.combinat.all import (
    CombinatorialElement as CombinatorialElement,
)
from sage.combinat.all import (
    CombinatorialObject as CombinatorialObject,
)
from sage.combinat.all import (
    FinitePoset as FinitePoset,
)
from sage.combinat.all import (
    Poset as Poset,
)
from sage.combinat.all import (
    Subsets as Subsets,
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
from sage.misc.cachefunc import (
    cached_function as cached_function,
)
from sage.misc.cachefunc import (
    cached_method as cached_method,
)
from sage.misc.lazy_attribute import (
    lazy_attribute as lazy_attribute,
)
from sage.misc.lazy_attribute import (
    lazy_class_attribute as lazy_class_attribute,
)
from sage.misc.unknown import (
    Unknown as Unknown,
)
from sage.misc.unknown import (
    UnknownClass as UnknownClass,
)
from sage.modules.free_module import FreeModule as FreeModule
from sage.rings.all import (
    AA as AA,
)
from sage.rings.all import (
    NN as NN,
)
from sage.rings.all import (
    QQ as QQ,
)
from sage.rings.all import (
    ZZ as ZZ,
)
from sage.rings.all import (
    AlgebraicField as AlgebraicField,
)
from sage.rings.all import (
    AlgebraicNumber as AlgebraicNumber,
)
from sage.rings.all import (
    AlgebraicReal as AlgebraicReal,
)
from sage.rings.all import (
    AlgebraicRealField as AlgebraicRealField,
)
from sage.rings.all import (
    Integer as Integer,
)
from sage.rings.all import (
    IntegerRing as IntegerRing,
)
from sage.rings.all import (
    IntegerRing_class as IntegerRing_class,
)
from sage.rings.all import (
    NonNegativeIntegerSemiring as NonNegativeIntegerSemiring,
)
from sage.rings.all import (
    QQbar as QQbar,
)
from sage.rings.all import (
    Rational as Rational,
)
from sage.rings.all import (
    RationalField as RationalField,
)
from sage.rings.complex_mpfr import ComplexField_class
from sage.rings.imaginary_unit import I as I
from sage.rings.real_mpfr import RealField_class
from sage.sets.all import (
    DisjointSet as DisjointSet,
)
from sage.sets.all import (
    Family as Family,
)
from sage.sets.all import (
    LazyFamily as LazyFamily,
)
from sage.sets.all import (
    Set as Set,
)
from sage.structure.coerce_dict import (
    MonoDict as MonoDict,
)
from sage.structure.coerce_dict import (
    TripleDict as TripleDict,
)
from sage.structure.dynamic_class import dynamic_class as dynamic_class
from sage.structure.element import Element as Element
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import (
    UniqueRepresentation as UniqueRepresentation,
)

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
