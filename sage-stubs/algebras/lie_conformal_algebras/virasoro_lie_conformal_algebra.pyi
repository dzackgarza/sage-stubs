from sage.algebras.lie_conformal_algebras.graded_lie_conformal_algebra import (
    GradedLieConformalAlgebra,
)
from sage.rings.ring import CommutativeRing

class VirasoroLieConformalAlgebra(GradedLieConformalAlgebra):
    def __init__(self, R: CommutativeRing) -> None: ...
    def _repr_(self) -> str: ...
