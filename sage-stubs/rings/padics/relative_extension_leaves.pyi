from sage.categories.morphism import Morphism
from sage.rings.integer import Integer
from sage.rings.padics.eisenstein_extension_generic import EisensteinExtensionGeneric
from sage.rings.padics.generic_nodes import (
    pAdicCappedAbsoluteRingGeneric,
    pAdicCappedRelativeFieldGeneric,
    pAdicCappedRelativeRingGeneric,
    pAdicFixedModRingGeneric,
    pAdicFloatingPointFieldGeneric,
    pAdicFloatingPointRingGeneric,
)
from sage.rings.padics.padic_generic_element import pAdicGenericElement
from sage.rings.ring import Ring
from sage.structure.parent import ElementConstructorInput

class pAdicRelativeBaseringInjection(Morphism):
    def __init__(
        self, R: Ring, S: pAdicGenericElement | ElementConstructorInput
    ) -> None: ...
    def section(self) -> Morphism: ...
    def _call_(
        self, x: pAdicGenericElement | ElementConstructorInput
    ) -> pAdicGenericElement: ...

class pAdicRelativeBaseringSection(Morphism):
    def __init__(
        self, S: pAdicGenericElement | ElementConstructorInput, R: Ring
    ) -> None: ...
    def _call_(
        self, x: pAdicGenericElement | ElementConstructorInput
    ) -> pAdicGenericElement: ...

class RelativeRamifiedExtensionRingFixedMod(
    EisensteinExtensionGeneric, pAdicFixedModRingGeneric
):
    def __init__(
        self,
        exact_modulus: ElementConstructorInput,
        approx_modulus: ElementConstructorInput,
        prec: int | Integer,
        print_mode: ElementConstructorInput,
        shift_seed: ElementConstructorInput,
        names: str | tuple[str, ...],
        implementation: str,
    ) -> None: ...

class RelativeRamifiedExtensionRingCappedAbsolute(
    EisensteinExtensionGeneric, pAdicCappedAbsoluteRingGeneric
):
    def __init__(
        self,
        exact_modulus: ElementConstructorInput,
        approx_modulus: ElementConstructorInput,
        prec: int | Integer,
        print_mode: ElementConstructorInput,
        shift_seed: ElementConstructorInput,
        names: str | tuple[str, ...],
        implementation: str,
    ) -> None: ...

class RelativeRamifiedExtensionRingCappedRelative(
    EisensteinExtensionGeneric, pAdicCappedRelativeRingGeneric
):
    def __init__(
        self,
        exact_modulus: ElementConstructorInput,
        approx_modulus: ElementConstructorInput,
        prec: int | Integer,
        print_mode: ElementConstructorInput,
        shift_seed: ElementConstructorInput,
        names: str | tuple[str, ...],
        implementation: str,
    ) -> None: ...

class RelativeRamifiedExtensionFieldCappedRelative(
    EisensteinExtensionGeneric, pAdicCappedRelativeFieldGeneric
):
    def __init__(
        self,
        exact_modulus: ElementConstructorInput,
        approx_modulus: ElementConstructorInput,
        prec: int | Integer,
        print_mode: ElementConstructorInput,
        shift_seed: ElementConstructorInput,
        names: str | tuple[str, ...],
        implementation: str,
    ) -> None: ...

class RelativeRamifiedExtensionRingFloatingPoint(
    EisensteinExtensionGeneric, pAdicFloatingPointRingGeneric
):
    def __init__(
        self,
        exact_modulus: ElementConstructorInput,
        approx_modulus: ElementConstructorInput,
        prec: int | Integer,
        print_mode: ElementConstructorInput,
        shift_seed: ElementConstructorInput,
        names: str | tuple[str, ...],
        implementation: str,
    ) -> None: ...

class RelativeRamifiedExtensionFieldFloatingPoint(
    EisensteinExtensionGeneric, pAdicFloatingPointFieldGeneric
):
    def __init__(
        self,
        exact_modulus: ElementConstructorInput,
        approx_modulus: ElementConstructorInput,
        prec: int | Integer,
        print_mode: ElementConstructorInput,
        shift_seed: ElementConstructorInput,
        names: str | tuple[str, ...],
        implementation: str,
    ) -> None: ...
