# Repo-scoped stubs; see lexicon/README.md.
#
# An automorphism of a finite abelian group, read as the matrix of its action
# on the group's generators -- the form the repo transposes to reach its own
# ``U^T G U = G`` convention.
from typing import TypeVar

from sage.structure.element import Matrix, MultiplicativeGroupElement
from sage.structure.parent import Parent

# abelian_aut.py:236, 434, 500; fqf_orthogonal.py:162: each group names the
# class of its elements in ``Element``.
_E = TypeVar(
    "_E",
    bound=AbelianGroupAutomorphism,
    default=AbelianGroupAutomorphism,
    covariant=True,
)

class AbelianGroupAutomorphismGroup_gap(Parent[_E]): ...
class AbelianGroupAutomorphismGroup(AbelianGroupAutomorphismGroup_gap[_E]): ...
class AbelianGroupAutomorphismGroup_subgroup(AbelianGroupAutomorphismGroup_gap[_E]): ...

class AbelianGroupAutomorphism(MultiplicativeGroupElement):
    def matrix(self) -> Matrix: ...
