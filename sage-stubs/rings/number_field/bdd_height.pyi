from collections.abc import Iterator, Sequence

from sage.matrix.matrix0 import Matrix
from sage.rings.integer import Integer
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber

def bdd_norm_pr_gens_iq(
    K: NumberField_generic, norm_list: Sequence[int | Integer]
) -> (
    Iterator[NumberFieldElement]
    | list[NumberFieldElement]
    | dict[Integer, list[NumberFieldElement]]
): ...
def bdd_height_iq(
    K: NumberField_generic, height_bound: int | Integer | Rational | RealNumber
) -> (
    Iterator[NumberFieldElement]
    | list[NumberFieldElement]
    | dict[Integer, list[NumberFieldElement]]
): ...
def bdd_norm_pr_ideal_gens(
    K: NumberField_generic, norm_list: Sequence[int | Integer]
) -> (
    Iterator[NumberFieldElement]
    | list[NumberFieldElement]
    | dict[Integer, list[NumberFieldElement]]
): ...
def integer_points_in_polytope(
    matrix: Matrix, interval_radius: int | Integer | Rational | RealNumber
) -> list[tuple[Integer, ...]]: ...
def bdd_height(
    K: NumberField_generic,
    height_bound: int | Integer | Rational | RealNumber,
    tolerance: int | Integer | Rational | RealNumber = ...,
    precision: int | Integer = ...,
) -> (
    Iterator[NumberFieldElement]
    | list[NumberFieldElement]
    | dict[Integer, list[NumberFieldElement]]
): ...
