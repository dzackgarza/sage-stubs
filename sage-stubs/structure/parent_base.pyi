from sage.rings.ring import Ring
from sage.structure.parent import Parent
from sage.structure.parent_old import Parent as Parent_old

class ParentWithBase(Parent_old):
    def __init__(self, base: Ring, *args: object, **kwds: object) -> None: ...
    def base_extend(self, X: Ring | Parent) -> Parent: ...
