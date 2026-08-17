from symengine.lib.symengine_wrapper import Basic

from sage.symbolic.expression import Expression


def symengine_to_sage(ex: Basic) -> Expression: ...
def sage_to_symengine(ex: Expression) -> Basic: ...
