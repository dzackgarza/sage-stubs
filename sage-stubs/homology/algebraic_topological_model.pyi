from typing import TypeVar

from sage.homology.chain_complex import ChainComplex_class
from sage.homology.chain_homotopy import ChainContraction
from sage.rings.integer import Integer
from sage.structure.element import FieldElement
from sage.structure.parent import Parent
from sage.topology.cell_complex import GenericCellComplex

_FieldScalar = TypeVar(
    "_FieldScalar",
    bound=FieldElement,
    default=FieldElement,
)

type AlgebraicTopologicalModel[_FieldScalar: FieldElement] = tuple[
    ChainContraction[Integer, _FieldScalar],
    ChainComplex_class[Integer, _FieldScalar],
]


def algebraic_topological_model(
    K: GenericCellComplex,
    base_ring: Parent[_FieldScalar] | None = ...,
) -> AlgebraicTopologicalModel[_FieldScalar]: ...


def algebraic_topological_model_delta_complex(
    K: GenericCellComplex,
    base_ring: Parent[_FieldScalar] | None = ...,
) -> AlgebraicTopologicalModel[_FieldScalar]: ...
