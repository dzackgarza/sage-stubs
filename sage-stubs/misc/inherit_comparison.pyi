from sage.misc.classcall_metaclass import ClasscallMetaclass

class InheritComparisonMetaclass(type):
    def __init__(self, *args: object) -> None: ...

class InheritComparisonClasscallMetaclass(
    ClasscallMetaclass,
    InheritComparisonMetaclass,
): ...
