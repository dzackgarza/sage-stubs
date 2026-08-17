from sage.symbolic.expression import Expression, SymbolicInput


class E(Expression):
    def __init__(self) -> None: ...
    def __pow__(
        self,
        exponent: SymbolicInput,
        modulus: int | None = None,
    ) -> Expression: ...
