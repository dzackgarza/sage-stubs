from sage.modules.free_module_element import FreeModuleElement_generic_dense
from sage.symbolic.expression import Expression


class Vector_callable_symbolic_dense(
    FreeModuleElement_generic_dense[Expression]
):
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
