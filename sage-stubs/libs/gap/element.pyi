from collections.abc import Hashable
from pathlib import Path
from typing import Protocol

from sage.rings.integer import Integer
from sage.structure.element import Element, RingElement, Vector


class _SupportsLibGap(Protocol):
    def _libgap_(self) -> GapElement: ...


class _SupportsGapInit(Protocol):
    def _gap_init_(self) -> str: ...


type GapInput = (
    GapElement
    | int
    | Integer
    | str
    | Path
    | Vector
    | _SupportsLibGap
    | _SupportsGapInit
    | list[GapInput]
    | tuple[GapInput, ...]
    | dict[Hashable, GapInput]
)


class GapElement(RingElement):
    def __getattr__(self, name: str) -> GapElement_MethodProxy: ...


class ElementLibGAP(Element): ...


class GapElement_Function(GapElement):
    def __call__(self, *args: GapInput) -> GapElement | None: ...


class GapElement_MethodProxy(GapElement_Function):
    def __call__(self, *args: GapInput) -> GapElement | None: ...
