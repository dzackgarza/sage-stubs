import sage.rings.abc
from sage.categories.pushout import CompletionFunctor
from sage.rings.integer_ring import IntegerRing_class
from sage.rings.padics.padic_base_generic import pAdicBaseGeneric
from sage.rings.padics.padic_generic import pAdicGeneric
from sage.rings.padics.padic_generic_element import pAdicGenericElement

class pAdicRingGeneric(pAdicGeneric, sage.rings.abc.pAdicRing):
    def is_field(self, proof: bool = True) -> bool: ...
    def krull_dimension(self) -> int: ...

class pAdicFieldGeneric(pAdicGeneric, sage.rings.abc.pAdicField):
    def is_field(self, proof: bool = True) -> bool: ...

class pAdicRingBaseGeneric(pAdicBaseGeneric, pAdicRingGeneric):
    def construction(self, forbid_frac_field: bool = False) -> tuple[CompletionFunctor, IntegerRing_class]: ...
    def random_element(self, algorithm: str = "default") -> pAdicGenericElement: ...
