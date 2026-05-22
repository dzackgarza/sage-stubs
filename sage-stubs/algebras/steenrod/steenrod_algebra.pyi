from typing import TYPE_CHECKING

if TYPE_CHECKING:  # noqa: PYI002
    from sage.structure.element import Element

class SteenrodAlgebra_generic:
    def prime(self) -> int: ...
    def basis(self, n: int) -> tuple['Element', ...]: ...  # noqa: PYI020
    def Sq(self, *args: int) -> 'Element': ...  # noqa: PYI020
