from collections.abc import Iterable, Sequence
from typing import TypeAlias

from sage.matrix.matrix2 import Matrix
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial_ideal import MPolynomialIdeal
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import RingElement

from ..generic.algebraic_scheme import AlgebraicScheme_subscheme
from ..generic.morphism import SchemeMorphism, SchemeMorphism_point
from ..projective.projective_subscheme import AlgebraicScheme_subscheme_projective
from .affine_morphism import SchemeMorphism_polynomial_affine_subscheme_field
from .affine_space import AffineSpace_generic

_PointInput: TypeAlias = SchemeMorphism_point | Sequence[RingElement]
_PolynomialInput: TypeAlias = Polynomial | Ideal_generic | Iterable[Polynomial]

class AlgebraicScheme_subscheme_affine(AlgebraicScheme_subscheme):
    def __init__(
        self,
        A: AffineSpace_generic,
        polynomials: _PolynomialInput,
        embedding_center: _PointInput | None = None,
        embedding_codomain: AlgebraicScheme_subscheme_projective | None = None,
        embedding_images: Sequence[Polynomial] | None = None,
    ) -> None: ...
    def _morphism(self, *args: object, **kwds: object) -> SchemeMorphism: ...
    def dimension(self) -> Integer: ...
    def projective_closure(
        self, i: int | None = None, PP: AlgebraicScheme_subscheme_projective | None = None
    ) -> AlgebraicScheme_subscheme_projective: ...
    def projective_embedding(
        self, i: int | None = None, PP: AlgebraicScheme_subscheme_projective | None = None
    ) -> SchemeMorphism: ...
    def is_smooth(self, point: _PointInput | None = None) -> bool: ...
    def intersection_multiplicity(self, X: AlgebraicScheme_subscheme_affine, P: _PointInput) -> int: ...
    def multiplicity(self, P: _PointInput) -> int: ...
    def defining_ideal(self) -> MPolynomialIdeal: ...
    def defining_polynomials(self) -> tuple[Polynomial, ...]: ...

class AlgebraicScheme_subscheme_affine_field(AlgebraicScheme_subscheme_affine):
    def _morphism(self, *args: object, **kwds: object) -> SchemeMorphism_polynomial_affine_subscheme_field: ...
    def tangent_space(self, p: _PointInput) -> AlgebraicScheme_subscheme_affine: ...
    def Jacobian_matrix(self) -> Matrix: ...
    def Jacobian(self) -> MPolynomialIdeal: ...
