from sage.categories.category import Category
from sage.rings.ring import Ring
from sage.structure.parent import Parent


class Module(Parent):
    def __init__(
        self,
        base: Ring,
        category: Category | None = None,
        names: str | tuple[str, ...] | None = None,
    ) -> None: ...
    def change_ring(self, R: Ring) -> Module: ...
    def base_extend(self, R: Ring) -> Module: ...
