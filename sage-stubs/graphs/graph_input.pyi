import builtins

class _SageObject: ...

def from_graph6(self, g6_string: builtins.object) -> _SageObject: ...
def from_sparse6(self, g6_string: builtins.object) -> _SageObject: ...
def from_dig6(self, dig6_string: builtins.object) -> _SageObject: ...
def from_seidel_adjacency_matrix(self, M: builtins.int) -> _SageObject: ...
def from_adjacency_matrix(
    self,
    M: builtins.int,
    loops: builtins.bool = ...,
    multiedges: builtins.bool = ...,
    weighted: builtins.bool = ...,
) -> _SageObject: ...
def from_incidence_matrix(
    self,
    M: builtins.int,
    loops: builtins.bool = ...,
    multiedges: builtins.bool = ...,
    weighted: builtins.bool = ...,
) -> _SageObject: ...
def from_oriented_incidence_matrix(
    self,
    M: builtins.int,
    loops: builtins.bool = ...,
    multiedges: builtins.bool = ...,
    weighted: builtins.bool = ...,
) -> _SageObject: ...
def from_dict_of_dicts(
    self,
    M: builtins.int,
    loops: builtins.bool = ...,
    multiedges: builtins.bool = ...,
    weighted: builtins.bool = ...,
    convert_empty_dict_labels_to_None: builtins.bool = ...,
) -> _SageObject: ...
def from_dict_of_lists(
    self,
    D: builtins.object,
    loops: builtins.bool = ...,
    multiedges: builtins.bool = ...,
    weighted: builtins.bool = ...,
) -> _SageObject: ...
def from_networkx_graph(
    self,
    gnx: builtins.object,
    weighted: builtins.object = ...,
    loops: builtins.object = ...,
    multiedges: builtins.object = ...,
    convert_empty_dict_labels_to_None: builtins.object = ...,
) -> _SageObject: ...
