import builtins

class _SageObject: ...

class ContourPlot:
    def __init__(
        self,
        xy_data_array: builtins.object,
        xrange: builtins.object,
        yrange: builtins.object,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...

def contour_plot(
    self, xrange: builtins.object, yrange: builtins.object, **options: builtins.object
) -> _SageObject: ...
def implicit_plot(
    self, xrange: builtins.object, yrange: builtins.object, **options: builtins.object
) -> _SageObject: ...
def region_plot(
    self, xrange: builtins.object, yrange: builtins.object, **options: builtins.object
) -> _SageObject: ...
def equify(self) -> _SageObject: ...
