from collections.abc import Mapping, Sequence
from typing import Literal, Self, overload

from sage.groups.braid import Braid
from sage.groups.finitely_presented import (
    FinitelyPresentedGroup,
    GroupMorphismWithGensImages,
)
from sage.homology.homology_group import HomologyGroup_class
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.modules.free_module import FreeModule_generic
from sage.plot.graphics import Graphics
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.integer import Integer
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Ring
from sage.structure.element import Element
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression


type Crossing = Sequence[int | Integer]
type PlanarDiagramInput = Sequence[Crossing]
type GaussComponents = Sequence[Sequence[int | Integer]]
type OrientedGaussCodeInput = Sequence[
    GaussComponents | Sequence[int | Integer]
]
type LinkData = Braid | PlanarDiagramInput | OrientedGaussCodeInput
type PlanarDiagram = list[list[int]]
type GaussCode = list[list[int]]
type OrientedGaussCode = list[list[list[int]] | list[int]]
type DiagramArc = list[int]
type DiagramRegion = list[int]
type KhovanovDegree = int | Integer
type KhovanovGroup = HomologyGroup_class | FreeModule_generic
type KhovanovHomology = dict[
    KhovanovDegree,
    dict[KhovanovDegree, KhovanovGroup],
]
type FoxColoring = dict[tuple[int, ...], IntegerMod_abstract]
type LinkPlotColor = str | Mapping[tuple[int, ...], int | Integer]
type KnotInfoIdentification = (
    KnotInfoBase
    | KnotInfoSeries
    | FreeKnotInfoMonoidElement
    | tuple[KnotInfoBase | KnotInfoSeries, SymmetryMutant]
)
type KnotInfoCandidate = (
    KnotInfoBase
    | FreeKnotInfoMonoidElement
    | tuple[KnotInfoBase, SymmetryMutant]
)


class Link(SageObject):
    def __init__(self, data: LinkData) -> None: ...
    def _repr_(self) -> str: ...
    def arcs(
        self,
        presentation: Literal["pd", "gauss_code"] = ...,
    ) -> list[DiagramArc]: ...
    def fundamental_group(
        self,
        presentation: Literal["wirtinger", "braid"] = ...,
        algorithm: Element | None = ...,
    ) -> FinitelyPresentedGroup: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def braid(self, remove_loops: bool = ...) -> Braid: ...
    def khovanov_homology(
        self,
        ring: Ring = ...,
        height: KhovanovDegree | None = ...,
        degree: KhovanovDegree | None = ...,
        implementation: Literal["native", "pari"] = ...,
        **kwds: Element | int | bool | str,
    ) -> KhovanovHomology: ...
    def oriented_gauss_code(self) -> OrientedGaussCode: ...
    def pd_code(self) -> PlanarDiagram: ...
    def gauss_code(self) -> GaussCode: ...
    def dowker_notation(self) -> list[tuple[int, int]]: ...
    def seifert_matrix(self) -> Matrix_integer_dense: ...
    def number_of_components(self) -> Integer: ...
    def is_knot(self) -> bool: ...
    def genus(self) -> Integer: ...
    def signature(self) -> Integer: ...
    def omega_signature(self, omega: Element | complex) -> Integer: ...
    def alexander_polynomial(self, var: str = ...) -> LaurentPolynomial: ...
    def conway_polynomial(self) -> Polynomial: ...
    def khovanov_polynomial(
        self,
        var1: str = ...,
        var2: str = ...,
        torsion: str = ...,
        ring: Ring = ...,
        base_ring: Ring | None = ...,
        implementation: Literal["native", "pari"] = ...,
        **kwds: Element | int | bool | str,
    ) -> LaurentPolynomial: ...
    def determinant(self) -> Integer: ...
    def is_alternating(self) -> bool: ...
    def orientation(self) -> list[int]: ...
    def seifert_circles(self) -> list[list[int]]: ...
    def regions(self) -> list[DiagramRegion]: ...
    def remove_loops(self) -> Self: ...
    def mirror_image(self) -> Self: ...
    def reverse(self) -> Self: ...
    def writhe(self) -> Integer: ...
    def jones_polynomial(
        self,
        variab: str | Element | None = ...,
        skein_normalization: bool = ...,
        algorithm: Literal["jonesrep", "statesum"] = ...,
    ) -> LaurentPolynomial | Expression: ...
    def homfly_polynomial(
        self,
        var1: str | None = ...,
        var2: str | None = ...,
        normalization: Literal["lm", "az", "vz"] = ...,
        algorithm: Element | None = ...,
    ) -> LaurentPolynomial: ...
    def links_gould_polynomial(
        self,
        varnames: str = ...,
    ) -> LaurentPolynomial: ...
    def is_colorable(self, n: int | Integer | None = ...) -> bool: ...
    def colorings(
        self,
        n: int | Integer | None = ...,
    ) -> list[FoxColoring]: ...
    def coloring_maps(
        self,
        n: int | Integer | None = ...,
        finitely_presented: bool = ...,
    ) -> list[GroupMorphismWithGensImages]: ...
    def plot(
        self,
        gap: float = ...,
        component_gap: float = ...,
        solver: str | None = ...,
        color: LinkPlotColor = ...,
        **kwargs: Element | int | float | bool | str,
    ) -> Graphics: ...

    @overload
    def get_knotinfo(
        self,
        mirror_version: bool = ...,
        unique: Literal[True] = ...,
    ) -> KnotInfoIdentification: ...
    @overload
    def get_knotinfo(
        self,
        mirror_version: bool,
        unique: Literal[False],
    ) -> list[KnotInfoCandidate]: ...

    def is_isotopic(self, other: Link) -> bool: ...
    def simplify(
        self,
        exhaustive: bool = ...,
        height: int = ...,
        threads: int = ...,
    ) -> Self: ...


from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoidElement
from sage.knots.knotinfo import KnotInfoBase, KnotInfoSeries, SymmetryMutant
