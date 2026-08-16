import builtins

class _SageObject: ...

def ChessboardGraphGenerator(
    self,
    rook: builtins.bool = ...,
    rook_radius: builtins.object = ...,
    bishop: builtins.bool = ...,
    bishop_radius: builtins.object = ...,
    knight: builtins.bool = ...,
    knight_x: builtins.int = ...,
    knight_y: builtins.int = ...,
    relabel: builtins.bool = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def QueenGraph(
    self,
    radius: builtins.object = ...,
    relabel: builtins.bool = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def KingGraph(
    self,
    radius: builtins.object = ...,
    relabel: builtins.bool = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def KnightGraph(
    self,
    one: builtins.int = ...,
    two: builtins.int = ...,
    relabel: builtins.bool = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RookGraph(
    self,
    radius: builtins.object = ...,
    relabel: builtins.bool = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def BishopGraph(
    self,
    radius: builtins.object = ...,
    relabel: builtins.bool = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
