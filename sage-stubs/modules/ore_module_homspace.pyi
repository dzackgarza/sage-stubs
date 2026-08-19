from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.homset import HomsetWithBase
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.ore_module_element import OreModuleElement
from sage.modules.ore_module_morphism import (
    OreModuleMorphism,
    OreModuleMorphismInput,
)
from sage.structure.element import RingElement
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class OreModule_homspace(
    UniqueRepresentation,
    HomsetWithBase[
        OreModuleMorphism[_Scalar],
        OreModuleElement[_Scalar],
        OreModuleElement[_Scalar],
    ],
    Generic[_Scalar],
):
    Element: type[OreModuleMorphism[_Scalar]]
    element_class: type[OreModuleMorphism[_Scalar]]

    def __init__(
        self,
        domain: OreModule[_Scalar],
        codomain: OreModule[_Scalar],
        category: Category | None = ...,
    ) -> None: ...
    def domain(self) -> OreModule[_Scalar]: ...
    def codomain(self) -> OreModule[_Scalar]: ...
    def _element_constructor_(
        self,
        im_gens: OreModuleMorphismInput[_Scalar],
        check: bool = ...,
    ) -> OreModuleMorphism[_Scalar]: ...
    def matrix_space(self) -> MatrixSpace[_Scalar]: ...
    def identity(self) -> OreModuleMorphism[_Scalar]: ...
    def zero(self) -> OreModuleMorphism[_Scalar]: ...

from sage.modules.ore_module import OreModule
