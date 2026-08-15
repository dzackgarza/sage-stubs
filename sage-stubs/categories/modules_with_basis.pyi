from collections.abc import Callable, Iterable, Iterator, Mapping
from collections.abc import Hashable

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.matrix.matrix2 import Matrix
from sage.rings.ring import CommutativeRing
from sage.sets.family import AbstractFamily
from sage.structure.element import CommutativeRingElement, Element
from sage.structure.parent import Parent
from sage.structure.sage_object import SageCoercionAtom
from sage.structure.support_view import SupportView

from sage.modules.with_basis.subquotient import QuotientModuleWithBasis, SubmoduleWithBasis


class ModulesWithBasis:
    class ParentMethods:
        def basis(self) -> AbstractFamily: ...
        def module_morphism(
            self,
            on_basis: Callable[[Hashable], Element | SageCoercionAtom] | None = ...,
            matrix: Matrix | None = ...,
            function: Callable[..., Element | SageCoercionAtom] | None = ...,
            diagonal: Callable[[Hashable], CommutativeRingElement | SageCoercionAtom] | None = ...,
            triangular: str | None = ...,
            unitriangular: bool = ...,
            codomain: Parent | None = ...,
            category: Category | None = ...,
            zero: Element | None = ...,
            position: int = ...,
            side: str = ...,
            key: Callable[[Hashable], int] | None = ...,
            inverse_on_support: str | None = ...,
            **keywords: bool | int | str | Hashable | Callable[[Hashable], Element | SageCoercionAtom] | Callable[[Hashable], int] | Callable[..., Element | SageCoercionAtom] | Category | Parent | CommutativeRingElement | SageCoercionAtom | CommutativeRing | Matrix | Map,
        ) -> Morphism: ...

        def echelon_form(
            self,
            elements: Iterable[Element],
            row_reduced: bool = ...,
            order: Iterable[Hashable] | Callable[[Hashable], Hashable] | None = ...,
        ) -> list[Element]: ...

        def submodule(
            self,
            gens: Iterable[Element] | Mapping[Hashable, Element] | AbstractFamily,
            check: bool = ...,
            already_echelonized: bool = ...,
            unitriangular: bool = ...,
            support_order: Iterable[Hashable] | Callable[[Hashable], int] | None = ...,
            category: Category | None = ...,
            submodule_class: type[SubmoduleWithBasis] | None = ...,
            *args: Parent | CommutativeRing | int | bool | Hashable,
            **opts: bool | int | str | Hashable | Callable[[Hashable], Element | SageCoercionAtom] | Callable[[Hashable], int] | Callable[..., Element | SageCoercionAtom] | Category | Parent | CommutativeRingElement | SageCoercionAtom | CommutativeRing | Matrix,
        ) -> SubmoduleWithBasis: ...

        def quotient_module(
            self,
            submodule: SubmoduleWithBasis | Iterable[Element] | Mapping[Hashable, Element] | AbstractFamily,
            check: bool = ...,
            already_echelonized: bool = ...,
            category: Category | None = ...,
        ) -> QuotientModuleWithBasis: ...

        def tensor(self, *parents: Parent) -> Parent: ...
        def intersection(self, other: Parent) -> Parent: ...
        def cardinality(self) -> int: ...
        def is_finite(self) -> bool: ...
        def monomial(self, i: Hashable) -> Element: ...
        def sum_of_monomials(self) -> Callable[[Iterable[Hashable]], Element]: ...
        def monomial_or_zero_if_none(self, index: Hashable | None) -> Element: ...
        def term(self, index: Hashable, coeff: CommutativeRingElement | SageCoercionAtom | None = ...) -> Element: ...
        def sum_of_terms(self, terms: Iterable[tuple[Hashable, CommutativeRingElement | SageCoercionAtom]]) -> Element: ...
        def dimension(self) -> int: ...
        def rank(self) -> int: ...
        def random_element(self, n: int = ...) -> Element: ...

    class ElementMethods:
        def monomial_coefficients(self, copy: bool = True) -> dict[Hashable, CommutativeRingElement]: ...
        def coefficient(self, m: Hashable) -> CommutativeRingElement: ...
        def items(self) -> Iterator[tuple[Hashable, CommutativeRingElement]]: ...
        def is_zero(self) -> bool: ...
        def length(self) -> int: ...
        def support(self) -> SupportView[Hashable]: ...
        def monomials(self) -> list[Element]: ...
        def terms(self) -> list[Element]: ...
        def coefficients(self, sort: bool = True) -> list[CommutativeRingElement]: ...
        def support_of_term(self) -> Hashable: ...
        def leading_support(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> Hashable: ...
        def leading_item(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> tuple[Hashable, CommutativeRingElement]: ...
        def leading_monomial(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> Element: ...
        def leading_coefficient(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> CommutativeRingElement: ...
        def leading_term(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> Element: ...
        def trailing_support(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> Hashable: ...
        def trailing_item(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> tuple[Hashable, CommutativeRingElement]: ...
        def trailing_monomial(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> Element: ...
        def trailing_coefficient(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> CommutativeRingElement: ...
        def trailing_term(
            self,
            *args: Hashable,
            key: Callable[[Hashable], int] | None = ...,
        ) -> Element: ...
        def map_coefficients(
            self,
            f: Map | Callable[[CommutativeRingElement], CommutativeRingElement],
            new_base_ring: Parent | None = ...,
        ) -> Element: ...
        def map_support(self, f: Callable[[Hashable], Hashable]) -> Element: ...
        def map_support_skip_none(self, f: Callable[[Hashable], Hashable | None]) -> Element: ...
        def map_item(
            self,
            f: Callable[[Hashable, CommutativeRingElement], tuple[Hashable, CommutativeRingElement]],
        ) -> Element: ...
        def tensor(self, *elements: Element) -> Element: ...

    class Homsets:
        class ParentMethods:
            ...

    class MorphismMethods:
        def on_basis(self) -> Callable[[Hashable], Element]: ...

    class CartesianProducts:
        def extra_super_categories(self) -> list[Category]: ...
        class ParentMethods:
            ...

    class TensorProducts:
        def extra_super_categories(self) -> list[Category]: ...
        class ParentMethods:
            ...
        class ElementMethods:
            def apply_multilinear_morphism(
                self,
                f: Callable[..., Element | SageCoercionAtom],
                codomain: Parent | None = ...,
            ) -> Element: ...

    class DualObjects:
        def extra_super_categories(self) -> list[Category]: ...
