class SageTimeitResult:
    stats: tuple[int, int, int, float, str]
    series: list[float] | None
    def __init__(self, stats: tuple[int, int, int, float, str], series: list[float] | None = ...) -> None: ...

def sage_timeit(
    stmt: str,
    globals_dict: dict[str, object] | None = ...,
    preparse: bool | None = ...,
    number: int = ...,
    repeat: int = ...,
    precision: int = ...,
    seconds: bool = ...,
) -> SageTimeitResult | float: ...
