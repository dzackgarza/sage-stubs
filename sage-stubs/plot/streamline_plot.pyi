import builtins

class _SageObject: ...

class StreamlinePlot:
    def __init__(
        self,
        xpos_array: builtins.object,
        ypos_array: builtins.object,
        xvec_array: builtins.object,
        yvec_array: builtins.object,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...

def streamline_plot(
    self, xrange: builtins.object, yrange: builtins.object, **options: builtins.object
) -> _SageObject: ...
