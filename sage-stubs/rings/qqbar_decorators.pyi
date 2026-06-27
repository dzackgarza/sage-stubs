from collections.abc import Callable
from typing import TypeVar

_F = TypeVar('_F', bound=Callable[..., object])

def handle_AA_and_QQbar(func: _F) -> _F: ...
