from sage.categories.morphism import Morphism
from sage.rings.function_field.derivations import FunctionFieldDerivation
from sage.rings.function_field.element import FunctionFieldElement
from sage.rings.function_field.function_field import FunctionField
from sage.schemes.elliptic_curves.ell_modular_symbols import zero
from sage.structure.parent import ElementConstructorInput

class FunctionFieldDerivation_rational(FunctionFieldDerivation):
    def __init__(self, parent: FunctionField, u: FunctionField = ...) -> None: ...
    def _call_(
        self, x: FunctionFieldElement | ElementConstructorInput
    ) -> FunctionFieldElement | Morphism | zero: ...
