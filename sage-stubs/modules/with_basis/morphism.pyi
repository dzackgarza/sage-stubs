from collections.abc import Callable
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement

class ModuleMorphism:
    def __init__(
        self,
        domain: object,
        codomain: object = ...,
        category: object = ...,
        affine: bool = ...,
    ) -> None: ...
    def __call__(self, x: IndexedFreeModuleElement) -> object: ...

class ModuleMorphismFromFunction(ModuleMorphism):
    def __init__(
        self,
        domain: object,
        codomain: object,
        function: Callable[[object], object],
        category: object = ...,
    ) -> None: ...

class ModuleMorphismByLinearity(ModuleMorphism):
    def __init__(
        self,
        domain: object,
        codomain: object = ...,
        on_basis: Callable[[object], object] | None = ...,
        category: object = ...,
    ) -> None: ...

class TriangularModuleMorphism(ModuleMorphism):
    def __init__(
        self,
        domain: object,
        codomain: object = ...,
        on_basis: Callable[[object], object] | None = ...,
        category: object = ...,
        unitriangular: str = ...,
    ) -> None: ...

class TriangularModuleMorphismByLinearity(ModuleMorphismByLinearity, TriangularModuleMorphism):
    ...
