from collections.abc import Hashable, Iterable, Mapping, Sequence
from typing import Generic, Literal, TypeVar, overload

from sage.categories.category import Category
from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import ModuleElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Degree = TypeVar("_Degree", bound=Hashable, default=Integer)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_HomologyScalar = TypeVar("_HomologyScalar", bound=RingElement)

type ChainComplexSequenceEntry[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | FreeModule_generic[_Scalar]
    | int
    | Integer
)
type ChainComplexData[
    _Degree: Hashable,
    _Scalar: RingElement,
] = (
    Mapping[_Degree, Matrix[_Scalar]]
    | Iterable[ChainComplexSequenceEntry[_Scalar]]
    | None
)
type ChainVectorInput[_Scalar: RingElement] = (
    FreeModuleElement[_Scalar]
    | Iterable[ElementConstructorInput]
)
type ChainInput[
    _Degree: Hashable,
    _Scalar: RingElement,
] = (
    Mapping[_Degree, ChainVectorInput[_Scalar]]
    | Chain_class[_Degree, _Scalar]
    | int
)
type HomologyObject[_Scalar: RingElement] = (
    HomologyGroup_class
    | FreeModule_generic[_Scalar]
)
type HomologyGenerator[
    _Degree: Hashable,
    _Scalar: RingElement,
] = tuple[
    HomologyObject[_Scalar],
    Chain_class[_Degree, _Scalar],
]


def _latex_module(
    R: Parent[_Scalar],
    m: int | Integer,
) -> str: ...


def ChainComplex(
    data: ChainComplexData[_Degree, _Scalar] = ...,
    base_ring: Parent[_Scalar] | None = ...,
    grading_group: Parent[_Degree] | None = ...,
    degree_of_differential: _Degree | int | Integer = ...,
    degree: _Degree | int | Integer = ...,
    check: bool = ...,
) -> ChainComplex_class[_Degree, _Scalar]: ...


class Chain_class(
    ModuleElement,
    Generic[_Degree, _Scalar],
):
    def __init__(
        self,
        parent: ChainComplex_class[_Degree, _Scalar],
        vectors: Mapping[_Degree, FreeModuleElement[_Scalar]],
        check: bool = ...,
    ) -> None: ...
    def parent(self) -> ChainComplex_class[_Degree, _Scalar]: ...
    def vector(self, degree: _Degree) -> FreeModuleElement[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def is_cycle(self) -> bool: ...
    def is_boundary(self) -> bool: ...
    def _add_(self, other: Chain_class[_Degree, _Scalar]) -> Chain_class[_Degree, _Scalar]: ...
    def _lmul_(self, scalar: _Scalar) -> Chain_class[_Degree, _Scalar]: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...


class ChainComplex_class(
    Parent[Chain_class[_Degree, _Scalar]],
    Generic[_Degree, _Scalar],
):
    Element: type[Chain_class[_Degree, _Scalar]]
    element_class: type[Chain_class[_Degree, _Scalar]]

    def __init__(
        self,
        grading_group: Parent[_Degree],
        degree_of_differential: _Degree,
        base_ring: Parent[_Scalar],
        differentials: Mapping[_Degree, Matrix[_Scalar]],
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def _element_constructor_(
        self,
        vectors: ChainInput[_Degree, _Scalar] = ...,
        check: bool = ...,
    ) -> Chain_class[_Degree, _Scalar]: ...
    def zero(self) -> Chain_class[_Degree, _Scalar]: ...
    def random_element(self) -> Chain_class[_Degree, _Scalar]: ...
    _an_element_ = random_element
    def rank(
        self,
        degree: _Degree,
        ring: Parent[RingElement] | None = ...,
    ) -> int | Integer: ...
    def grading_group(self) -> Parent[_Degree]: ...
    def nonzero_degrees(self) -> tuple[_Degree, ...]: ...

    @overload
    def ordered_degrees(
        self,
        start: None = ...,
        exclude_first: bool = ...,
    ) -> tuple[tuple[_Degree, ...], ...]: ...
    @overload
    def ordered_degrees(
        self,
        start: _Degree,
        exclude_first: bool = ...,
    ) -> tuple[_Degree, ...]: ...

    def degree_of_differential(self) -> _Degree: ...

    @overload
    def differential(self, dim: None = ...) -> dict[_Degree, Matrix[_Scalar]]: ...
    @overload
    def differential(self, dim: _Degree) -> Matrix[_Scalar]: ...

    def dual(self) -> ChainComplex_class[_Degree, _Scalar]: ...
    def free_module_rank(self, degree: _Degree) -> int | Integer: ...
    def free_module(
        self,
        degree: _Degree | None = ...,
    ) -> FreeModule_generic[_Scalar]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

    @overload
    def homology(
        self,
        deg: None = ...,
        base_ring: None = ...,
        generators: Literal[False] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> dict[_Degree, HomologyObject[_Scalar]]: ...
    @overload
    def homology(
        self,
        deg: _Degree,
        base_ring: None = ...,
        generators: Literal[False] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> HomologyObject[_Scalar]: ...
    @overload
    def homology(
        self,
        deg: None,
        base_ring: Parent[_HomologyScalar],
        generators: Literal[False] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> dict[_Degree, HomologyObject[_HomologyScalar]]: ...
    @overload
    def homology(
        self,
        deg: _Degree,
        base_ring: Parent[_HomologyScalar],
        generators: Literal[False] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> HomologyObject[_HomologyScalar]: ...
    @overload
    def homology(
        self,
        deg: None = ...,
        base_ring: None = ...,
        generators: Literal[True] = ...,
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> dict[_Degree, list[HomologyGenerator[_Degree, _Scalar]]]: ...
    @overload
    def homology(
        self,
        deg: _Degree,
        base_ring: None,
        generators: Literal[True],
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> list[HomologyGenerator[_Degree, _Scalar]]: ...
    @overload
    def homology(
        self,
        deg: None,
        base_ring: Parent[_HomologyScalar],
        generators: Literal[True],
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> dict[_Degree, list[HomologyGenerator[_Degree, _HomologyScalar]]]: ...
    @overload
    def homology(
        self,
        deg: _Degree,
        base_ring: Parent[_HomologyScalar],
        generators: Literal[True],
        verbose: bool = ...,
        algorithm: str = ...,
    ) -> list[HomologyGenerator[_Degree, _HomologyScalar]]: ...

    @overload
    def betti(
        self,
        deg: None = ...,
        base_ring: Parent[RingElement] | None = ...,
    ) -> dict[_Degree, int]: ...
    @overload
    def betti(
        self,
        deg: _Degree,
        base_ring: Parent[RingElement] | None = ...,
    ) -> int: ...

    def torsion_list(
        self,
        max_prime: int | Integer,
        min_prime: int | Integer = ...,
    ) -> list[tuple[Integer, list[_Degree]]]: ...
    def _Hom_(
        self,
        other: ChainComplex_class[_Degree, _Scalar],
        category: Category | None = ...,
    ) -> ChainComplexHomspace[_Degree, _Scalar]: ...
    def _flip_(self) -> ChainComplex_class[_Degree, _Scalar]: ...
    def shift(
        self,
        n: int | Integer = ...,
    ) -> ChainComplex_class[_Degree, _Scalar]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def cartesian_product(
        self,
        *factors: ChainComplex_class[_Degree, _Scalar],
        **kwds: bool,
    ) -> ChainComplex_class[_Degree, _Scalar]: ...
    def tensor(
        self,
        *factors: ChainComplex_class[_Degree, _Scalar],
        **kwds: bool,
    ) -> ChainComplex_class[_Degree, _Scalar]: ...


from sage.homology.chain_complex_homspace import ChainComplexHomspace
from sage.homology.homology_group import HomologyGroup_class
