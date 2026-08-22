from typing import Generic, TypeVar

from sage.categories.action import Action
from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.schemes.generic.homset import SchemeHomset_generic, SchemeHomset_points
from sage.schemes.generic.morphism import (
    SchemeMorphism_point,
    SchemeMorphism_polynomial,
)
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_MatrixScalar = TypeVar("_MatrixScalar", bound=RingElement, default=RingElement)
_ObjectScalar = TypeVar("_ObjectScalar", bound=RingElement, default=RingElement)
_ResultScalar = TypeVar("_ResultScalar", bound=RingElement, default=RingElement)
_SchemeMap = TypeVar(
    "_SchemeMap",
    bound=SchemeMorphism_polynomial,
    default=SchemeMorphism_polynomial,
)
_SchemePoint = TypeVar(
    "_SchemePoint",
    bound=SchemeMorphism_point,
    default=SchemeMorphism_point,
)

type _ActedUpon = Parent | SchemeHomset_generic | SchemeHomset_points
type _ActionCodomain = Parent | SchemeHomset_generic | SchemeHomset_points


class MatrixMulAction(Action, Generic[_ResultScalar]):
    def __init__(
        self,
        G: MatrixSpace[RingElement],
        S: _ActedUpon,
        is_left: bool,
    ) -> None: ...
    def codomain(self) -> _ActionCodomain: ...


class MatrixMatrixAction(
    MatrixMulAction[_ResultScalar],
    Generic[_MatrixScalar, _ObjectScalar, _ResultScalar],
):
    def __init__(
        self,
        G: MatrixSpace[_MatrixScalar],
        S: MatrixSpace[_ObjectScalar],
    ) -> None: ...
    def _create_codomain(
        self,
        base: Parent[_ResultScalar],
    ) -> MatrixSpace[_ResultScalar]: ...
    def _act_(
        self,
        g: Matrix[_MatrixScalar],
        s: Matrix[_ObjectScalar],
    ) -> Matrix[_ResultScalar]: ...
    def codomain(self) -> MatrixSpace[_ResultScalar]: ...


class MatrixVectorAction(
    MatrixMulAction[_ResultScalar],
    Generic[_MatrixScalar, _ObjectScalar, _ResultScalar],
):
    def __init__(
        self,
        G: MatrixSpace[_MatrixScalar],
        S: FreeModule_generic[_ObjectScalar],
    ) -> None: ...
    def _create_codomain(
        self,
        base: Parent[_ResultScalar],
    ) -> FreeModule_generic[_ResultScalar]: ...
    def _act_(
        self,
        g: Matrix[_MatrixScalar],
        s: FreeModuleElement[_ObjectScalar],
    ) -> FreeModuleElement[_ResultScalar]: ...
    def codomain(self) -> FreeModule_generic[_ResultScalar]: ...


class VectorMatrixAction(
    MatrixMulAction[_ResultScalar],
    Generic[_MatrixScalar, _ObjectScalar, _ResultScalar],
):
    def __init__(
        self,
        G: MatrixSpace[_MatrixScalar],
        S: FreeModule_generic[_ObjectScalar],
    ) -> None: ...
    def _create_codomain(
        self,
        base: Parent[_ResultScalar],
    ) -> FreeModule_generic[_ResultScalar]: ...
    def _act_(
        self,
        g: Matrix[_MatrixScalar],
        s: FreeModuleElement[_ObjectScalar],
    ) -> FreeModuleElement[_ResultScalar]: ...
    def codomain(self) -> FreeModule_generic[_ResultScalar]: ...


class MatrixPolymapAction(
    MatrixMulAction[_ResultScalar],
    Generic[_MatrixScalar, _ResultScalar, _SchemeMap],
):
    def __init__(
        self,
        G: MatrixSpace[_MatrixScalar],
        S: SchemeHomset_generic,
    ) -> None: ...
    def _create_codomain(
        self,
        base: Parent[_ResultScalar],
    ) -> SchemeHomset_generic: ...
    def _act_(
        self,
        mat: Matrix[_MatrixScalar],
        f: _SchemeMap,
    ) -> _SchemeMap: ...
    def codomain(self) -> SchemeHomset_generic: ...


class PolymapMatrixAction(
    MatrixMulAction[_ResultScalar],
    Generic[_MatrixScalar, _ResultScalar, _SchemeMap],
):
    def __init__(
        self,
        G: MatrixSpace[_MatrixScalar],
        S: SchemeHomset_generic,
    ) -> None: ...
    def _create_codomain(
        self,
        base: Parent[_ResultScalar],
    ) -> SchemeHomset_generic: ...
    def _act_(
        self,
        mat: Matrix[_MatrixScalar],
        f: _SchemeMap,
    ) -> _SchemeMap: ...
    def codomain(self) -> SchemeHomset_generic: ...


class MatrixSchemePointAction(
    MatrixMulAction[_ResultScalar],
    Generic[_MatrixScalar, _ResultScalar, _SchemePoint],
):
    def __init__(
        self,
        G: MatrixSpace[_MatrixScalar],
        S: SchemeHomset_points,
    ) -> None: ...
    def _create_codomain(
        self,
        base: Parent[_ResultScalar],
    ) -> SchemeHomset_points: ...
    def _act_(
        self,
        mat: Matrix[_MatrixScalar],
        P: _SchemePoint,
    ) -> _SchemePoint: ...
    def codomain(self) -> SchemeHomset_points: ...
