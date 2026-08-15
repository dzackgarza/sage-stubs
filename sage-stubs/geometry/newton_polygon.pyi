from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

class NewtonPolygon_element(Element): ...

class ParentNewtonPolygon(Parent, UniqueRepresentation): ...

NewtonPolygon = ParentNewtonPolygon()
