from sage.categories.category import Category
from sage.rings.ring import CommutativeRing
from sage.structure.category_object import NameSpec
from sage.structure.parent import Parent

class LazySeriesRing(Parent): ...

class LazyLaurentSeriesRing(LazySeriesRing):
    def __init__(
        self,
        base_ring: CommutativeRing,
        names: NameSpec,
        sparse: bool = True,
        category: Category | None = None,
    ) -> None: ...

class LazyPowerSeriesRing(LazySeriesRing):
    def __init__(
        self,
        base_ring: CommutativeRing,
        names: NameSpec,
        sparse: bool = True,
        category: Category | None = None,
    ) -> None: ...
