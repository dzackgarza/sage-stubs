from sage.groups.matrix_gps.coxeter_group import CoxeterMatrixGroup
from sage.structure.parent import Parent

def CoxeterGroup(
    self,
    implementation: str = "reflection",
    base_ring: object | None = None,
    index_set: object | None = None,
) -> CoxeterMatrixGroup | Parent: ...
