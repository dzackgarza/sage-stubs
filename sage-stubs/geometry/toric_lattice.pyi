from collections.abc import Iterable, Sequence
from typing import Self, TypeVar, overload

from sage.categories.map import Map
from sage.geometry.toric_lattice_element import (
    ToricLatticeElement,
    ToricPlot,
)
from sage.matrix.matrix0 import Matrix
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import (
    FreeModule_ambient_pid,
    FreeModule_generic,
    FreeModule_generic_pid,
    FreeModule_submodule_pid,
    FreeModule_submodule_with_basis_pid,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.quotient_module import FreeModule_ambient_field_quotient
from sage.rings.integer import Integer
from sage.rings.integer_ring import IntegerRing_class
from sage.rings.rational import Rational
from sage.rings.rational_field import RationalField
from sage.structure.element import RingElement
from sage.structure.factory import FactoryVersion, UniqueFactory
from sage.structure.parent import ElementConstructorInput, Parent

_OtherScalar = TypeVar("_OtherScalar", bound=RingElement)


type ToricIntegralCoordinates = Sequence[int | Integer]
type ToricElementInput = (
    ToricLatticeElement
    | ToricLattice_quotient_element
    | FreeModuleElement[RingElement]
    | Sequence[ElementConstructorInput]
    | int
    | Integer
)
type ToricGenerator = ToricLatticeElement | ToricIntegralCoordinates
type ToricGenerators = Iterable[ToricGenerator]
type GenericLatticeGenerator = (
    FreeModuleElement[RingElement]
    | Sequence[ElementConstructorInput]
)
type GenericLatticeGenerators = Iterable[GenericLatticeGenerator]
type ToricLatticeKey = tuple[int, str, str, str, str]


class ToricLatticeFactory(UniqueFactory):
    def __call__(
        self,
        rank: int | Integer,
        name: str | None = ...,
        dual_name: str | None = ...,
        latex_name: str | None = ...,
        latex_dual_name: str | None = ...,
    ) -> ToricLattice_ambient: ...
    def create_key(
        self,
        rank: int | Integer,
        name: str | None = ...,
        dual_name: str | None = ...,
        latex_name: str | None = ...,
        latex_dual_name: str | None = ...,
    ) -> ToricLatticeKey: ...
    def create_object(
        self,
        version: FactoryVersion,
        key: ToricLatticeKey,
    ) -> ToricLattice_ambient: ...


ToricLattice: ToricLatticeFactory


class ToricLattice_generic(FreeModule_generic_pid[Integer]):
    Element: type[ToricLatticeElement]

    @overload
    def __call__(
        self,
        coordinates: ToricElementInput = ...,
        **kwds: object,
    ) -> ToricLatticeElement: ...
    @overload
    def __call__(
        self,
        x: int | Integer,
        y: int | Integer,
        *coordinates: int | Integer,
        **kwds: object,
    ) -> ToricLatticeElement: ...
    def _coerce_map_from_(
        self,
        other: Parent,
    ) -> Map | None: ...
    def __contains__(self, point: object) -> bool: ...
    def construction(self) -> None: ...
    @overload
    def direct_sum(
        self,
        other: ToricLattice_generic,
    ) -> ToricLattice_ambient: ...
    @overload
    def direct_sum(
        self,
        other: FreeModule_generic[_OtherScalar],
    ) -> FreeModule_generic[RingElement]: ...
    def intersection(
        self,
        other: FreeModule_generic[Integer],
    ) -> ToricLattice_generic: ...
    def quotient(
        self,
        sub: ToricLattice_generic | ToricGenerators,
        check: bool = ...,
        positive_point: ToricLatticeElement | None = ...,
        positive_dual_point: ToricLatticeElement | None = ...,
        **kwds: object,
    ) -> ToricLattice_quotient: ...
    __truediv__ = quotient
    def saturation(self) -> ToricLattice_generic: ...
    @overload
    def span(
        self,
        gens: ToricGenerators,
        base_ring: IntegerRing_class = ...,
        *args: object,
        **kwds: object,
    ) -> ToricLattice_sublattice: ...
    @overload
    def span(
        self,
        gens: GenericLatticeGenerators,
        base_ring: Parent[_OtherScalar],
        *args: object,
        **kwds: object,
    ) -> FreeModule_generic[_OtherScalar]: ...
    @overload
    def span_of_basis(
        self,
        basis: ToricGenerators,
        base_ring: IntegerRing_class = ...,
        *args: object,
        **kwds: object,
    ) -> ToricLattice_sublattice_with_basis: ...
    @overload
    def span_of_basis(
        self,
        basis: GenericLatticeGenerators,
        base_ring: Parent[_OtherScalar],
        *args: object,
        **kwds: object,
    ) -> FreeModule_generic[_OtherScalar]: ...
    def submodule(
        self,
        gens: ToricGenerators | ToricLattice_generic,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> ToricLattice_sublattice: ...
    def submodule_with_basis(
        self,
        basis: ToricGenerators,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> ToricLattice_sublattice_with_basis: ...
    def zero_submodule(self) -> ToricLattice_sublattice: ...
    def ambient_module(self) -> ToricLattice_ambient: ...
    def dual(self) -> ToricLattice_generic | ToricLattice_quotient: ...
    def gen(self, i: int | Integer = ...) -> ToricLatticeElement: ...
    def gens(self) -> tuple[ToricLatticeElement, ...]: ...
    def basis(self) -> Sequence[ToricLatticeElement]: ...


class ToricLattice_ambient(
    ToricLattice_generic,
    FreeModule_ambient_pid[Integer],
):
    Element: type[ToricLatticeElement]

    def __init__(
        self,
        rank: int | Integer,
        name: str,
        dual_name: str,
        latex_name: str,
        latex_dual_name: str,
    ) -> None: ...
    def _sage_input_(self, sib: object, coerced: bool) -> object: ...
    def __richcmp__(
        self,
        other: ToricLattice_ambient,
        op: int,
    ) -> bool: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
    def ambient_module(self) -> Self: ...
    def dual(self) -> ToricLattice_ambient: ...
    def plot(self, **options: object) -> ToricPlot: ...


class ToricLattice_sublattice_with_basis(
    ToricLattice_generic,
    FreeModule_submodule_with_basis_pid[Integer],
):
    def __init__(
        self,
        ambient: ToricLattice_ambient,
        basis: ToricGenerators,
        check: bool = ...,
        echelonize: bool = ...,
        echelonized_basis: Matrix[Integer] | None = ...,
        already_echelonized: bool = ...,
        **kwds: object,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def ambient_module(self) -> ToricLattice_ambient: ...
    def dual(self) -> ToricLattice_quotient: ...
    def saturation(self) -> ToricLattice_sublattice: ...
    def plot(self, **options: object) -> ToricPlot: ...
    def gen(self, i: int | Integer = ...) -> ToricLatticeElement: ...
    def gens(self) -> tuple[ToricLatticeElement, ...]: ...
    def basis(self) -> Sequence[ToricLatticeElement]: ...


class ToricLattice_sublattice(
    ToricLattice_sublattice_with_basis,
    FreeModule_submodule_pid[Integer],
):
    def __init__(
        self,
        ambient: ToricLattice_ambient,
        gens: ToricGenerators,
        check: bool = ...,
        already_echelonized: bool = ...,
        **kwds: object,
    ) -> None: ...


class ToricLattice_quotient_element(FGP_Element[Integer]):
    def parent(self) -> ToricLattice_quotient: ...
    def lift(self) -> ToricLatticeElement: ...
    def vector(self) -> FreeModuleElement[Integer]: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
    def set_immutable(self) -> None: ...


class ToricLattice_quotient(FGP_Module_class[Integer]):
    Element: type[ToricLattice_quotient_element]

    def __init__(
        self,
        V: ToricLattice_generic,
        W: ToricLattice_generic | ToricGenerators,
        check: bool = ...,
        positive_point: ToricLatticeElement | None = ...,
        positive_dual_point: ToricLatticeElement | None = ...,
        **kwds: object,
    ) -> None: ...
    def gens(self) -> tuple[ToricLattice_quotient_element, ...]: ...
    def gen(
        self,
        i: int | Integer = ...,
    ) -> ToricLattice_quotient_element: ...
    def _element_constructor_(
        self,
        *x: object,
        **kwds: object,
    ) -> ToricLattice_quotient_element: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
    def _module_constructor(
        self,
        V: ToricLattice_generic,
        W: ToricLattice_generic,
        check: bool = ...,
    ) -> ToricLattice_quotient: ...
    @overload
    def base_extend(
        self,
        R: IntegerRing_class,
    ) -> Self: ...
    @overload
    def base_extend(
        self,
        R: RationalField,
    ) -> FreeModule_ambient_field_quotient[Rational]: ...
    def is_torsion_free(self) -> bool: ...
    def dual(self) -> ToricLattice_sublattice: ...
    def rank(self) -> int: ...
    dimension = rank
    def coordinate_vector(
        self,
        x: ToricLattice_quotient_element
        | ToricLatticeElement
        | Sequence[ElementConstructorInput],
        reduce: bool = ...,
    ) -> FreeModuleElement[Integer]: ...
    def V(self) -> ToricLattice_generic: ...
    def cover(self) -> ToricLattice_generic: ...
    def W(self) -> ToricLattice_sublattice: ...
    def relations(self) -> ToricLattice_sublattice: ...
