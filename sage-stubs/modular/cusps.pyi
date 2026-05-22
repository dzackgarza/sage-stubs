from typing import TYPE_CHECKING, overload
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.rings.integer import Integer
from sage.rings.rational import Rational

if TYPE_CHECKING:
    from sage.matrix.matrix_integer_dense import Matrix_integer_dense
    from sage.modular.arithgroup.congroup_gammaH import GammaH_class

class Cusp(Element):
    """A cusp, i.e., an element of the projective line over Q."""

    def __init__(self, a, b=None, parent=None, check: bool = True) -> None: ...

    def __hash__(self) -> int: ...

    def _richcmp_(self, other: Cusp, op: int) -> bool: ...

    def is_infinity(self) -> bool:
        """Return True if this is the cusp infinity."""
        ...

    def numerator(self) -> Integer:
        """Return the numerator of the cusp a/b."""
        ...

    def denominator(self) -> Integer:
        """Return the denominator of the cusp a/b."""
        ...

    def _rational_(self) -> Rational:
        """Coerce to a rational number."""
        ...

    def _integer_(self, ZZ=None) -> Integer:
        """Coerce to an integer."""
        ...

    def _repr_(self) -> str:
        """String representation of this cusp."""
        ...

    def _latex_(self) -> str:
        """Latex representation of this cusp."""
        ...

    def __neg__(self) -> Cusp:
        """The negative of this cusp."""
        ...

    @overload
    def is_gamma0_equiv(self, other: Cusp, N: int, transformation: None = None) -> bool: ...
    @overload
    def is_gamma0_equiv(self, other: Cusp, N: int, transformation: str) -> tuple[bool, Integer | Matrix_integer_dense | None]: ...

    def is_gamma1_equiv(self, other: Cusp, N: int) -> tuple[bool, int]:
        """Return whether self and other are equivalent modulo Gamma_1(N)."""
        ...

    def is_gamma_h_equiv(self, other: Cusp, G: GammaH_class) -> tuple[bool, int]:
        """Return whether self and other are equivalent modulo Gamma_H(N)."""
        ...

    def _acted_upon_(self, g, self_on_left: bool):
        """Implement the left action of SL_2(Z) on self."""
        ...

class Cusps_class(Parent):
    """The set of cusps, i.e., P^1(QQ)."""

    Element: type[Cusp]

    def __init__(self) -> None: ...

    def _repr_(self) -> str:
        """String representation of the set of cusps."""
        ...

    def _latex_(self) -> str:
        """Return latex representation of self."""
        ...

    def __call__(self, x) -> Cusp:
        """Coerce x into the set of cusps."""
        ...

    def _coerce_map_from_(self, R) -> bool: ...

    def _element_constructor_(self, x) -> Cusp: ...

Cusps: Cusps_class
