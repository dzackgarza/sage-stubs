from typing import Self

class LazyFormat(str):
    _args: str | float | tuple[str | float, ...] | list[str | float]
    def __mod__(self, args: str | float | tuple[str | float, ...] | list[str | float]) -> Self: ...
