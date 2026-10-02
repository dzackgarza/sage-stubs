from collections.abc import Iterator

from sage.categories.groups import Groups
from sage.groups.abelian_gps.abelian_aut import (
    AbelianGroupAutomorphism,
    AbelianGroupAutomorphismGroup_subgroup,
)
from sage.modules.torsion_quadratic_module import TorsionQuadraticModuleElement
from sage.rings.integer import Integer

class FqfIsometry(AbelianGroupAutomorphism):
    def parent(self) -> FqfOrthogonalGroup: ...
    # fqf_orthogonal.py:95: the image of an element of the invariant form.
    def __call__(
        self, x: TorsionQuadraticModuleElement
    ) -> TorsionQuadraticModuleElement: ...

class FqfOrthogonalGroup(
    AbelianGroupAutomorphismGroup_subgroup[FqfIsometry],
    Groups.ParentMethods[FqfIsometry],
):
    def gens(self) -> tuple[FqfIsometry, ...]: ...
    def ngens(self) -> int: ...
    def order(self) -> Integer: ...
    def is_finite(self) -> bool: ...
    def __iter__(self) -> Iterator[FqfIsometry]: ...
