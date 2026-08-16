import builtins

from sage.manifolds.differentiable.symplectic_form import SymplecticForm

class _SageObject: ...

class StandardSymplecticSpace:
    def __init__(
        self,
        dimension: builtins.int,
        name: builtins.str = ...,
        latex_name: builtins.str = ...,
        coordinates: builtins.str = ...,
        symbols: builtins.object = ...,
        symplectic_name: builtins.str = ...,
        symplectic_latex_name: builtins.str = ...,
        start_index: builtins.int = ...,
        base_manifold: builtins.object = ...,
        names: builtins.object = ...,
    ) -> None: ...
    def symplectic_form(self) -> SymplecticForm: ...
