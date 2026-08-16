import builtins

from sage.graphs.digraph import DiGraph

class _SageObject: ...

class HighestWeightCrystalOfTypeA:
    n: builtins.int

    def __init__(self, n: builtins.int = ...) -> None: ...

    class Element:
        def e(self, i: builtins.int) -> _SageObject: ...
        def f(self, i: builtins.int) -> _SageObject: ...

class NaiveCrystal:
    G: DiGraph
    n: int

    def __init__(self) -> None: ...

    class Element:
        def e(self, i: builtins.int) -> _SageObject: ...
        def f(self, i: builtins.int) -> _SageObject: ...
