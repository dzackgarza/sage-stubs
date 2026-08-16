from sage.structure.element import Element
from sage.symbolic.expression import Expression

type GammaInput = Element | int | float | complex

def gamma(self) -> Expression | Element: ...
