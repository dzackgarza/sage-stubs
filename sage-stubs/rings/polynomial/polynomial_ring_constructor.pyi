from sage.structure.parent import Parent

def PolynomialRing(
    base_ring: object,
    *args: object,
    **kwds: object,
) -> Parent: ...

def BooleanPolynomialRing_constructor(
    n: int | None = None,
    names: str | list[str] | tuple[str, ...] | None = None,
    order: str = "lex",
) -> Parent: ...
