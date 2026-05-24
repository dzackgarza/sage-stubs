from collections.abc import Iterable, Iterator, Sequence
from typing import Protocol, TypeAlias, overload

from sage.categories.morphism import SetIsomorphism
from sage.categories.pushout import VectorFunctor
from sage.matrix.matrix2 import Matrix
from sage.rings.commutative_ring import CommutativeRing
from sage.rings.integer import Integer
from sage.structure.category_object import CategoryObject
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.tensor.modules.comp import Components
from sage.tensor.modules.ext_pow_free_module import ExtPowerDualFreeModule, ExtPowerFreeModule
from sage.tensor.modules.free_module_alt_form import FreeModuleAltForm
from sage.tensor.modules.free_module_automorphism import FreeModuleAutomorphism
from sage.tensor.modules.free_module_basis import FreeModuleBasis
from sage.tensor.modules.free_module_element import FiniteRankFreeModuleElement
from sage.tensor.modules.free_module_linear_group import FreeModuleLinearGroup
from sage.tensor.modules.free_module_morphism import FiniteRankFreeModuleMorphism
from sage.tensor.modules.free_module_tensor import FreeModuleTensor
from sage.tensor.modules.reflexive_module import (
    ReflexiveModule_abstract,
    ReflexiveModule_base,
    ReflexiveModule_dual,
)
from sage.tensor.modules.tensor_free_module import TensorFreeModule
from sage.tensor.modules.tensor_free_submodule import TensorFreeSubmodule_sym

_Name: TypeAlias = str | None
_BasisSymbol: TypeAlias = str | Sequence[str]
_BasisIndices: TypeAlias = Sequence[str] | None
_TensorType: TypeAlias = tuple[int, int]
_IndexBlock: TypeAlias = Iterable[int]
_Symmetry: TypeAlias = _IndexBlock | Iterable[_IndexBlock] | None
_TensorKeyword: TypeAlias = str | _Symmetry
_RingElementInput: TypeAlias = SageElement | int | Integer
_ComponentVector: TypeAlias = Sequence[_RingElementInput]
_ComponentMatrix: TypeAlias = Sequence[_ComponentVector]
_MatrixLike: TypeAlias = Matrix | _ComponentMatrix

class _Formatter1(Protocol):
    def __call__(self, value: SageElement) -> SageElement: ...

class _Formatter2(Protocol):
    def __call__(self, value: SageElement, format_spec: int | str) -> SageElement: ...

_OutputFormatter: TypeAlias = _Formatter1 | _Formatter2

class FiniteRankFreeModule_abstract(UniqueRepresentation, ReflexiveModule_abstract):
    def __init__(
        self,
        ring: CommutativeRing,
        rank: int | Integer,
        name: _Name = ...,
        latex_name: _Name = ...,
        category: CategoryObject | None = ...,
        ambient: ReflexiveModule_abstract | None = ...,
    ) -> None: ...
    def rank(self) -> int: ...
    def zero(self) -> FiniteRankFreeModuleElement | FreeModuleTensor: ...
    def ambient_module(self) -> ReflexiveModule_abstract: ...
    ambient = ambient_module
    def is_submodule(self, other: ReflexiveModule_abstract) -> bool: ...
    def isomorphism_with_fixed_basis(
        self,
        basis: FreeModuleBasis | None = ...,
        codomain: Parent | None = ...,
    ) -> SetIsomorphism: ...

class FiniteRankFreeModule(ReflexiveModule_base, FiniteRankFreeModule_abstract):
    Element: type[FiniteRankFreeModuleElement]
    @staticmethod
    def __classcall_private__(
        cls: type[FiniteRankFreeModule],
        ring: CommutativeRing,
        rank: int | Integer,
        name: _Name = ...,
        latex_name: _Name = ...,
        start_index: int | Integer = ...,
        output_formatter: _OutputFormatter | None = ...,
        category: CategoryObject | None = ...,
        ambient: ReflexiveModule_abstract | None = ...,
    ) -> FiniteRankFreeModule: ...
    def __init__(
        self,
        ring: CommutativeRing,
        rank: int | Integer,
        name: _Name = ...,
        latex_name: _Name = ...,
        start_index: int | Integer = ...,
        output_formatter: _OutputFormatter | None = ...,
        category: CategoryObject | None = ...,
        ambient: ReflexiveModule_abstract | None = ...,
    ) -> None: ...
    def construction(self) -> tuple[VectorFunctor, CommutativeRing] | None: ...
    def tensor_module(
        self,
        k: int | Integer,
        l: int | Integer,
        *,
        sym: _Symmetry = ...,
        antisym: _Symmetry = ...,
    ) -> FiniteRankFreeModule | ReflexiveModule_dual | TensorFreeModule | TensorFreeSubmodule_sym: ...
    def symmetric_power(self, p: int | Integer) -> ReflexiveModule_abstract: ...
    def dual_symmetric_power(self, p: int | Integer) -> ReflexiveModule_abstract: ...
    def exterior_power(self, p: int | Integer) -> CommutativeRing | FiniteRankFreeModule | ExtPowerFreeModule: ...
    def dual_exterior_power(self, p: int | Integer) -> CommutativeRing | FiniteRankDualFreeModule | ExtPowerDualFreeModule: ...
    def general_linear_group(self) -> FreeModuleLinearGroup: ...
    def basis(
        self,
        symbol: _BasisSymbol,
        latex_symbol: _BasisSymbol | None = ...,
        from_family: Sequence[FiniteRankFreeModuleElement] | None = ...,
        indices: _BasisIndices = ...,
        latex_indices: _BasisIndices = ...,
        symbol_dual: _BasisSymbol | None = ...,
        latex_symbol_dual: _BasisSymbol | None = ...,
    ) -> FreeModuleBasis: ...
    @overload
    def tensor(self, tensor_type: _TensorType, **kwds: _TensorKeyword) -> FreeModuleTensor | FreeModuleAltForm | FiniteRankFreeModuleElement: ...
    @overload
    def tensor(self, first: Parent, *args: Parent, **kwds: _TensorKeyword) -> ReflexiveModule_abstract: ...
    @overload
    def tensor(self, *args: ReflexiveModule_abstract, **kwds: _TensorKeyword) -> ReflexiveModule_abstract: ...
    def tensor_from_comp(
        self,
        tensor_type: _TensorType,
        comp: Components[SageElement, SageElement, int | str],
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> FreeModuleTensor | FreeModuleAltForm | FiniteRankFreeModuleElement: ...
    def alternating_contravariant_tensor(
        self,
        degree: int | Integer,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> FreeModuleTensor | FiniteRankFreeModuleElement: ...
    def alternating_form(
        self,
        degree: int | Integer,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> SageElement | FreeModuleAltForm: ...
    def linear_form(self, name: _Name = ..., latex_name: _Name = ...) -> FreeModuleAltForm: ...
    def automorphism(
        self,
        matrix: _MatrixLike | None = ...,
        basis: FreeModuleBasis | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> FreeModuleAutomorphism: ...
    def sym_bilinear_form(self, name: _Name = ..., latex_name: _Name = ...) -> FreeModuleTensor: ...
    def dual(self) -> FiniteRankDualFreeModule: ...
    def irange(self, start: int | Integer | None = ...) -> Iterator[int]: ...
    def default_basis(self) -> FreeModuleBasis | None: ...
    def set_default_basis(self, basis: FreeModuleBasis) -> None: ...
    def print_bases(self) -> None: ...
    def bases(self) -> list[FreeModuleBasis]: ...
    def change_of_basis(self, basis1: FreeModuleBasis, basis2: FreeModuleBasis) -> FreeModuleAutomorphism: ...
    def set_change_of_basis(
        self,
        basis1: FreeModuleBasis,
        basis2: FreeModuleBasis,
        change_of_basis: FreeModuleAutomorphism,
        compute_inverse: bool = ...,
    ) -> None: ...
    def hom(
        self,
        codomain: FiniteRankFreeModule,
        matrix_rep: _MatrixLike,
        bases: tuple[FreeModuleBasis, FreeModuleBasis] | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> FiniteRankFreeModuleMorphism: ...
    def endomorphism(
        self,
        matrix_rep: _MatrixLike,
        basis: FreeModuleBasis | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> FiniteRankFreeModuleMorphism: ...
    def identity_map(self, name: str = ..., latex_name: _Name = ...) -> FreeModuleAutomorphism: ...

class FiniteRankDualFreeModule(ReflexiveModule_dual, FiniteRankFreeModule_abstract):
    Element: type[FreeModuleAltForm]
    def __init__(self, fmodule: FiniteRankFreeModule, name: _Name = ..., latex_name: _Name = ...) -> None: ...
    def zero(self) -> FreeModuleAltForm: ...
    def base_module(self) -> FiniteRankFreeModule: ...
