from sage.structure.parent import Parent

class OrePolynomialRing:
    def quotient_module(
        self,
        P: object,
        names: str | tuple[str, ...] | list[str] | None = None,
    ) -> Parent: ...
