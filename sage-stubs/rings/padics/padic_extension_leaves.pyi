import builtins

class _SageObject: ...

class UnramifiedExtensionRingCappedRelative:
    prime_pow: PowComputer_ext_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...

class UnramifiedExtensionFieldCappedRelative:
    prime_pow: PowComputer_ext_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...

class UnramifiedExtensionRingCappedAbsolute:
    prime_pow: PowComputer_ext_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...

class UnramifiedExtensionRingFixedMod:
    prime_pow: PowComputer_flint_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...

class UnramifiedExtensionRingFloatingPoint:
    prime_pow: PowComputer_flint_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...

class UnramifiedExtensionFieldFloatingPoint:
    prime_pow: PowComputer_flint_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...

class EisensteinExtensionRingCappedRelative:
    prime_pow: PowComputer_ext_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...

class EisensteinExtensionFieldCappedRelative:
    prime_pow: PowComputer_ext_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...

class EisensteinExtensionRingCappedAbsolute:
    prime_pow: PowComputer_ext_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str,
    ) -> None: ...

class EisensteinExtensionRingFixedMod:
    prime_pow: PowComputer_ext_maker

    def __init__(
        self,
        exact_modulus: builtins.object,
        poly: builtins.object,
        prec: builtins.int,
        print_mode: builtins.object,
        shift_seed: builtins.object,
        names: builtins.object,
        implementation: builtins.str = ...,
    ) -> None: ...
    def fraction_field(self) -> _SageObject: ...
