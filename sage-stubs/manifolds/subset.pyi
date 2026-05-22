from sage.structure.parent import Parent

class ManifoldSubset(Parent):
    def is_open(self) -> bool: ...
