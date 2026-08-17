from sage.categories.category import Category
from sage.rings.integer import Integer
from sage.rings.padics.generic_nodes import (
    pAdicCappedAbsoluteRingGeneric,
    pAdicCappedRelativeFieldGeneric,
    pAdicCappedRelativeRingGeneric,
    pAdicFieldBaseGeneric,
    pAdicFixedModRingGeneric,
    pAdicFloatingPointFieldGeneric,
    pAdicFloatingPointRingGeneric,
    pAdicLatticeGeneric,
    pAdicRelaxedGeneric,
    pAdicRingBaseGeneric,
)
from sage.rings.padics.padic_generic_element import pAdicGenericElement
from sage.rings.ring import Ring
from sage.structure.parent import ElementConstructorInput

class pAdicRingCappedRelative(pAdicRingBaseGeneric, pAdicCappedRelativeRingGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        print_mode: Ring,
        names: str | tuple[str, ...],
        category: Category = ...,
    ) -> None: ...
    def _coerce_map_from_(self, R: Ring) -> bool: ...

class pAdicRingCappedAbsolute(pAdicRingBaseGeneric, pAdicCappedAbsoluteRingGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        print_mode: Ring,
        names: str | tuple[str, ...],
        category: Category = ...,
    ) -> None: ...
    def _coerce_map_from_(self, R: Ring) -> bool: ...
    def _magma_init_(self, magma: ElementConstructorInput) -> str: ...

class pAdicRingFloatingPoint(pAdicRingBaseGeneric, pAdicFloatingPointRingGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        print_mode: Ring,
        names: str | tuple[str, ...],
        category: Category = ...,
    ) -> None: ...
    def _coerce_map_from_(self, R: Ring) -> bool: ...

class pAdicRingFixedMod(pAdicRingBaseGeneric, pAdicFixedModRingGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        print_mode: Ring,
        names: str | tuple[str, ...],
        category: Category = ...,
    ) -> None: ...
    def _coerce_map_from_(self, R: Ring) -> bool: ...
    def _magma_init_(self, magma: ElementConstructorInput) -> str: ...

class pAdicFieldCappedRelative(pAdicFieldBaseGeneric, pAdicCappedRelativeFieldGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        print_mode: Ring,
        names: str | tuple[str, ...],
        category: Category = ...,
    ) -> None: ...
    def random_element(self, algorithm: str = ...) -> pAdicGenericElement: ...
    def _coerce_map_from_(self, R: Ring) -> bool: ...
    def _magma_init_(self, magma: ElementConstructorInput) -> str: ...

class pAdicFieldFloatingPoint(pAdicFieldBaseGeneric, pAdicFloatingPointFieldGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        print_mode: Ring,
        names: str | tuple[str, ...],
        category: Category = ...,
    ) -> None: ...
    def _coerce_map_from_(self, R: Ring) -> bool: ...

class pAdicRingLattice(pAdicLatticeGeneric, pAdicRingBaseGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        subtype: ElementConstructorInput,
        print_mode: ElementConstructorInput,
        names: str | tuple[str, ...],
        label: ElementConstructorInput = ...,
        category: Category = ...,
    ) -> None: ...
    def random_element(self, prec: int | Integer = ...) -> pAdicGenericElement: ...
    def _coerce_map_from_(self, R: Ring) -> bool: ...

class pAdicFieldLattice(pAdicLatticeGeneric, pAdicFieldBaseGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        subtype: ElementConstructorInput,
        print_mode: ElementConstructorInput,
        names: str | tuple[str, ...],
        label: ElementConstructorInput = ...,
        category: Category = ...,
    ) -> None: ...
    def random_element(
        self, prec: int | Integer = ..., integral: bool = ...
    ) -> pAdicGenericElement: ...
    def _coerce_map_from_(self, R: Ring) -> bool: ...

class pAdicRingRelaxed(pAdicRelaxedGeneric, pAdicRingBaseGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        print_mode: ElementConstructorInput,
        names: str | tuple[str, ...],
        category: Category = ...,
    ) -> None: ...

class pAdicFieldRelaxed(pAdicRelaxedGeneric, pAdicFieldBaseGeneric):
    def __init__(
        self,
        p: int | Integer,
        prec: int | Integer,
        print_mode: ElementConstructorInput,
        names: str | tuple[str, ...],
        category: Category = ...,
    ) -> None: ...
