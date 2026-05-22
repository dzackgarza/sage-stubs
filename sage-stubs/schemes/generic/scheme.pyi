from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

class Scheme(Parent):
    ...

class AffineScheme(UniqueRepresentation, Scheme):
    ...
