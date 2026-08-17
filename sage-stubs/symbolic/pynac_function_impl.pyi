from sage.structure.parent import Parent
from sage.symbolic.function import Function, FunctionArgument, FunctionResult


def call_registered_function(
    serial: int,
    nargs: int,
    args: list[FunctionArgument],
    hold: bool,
    allow_numeric_result: bool,
    result_parent: Parent,
) -> FunctionResult: ...
def find_registered_function(name: str, nargs: int) -> int: ...
def register_or_update_function(
    self: Function,
    name: str,
    latex_name: str,
    nargs: int,
    evalf_params_first: bool,
    update: bool,
) -> int: ...
def get_sfunction_from_serial(serial: int) -> Function: ...
def get_sfunction_from_hash(myhash: int) -> Function: ...
