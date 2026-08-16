from typing import assert_type

from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.module import Module, Module_free
from sage.rings.ring import Ring
from sage.structure.element import ModuleElement, RingElement


class Scalar(RingElement): ...


class Vector(FreeModuleElement[Scalar]): ...


class AbstractModuleElement(ModuleElement): ...


def check_module(
    module: Module[Scalar, AbstractModuleElement],
) -> None:
    assert_type(module.base_ring(), Ring[Scalar])
    assert_type(module.an_element(), AbstractModuleElement)
    assert_type(module(0), AbstractModuleElement)


def check_free_parent(
    module: Module_free[Scalar, Vector],
) -> None:
    assert_type(module.base_ring(), Ring[Scalar])
    assert_type(module.an_element(), Vector)
    assert_type(module.gen(0), Vector)
    assert_type(module.gens(), tuple[Vector, ...])


def check_free_module(
    module: FreeModule_generic[Scalar, Vector],
) -> None:
    assert_type(module.base_ring(), Ring[Scalar])
    assert_type(module.an_element(), Vector)
    assert_type(module.gen(0), Vector)
    assert_type(module.gens(), tuple[Vector, ...])


def check_vector(vector: Vector, other: Vector) -> None:
    assert_type(vector.base_ring(), Ring[Scalar])
    assert_type(vector.list(), list[Scalar])
    assert_type(vector.dot_product(other), Scalar)
