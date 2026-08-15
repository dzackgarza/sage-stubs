# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

ancestors_of_associahedron: _SageObject
def Associahedron(cartan_type: builtins.object, backend: builtins.str = ...) -> _SageObject: ...

class Associahedron_class_base:
    def __new__(typ: builtins.object, parent: builtins.object = ..., Vrep: builtins.object = ..., Hrep: builtins.object = ..., cartan_type: builtins.object = ..., **kwds: builtins.object) -> Self: ...
    def __init__(self, parent: builtins.object, Vrep: builtins.object, Hrep: builtins.object, cartan_type: builtins.object = ..., **kwds: builtins.object) -> None: ...
    def cartan_type(self) -> _SageObject: ...
    def vertices_in_root_space(self) -> _SageObject: ...

class Associahedron_class_ppl:
    ...

class Associahedron_class_normaliz:
    ...

class Associahedron_class_cdd:
    ...

class Associahedron_class_polymake:
    ...

class Associahedron_class_field:
    ...

def Associahedra(base_ring: builtins.object, ambient_dim: builtins.object, backend: builtins.str = ...) -> _SageObject: ...

class Associahedra_base:
    ...

class Associahedra_ppl:
    Element: _SageObject

class Associahedra_normaliz:
    Element: _SageObject

class Associahedra_cdd:
    Element: _SageObject

class Associahedra_polymake:
    Element: _SageObject

class Associahedra_field:
    Element: _SageObject
