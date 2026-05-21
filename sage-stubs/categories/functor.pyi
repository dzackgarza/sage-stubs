from typing import Any

class Functor:
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
