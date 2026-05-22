from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.geometry.polyhedron.base import Polyhedron_base
    from sage.rings.ring import Ring

def Polyhedron(vertices: object = ..., rays: object = ..., lines: object = ..., ieqs: object = ..., eqns: object = ..., ambient_dim: int | None = ..., base_ring: Ring | None = ..., minimize: bool = ..., verbose: bool = ..., backend: str | None = ..., mutable: bool = ...) -> Polyhedron_base: ...
