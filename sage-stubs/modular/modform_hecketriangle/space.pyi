import builtins

from sage.structure.element import Element

class _SageObject: ...

def canonical_parameters(
    self,
    base_ring: builtins.object,
    k: builtins.int,
    ep: builtins.object,
    n: builtins.int = ...,
) -> _SageObject: ...

class QuasiMeromorphicModularForms:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...

class QuasiWeakModularForms:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...

class QuasiModularForms:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...
    def gens(self) -> tuple[Element, ...]: ...
    def dimension(self) -> _SageObject: ...
    def coordinate_vector(self, v: builtins.object) -> _SageObject: ...

class QuasiCuspForms:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...
    def gens(self) -> tuple[Element, ...]: ...
    def dimension(self) -> _SageObject: ...
    def coordinate_vector(self, v: builtins.object) -> _SageObject: ...

class MeromorphicModularForms:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...

class WeakModularForms:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...

class ModularForms:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...
    def gens(self) -> tuple[Element, ...]: ...
    def dimension(self) -> _SageObject: ...
    def coordinate_vector(self, v: builtins.object) -> _SageObject: ...

class CuspForms:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...
    def gens(self) -> tuple[Element, ...]: ...
    def dimension(self) -> _SageObject: ...
    def coordinate_vector(self, v: builtins.object) -> _SageObject: ...

class ZeroForm:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        group: builtins.object = ...,
        base_ring: builtins.object = ...,
        k: builtins.int = ...,
        ep: builtins.object = ...,
        n: builtins.int = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        group: builtins.object,
        base_ring: builtins.object,
        k: builtins.int,
        ep: builtins.object,
        n: builtins.int,
    ) -> None: ...
    def gens(self) -> tuple[Element, ...]: ...
    def dimension(self) -> _SageObject: ...
    def coordinate_vector(self, v: builtins.object) -> _SageObject: ...
