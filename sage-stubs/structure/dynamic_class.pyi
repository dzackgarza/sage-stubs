def dynamic_class(
    name: str,
    bases: tuple[type, ...],
    cls: type | None = None,
    reduction: tuple[object, ...] | None = None,
    doccls: type | None = None,
    prepend_cls_bases: bool = True,
    cache: bool | str = True,
) -> type: ...
