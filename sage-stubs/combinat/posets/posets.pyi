from typing import Literal, overload

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
    def height(self, certificate: bool = False) -> int | tuple[int, list[object]]: ...
    def width(self, certificate: bool = False) -> int | tuple[int, list[object]]: ...
    @overload
    def is_meet_semilattice(self, certificate: Literal[False] = False) -> bool: ...
    @overload
    def is_meet_semilattice(
        self,
        certificate: Literal[True],
    ) -> tuple[bool, tuple[object, object] | None]: ...
    @overload
    def is_meet_semilattice(
        self,
        certificate: bool,
    ) -> bool | tuple[bool, tuple[object, object] | None]: ...
    @overload
    def is_join_semilattice(self, certificate: Literal[False] = False) -> bool: ...
    @overload
    def is_join_semilattice(
        self,
        certificate: Literal[True],
    ) -> tuple[bool, tuple[object, object] | None]: ...
    @overload
    def is_join_semilattice(
        self,
        certificate: bool,
    ) -> bool | tuple[bool, tuple[object, object] | None]: ...
