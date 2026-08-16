import builtins

class _SageObject: ...

class MatrixPlot:
    def __init__(
        self,
        xy_data_array: builtins.object,
        xrange: builtins.object,
        yrange: builtins.object,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...

def matrix_plot(
    self,
    xrange: builtins.object = ...,
    yrange: builtins.object = ...,
    **options: builtins.object,
) -> _SageObject: ...
