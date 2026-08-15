# Repo-scoped stubs; see lexicon/README.md.
#
# An automorphism of a finite abelian group, read as the matrix of its action
# on the group's generators -- the form the repo transposes to reach its own
# ``U^T G U = G`` convention.
from sage.structure.element import Matrix, MultiplicativeGroupElement
from sage.structure.parent import Parent

class AbelianGroupAutomorphismGroup_gap(Parent): ...
class AbelianGroupAutomorphismGroup(AbelianGroupAutomorphismGroup_gap): ...
class AbelianGroupAutomorphismGroup_subgroup(AbelianGroupAutomorphismGroup_gap): ...

class AbelianGroupAutomorphism(MultiplicativeGroupElement):
    def matrix(self) -> Matrix: ...
