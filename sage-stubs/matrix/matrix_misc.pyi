from collections.abc import Iterator

from sage.structure.element import Element

def row_iterator(self) -> Iterator[object]: ...
def prm_mul(
    self, p2: dict[int, Element], mask_free: int, prec: int | None
) -> dict[int, Element]: ...
def permanental_minor_polynomial(
    self, permanent_only: bool = False, var: str = "t", prec: int | None = None
) -> Element: ...
