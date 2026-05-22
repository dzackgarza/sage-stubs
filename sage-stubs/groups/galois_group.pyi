from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.rings.integer import Integer
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.rings.morphism import RingHomomorphism
from sage.rings.ring import Field

AbelianGroup_subgroup = AbelianGroup_class


class _GMixin:
    

    @property
    def _default_algorithm(self) -> str | None: ...

    @property
    def _gcdata(self) -> tuple[Field, RingHomomorphism]: ...

    def _get_algorithm(self, algorithm: str | None) -> str | None: ...

    @property
    def _galois_closure(self) -> Field: ...

    def splitting_field(self) -> Field: ...

    @property
    def _gc_map(self) -> RingHomomorphism: ...

class _GaloisMixin(_GMixin):
    

    @property
    def _field(self) -> Field: ...

    def _repr_(self) -> str: ...

    def top_field(self) -> Field: ...

    @property
    def _field_degree(self) -> int: ...

    def transitive_label(self) -> str: ...

    def is_galois(self) -> bool: ...

class _SubGaloisMixin(_GMixin):
    

    @property
    def _ambient_group(self) -> _GaloisMixin: ...

    def fixed_field(self, name: str | None = None, polred: bool | None = None, threshold: int | None = None) -> tuple[Field, RingHomomorphism]: ...

    @property
    def _gcdata(self) -> tuple[Field, RingHomomorphism]: ...

class GaloisGroup_ab(_GaloisMixin, AbelianGroup_class):
    

    def __init__(self, field: Field, generator_orders: tuple[int, ...], algorithm: str | None = None, gen_names: str = 'sigma') -> None: ...

    def is_galois(self) -> bool: ...

    @property
    def _gcdata(self) -> tuple[Field, RingHomomorphism]: ...

    def permutation_group(self) -> PermutationGroup_generic: ...

    def transitive_number(self, algorithm: str | None = None, recompute: bool = False) -> Integer: ...

class GaloisGroup_cyc(GaloisGroup_ab):
    

    def transitive_number(self, algorithm: str | None = None, recompute: bool = False) -> Integer: ...

    def signature(self) -> Integer: ...

class GaloisSubgroup_ab(AbelianGroup_subgroup, _SubGaloisMixin):
    ...
