
from sage.modular.modform_hecketriangle.abstract_space import FormsSpace_abstract
from sage.modular.modform_hecketriangle.element import FormsElement
from sage.modular.modform_hecketriangle.hecke_triangle_group_element import (
    HeckeTriangleGroupElement,
)
from sage.modular.modform_hecketriangle.hecke_triangle_groups import HeckeTriangleGroup
from sage.modules.module import Module
from sage.rings.rational import Rational
from sage.rings.ring import Ring
from sage.structure.element import Vector
from sage.structure.unique_representation import UniqueRepresentation

def canonical_parameters(
    group: HeckeTriangleGroup,
    base_ring: Ring,
    k: Rational | int,
    ep: HeckeTriangleGroupElement | int | None,
    n: int | None = ...,
) -> tuple[HeckeTriangleGroup, Ring, Rational | int, HeckeTriangleGroupElement | int | None, int | None]: ...

class QuasiMeromorphicModularForms(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> QuasiMeromorphicModularForms: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...

class QuasiWeakModularForms(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> QuasiWeakModularForms: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...

class QuasiModularForms(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> QuasiModularForms: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...
    def gens(self) -> tuple[FormsElement, ...]: ...
    def dimension(self) -> int: ...
    def coordinate_vector(self, v: FormsElement) -> Vector: ...

class QuasiCuspForms(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> QuasiCuspForms: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...
    def gens(self) -> tuple[FormsElement, ...]: ...
    def dimension(self) -> int: ...
    def coordinate_vector(self, v: FormsElement) -> Vector: ...

class MeromorphicModularForms(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> MeromorphicModularForms: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...

class WeakModularForms(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> WeakModularForms: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...

class ModularForms(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> ModularForms: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...
    def gens(self) -> tuple[FormsElement, ...]: ...
    def dimension(self) -> int: ...
    def coordinate_vector(self, v: FormsElement) -> Vector: ...

class CuspForms(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> CuspForms: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...
    def gens(self) -> tuple[FormsElement, ...]: ...
    def dimension(self) -> int: ...
    def coordinate_vector(self, v: FormsElement) -> Vector: ...

class ZeroForm(FormsSpace_abstract, Module, UniqueRepresentation):
    @classmethod
    def __classcall__(cls, *args: object, **options: object) -> ZeroForm: ...
    def __init__(
        self,
        group: HeckeTriangleGroup,
        base_ring: Ring,
        k: Rational | int,
        ep: HeckeTriangleGroupElement | int | None,
        n: int | None,
    ) -> None: ...
    def gens(self) -> tuple[()]: ...
    def dimension(self) -> int: ...
    def coordinate_vector(self, v: FormsElement) -> Vector: ...
