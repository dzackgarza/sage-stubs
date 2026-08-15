from sage.groups.group import Group
from sage.structure.element import MultiplicativeGroupElement

class ArithmeticSubgroupElement(MultiplicativeGroupElement):
    def __init__(self, parent: Group, x: list[int], check: bool = True) -> None: ...
