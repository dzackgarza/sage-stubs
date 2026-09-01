from collections.abc import Sequence

from sage.misc.classcall_metaclass import ClasscallMetaclass
from sage.misc.inherit_comparison import (
    InheritComparisonClasscallMetaclass,
    InheritComparisonMetaclass,
)

class DynamicMetaclass(type): ...
class DynamicClasscallMetaclass(DynamicMetaclass, ClasscallMetaclass): ...
class DynamicInheritComparisonMetaclass(DynamicMetaclass, InheritComparisonMetaclass): ...
class DynamicInheritComparisonClasscallMetaclass(DynamicMetaclass, InheritComparisonClasscallMetaclass): ...

def dynamic_class(
    name: str,
    bases: tuple[type, ...] | list[type] | Sequence[type],
    cls: type | None = None,
    reduction: tuple[object, ...] | None = None,
    doccls: type | None = None,
    prepend_cls_bases: bool = True,
    cache: bool | str = True,
) -> type: ...

def dynamic_class_internal(
    name: str,
    bases: tuple[type, ...] | list[type] | Sequence[type],
    cls: type | None = None,
    reduction: tuple[object, ...] | None = None,
    doccls: type | None = None,
    prepend_cls_bases: bool = True,
) -> type: ...
