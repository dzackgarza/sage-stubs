from typing import TYPE_CHECKING

from sage.structure.element import Element
class SteenrodAlgebra_generic:
    def prime(self) -> int: ...
    def basis(self, n: int) -> tuple['Element', ...]: ...  # noqa: PYI020
    def Sq(self, *args: int) -> 'Element': ...  # noqa: PYI020
