from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Literal, overload

from sage.algebras.steenrod.steenrod_algebra_bases import SteenrodBasisKey
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.fp_graded.steenrod.module import SteenrodFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.finite_rings.finite_field_base import FiniteField
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily

type SteenrodTensorKey = tuple[SteenrodBasisKey, SteenrodBasisKey]
type SteenrodTensorElement = IndexedFreeModuleElement[
    SteenrodTensorKey,
    FiniteRingElement,
]
type SteenrodProfileValue = int | Integer | PlusInfinity
type SteenrodProfileFunction = Callable[
    [int | Integer],
    SteenrodProfileValue,
]
type SteenrodModTwoProfileInput = (
    Iterable[SteenrodProfileValue]
    | SteenrodProfileFunction
)
type SteenrodOddExteriorProfileInput = (
    Iterable[int | Integer]
    | Callable[[int | Integer], int | Integer]
)
type SteenrodProfileInput = (
    SteenrodModTwoProfileInput
    | tuple[
        SteenrodModTwoProfileInput,
        SteenrodOddExteriorProfileInput,
    ]
    | PlusInfinity
    | None
)
type SteenrodGenericFlag = bool | Literal["auto"]


@overload
def SteenrodAlgebra(
    p: Literal[2] = ...,
    basis: str = ...,
    generic: Literal["auto", False] = ...,
    **kwds: Element | int | float | complex | str | bool | list[Element],
) -> SteenrodAlgebra_mod_two: ...
@overload
def SteenrodAlgebra(
    p: Literal[2],
    basis: str = ...,
    generic: Literal[True] = ...,
    **kwds: Element | int | float | complex | str | bool | list[Element],
) -> SteenrodAlgebra_generic: ...
@overload
def SteenrodAlgebra(
    p: int | Integer = ...,
    basis: str = ...,
    generic: SteenrodGenericFlag = ...,
    **kwds: Element | int | float | complex | str | bool | list[Element],
) -> SteenrodAlgebra_generic | SteenrodAlgebra_mod_two: ...


@overload
def AA(
    n: int | Integer | None = ...,
    p: Literal[2] = ...,
) -> SteenrodAlgebra_mod_two: ...
@overload
def AA(
    n: int | Integer | None = ...,
    p: int | Integer = ...,
) -> SteenrodAlgebra_generic | SteenrodAlgebra_mod_two: ...


def Sq(*nums: int | Integer) -> SteenrodAlgebra_mod_two.Element: ...


class SteenrodAlgebra_generic(CombinatorialFreeModule):
    class Element(
        IndexedFreeModuleElement[
            SteenrodBasisKey,
            FiniteRingElement,
        ]
    ):
        def parent(self) -> SteenrodAlgebra_generic: ...
        def prime(self) -> int | Integer: ...
        def basis_name(self) -> str: ...
        def is_homogeneous(self) -> bool: ...
        def degree(self) -> int | Integer: ...
        def milnor(self) -> SteenrodAlgebra_generic.Element: ...
        def change_basis(
            self,
            basis: str = ...,
        ) -> SteenrodAlgebra_generic.Element: ...
        def _basis_dictionary(
            self,
            basis: str,
        ) -> dict[SteenrodBasisKey, FiniteRingElement]: ...
        def coproduct(
            self,
            algorithm: str | None = ...,
        ) -> SteenrodTensorElement: ...
        def excess(self) -> int | Integer: ...
        def is_unit(self) -> bool: ...
        def is_nilpotent(self) -> bool: ...
        def may_weight(self) -> int | Integer | PlusInfinity: ...
        def is_decomposable(self) -> bool: ...
        def wall_height(self) -> list[int | Integer]: ...
        def additive_order(self) -> int | Integer: ...

    @staticmethod
    def __classcall__(
        class_: type[SteenrodAlgebra_generic],
        p: int | Integer = ...,
        basis: str = ...,
        **kwds: Element | int | float | complex | str | bool | list[Element],
    ) -> SteenrodAlgebra_generic: ...
    def __init__(
        self,
        p: int | Integer = ...,
        basis: str = ...,
        **kwds: Element | int | float | complex | str | bool | list[Element],
    ) -> None: ...
    def base_ring(self) -> FiniteField: ...
    def free_graded_module(
        self,
        generator_degrees: Iterable[int | Integer],
        names: str | Sequence[str] | None = ...,
    ) -> SteenrodFreeModule: ...
    def _basis_key_iterator(self) -> Iterator[SteenrodBasisKey]: ...
    def prime(self) -> int | Integer: ...
    def basis_name(self) -> str: ...
    def _has_nontrivial_profile(self) -> bool: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _repr_term(self, t: SteenrodBasisKey) -> str: ...
    def _latex_term(self, t: SteenrodBasisKey) -> str: ...
    def profile(
        self,
        i: int | Integer,
        component: int | Integer = ...,
    ) -> SteenrodProfileValue: ...
    def homogeneous_component(
        self,
        n: int | Integer,
    ) -> CombinatorialFreeModule: ...
    __getitem__ = homogeneous_component
    def one_basis(self) -> SteenrodBasisKey: ...
    def zero(self) -> SteenrodAlgebra_generic.Element: ...
    def one(self) -> SteenrodAlgebra_generic.Element: ...
    def monomial(
        self,
        index: SteenrodBasisKey,
    ) -> SteenrodAlgebra_generic.Element: ...
    def term(
        self,
        index: SteenrodBasisKey,
        coeff: FiniteRingElement | int | Integer = ...,
    ) -> SteenrodAlgebra_generic.Element: ...
    def _from_dict(
        self,
        d: Mapping[
            SteenrodBasisKey,
            FiniteRingElement | int | Integer,
        ],
        coerce: bool = ...,
        remove_zeros: bool = ...,
    ) -> SteenrodAlgebra_generic.Element: ...
    def product_on_basis(
        self,
        t1: SteenrodBasisKey,
        t2: SteenrodBasisKey,
    ) -> SteenrodAlgebra_generic.Element: ...
    def coproduct_on_basis(
        self,
        t: SteenrodBasisKey,
        algorithm: str | None = ...,
    ) -> SteenrodTensorElement: ...
    def coproduct(
        self,
        x: SteenrodAlgebra_generic.Element,
        algorithm: str | None = ...,
    ) -> SteenrodTensorElement: ...
    def antipode_on_basis(
        self,
        t: SteenrodBasisKey,
    ) -> SteenrodAlgebra_generic.Element: ...
    def counit_on_basis(
        self,
        t: SteenrodBasisKey,
    ) -> FiniteRingElement: ...
    def _milnor_on_basis(
        self,
        t: SteenrodBasisKey,
    ) -> SteenrodAlgebra_generic.Element: ...
    milnor: ModuleMorphism[
        SteenrodBasisKey,
        SteenrodBasisKey,
        FiniteRingElement,
    ]
    def _change_basis_on_basis(
        self,
        t: SteenrodBasisKey,
        basis: str = ...,
    ) -> SteenrodAlgebra_generic.Element: ...
    def _change_basis(
        self,
        x: SteenrodAlgebra_generic.Element,
        basis: str = ...,
    ) -> SteenrodAlgebra_generic.Element: ...
    def degree_on_basis(
        self,
        t: SteenrodBasisKey,
    ) -> int | Integer: ...
    def _coerce_map_from_(self, S: Parent) -> bool: ...
    def _element_constructor_(
        self,
        x: Element | int | float | complex | str | bool | list[Element],
    ) -> SteenrodAlgebra_generic.Element: ...
    def __contains__(self, x: Element | int | float | complex | str | bool | list[Element]) -> bool: ...
    def basis(
        self,
        d: int | Integer | None = ...,
    ) -> AbstractFamily: ...
    def _check_profile_on_basis(
        self,
        t: SteenrodBasisKey,
    ) -> bool: ...
    def P(
        self,
        *nums: int | Integer,
    ) -> SteenrodAlgebra_generic.Element: ...
    def Q_exp(
        self,
        *nums: int | Integer,
    ) -> SteenrodAlgebra_generic.Element: ...
    def Q(
        self,
        *nums: int | Integer,
    ) -> SteenrodAlgebra_generic.Element: ...
    def _an_element_(self) -> SteenrodAlgebra_generic.Element: ...
    def an_element(self) -> SteenrodAlgebra_generic.Element: ...
    def pst(
        self,
        s: int | Integer,
        t: int | Integer,
    ) -> SteenrodAlgebra_generic.Element: ...
    def ngens(self) -> int | Integer | PlusInfinity: ...
    def gens(self) -> AbstractFamily: ...
    algebra_generators = gens
    def gen(
        self,
        i: int | Integer = ...,
    ) -> SteenrodAlgebra_generic.Element: ...
    def is_commutative(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def dimension(self) -> int | Integer | PlusInfinity: ...
    def top_class(self) -> SteenrodAlgebra_generic.Element: ...
    def order(self) -> int | Integer | PlusInfinity: ...
    def is_division_algebra(self) -> bool: ...
    def is_field(self, proof: bool = ...) -> bool: ...
    def is_integral_domain(self, proof: bool = ...) -> bool: ...
    def is_noetherian(self) -> bool: ...
    def is_generic(self) -> bool: ...


class SteenrodAlgebra_mod_two(SteenrodAlgebra_generic):
    def Sq(
        self,
        *nums: int | Integer,
    ) -> SteenrodAlgebra_mod_two.Element: ...


SteenrodAlgebraElement = SteenrodAlgebra_generic.Element


