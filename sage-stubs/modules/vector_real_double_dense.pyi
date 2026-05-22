from sage.modules.free_module_element import FreeModuleElement
from sage.structure.parent import Parent

class Vector_real_double_dense(FreeModuleElement):
    def __init__(
        self,
        parent: Parent,
        x: object,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def list(self, copy: bool = ...) -> list[float]: ...
