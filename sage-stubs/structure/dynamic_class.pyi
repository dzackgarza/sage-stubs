from sage.structure.sage_object import SageObject

class DynamicMetaclass(type): ...

def dynamic_class(
    self,
    bases: tuple[type, ...],
    cls: type | None = None,
    reduction: tuple[object, ...] | None = None,
    doccls: type | None = None,
    prepend_cls_bases: bool = True,
    cache: bool | str = True,
) -> type[SageObject]: ...
