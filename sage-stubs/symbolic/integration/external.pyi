from sage.symbolic.expression import Expression, SymbolicInput


type IntegrationBound = SymbolicInput | None


def maxima_integrator(
    expression: Expression,
    v: Expression,
    a: IntegrationBound = None,
    b: IntegrationBound = None,
) -> Expression: ...
def sympy_integrator(
    expression: Expression,
    v: Expression,
    a: IntegrationBound = None,
    b: IntegrationBound = None,
) -> Expression: ...
def mma_free_integrator(
    expression: Expression,
    v: Expression,
    a: IntegrationBound = None,
    b: IntegrationBound = None,
) -> Expression: ...
def fricas_integrator(
    expression: Expression,
    v: Expression,
    a: IntegrationBound = None,
    b: IntegrationBound = None,
    noPole: bool = True,
) -> Expression: ...
def libgiac_integrator(
    expression: Expression,
    v: Expression,
    a: IntegrationBound = None,
    b: IntegrationBound = None,
) -> Expression: ...
