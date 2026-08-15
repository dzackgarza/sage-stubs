from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.modules.free_module import FreeModule_generic
from sage.rings.ring import Ring
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

class CliffordAlgebra(Parent, UniqueRepresentation):
    def quadratic_form(self) -> QuadraticForm: ...
    def n(self) -> int: ...
    def degree_on_basis(self, m: object) -> int: ...

class ExteriorAlgebra(CliffordAlgebra):
    def __init__(
        self,
        R: Ring | FreeModule_generic,
        names: str | tuple[str, ...] | list[str] | int | None = ...,
        n: int | None = ...,
    ) -> None: ...
