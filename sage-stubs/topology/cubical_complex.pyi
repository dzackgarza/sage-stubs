from typing import TYPE_CHECKING

if TYPE_CHECKING:  # noqa: PYI002
    from sage.groups.abelian_gps.abelian_group import AbelianGroup

class GenericCellComplex: ...

class CubicalComplex(GenericCellComplex):
    def dimension(self) -> int: ...
    def euler_characteristic(self) -> int: ...
    def homology(self, deg: int | None = None) -> dict[int, "AbelianGroup"] | "AbelianGroup": ...  # noqa: PYI020
