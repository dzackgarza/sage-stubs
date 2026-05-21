from sage.structure.parent import Parent

class CommutativeRings:
    class ElementMethods:
        ...
    class ParentMethods:
        def extension(
            self,
            poly: object,
            name: str | tuple[str, ...] | None = None,
            names: str | tuple[str, ...] | None = None,
            **kwds: object,
        ) -> Parent: ...
    class Finite:
        class ParentMethods:
            ...
