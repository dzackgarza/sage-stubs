from sage.rings.integer import Integer
from sage.rings.padics.eisenstein_extension_generic import EisensteinExtensionGeneric
from sage.rings.padics.padic_generic import pAdicGeneric
from sage.rings.padics.padic_generic_element import pAdicGenericElement
from sage.rings.padics.unramified_extension_generic import UnramifiedExtensionGeneric
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Ring

class pAdicCappedAbsoluteRingGeneric: ...
class pAdicCappedRelativeFieldGeneric: ...
class pAdicCappedRelativeRingGeneric: ...
class pAdicFixedModRingGeneric: ...
class pAdicFloatingPointFieldGeneric: ...
class pAdicFloatingPointRingGeneric: ...

class UnramifiedExtensionRingCappedRelative(
    UnramifiedExtensionGeneric, pAdicCappedRelativeRingGeneric
):
    def __init__(
        self,
        exact_modulus: int | Integer,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: int | Integer,
        shift_seed: int | Integer,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...

class UnramifiedExtensionFieldCappedRelative(
    UnramifiedExtensionGeneric, pAdicCappedRelativeFieldGeneric
):
    def __init__(
        self,
        exact_modulus: Polynomial | MPolynomial,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: Polynomial | MPolynomial,
        shift_seed: Polynomial | MPolynomial,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...
    def _coerce_map_from_(self, R: Ring) -> pAdicGenericElement: ...

class UnramifiedExtensionRingCappedAbsolute(
    UnramifiedExtensionGeneric, pAdicCappedAbsoluteRingGeneric
):
    def __init__(
        self,
        exact_modulus: int | Integer,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: int | Integer,
        shift_seed: int | Integer,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...

class UnramifiedExtensionRingFixedMod(
    UnramifiedExtensionGeneric, pAdicFixedModRingGeneric
):
    def __init__(
        self,
        exact_modulus: int | Integer,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: int | Integer,
        shift_seed: int | Integer,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...

class UnramifiedExtensionRingFloatingPoint(
    UnramifiedExtensionGeneric, pAdicFloatingPointRingGeneric
):
    def __init__(
        self,
        exact_modulus: int | Integer,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: int | Integer,
        shift_seed: int | Integer,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...

class UnramifiedExtensionFieldFloatingPoint(
    UnramifiedExtensionGeneric, pAdicFloatingPointFieldGeneric
):
    def __init__(
        self,
        exact_modulus: Polynomial | MPolynomial,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: Polynomial | MPolynomial,
        shift_seed: Polynomial | MPolynomial,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...
    def _coerce_map_from_(self, R: Ring) -> pAdicGenericElement: ...

class EisensteinExtensionRingCappedRelative(
    EisensteinExtensionGeneric, pAdicCappedRelativeRingGeneric
):
    def __init__(
        self,
        exact_modulus: int | Integer,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: int | Integer,
        shift_seed: int | Integer,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...

class EisensteinExtensionFieldCappedRelative(
    EisensteinExtensionGeneric, pAdicCappedRelativeFieldGeneric
):
    def __init__(
        self,
        exact_modulus: Polynomial | MPolynomial,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: Polynomial | MPolynomial,
        shift_seed: Polynomial | MPolynomial,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...

class EisensteinExtensionRingCappedAbsolute(
    EisensteinExtensionGeneric, pAdicCappedAbsoluteRingGeneric
):
    def __init__(
        self,
        exact_modulus: int | Integer,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: int | Integer,
        shift_seed: int | Integer,
        names: str | tuple[str, ...],
        implementation: str,
    ) -> None: ...

class EisensteinExtensionRingFixedMod(
    EisensteinExtensionGeneric, pAdicFixedModRingGeneric
):
    def __init__(
        self,
        exact_modulus: int | Integer,
        poly: Polynomial | MPolynomial,
        prec: int | Integer,
        print_mode: int | Integer,
        shift_seed: int | Integer,
        names: str | tuple[str, ...],
        implementation: str = ...,
    ) -> None: ...
    def fraction_field(self) -> pAdicGeneric: ...
