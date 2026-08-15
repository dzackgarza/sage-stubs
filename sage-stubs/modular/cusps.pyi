from typing import TYPE_CHECKING, overload
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.rings.integer import Integer
from sage.rings.rational import Rational

from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.modular.arithgroup.congroup_gammaH import GammaH_class
class Cusp(Element):
    

    def __init__(self, a, b=None, parent=None, check: bool = True) -> None: ...

    def __hash__(self) -> int: ...

    def _richcmp_(self, other: Cusp, op: int) -> bool: ...

    def is_infinity(self) -> bool:
        
        ...

    def numerator(self) -> Integer:
        
        ...

    def denominator(self) -> Integer:
        
        ...

    def _rational_(self) -> Rational:
        
        ...

    def _integer_(self, ZZ=None) -> Integer:
        
        ...

    def _repr_(self) -> str:
        
        ...

    def _latex_(self) -> str:
        
        ...

    def __neg__(self) -> Cusp:
        
        ...

    @overload
    def is_gamma0_equiv(self, other: Cusp, N: int, transformation: None = None) -> bool: ...
    @overload
    def is_gamma0_equiv(self, other: Cusp, N: int, transformation: str) -> tuple[bool, Integer | Matrix_integer_dense | None]: ...

    def is_gamma1_equiv(self, other: Cusp, N: int) -> tuple[bool, int]:
        
        ...

    def is_gamma_h_equiv(self, other: Cusp, G: GammaH_class) -> tuple[bool, int]:
        
        ...

    def _acted_upon_(self, g, self_on_left: bool):
        
        ...

class Cusps_class(Parent):
    

    Element: type[Cusp]

    def __init__(self) -> None: ...

    def _repr_(self) -> str:
        
        ...

    def _latex_(self) -> str:
        
        ...

    def __call__(self, x) -> Cusp:
        
        ...

    def _coerce_map_from_(self, R) -> bool: ...

    def _element_constructor_(self, x) -> Cusp: ...

Cusps: Cusps_class
