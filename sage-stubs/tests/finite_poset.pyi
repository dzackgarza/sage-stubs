import builtins

class _SageObject: ...

implications: _SageObject
dual_properties: _SageObject
selfdual_properties: _SageObject
dual_elements: _SageObject
two_to_one: _SageObject
mutually_exclusive: _SageObject
set_inclusions: _SageObject
sublattice_closed: _SageObject

def check_attrcall(self, L: builtins.object) -> _SageObject: ...
def check_finite_lattice(self) -> _SageObject: ...
def check_finite_poset(self) -> _SageObject: ...
