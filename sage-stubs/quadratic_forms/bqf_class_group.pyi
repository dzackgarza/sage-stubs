from collections.abc import Iterator, Sequence
from typing import Self, TypeVar
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_double import RealDoubleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.quadratic_forms.binary_qf import BinaryQF

class BQFClassGroup:
    def __init__(self, D: int) -> None: ...
    def discriminant(self) -> int: ...
    def order(self) -> int: ...
    def abelian_group(self) -> AbelianGroup_class: ...
    def gens(self) -> list[BQFClassElement]: ...
    def zero(self) -> BQFClassElement: ...
    def __call__(self, form: ElementConstructorInput) -> BQFClassElement: ...

class BQFClassElement:
    def __init__(
        self, parent: BQFClassGroup, form: ElementConstructorInput
    ) -> None: ...
    def form(self) -> BinaryQF: ...
    def order(self) -> int: ...
    def __add__(self, other: BQFClassElement) -> BQFClassElement: ...
    def __neg__(self) -> BQFClassElement: ...
