from collections.abc import Callable, Hashable, Mapping, Sequence
from typing import Generic, TypeVar

from sage.rings.integer import Integer
from sage.sets.set import Set_generic
from sage.structure.element import Element, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Outcome = TypeVar("_Outcome", bound=Hashable, default=Hashable)
_Value = TypeVar("_Value", bound=RingElement, default=RingElement)

type OutcomeTranslation[_Outcome: Hashable] = Callable[[_Outcome], _Outcome]
type DiscreteFunction[_Outcome: Hashable] = Mapping[
    _Outcome,
    ElementConstructorInput,
]


class RandomVariable_generic(
    Parent[_Value],
    Generic[_Outcome, _Value],
):
    def __init__(
        self,
        X: ProbabilitySpace_generic[_Outcome, _Value],
        RR: Parent[_Value],
    ) -> None: ...
    def probability_space(
        self,
    ) -> ProbabilitySpace_generic[_Outcome, _Value]: ...
    def domain(
        self,
    ) -> ProbabilitySpace_generic[_Outcome, _Value]: ...
    def codomain(self) -> Parent[_Value]: ...
    def field(self) -> Parent[_Value]: ...


class DiscreteRandomVariable(
    RandomVariable_generic[_Outcome, _Value],
    Generic[_Outcome, _Value],
):
    def __init__(
        self,
        X: DiscreteProbabilitySpace[_Outcome, _Value],
        f: DiscreteFunction[_Outcome],
        codomain: Parent[_Value] | None = ...,
        check: bool = ...,
    ) -> None: ...
    def __call__(self, x: _Outcome) -> _Value: ...
    def __repr__(self) -> str: ...
    def function(self) -> DiscreteFunction[_Outcome]: ...
    def expectation(self) -> _Value: ...
    def translation_expectation(
        self,
        map: OutcomeTranslation[_Outcome],
    ) -> _Value: ...
    def variance(self) -> _Value: ...
    def translation_variance(
        self,
        map: OutcomeTranslation[_Outcome],
    ) -> _Value: ...
    def covariance(
        self,
        other: DiscreteRandomVariable[_Outcome, _Value],
    ) -> _Value: ...
    def translation_covariance(
        self,
        other: DiscreteRandomVariable[_Outcome, _Value],
        map: OutcomeTranslation[_Outcome],
    ) -> _Value: ...
    def standard_deviation(self) -> Element: ...
    def translation_standard_deviation(
        self,
        map: OutcomeTranslation[_Outcome],
    ) -> Element: ...
    def correlation(
        self,
        other: DiscreteRandomVariable[_Outcome, _Value],
    ) -> Element: ...
    def translation_correlation(
        self,
        other: DiscreteRandomVariable[_Outcome, _Value],
        map: OutcomeTranslation[_Outcome],
    ) -> Element: ...


class ProbabilitySpace_generic(
    RandomVariable_generic[_Outcome, _Value],
    Generic[_Outcome, _Value],
):
    def __init__(
        self,
        domain: Sequence[_Outcome],
        RR: Parent[_Value],
    ) -> None: ...
    def domain(self) -> tuple[_Outcome, ...]: ...


class DiscreteProbabilitySpace(
    ProbabilitySpace_generic[_Outcome, _Value],
    DiscreteRandomVariable[_Outcome, _Value],
    Generic[_Outcome, _Value],
):
    def __init__(
        self,
        X: Sequence[_Outcome],
        P: DiscreteFunction[_Outcome],
        codomain: Parent[_Value] | None = ...,
        check: bool = ...,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def probability_space(self) -> DiscreteProbabilitySpace[_Outcome, _Value]: ...
    def set(self) -> Set_generic[_Outcome]: ...
    def entropy(self) -> Element: ...
