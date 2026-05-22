from collections.abc import Iterable
from typing import overload
from sage.structure.element import Element

@overload
def lcm(a: Iterable[object], b: None = None) -> Element: ...
@overload
def lcm(a: object, b: object) -> Element: ...
def LCM_list(v: Iterable[object]) -> Element: ...

