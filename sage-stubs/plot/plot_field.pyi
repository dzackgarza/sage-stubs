import builtins

class _SageObject: ...

class PlotField:
    def __init__(
        self,
        xpos_array: builtins.object,
        ypos_array: builtins.object,
        xvec_array: builtins.object,
        yvec_array: builtins.object,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...

def plot_vector_field(
    self, xrange: builtins.object, yrange: builtins.object, **options: builtins.object
) -> _SageObject: ...
def plot_slope_field(
    self, xrange: builtins.object, yrange: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
