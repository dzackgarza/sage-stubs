# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

def Polyhedra(ambient_space_or_base_ring: builtins.object = ..., ambient_dim: builtins.object = ..., backend: builtins.object = ..., *, ambient_space: builtins.object = ..., base_ring: builtins.object = ...) -> _SageObject: ...

class Polyhedra_base:
    def __init__(self, base_ring: builtins.object, ambient_dim: builtins.object, backend: builtins.object) -> None: ...
    def list(self) -> _SageObject: ...
    def recycle(self, polyhedron: builtins.object) -> _SageObject: ...
    def ambient_dim(self) -> _SageObject: ...
    def backend(self) -> _SageObject: ...
    def an_element(self) -> _SageObject: ...
    def some_elements(self) -> _SageObject: ...
    def zero(self) -> _SageObject: ...
    def empty(self) -> _SageObject: ...
    def universe(self) -> _SageObject: ...
    def Vrepresentation_space(self) -> _SageObject: ...
    ambient_space: _SageObject
    def Hrepresentation_space(self) -> _SageObject: ...
    def base_extend(self, base_ring: builtins.object, backend: builtins.object = ..., ambient_dim: builtins.object = ...) -> _SageObject: ...
    def change_ring(self, base_ring: builtins.object, backend: builtins.object = ..., ambient_dim: builtins.object = ...) -> _SageObject: ...

class Polyhedra_ZZ_ppl:
    Element: _SageObject

class Polyhedra_ZZ_normaliz:
    Element: _SageObject

class Polyhedra_QQ_ppl:
    Element: _SageObject

class Polyhedra_QQ_normaliz:
    Element: _SageObject

class Polyhedra_QQ_cdd:
    Element: _SageObject

class Polyhedra_RDF_cdd:
    Element: _SageObject

class Polyhedra_normaliz:
    Element: _SageObject

class Polyhedra_polymake:
    Element: _SageObject

class Polyhedra_field:
    Element: _SageObject

class Polyhedra_number_field:
    Element: _SageObject

def does_backend_handle_base_ring(base_ring: builtins.object, backend: builtins.object) -> _SageObject: ...
