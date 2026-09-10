from collections.abc import Callable
from typing import Generic, ParamSpec, Protocol, Self, TypeVar, overload

from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Ring
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject
from sage.structure.unique_representation import _PickleReduction

type FactoryVersion = tuple[int, ...]
type FactoryCacheKeyComponent = (
    Integer | int | str | bool | tuple[str, ...] | Polynomial | Ring | None
)
type FactoryCacheKey = tuple[FactoryCacheKeyComponent, ...]
type FactoryExtraArgs = dict[str, bool]
type FactoryPickleState = dict[str, Callable[..., SageObject]]
type FactoryArgument = (
    SageObject
    | int
    | str
    | bool
    | bytes
    | tuple[FactoryArgument, ...]
    | dict[str, FactoryArgument]
    | None
)

_Key = TypeVar("_Key", default=FactoryCacheKey)
_Product = TypeVar("_Product", default=SageObject)
_Extra = TypeVar("_Extra", default=FactoryArgument)
_Arguments = ParamSpec("_Arguments", default=...)

# factory.pyx:340-372 forwards the complete key-producer call, including
# keyword names and defaults, to get_object. Infer these from the supplied
# factory rather than fixing one global argument or key shape.
class _FactoryCall[**P, K, R, E](Protocol):
    def create_key_and_extra_args(
        self, *args: P.args, **kwds: P.kwargs
    ) -> tuple[K, dict[str, E]]: ...
    def get_object(
        self, version: FactoryVersion, key: K, extra_args: dict[str, E]
    ) -> R: ...

class UniqueFactory(SageObject, Generic[_Key, _Product, _Extra, _Arguments]):
    def __init__(self, name: str) -> None: ...
    def __reduce__(self) -> _PickleReduction[Self]: ...
    def __call__[**P, K, R, E](
        self: _FactoryCall[P, K, R, E], *args: P.args, **kwds: P.kwargs
    ) -> R: ...
    def get_object(
        self,
        version: FactoryVersion,
        key: _Key,
        extra_args: dict[str, _Extra],
    ) -> _Product: ...
    def get_version(self, sage_version: FactoryVersion) -> FactoryVersion: ...
    def create_key_and_extra_args(
        self, *args: _Arguments.args, **kwds: _Arguments.kwargs
    ) -> tuple[_Key, dict[str, _Extra]]: ...
    def create_key(self, *args: _Arguments.args, **kwds: _Arguments.kwargs) -> _Key: ...
    def create_object(
        self,
        version: FactoryVersion,
        key: _Key,
        **extra_args: _Extra,
    ) -> _Product: ...
    def other_keys(self, key: _Key, obj: _Product) -> list[_Key]: ...
    def reduce_data(
        self, obj: SageObject
    ) -> (
        tuple[
            Callable[..., SageObject],
            tuple[UniqueFactory, FactoryVersion, FactoryCacheKey, FactoryExtraArgs],
        ]
        | tuple[
            Callable[..., SageObject],
            tuple[
                UniqueFactory,
                FactoryVersion,
                FactoryCacheKey,
                FactoryExtraArgs,
                FactoryPickleState,
            ],
        ]
    ): ...

def register_factory_unpickle(name: str, callable: Callable[..., Parent]) -> None: ...
@overload
def generic_factory_unpickle(
    factory: UniqueFactory,
    version: FactoryVersion,
    key: FactoryCacheKey,
    extra_args: FactoryExtraArgs,
) -> SageObject: ...
@overload
def generic_factory_unpickle(
    factory: UniqueFactory,
    version: FactoryVersion,
    key: FactoryCacheKey,
    extra_args: FactoryExtraArgs,
    state: FactoryPickleState,
) -> SageObject: ...
def generic_factory_reduce(
    self: SageObject, proto: int
) -> tuple[Callable[..., SageObject], ...]: ...
def generic_factory_getstate(obj: SageObject) -> FactoryPickleState: ...
def generic_factory_setstate(self: SageObject, d: FactoryPickleState) -> None: ...
def lookup_global(name: str) -> UniqueFactory: ...
