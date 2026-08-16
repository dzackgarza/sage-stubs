import builtins

from sage.rings.padics.pow_computer_relative import PowComputer_relative_maker

class _SageObject: ...

class pAdicRelativeBaseringInjection:
    def __init__(self, R: builtins.int, S: builtins.object) -> None: ...
    def section(self) -> _SageObject: ...

class pAdicRelativeBaseringSection:
    def __init__(self, S: builtins.object, R: builtins.int) -> None: ...

class RelativeRamifiedExtensionRingFixedMod:
    prime_pow: PowComputer_relative_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        approx_modulus: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str,
    ) -> None: ...

class RelativeRamifiedExtensionRingCappedAbsolute:
    prime_pow: PowComputer_relative_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        approx_modulus: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str,
    ) -> None: ...

class RelativeRamifiedExtensionRingCappedRelative:
    prime_pow: PowComputer_relative_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        approx_modulus: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str,
    ) -> None: ...

class RelativeRamifiedExtensionFieldCappedRelative:
    prime_pow: PowComputer_relative_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        approx_modulus: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str,
    ) -> None: ...

class RelativeRamifiedExtensionRingFloatingPoint:
    prime_pow: PowComputer_relative_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        approx_modulus: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str,
    ) -> None: ...

class RelativeRamifiedExtensionFieldFloatingPoint:
    prime_pow: PowComputer_relative_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        approx_modulus: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str,
    ) -> None: ...
