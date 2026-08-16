import builtins

class _SageObject: ...

Color: _SageObject

def input_box(
    self=...,
    label: builtins.str = ...,
    type: builtins.object = ...,
    width: builtins.int = ...,
    height: builtins.int = ...,
) -> _SageObject: ...
def slider(
    self,
    vmax: builtins.object = ...,
    step_size: builtins.object = ...,
    default: builtins.object = ...,
    label: builtins.str = ...,
    display_value: builtins.bool = ...,
    _range: builtins.bool = ...,
) -> _SageObject: ...
def range_slider(
    self, *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def checkbox(self=..., label: builtins.str = ...) -> _SageObject: ...
def selector(
    self,
    label: builtins.str = ...,
    default: builtins.object = ...,
    nrows: builtins.object = ...,
    ncols: builtins.object = ...,
    width: builtins.object = ...,
    buttons: builtins.bool = ...,
) -> _SageObject: ...
def input_grid(
    self,
    ncols: builtins.object,
    default: builtins.object = ...,
    label: builtins.str = ...,
    to_value: builtins.object = ...,
    width: builtins.int = ...,
) -> _SageObject: ...
def color_selector(
    self=...,
    label: builtins.str = ...,
    widget: builtins.object = ...,
    hide_box: builtins.bool = ...,
) -> _SageObject: ...
