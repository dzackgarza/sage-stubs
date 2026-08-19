from collections.abc import Iterator, Mapping
from enum import Enum
from typing import Literal, Protocol, overload

from sage.databases.knotinfo_db import KnotInfoColumns
from sage.groups.braid import Braid
from sage.knots.link import Link
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Ring
from sage.structure.element import Element
from sage.structure.sage_object import SageObject
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.expression import Expression


type KnotInfoScalar = int | str | bool
type KnotInfoFlatSequence = (
    tuple[KnotInfoScalar, ...]
    | list[KnotInfoScalar]
)
type KnotInfoNestedSequence = (
    tuple[KnotInfoScalar | KnotInfoFlatSequence, ...]
    | list[KnotInfoScalar | KnotInfoFlatSequence]
)
type KnotInfoEvaluatedValue = (
    KnotInfoScalar
    | KnotInfoFlatSequence
    | KnotInfoNestedSequence
)
type PlanarDiagram = list[list[int]]
type DowkerNotation = list[int] | list[list[int]]
type GaussNotation = list[list[int]]
type BraidNotation = tuple[int, ...]
type KnotInfoPolynomial = LaurentPolynomial | Polynomial | Expression


class _SpherogramLink(Protocol):
    def sage_link(self) -> Link: ...
    def PD_code(self) -> PlanarDiagram: ...


def eval_knotinfo(
    string: str,
    locals: Mapping[str, Element | KnotInfoEvaluatedValue] = ...,
    to_tuple: bool = ...,
) -> KnotInfoEvaluatedValue: ...


def knotinfo_int(string: str) -> int: ...


def knotinfo_bool(string: str) -> bool: ...


class SymmetryMutant(Enum):
    itself: SymmetryMutant
    reverse: SymmetryMutant
    concordance_inverse: SymmetryMutant
    mirror_image: SymmetryMutant
    mixed: SymmetryMutant
    unknown: SymmetryMutant
    value: str

    def __gt__(self, other: SymmetryMutant) -> bool: ...
    def rev(self) -> SymmetryMutant: ...
    def mir(self) -> SymmetryMutant: ...
    def matches(
        self,
        link: KnotInfoBase,
    ) -> bool | list[SymmetryMutant]: ...
    def is_minimal(self, link: KnotInfoBase) -> bool: ...


class KnotInfoBase(Enum):
    value: str

    def __gt__(self, other: KnotInfoBase) -> bool: ...
    @property
    def items(self) -> type[KnotInfoColumns]: ...
    def __getitem__(self, item: KnotInfoColumns) -> str: ...

    @overload
    def pd_notation(self, original: Literal[True]) -> str: ...
    @overload
    def pd_notation(self, original: Literal[False] = ...) -> PlanarDiagram: ...

    @overload
    def dt_notation(self, original: Literal[True]) -> str: ...
    @overload
    def dt_notation(self, original: Literal[False] = ...) -> DowkerNotation: ...

    @overload
    def gauss_notation(self, original: Literal[True]) -> str: ...
    @overload
    def gauss_notation(self, original: Literal[False] = ...) -> GaussNotation: ...

    @overload
    def braid_notation(self, original: Literal[True]) -> str: ...
    @overload
    def braid_notation(self, original: Literal[False] = ...) -> BraidNotation: ...

    def braid_index(self) -> int: ...
    def braid_length(self) -> int: ...
    def braid(self) -> Braid: ...
    def num_components(self) -> int: ...
    def crossing_number(self) -> int: ...
    def determinant(self) -> int: ...
    def three_genus(self) -> int: ...
    def signature(self) -> int: ...
    def is_knot(self) -> bool: ...
    def name_unoriented(self) -> str: ...
    def symmetry_type(self) -> str: ...
    def is_reversible(self) -> bool | None: ...
    def is_amphicheiral(self, positive: bool = ...) -> bool | None: ...
    def is_hyperbolic(self) -> bool: ...
    def is_alternating(self) -> bool: ...
    def is_almost_alternating(self) -> bool: ...
    def is_quasi_alternating(self) -> bool: ...
    def is_adequate(self) -> bool: ...
    def is_positive(self) -> bool: ...
    def is_quasipositive(self) -> bool: ...
    def is_strongly_quasipositive(self) -> bool: ...
    def is_positive_braid(self) -> bool: ...
    def is_fibered(self) -> bool: ...
    def is_oriented(self) -> bool: ...
    def cosmetic_crossing_conjecture_verified(self) -> bool | None: ...

    @overload
    def homfly_polynomial(
        self,
        var1: str = ...,
        var2: str = ...,
        original: Literal[False] = ...,
    ) -> LaurentPolynomial: ...
    @overload
    def homfly_polynomial(
        self,
        var1: str,
        var2: str,
        original: Literal[True],
    ) -> str: ...

    @overload
    def kauffman_polynomial(
        self,
        var1: str = ...,
        var2: str = ...,
        original: Literal[False] = ...,
    ) -> LaurentPolynomial: ...
    @overload
    def kauffman_polynomial(
        self,
        var1: str,
        var2: str,
        original: Literal[True],
    ) -> str: ...

    @overload
    def jones_polynomial(
        self,
        variab: str | Element | None = ...,
        skein_normalization: bool = ...,
        puiseux: bool = ...,
        original: Literal[False] = ...,
        use_sqrt: bool = ...,
    ) -> LaurentPolynomial | Expression: ...
    @overload
    def jones_polynomial(
        self,
        variab: str | Element | None,
        skein_normalization: bool,
        puiseux: bool,
        original: Literal[True],
        use_sqrt: bool = ...,
    ) -> str: ...

    @overload
    def alexander_polynomial(
        self,
        var: str = ...,
        original: Literal[False] = ...,
        laurent_poly: bool = ...,
    ) -> Polynomial | LaurentPolynomial: ...
    @overload
    def alexander_polynomial(
        self,
        var: str,
        original: Literal[True],
        laurent_poly: bool = ...,
    ) -> str: ...

    @overload
    def conway_polynomial(
        self,
        var: str = ...,
        original: Literal[False] = ...,
    ) -> Polynomial: ...
    @overload
    def conway_polynomial(
        self,
        var: str,
        original: Literal[True],
    ) -> str: ...

    @overload
    def khovanov_polynomial(
        self,
        var1: str = ...,
        var2: str = ...,
        torsion: str = ...,
        ring: Ring = ...,
        original: Literal[False] = ...,
        reduced: bool = ...,
        odd: bool = ...,
        base_ring: Ring | None = ...,
    ) -> LaurentPolynomial: ...
    @overload
    def khovanov_polynomial(
        self,
        var1: str,
        var2: str,
        torsion: str,
        ring: Ring,
        original: Literal[True],
        reduced: bool = ...,
        odd: bool = ...,
        base_ring: Ring | None = ...,
    ) -> str: ...

    @overload
    def link(
        self,
        use_item: KnotInfoColumns | None = ...,
        snappy: Literal[False] = ...,
    ) -> Link: ...
    @overload
    def link(
        self,
        use_item: KnotInfoColumns | None,
        snappy: Literal[True],
    ) -> _SpherogramLink: ...
    @overload
    def link(
        self,
        use_item: KnotInfoColumns | None = ...,
        snappy: bool = ...,
    ) -> Link | _SpherogramLink: ...

    def is_unique(self) -> bool: ...
    def is_recoverable(self, unique: bool = ...) -> bool: ...
    def inject(self, verbose: bool = ...) -> None: ...
    def series(self, oriented: bool = ...) -> KnotInfoSeries: ...
    def diagram(
        self,
        single: bool = ...,
        new: int = ...,
        autoraise: bool = ...,
    ) -> bool: ...
    def knot_atlas_webpage(
        self,
        new: int = ...,
        autoraise: bool = ...,
    ) -> bool: ...
    def knotilus_webpage(
        self,
        new: int = ...,
        autoraise: bool = ...,
    ) -> bool: ...


class KnotInfoSeries(UniqueRepresentation, SageObject):
    def __init__(
        self,
        crossing_number: int | Integer,
        is_knot: bool,
        is_alternating: bool,
        name_unoriented: str | None = ...,
    ) -> None: ...
    def list(
        self,
        oriented: bool = ...,
        comp: int | Integer | None = ...,
        det: int | Integer | None = ...,
        homfly: LaurentPolynomial | None = ...,
    ) -> list[KnotInfoBase | KnotInfoSeries]: ...
    def lower_list(
        self,
        oriented: bool = ...,
        comp: int | Integer | None = ...,
        det: int | Integer | None = ...,
        homfly: LaurentPolynomial | None = ...,
    ) -> list[KnotInfoBase | KnotInfoSeries]: ...
    def __repr__(self) -> str: ...
    def __getitem__(
        self,
        item: int | Integer,
    ) -> KnotInfoBase | KnotInfoSeries: ...
    def __call__(
        self,
        item: int | Integer | str,
    ) -> KnotInfoBase | KnotInfoSeries: ...
    def _name(self) -> str: ...
    def is_recoverable(
        self,
        unique: bool = ...,
        max_samples: int | Integer | PlusInfinity = ...,
    ) -> bool: ...
    def inject(self, verbose: bool = ...) -> None: ...


KnotInfo: type[KnotInfoBase]
