import builtins

class _SageObject: ...

class Gnuplot:
    def gnuplot(self) -> _SageObject: ...
    def __call__(self, line: builtins.object) -> _SageObject: ...
    def plot(
        self,
        cmd: builtins.object,
        file: builtins.object = ...,
        verbose: builtins.bool = ...,
        reset: builtins.bool = ...,
    ) -> _SageObject: ...
    def plot3d(
        self,
        f: builtins.object,
        xmin: builtins.object = ...,
        xmax: builtins.int = ...,
        ymin: builtins.object = ...,
        ymax: builtins.int = ...,
        zmin: builtins.object = ...,
        zmax: builtins.int = ...,
        title: builtins.object = ...,
        samples: builtins.int = ...,
        isosamples: builtins.int = ...,
        xlabel: builtins.str = ...,
        ylabel: builtins.str = ...,
        interact: builtins.bool = ...,
    ) -> _SageObject: ...
    def plot3d_parametric(
        self,
        f: builtins.str = ...,
        range1: builtins.str = ...,
        range2: builtins.str = ...,
        samples: builtins.int = ...,
        title: builtins.object = ...,
        interact: builtins.bool = ...,
    ) -> _SageObject: ...
    def interact(self, cmd: builtins.object) -> _SageObject: ...
    def console(self) -> _SageObject: ...

gnuplot: _SageObject

def gnuplot_console(self) -> _SageObject: ...
