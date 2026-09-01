from collections.abc import Iterable, Sequence

from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.groups.additive_abelian.qmodnz_element import QmodnZ_Element
from sage.groups.fqf_orthogonal import FqfOrthogonalGroup
from sage.matrix.matrix0 import Matrix
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import RingElement
from sage.structure.unique_representation import CachedRepresentation

type SignaturePair = tuple[int | Integer, int | Integer]
type QuadraticGenerator = FreeModuleElement[RingElement] | Sequence[RingElement]


def TorsionQuadraticForm(q: Matrix[Rational]) -> TorsionQuadraticModule: ...
def _brown_indecomposable(
    q: Matrix[Rational],
    p: int | Integer,
) -> IntegerMod_abstract: ...


class TorsionQuadraticModuleElement(FGP_Element[RingElement]):
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _mul_(
        self,
        other: TorsionQuadraticModuleElement,
    ) -> QmodnZ_Element: ...
    def inner_product(
        self,
        other: TorsionQuadraticModuleElement,
    ) -> QmodnZ_Element: ...
    def b(
        self,
        other: TorsionQuadraticModuleElement,
    ) -> QmodnZ_Element: ...
    def quadratic_product(self) -> QmodnZ_Element: ...
    def q(self) -> QmodnZ_Element: ...


class TorsionQuadraticModule(
    FGP_Module_class[RingElement],
    CachedRepresentation,
):
    Element: type[TorsionQuadraticModuleElement]

    @staticmethod
    def __classcall__(
        class_: type[TorsionQuadraticModule],
        V: FreeModule_generic[RingElement],
        W: FreeModule_generic[RingElement],
        gens: Iterable[QuadraticGenerator] | None = ...,
        modulus: int | Integer | Rational | None = ...,
        modulus_qf: int | Integer | Rational | None = ...,
        check: bool = ...,
    ) -> TorsionQuadraticModule: ...
    def __init__(
        self,
        V: FreeModule_generic[RingElement],
        W: FreeModule_generic[RingElement],
        gens: tuple[QuadraticGenerator, ...] | None,
        modulus: Rational,
        modulus_qf: Rational,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _module_constructor(
        self,
        V: FreeModule_generic[RingElement],
        W: FreeModule_generic[RingElement],
        check: bool = ...,
    ) -> TorsionQuadraticModule: ...
    def all_submodules(self) -> list[TorsionQuadraticModule]: ...
    def brown_invariant(self) -> IntegerMod_abstract: ...
    def gram_matrix_bilinear(self) -> Matrix[Rational]: ...
    def gram_matrix_quadratic(self) -> Matrix[Rational]: ...
    def gens(self) -> tuple[TorsionQuadraticModuleElement, ...]: ...
    def genus(self, signature_pair: SignaturePair) -> GenusSymbol_global_ring: ...
    def is_genus(
        self,
        signature_pair: SignaturePair,
        even: bool = ...,
    ) -> bool: ...
    def orthogonal_group(
        self,
        gens: Iterable[object] | None = ...,
        check: bool = ...,
    ) -> FqfOrthogonalGroup: ...
    def orthogonal_submodule_to(
        self,
        S: FGP_Module_class[RingElement],
    ) -> TorsionQuadraticModule: ...
    def normal_form(self, partial: bool = ...) -> TorsionQuadraticModule: ...
    def primary_part(
        self,
        m: int | Integer,
    ) -> TorsionQuadraticModule: ...
    def submodule_with_gens(
        self,
        gens: Iterable[TorsionQuadraticModuleElement],
    ) -> TorsionQuadraticModule: ...
    def twist(
        self,
        s: int | Integer | Rational,
    ) -> TorsionQuadraticModule: ...
    def value_module(self) -> QmodnZ: ...
    def value_module_qf(self) -> QmodnZ: ...
