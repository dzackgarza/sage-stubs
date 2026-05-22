from sage.modules.free_module_element import FreeModuleElement
from sage.structure.parent import Parent
from sage.rings.finite_rings.integer_mod import IntegerMod

class Vector_modn_dense(FreeModuleElement):
    def __init__(
        self,
        parent: Parent,
        x: object,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def list(self, copy: bool = ...) -> list[IntegerMod]: ...
