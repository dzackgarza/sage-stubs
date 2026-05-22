from collections.abc import Callable

class ArgumentFixer:
    f: Callable[..., object]
    _nargs: int
    _ndefault: int
    _arg_names: tuple[str, ...]
    _classmethod: bool
    _defaults: dict[str, object]
    _default_tuple: tuple[object, ...]

    def __init__(self, f: Callable[..., object], classmethod: bool = False) -> None: ...
    def fix_to_named(self, *args: object, **kwargs: object) -> tuple[tuple[object, ...], tuple[tuple[str, object], ...]]: ...
    def fix_to_pos(self, *args: object, **kwds: object) -> tuple[tuple[object, ...], tuple[tuple[str, object], ...]]: ...
