from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping, Sequence
from types import NotImplementedType
from typing import Generic, Literal, Protocol, TypeVar, overload

from sage.algebras.clifford_algebra_element import (
    CliffordAlgebraElement,
    ExteriorAlgebraElement,
)
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.poor_man_map import PoorManMap
from sage.categories.rings import Rings
from sage.combinat.free_module import CombinatorialFreeModule
from sage.data_structures.bitset import FrozenBitset
from sage.homology.chain_complex import (
    ChainComplex_class,
    HomologyGenerator,
    HomologyObject,
)
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphismByLinearity
from sage.modules.with_basis.subquotient import SubmoduleWithBasis
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer import Integer
from sage.rings.noncommutative_ideals import IdealSide, Ideal_nc
from sage.rings.ring import Ring
from sage.sets.family import Family
from sage.structure.element import ModuleElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.typeset.ascii_art import AsciiArt
from sage.typeset.unicode_art import UnicodeArt

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)
_NewCoefficient = TypeVar("_NewCoefficient", bound=RingElement)
_HomologyCoefficient = TypeVar("_HomologyCoefficient", bound=RingElement)

type CliffordGeneratorNames = str | Sequence[str]
type CliffordBasisIndex = FrozenBitset | tuple[int | Integer, ...]
type CliffordIndexInput = int | Integer | Iterable[int | Integer] | FrozenBitset
type CliffordElementInput[_Coefficient: RingElement] = (
    CliffordAlgebraElement[RingElement]
    | FreeModuleElement[RingElement]
    | tuple[int | Integer, ...]
    | ElementConstructorInput
)
type ExteriorStructureValue[_Coefficient: RingElement] = (
    ExteriorAlgebraElement[_Coefficient]
    | FreeModuleElement[_Coefficient]
    | Mapping[int | Integer, ElementConstructorInput]
    | ElementConstructorInput
)
type ExteriorStructureCoefficients[_Coefficient: RingElement] = (
    Mapping[
        tuple[int | Integer, int | Integer],
        ExteriorStructureValue[_Coefficient],
    ]
    | Iterable[
        tuple[
            tuple[int | Integer, int | Integer],
            ExteriorStructureValue[_Coefficient],
        ]
    ]
)
type ExteriorTensorElement[_Coefficient: RingElement] = IndexedFreeModuleElement[
    tuple[FrozenBitset, FrozenBitset],
    _Coefficient,
]
class _CliffordGeneratorFamily(Protocol[_Coefficient]):
    def __getitem__(self, name: str) -> CliffordAlgebraElement[_Coefficient]: ...
    def __iter__(self) -> Iterator[CliffordAlgebraElement[_Coefficient]]: ...
    def keys(self) -> Iterable[str]: ...
    def values(self) -> Iterable[CliffordAlgebraElement[_Coefficient]]: ...

class CliffordAlgebraIndices(
    UniqueRepresentation,
    Parent[FrozenBitset],
):
    def __init__(
        self,
        Qdim: int | Integer,
        degree: int | Integer | None = ...,
    ) -> None: ...
    def _element_constructor_(self, x: CliffordIndexInput) -> FrozenBitset: ...
    def __call__(
        self,
        x: CliffordIndexInput | ElementConstructorInput = ...,
        *args: object,
        **kwds: object,
    ) -> FrozenBitset: ...
    def cardinality(self) -> int | Integer: ...
    def __len__(self) -> int: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def __iter__(self) -> Iterator[FrozenBitset]: ...
    def __contains__(self, elt: object) -> bool: ...
    def _an_element_(self) -> FrozenBitset: ...

class CliffordAlgebra(
    CombinatorialFreeModule,
    Generic[_Coefficient],
):
    def __init__(
        self,
        Q: QuadraticForm,
        names: CliffordGeneratorNames | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, m: CliffordBasisIndex) -> str: ...
    def _latex_term(self, m: CliffordBasisIndex) -> str: ...
    def _coerce_map_from_(
        self,
        R: Parent | type,
        /,
    ) -> (
        Callable[[Parent, ModuleElement], ModuleElement]
        | Morphism[ModuleElement, ModuleElement]
        | None
    ): ...
    def _element_constructor_(
        self,
        x: CliffordElementInput[_Coefficient],
    ) -> CliffordAlgebraElement[_Coefficient]: ...
    def _basis_index_function(
        self,
        x: int | Integer | tuple[int | Integer, ...],
    ) -> FrozenBitset: ...
    def gen(self, i: int | Integer) -> CliffordAlgebraElement[_Coefficient]: ...
    def algebra_generators(
        self,
    ) -> _CliffordGeneratorFamily[_Coefficient]: ...
    def gens(self) -> tuple[CliffordAlgebraElement[_Coefficient], ...]: ...
    def ngens(self) -> int: ...
    def one_basis(self) -> FrozenBitset: ...
    def quadratic_form(self) -> QuadraticForm: ...
    def degree_on_basis(self, m: CliffordBasisIndex) -> Integer: ...
    def graded_algebra(self) -> ExteriorAlgebra[_Coefficient]: ...
    def free_module(self) -> FreeModule_generic[_Coefficient]: ...
    def dimension(self) -> Integer: ...
    def pseudoscalar(self) -> CliffordAlgebraElement[_Coefficient]: ...
    def lift_module_morphism(
        self,
        m: Matrix[_Coefficient],
        names: CliffordGeneratorNames | None = ...,
    ) -> ModuleMorphismByLinearity[FrozenBitset, FrozenBitset, _Coefficient]: ...
    def lift_isometry(
        self,
        m: Matrix[_Coefficient],
        names: CliffordGeneratorNames | None = ...,
    ) -> ModuleMorphismByLinearity[FrozenBitset, FrozenBitset, _Coefficient]: ...
    def center_basis(self) -> tuple[CliffordAlgebraElement[_Coefficient], ...]: ...
    def supercenter_basis(
        self,
    ) -> tuple[CliffordAlgebraElement[_Coefficient], ...]: ...

class ExteriorAlgebra(
    CliffordAlgebra[_Coefficient],
    Generic[_Coefficient],
):
    def __init__(
        self,
        R: Rings.ParentMethods[_Coefficient] | FreeModule_generic[_Coefficient],
        names: CliffordGeneratorNames | int | Integer | None = ...,
        n: int | Integer | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, m: CliffordBasisIndex) -> str: ...
    def _ascii_art_term(self, m: CliffordBasisIndex) -> AsciiArt: ...
    def _unicode_art_term(self, m: CliffordBasisIndex) -> UnicodeArt: ...
    def _latex_term(self, m: CliffordBasisIndex) -> str: ...
    def lift_morphism(
        self,
        phi: Matrix[_Coefficient],
        names: CliffordGeneratorNames | None = ...,
    ) -> ModuleMorphismByLinearity[FrozenBitset, FrozenBitset, _Coefficient]: ...
    def volume_form(self) -> ExteriorAlgebraElement[_Coefficient]: ...
    def boundary(
        self,
        s_coeff: ExteriorStructureCoefficients[_Coefficient],
    ) -> ExteriorAlgebraBoundary[_Coefficient]: ...
    def coboundary(
        self,
        s_coeff: ExteriorStructureCoefficients[_Coefficient],
    ) -> ExteriorAlgebraCoboundary[_Coefficient]: ...
    def degree_on_basis(self, m: CliffordBasisIndex) -> Integer: ...
    def coproduct_on_basis(
        self,
        a: CliffordBasisIndex,
    ) -> ExteriorTensorElement[_Coefficient]: ...
    def antipode_on_basis(
        self,
        m: CliffordBasisIndex,
    ) -> ExteriorAlgebraElement[_Coefficient]: ...
    def counit(self, x: ExteriorAlgebraElement[_Coefficient]) -> _Coefficient: ...
    def interior_product_on_basis(
        self,
        a: CliffordBasisIndex,
        b: CliffordBasisIndex,
    ) -> ExteriorAlgebraElement[_Coefficient]: ...
    def lifted_bilinear_form(
        self,
        M: Matrix[_Coefficient],
    ) -> PoorManMap: ...
    def _ideal_class_(
        self,
        n: int | Integer = ...,
    ) -> type[ExteriorAlgebraIdeal[_Coefficient]]: ...

class ExteriorAlgebraDifferential(
    ModuleMorphismByLinearity[FrozenBitset, FrozenBitset, _Coefficient],
    UniqueRepresentation,
    Generic[_Coefficient],
):
    def __init__(
        self,
        E: ExteriorAlgebra[_Coefficient],
        s_coeff: Family,
    ) -> None: ...

    @overload
    def homology(
        self,
        deg: None = ...,
        *,
        base_ring: None = ...,
        generators: Literal[False] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> dict[int, HomologyObject[_Coefficient]]: ...
    @overload
    def homology(
        self,
        deg: int | Integer,
        *,
        base_ring: None = ...,
        generators: Literal[False] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> HomologyObject[_Coefficient]: ...
    @overload
    def homology(
        self,
        deg: None,
        *,
        base_ring: Parent[_HomologyCoefficient],
        generators: Literal[False] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> dict[int, HomologyObject[_HomologyCoefficient]]: ...
    @overload
    def homology(
        self,
        deg: int | Integer,
        *,
        base_ring: Parent[_HomologyCoefficient],
        generators: Literal[False] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> HomologyObject[_HomologyCoefficient]: ...
    @overload
    def homology(
        self,
        deg: None = ...,
        *,
        base_ring: None = ...,
        generators: Literal[True],
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> dict[int, list[HomologyGenerator[int, _Coefficient]]]: ...
    @overload
    def homology(
        self,
        deg: int | Integer,
        *,
        base_ring: None = ...,
        generators: Literal[True],
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> list[HomologyGenerator[int, _Coefficient]]: ...
    @overload
    def homology(
        self,
        deg: None,
        *,
        base_ring: Parent[_HomologyCoefficient],
        generators: Literal[True],
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> dict[int, list[HomologyGenerator[int, _HomologyCoefficient]]]: ...
    @overload
    def homology(
        self,
        deg: int | Integer,
        *,
        base_ring: Parent[_HomologyCoefficient],
        generators: Literal[True],
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> list[HomologyGenerator[int, _HomologyCoefficient]]: ...

class ExteriorAlgebraBoundary(
    ExteriorAlgebraDifferential[_Coefficient],
    Generic[_Coefficient],
):
    def _repr_type(self) -> str: ...
    def _on_basis(
        self,
        m: CliffordBasisIndex,
    ) -> ExteriorAlgebraElement[_Coefficient]: ...
    @overload
    def chain_complex(
        self,
        R: None = ...,
    ) -> ChainComplex_class[int, _Coefficient]: ...
    @overload
    def chain_complex(
        self,
        R: Parent[_NewCoefficient],
    ) -> ChainComplex_class[int, _NewCoefficient]: ...

class ExteriorAlgebraCoboundary(
    ExteriorAlgebraDifferential[_Coefficient],
    Generic[_Coefficient],
):
    def __init__(
        self,
        E: ExteriorAlgebra[_Coefficient],
        s_coeff: Family,
    ) -> None: ...
    def _repr_type(self) -> str: ...
    def _on_basis(
        self,
        m: CliffordBasisIndex,
    ) -> ExteriorAlgebraElement[_Coefficient]: ...
    @overload
    def chain_complex(
        self,
        R: None = ...,
    ) -> ChainComplex_class[int, _Coefficient]: ...
    @overload
    def chain_complex(
        self,
        R: Parent[_NewCoefficient],
    ) -> ChainComplex_class[int, _NewCoefficient]: ...

class ExteriorAlgebraIdeal(
    Ideal_nc,
    Generic[_Coefficient],
):
    def __init__(
        self,
        ring: ExteriorAlgebra[_Coefficient],
        gens: Sequence[ExteriorAlgebraElement[_Coefficient] | ElementConstructorInput],
        coerce: bool = ...,
        side: IdealSide = ...,
    ) -> None: ...
    def reduce(
        self,
        f: ExteriorAlgebraElement[_Coefficient] | ElementConstructorInput,
    ) -> ExteriorAlgebraElement[_Coefficient]: ...
    def _contains_(
        self,
        f: ExteriorAlgebraElement[_Coefficient] | ElementConstructorInput,
    ) -> bool: ...
    def __richcmp__(
        self,
        other: object,
        op: int,
    ) -> bool | NotImplementedType: ...
    def __mul__(
        self,
        other: Ideal_nc | Ring,
    ) -> Ideal_nc | SubmoduleWithBasis[Hashable, _Coefficient]: ...
    def groebner_basis(
        self,
        term_order: Literal["neglex", "degrevlex", "deglex"] | None = ...,
        reduced: bool = ...,
    ) -> tuple[ExteriorAlgebraElement[_Coefficient], ...]: ...

