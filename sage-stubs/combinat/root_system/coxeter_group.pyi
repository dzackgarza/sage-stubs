from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.combinat.root_system.cartan_type import CartanType_abstract
    from sage.structure.parent import Parent
    from sage.groups.matrix_gps.coxeter_group import CoxeterMatrixGroup

def CoxeterGroup(
    data: object,
    implementation: str = "reflection",
    base_ring: object | None = None,
    index_set: object | None = None,
) -> CoxeterMatrixGroup | Parent: ...
