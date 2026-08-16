import builtins

class _SageObject: ...

def list_plot3d(
    self,
    interpolation_type: builtins.str = ...,
    point_list: builtins.object = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def list_plot3d_matrix(self, **kwds: builtins.object) -> _SageObject: ...
def list_plot3d_array_of_arrays(
    self, interpolation_type: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def list_plot3d_tuples(
    self, interpolation_type: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
