import builtins

class _SageObject: ...

class AbelianLieAlgebra:
    @staticmethod
    def __classcall_private__(
        cls: builtins.object,
        R: builtins.int,
        names: builtins.object = ...,
        index_set: builtins.object = ...,
        category: builtins.object = ...,
        **kwds: builtins.object,
    ) -> _SageObject: ...
    def __init__(
        self,
        R: builtins.int,
        names: builtins.object,
        index_set: builtins.object,
        category: builtins.object,
        **kwds: builtins.object,
    ) -> None: ...
    def is_abelian(self) -> bool: ...
    is_nilpotent: _SageObject
    is_solvable: _SageObject

    class Element: ...

class InfiniteDimensionalAbelianLieAlgebra:
    def __init__(
        self,
        R: builtins.int,
        index_set: builtins.object,
        prefix: builtins.str = ...,
        **kwds: builtins.object,
    ) -> None: ...
    def dimension(self) -> _SageObject: ...
    def is_abelian(self) -> bool: ...
    is_nilpotent: _SageObject
    is_solvable: _SageObject

    class Element: ...
