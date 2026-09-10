from collections.abc import Callable
from typing import Protocol, Self

from sage.misc.fast_methods import WithEqualityById

# The source exposes a static callable, not an instance-bound method:
# staticmethod at 585 and weak_cached_function at 1192. Its returned class
# follows the supplied constructor; subclasses may normalize its arguments.
class _Classcall[**P](Protocol):
    def __call__[T](self, cls: type[T], *args: P.args, **options: P.kwargs) -> T: ...

# unique_representation.py:617-636 and factory.pyx:311-338 use the
# standard two-item reduction, with optional state as the third item.
type _PickleReduction[T] = (
    tuple[Callable[..., T], tuple[object, ...]]
    | tuple[Callable[..., T], tuple[object, ...], dict[str, object]]
)

class WithPicklingByInitArgs:
    __classcall__: _Classcall[...]
    def __reduce__(self) -> _PickleReduction[Self]: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: dict[int, object]) -> Self: ...
    def __getstate__(self) -> dict[str, object]: ...
    def __setstate__(self, d: dict[str, object]) -> None: ...

def unreduce[**P, T](
    cls: Callable[P, T], args: tuple[object, ...], keywords: dict[str, object]
) -> T: ...

class CachedRepresentation(WithPicklingByInitArgs):
    __classcall__: _Classcall[...]
    @classmethod
    def _clear_cache_(cls) -> None: ...

# Source 1298 onward has no directly defined methods; in particular,
# _reduction is stored instance data, not a class method.
class UniqueRepresentation(WithEqualityById, CachedRepresentation): ...
