from typing import TYPE_CHECKING, Literal
from sage.rings.integer import Integer
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class, AbelianGroup_subgroup

if TYPE_CHECKING:
    from sage.rings.number_field.number_field import NumberField
    from sage.groups.perm_gps.permgroup import PermutationGroup
    from sage.categories.morphism import RingMorphism

class _GMixin:
    """Base mixin providing common functionality for Galois groups."""

    @property
    def _default_algorithm(self) -> str: ...

    @property
    def _gcdata(self) -> tuple: ...

    def _get_algorithm(self, algorithm: str | None) -> str: ...

    @property
    def _galois_closure(self) -> NumberField: ...

    def splitting_field(self) -> NumberField: ...

    @property
    def _gc_map(self) -> RingMorphism: ...

class _GaloisMixin(_GMixin):
    """Mixin for Galois groups of field extensions."""

    @property
    def _field(self) -> NumberField: ...

    def _repr_(self) -> str: ...

    def top_field(self) -> NumberField: ...

    @property
    def _field_degree(self) -> int: ...

    def transitive_label(self) -> str: ...

    def is_galois(self) -> bool: ...

class _SubGaloisMixin(_GMixin):
    """Mixin for subgroups of Galois groups."""

    @property
    def _ambient_group(self): ...

    def fixed_field(self, name: str | None = None, polred: bool | None = None, threshold: int | None = None) -> tuple[NumberField, RingMorphism]: ...

    @property
    def _gcdata(self) -> tuple: ...

class GaloisGroup_ab(_GaloisMixin, AbelianGroup_class):
    """Abelian Galois groups."""

    def __init__(self, field: NumberField, generator_orders: tuple[int, ...], algorithm: str | None = None, gen_names: str = 'sigma') -> None: ...

    def is_galois(self) -> bool: ...

    @property
    def _gcdata(self) -> tuple: ...

    def permutation_group(self) -> PermutationGroup: ...

    def transitive_number(self, algorithm: str | None = None, recompute: bool = False) -> Integer: ...

class GaloisGroup_cyc(GaloisGroup_ab):
    """Cyclic Galois groups."""

    def transitive_number(self, algorithm: str | None = None, recompute: bool = False) -> Integer: ...

    def signature(self) -> Integer: ...

class GaloisSubgroup_ab(AbelianGroup_subgroup, _SubGaloisMixin):
    """Subgroups of abelian Galois groups."""
    pass
