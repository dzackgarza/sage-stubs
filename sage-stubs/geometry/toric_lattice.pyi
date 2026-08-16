import builtins

from sage.structure.element import Element

class _SageObject: ...

class ToricLatticeFactory:
    def create_key(
        self,
        rank: builtins.int,
        name: builtins.str = ...,
        dual_name: builtins.str = ...,
        latex_name: builtins.str = ...,
        latex_dual_name: builtins.str = ...,
    ) -> _SageObject: ...
    def create_object(
        self, version: builtins.object, key: builtins.object
    ) -> _SageObject: ...

ToricLattice: _SageObject

class ToricLattice_generic:
    Element: _SageObject

    def __call__(
        self, *args: builtins.object, **kwds: builtins.object
    ) -> _SageObject: ...
    def __contains__(self, point: object) -> bool: ...
    def construction(self) -> _SageObject: ...
    def direct_sum(self, other: builtins.object) -> _SageObject: ...
    def intersection(self, other: builtins.object) -> _SageObject: ...
    def quotient(
        self,
        sub: builtins.object,
        check: builtins.bool = ...,
        positive_point: builtins.object = ...,
        positive_dual_point: builtins.object = ...,
        **kwds: builtins.object,
    ) -> _SageObject: ...
    def saturation(self) -> _SageObject: ...
    def span(
        self,
        gens: builtins.object,
        base_ring: builtins.object = ...,
        *args: builtins.object,
        **kwds: builtins.object,
    ) -> _SageObject: ...
    def span_of_basis(
        self,
        basis: builtins.object,
        base_ring: builtins.object = ...,
        *args: builtins.object,
        **kwds: builtins.object,
    ) -> _SageObject: ...

class ToricLattice_ambient:
    Element: _SageObject

    def __init__(
        self,
        rank: builtins.int,
        name: builtins.str,
        dual_name: builtins.str,
        latex_name: builtins.str,
        latex_dual_name: builtins.str,
    ) -> None: ...
    def __richcmp__(
        self, other: builtins.object, op: builtins.object
    ) -> _SageObject: ...
    def ambient_module(self) -> _SageObject: ...
    def dual(self) -> _SageObject: ...
    def plot(self, **options: builtins.object) -> _SageObject: ...

class ToricLattice_sublattice_with_basis:
    def dual(self) -> _SageObject: ...
    def plot(self, **options: builtins.object) -> _SageObject: ...

class ToricLattice_sublattice: ...

class ToricLattice_quotient_element:
    def set_immutable(self) -> _SageObject: ...

class ToricLattice_quotient:
    def __init__(
        self,
        V: builtins.object,
        W: builtins.object,
        check: builtins.bool = ...,
        positive_point: builtins.object = ...,
        positive_dual_point: builtins.object = ...,
        **kwds: builtins.object,
    ) -> None: ...
    def gens(self) -> tuple[Element, ...]: ...
    Element: _SageObject

    def base_extend(self, R: builtins.int) -> _SageObject: ...
    def is_torsion_free(self) -> builtins.bool: ...
    def dual(self) -> _SageObject: ...
    def rank(self) -> _SageObject: ...
    dimension: _SageObject

    def coordinate_vector(
        self, x: builtins.object, reduce: builtins.bool = ...
    ) -> _SageObject: ...
