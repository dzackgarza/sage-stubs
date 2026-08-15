from sage.rings.integer import Integer
from sage.symbolic.expression import Expression
from sage.structure.element import Element

type RealInput = Element | int | float
type RadicalInput = Element | int | float | complex

def ceil(x: RealInput) -> Integer | Expression: ...
def floor(x: RealInput) -> Integer | Expression: ...
def sqrt(x: RadicalInput) -> Element | float | complex: ...

class Function_abs:
    def __call__(self, x: RadicalInput) -> Element: ...

abs_symbolic: Function_abs
