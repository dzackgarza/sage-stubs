import builtins

from sage.combinat.crystals.tensor_product import TensorProductOfCrystals

class _SageObject: ...

def HighestWeightCrystal(self, model: builtins.object = ...) -> _SageObject: ...

class FiniteDimensionalHighestWeightCrystal_TypeE:
    def __init__(self, dominant_weight: builtins.object) -> None: ...
    Element: _SageObject

    def module_generator(self) -> _SageObject: ...

class FiniteDimensionalHighestWeightCrystal_TypeE6:
    column_crystal: dict[int, TensorProductOfCrystals]

    def __init__(self, dominant_weight: builtins.object) -> None: ...

class FiniteDimensionalHighestWeightCrystal_TypeE7:
    column_crystal: dict[int, TensorProductOfCrystals]

    def __init__(self, dominant_weight: builtins.object) -> None: ...
