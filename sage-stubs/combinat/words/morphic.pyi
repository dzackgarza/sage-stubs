import builtins
from collections.abc import Iterator

from sage.structure.element import Element

class _SageObject: ...

class WordDatatype_morphic:
    def __init__(
        self,
        parent: builtins.object,
        morphism: builtins.object,
        letter: builtins.object,
        coding: builtins.object = ...,
        length: builtins.int = ...,
    ) -> None: ...
    def __reduce__(self) -> tuple[Element, ...]: ...
    def representation(self, n: builtins.int) -> list[Element]: ...
    def __iter__(self) -> Iterator[Element]: ...
