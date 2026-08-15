from sage.symbolic.expression import Expression
from sage.structure.element import Element

type GammaInput = Element | int | float | complex

def gamma(x: GammaInput) -> Expression | Element: ...
