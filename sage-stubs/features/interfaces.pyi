import builtins

class _SageObject: ...

class InterfaceFeature:
    @staticmethod
    def __classcall__(
        cls: builtins.object,
        name: builtins.str,
        module: builtins.object,
        description: builtins.object = ...,
    ) -> _SageObject: ...
    def __init__(
        self, name: builtins.str, module: builtins.object, description: builtins.object
    ) -> None: ...

class Mathics:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class Regina:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class Magma:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class Matlab:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class Mathematica:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class Maple:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class Macaulay2:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class Octave:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

class Scilab:
    @staticmethod
    def __classcall__(cls: builtins.object) -> _SageObject: ...

def all_features(self) -> _SageObject: ...
