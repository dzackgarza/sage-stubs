import builtins
from collections.abc import (
    Hashable,
)

from sage.structure.element import Element

class _SageObject: ...

class ChowRingIdeal:
    def matroid(self) -> _SageObject: ...
    def flats_to_generator_dict(self) -> dict[Hashable, Element]: ...

class ChowRingIdeal_nonaug_fy:
    def __init__(self, M: builtins.int, R: builtins.int) -> None: ...
    def groebner_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def normal_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...

class ChowRingIdeal_nonaug_af:
    def __init__(self, M: builtins.int, R: builtins.int) -> None: ...
    def groebner_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def normal_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...

class ChowRingIdeal_nonaug_sp:
    def __init__(self, M: builtins.int, R: builtins.int) -> None: ...
    def groebner_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def normal_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...

class AugmentedChowRingIdeal_fy:
    def __init__(self, M: builtins.int, R: builtins.int) -> None: ...
    def groebner_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def normal_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...

class AugmentedChowRingIdeal_atom_free:
    def __init__(self, M: builtins.int, R: builtins.int) -> None: ...
    def groebner_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def normal_basis(
        self,
        algorithm: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
