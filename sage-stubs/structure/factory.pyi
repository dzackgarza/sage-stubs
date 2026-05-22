from collections.abc import Callable
from typing import overload, TypeAlias

from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Ring
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

FactoryVersion: TypeAlias = tuple[int, ...]
FactoryCacheKeyComponent: TypeAlias = (
    Integer | int | str | bool | None | tuple[str, ...] | Polynomial | Ring
)
FactoryCacheKey: TypeAlias = tuple[FactoryCacheKeyComponent, ...]
FactoryExtraArgs: TypeAlias = dict[str, bool]
FactoryPickleState: TypeAlias = dict[str, Callable[..., SageObject]]

class UniqueFactory(SageObject):
    def __init__(self, name: str) -> None: ...
    def __reduce__(self) -> tuple[Callable[[str], UniqueFactory], tuple[str]]: ...
    def __call__(self, *args: object, **kwds: object) -> SageObject: ...
    def get_object(
        self,
        version: FactoryVersion,
        key: FactoryCacheKey,
        extra_args: FactoryExtraArgs,
    ) -> SageObject: ...
    def get_version(self, sage_version: FactoryVersion) -> FactoryVersion: ...
    def create_key_and_extra_args(
        self, *args: object, **kwds: object
    ) -> tuple[FactoryCacheKey, FactoryExtraArgs]: ...
    def create_key(self, *args: object, **kwds: object) -> FactoryCacheKey: ...
    def create_object(
        self,
        version: FactoryVersion,
        key: FactoryCacheKey,
        **extra_args: object,
    ) -> SageObject: ...
    def other_keys(self, key: FactoryCacheKey, obj: SageObject) -> list[FactoryCacheKey]: ...
    def reduce_data(
        self, obj: SageObject
    ) -> tuple[
        Callable[..., SageObject],
        tuple[UniqueFactory, FactoryVersion, FactoryCacheKey, FactoryExtraArgs],
    ] | tuple[
        Callable[..., SageObject],
        tuple[
            UniqueFactory,
            FactoryVersion,
            FactoryCacheKey,
            FactoryExtraArgs,
            FactoryPickleState,
        ],
    ]: ...

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
def generic_factory_reduce(self: SageObject, proto: int) -> tuple[Callable[..., SageObject], ...]: ...
def generic_factory_getstate(obj: SageObject) -> FactoryPickleState: ...
def generic_factory_setstate(self: SageObject, d: FactoryPickleState) -> None: ...
def lookup_global(name: str) -> UniqueFactory: ...
