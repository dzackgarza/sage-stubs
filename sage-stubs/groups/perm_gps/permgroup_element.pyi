from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.structure.element import MultiplicativeGroupElement

class PermutationGroupElement(MultiplicativeGroupElement):
    def parent(self) -> PermutationGroup_generic: ...

class SymmetricGroupElement(PermutationGroupElement): ...
