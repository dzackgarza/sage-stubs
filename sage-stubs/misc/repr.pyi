def coeff_repr(c: object, is_latex: bool = ...) -> str: ...
def repr_lincomb(
    terms: list[tuple[object, object]],
    is_latex: bool = ...,
    scalar_mult: str = ...,
    strip_one: bool = ...,
    repr_monomial: object = ...,
    latex_scalar_mult: str | None = ...,
) -> str: ...
