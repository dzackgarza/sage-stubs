import builtins

class _SageObject: ...

class FunctionFieldVectorSpaceIsomorphism:
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def __hash__(self) -> int: ...

class MapVectorSpaceToFunctionField:
    def __init__(self, V: builtins.object, K: builtins.int) -> None: ...
    def domain(self) -> _SageObject: ...
    def codomain(self) -> _SageObject: ...

class MapFunctionFieldToVectorSpace:
    def __init__(self, K: builtins.int, V: builtins.object) -> None: ...

class FunctionFieldMorphism:
    def __init__(
        self,
        parent: builtins.object,
        im_gen: builtins.object,
        base_morphism: builtins.object,
    ) -> None: ...

class FunctionFieldMorphism_polymod:
    def __init__(
        self,
        parent: builtins.object,
        im_gen: builtins.object,
        base_morphism: builtins.object,
    ) -> None: ...

class FunctionFieldMorphism_rational:
    def __init__(
        self,
        parent: builtins.object,
        im_gen: builtins.object,
        base_morphism: builtins.object,
    ) -> None: ...

class FunctionFieldConversionToConstantBaseField:
    def __init__(self, parent: builtins.object) -> None: ...

class FunctionFieldToFractionField:
    def section(self) -> _SageObject: ...

class FractionFieldToFunctionField:
    def section(self) -> _SageObject: ...

class FunctionFieldCompletion:
    def __init__(
        self,
        field: builtins.object,
        place: builtins.object,
        name: builtins.str = ...,
        prec: builtins.int = ...,
        gen_name: builtins.str = ...,
    ) -> None: ...
    def default_precision(self) -> _SageObject: ...

class FunctionFieldRingMorphism: ...
class FunctionFieldLinearMap: ...
class FunctionFieldLinearMapSection: ...
