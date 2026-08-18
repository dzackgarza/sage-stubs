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

from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.groups.fqf_orthogonal import FqfOrthogonalGroup
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring

class TorsionQuadraticModule(FGP_Module_class):
    _modulus: Rational
    _modulus_qf: Rational

    def __init__(
        self,
        V: FreeModule_generic,
        W: FreeModule_generic,
        gens: Iterable[FGP_Element] | None = ...,
        modulus: Rational | Integer | None = ...,
        modulus_qf: Rational | Integer | None = ...,
        check: bool = ...,
    ) -> None: ...
    def gram_matrix_quadratic(self) -> Matrix[_Scalar]: ...
    def gram_matrix_bilinear(self) -> Matrix[_Scalar]: ...
    def value_module(self) -> QmodnZ: ...
    def value_module_qf(self) -> QmodnZ: ...
    def normal_form(self, partial: bool = ...) -> TorsionQuadraticModule: ...
    def brown_invariant(self) -> Integer: ...
    def genus(self, signature_pair: tuple[int, int]) -> GenusSymbol_global_ring: ...
    def is_genus(
        self, signature_pair: tuple[int | Integer, int | Integer], even: bool = ...
    ) -> bool: ...
    def twist(self, s: int | Integer) -> TorsionQuadraticModule: ...
    def primary_part(self, p: int | Integer) -> TorsionQuadraticModule: ...
    def orthogonal_group(
        self, gens: ElementConstructorInput = ..., check: bool = ...
    ) -> FqfOrthogonalGroup: ...
    def orthogonal_submodule_to(
        self, S: ElementConstructorInput
    ) -> TorsionQuadraticModule: ...
    def submodule_with_gens(
        self, gens: Iterable[FGP_Element]
    ) -> TorsionQuadraticModule: ...
    def all_submodules(self) -> list[TorsionQuadraticModule]: ...

def TorsionQuadraticForm(q: ElementConstructorInput) -> TorsionQuadraticModule: ...
def _brown_indecomposable(q: ElementConstructorInput, p: Integer) -> Integer: ...
