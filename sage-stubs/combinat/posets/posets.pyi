def Poset(
    data: object | None = None,
    element_labels: object | None = None,
    cover_relations: bool = False,
    linear_extension: bool = False,
    category: object | None = None,
    facade: bool | None = None,
    key: object | None = None,
) -> FinitePoset: ...

class FinitePoset:
    def is_meet_semilattice(self) -> bool: ...
    def is_join_semilattice(self) -> bool: ...
