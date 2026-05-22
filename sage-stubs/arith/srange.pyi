from collections.abc import Iterator

def xsrange(
    start: object,
    end: object | None = ...,
    step: object = ...,
    universe: object | None = ...,
    *,
    coerce: bool = ...,
    include_endpoint: bool = ...,
    endpoint_tolerance: float = ...,
) -> Iterator[object]: ...

def srange(*args: object, **kwds: object) -> list[object]: ...

def ellipsis_iter(*args: object, step: object = ...) -> Iterator[object]: ...

def ellipsis_range(*args: object, step: object = ...) -> list[object]: ...
