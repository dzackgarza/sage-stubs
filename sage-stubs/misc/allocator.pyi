from collections.abc import Callable

from sage.structure.sage_object import SageObject

type NewFunction = Callable[[type[SageObject]], SageObject]
type Destructor = Callable[[SageObject], None]

def hook_tp_functions_type(
    tp: type[SageObject], tp_new: NewFunction, tp_dealloc: Destructor, useGC: bool
) -> None: ...
def hook_tp_functions(
    global_dummy: SageObject, tp_new: NewFunction, tp_dealloc: Destructor, useGC: bool
) -> None: ...
