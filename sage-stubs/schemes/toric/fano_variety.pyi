import builtins

class _SageObject: ...

DEFAULT_COEFFICIENT: _SageObject
DEFAULT_COEFFICIENTS: _SageObject

def CPRFanoToricVariety(
    self=...,
    Delta_polar: builtins.object = ...,
    coordinate_points: builtins.object = ...,
    charts: builtins.object = ...,
    coordinate_names: builtins.object = ...,
    names: builtins.object = ...,
    coordinate_name_indices: builtins.object = ...,
    make_simplicial: builtins.bool = ...,
    base_ring: builtins.object = ...,
    base_field: builtins.object = ...,
    check: builtins.bool = ...,
) -> _SageObject: ...

class CPRFanoToricVariety_field:
    def __init__(
        self,
        Delta_polar: builtins.object,
        fan: builtins.object,
        coordinate_points: builtins.object,
        point_to_ray: builtins.object,
        coordinate_names: builtins.object,
        coordinate_name_indices: builtins.object,
        base_field: builtins.object,
    ) -> None: ...
    def anticanonical_hypersurface(self, **kwds: builtins.object) -> _SageObject: ...
    def change_ring(self, F: builtins.object) -> _SageObject: ...
    def coordinate_point_to_coordinate(self, point: builtins.object) -> _SageObject: ...
    def coordinate_points(self) -> _SageObject: ...
    def Delta(self) -> _SageObject: ...
    def Delta_polar(self) -> _SageObject: ...
    def nef_complete_intersection(
        self, nef_partition: builtins.object, **kwds: builtins.object
    ) -> _SageObject: ...
    def cartesian_product(
        self,
        other: builtins.object,
        coordinate_names: builtins.object = ...,
        coordinate_indices: builtins.object = ...,
    ) -> _SageObject: ...
    def resolve(self, **kwds: builtins.object) -> _SageObject: ...

class AnticanonicalHypersurface:
    def __init__(
        self,
        P_Delta: builtins.object,
        monomial_points: builtins.object = ...,
        coefficient_names: builtins.object = ...,
        coefficient_name_indices: builtins.object = ...,
        coefficients: builtins.object = ...,
    ) -> None: ...

class NefCompleteIntersection:
    def __init__(
        self,
        P_Delta: builtins.object,
        nef_partition: builtins.object,
        monomial_points: builtins.str = ...,
        coefficient_names: builtins.object = ...,
        coefficient_name_indices: builtins.object = ...,
        coefficients: builtins.object = ...,
    ) -> None: ...
    def cohomology_class(self) -> _SageObject: ...
    def nef_partition(self) -> _SageObject: ...

def add_variables(self, variables: builtins.object) -> _SageObject: ...
