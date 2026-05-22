from sage.structure.element import Element

class FinitelyGeneratedMagmas:
    class ParentMethods:
        def magma_generators(self) -> tuple[Element, ...]: ...
