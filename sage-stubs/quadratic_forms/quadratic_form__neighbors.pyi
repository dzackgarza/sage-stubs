from collections.abc import Sequence
from typing import Literal, overload

from sage.matrix.matrix import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.integer import Integer
from sage.structure.element import RingElement

def find_primitive_p_divisible_vector__random(
    self: QuadraticForm, p: int | Integer
) -> FreeModuleElement[Integer]: ...

# quadratic_form__neighbors.py:55: None once the vectors are exhausted.
def find_primitive_p_divisible_vector__next(
    self: QuadraticForm, p: int | Integer, v: FreeModuleElement[Integer] | None = None
) -> FreeModuleElement[Integer] | None: ...

# quadratic_form__neighbors.py:243-248: the neighbour, or with
# ``return_matrix`` the transpose of its basis over QQ.
@overload
def find_p_neighbor_from_vec(
    self: QuadraticForm,
    p: int | Integer,
    y: FreeModuleElement[Integer],
    return_matrix: Literal[False] = False,
) -> QuadraticForm: ...
@overload
def find_p_neighbor_from_vec(
    self: QuadraticForm,
    p: int | Integer,
    y: FreeModuleElement[Integer],
    return_matrix: Literal[True],
) -> Matrix[RingElement]: ...

# quadratic_form__neighbors.py:251: the classes of the p-neighbour graph
# reached from the seeds, one form per class.
def neighbor_iteration(
    seeds: Sequence[QuadraticForm],
    p: int | Integer,
    mass: RingElement | None = None,
    max_classes: int | Integer | None = None,
    algorithm: str | None = None,
    max_neighbors: int | Integer = 1000,
    verbose: bool = False,
) -> list[QuadraticForm]: ...

# quadratic_form__neighbors.py:379: representatives of the orbits of the
# automorphism group on the lines of (ZZ/pZZ)^n.
def orbits_lines_mod_p(
    self: QuadraticForm, p: int | Integer
) -> list[FreeModuleElement[IntegerMod_abstract]]: ...
