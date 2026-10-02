from collections.abc import Callable, Hashable, Iterable
from typing import Literal, TypeVar, overload

from sage.categories.category import Category
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.homology.homology_group import HomologyGroup_class
from sage.libs.gap.element import GapElement
from sage.modules.free_module import FreeModule_ambient_field
from sage.rings.integer_ring import IntegerRing_class
from sage.structure.element import FieldElement
from sage.structure.parent import Parent

_FieldScalar = TypeVar("_FieldScalar", bound=FieldElement)

class GenericCellComplex: ...

class SimplicialComplex(GenericCellComplex):
    def __init__(
        self,
        maximal_faces: Iterable[Iterable[Hashable]] | SimplicialComplex | None = None,
        from_characteristic_function: tuple[
            Callable[[frozenset[Hashable]], bool], Iterable[Hashable]
        ]
        | None = None,
        maximality_check: bool = True,
        sort_facets: dict[Hashable, int] | None = None,
        name_check: bool = False,
        immutable: bool = False,
        category: Category | None = None,
    ) -> None: ...
    def dimension(self) -> int: ...
    def f_vector(self) -> list[int]: ...
    # cell_complex.py ``GenericCellComplex.homology``: every dimension when
    # ``dim`` is ``None``, one group when it is an integer; groups over ``ZZ``,
    # vector spaces over a field.
    @overload
    def homology(
        self,
        dim: None = None,
        base_ring: IntegerRing_class = ...,
        subcomplex: SimplicialComplex | None = None,
        generators: Literal[False] = False,
        cohomology: bool = False,
        algorithm: str = "pari",
        verbose: bool = False,
        reduced: bool = True,
        **kwds: bool,
    ) -> dict[int, HomologyGroup_class]: ...
    @overload
    def homology(
        self,
        dim: int,
        base_ring: IntegerRing_class = ...,
        subcomplex: SimplicialComplex | None = None,
        generators: Literal[False] = False,
        cohomology: bool = False,
        algorithm: str = "pari",
        verbose: bool = False,
        reduced: bool = True,
        **kwds: bool,
    ) -> HomologyGroup_class: ...
    @overload
    def homology(
        self,
        dim: None,
        base_ring: Parent[_FieldScalar],
        subcomplex: SimplicialComplex | None = None,
        generators: Literal[False] = False,
        cohomology: bool = False,
        algorithm: str = "pari",
        verbose: bool = False,
        reduced: bool = True,
        **kwds: bool,
    ) -> dict[int, FreeModule_ambient_field[_FieldScalar] | HomologyGroup_class]: ...
    @overload
    def homology(
        self,
        dim: int,
        base_ring: Parent[_FieldScalar],
        subcomplex: SimplicialComplex | None = None,
        generators: Literal[False] = False,
        cohomology: bool = False,
        algorithm: str = "pari",
        verbose: bool = False,
        reduced: bool = True,
        **kwds: bool,
    ) -> FreeModule_ambient_field[_FieldScalar] | HomologyGroup_class: ...
    def euler_characteristic(self) -> int: ...
    def vertices(self) -> frozenset[object]: ...
    def facets(self) -> list[frozenset[object]]: ...
    # simplicial_complex.py ``fundamental_group``: ``libgap.TrivialGroup()``
    # when the 1-skeleton is a tree, otherwise a quotient of a free group.
    def fundamental_group(
        self, base_point: Hashable | None = None, simplify: bool = True
    ) -> FinitelyPresentedGroup | GapElement: ...
