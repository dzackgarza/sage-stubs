from sage.misc.sage_timeit import SageTimeitResult

class SageTimeit:
    def eval(
        self,
        code: str,
        globs: dict[str, object] | None = ...,
        locals: dict[str, object] | None = ...,
        **kwds: object,
    ) -> SageTimeitResult | float: ...
    def __call__(
        self,
        code: str,
        globals: dict[str, object] | None = ...,
        **kwds: object,
    ) -> SageTimeitResult | float: ...

timeit: SageTimeit
