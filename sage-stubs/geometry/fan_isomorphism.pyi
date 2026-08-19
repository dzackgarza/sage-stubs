from collections.abc import Iterator

from sage.geometry.fan import RationalPolyhedralFan
from sage.geometry.fan_morphism import FanMorphism
from sage.geometry.point_collection import PointCollection
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.modules.free_module import FreeModule_generic_pid
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer


class FanNotIsomorphicError(Exception): ...


def fan_isomorphic_necessary_conditions(
    fan1: RationalPolyhedralFan,
    fan2: RationalPolyhedralFan,
) -> bool: ...


def fan_isomorphism_generator(
    fan1: RationalPolyhedralFan,
    fan2: RationalPolyhedralFan,
) -> Iterator[Matrix_integer_dense]: ...


def find_isomorphism(
    fan1: RationalPolyhedralFan,
    fan2: RationalPolyhedralFan,
    check: bool = ...,
) -> FanMorphism: ...


def fan_2d_cyclically_ordered_rays(
    fan: RationalPolyhedralFan,
) -> PointCollection[
    FreeModuleElement[Integer],
    FreeModule_generic_pid[Integer],
    Integer,
]: ...


def fan_2d_echelon_forms(
    fan: RationalPolyhedralFan,
) -> frozenset[Matrix_integer_dense]: ...


def fan_2d_echelon_form(
    fan: RationalPolyhedralFan,
) -> Matrix_integer_dense: ...
