from collections.abc import Callable

class _lazy_attribute:
    f: Callable[[object], object]
    __name__: str
    __doc__: str | None
    __module__: str
    def __init__(self, f: Callable[[object], object]) -> None: ...
    def _sage_src_lines_(self) -> tuple[list[str], int]: ...

class lazy_attribute(_lazy_attribute):
    def __init__(self, f: Callable[[object], object]) -> None: ...

class lazy_class_attribute(_lazy_attribute): ...
