from sage.libs.gap.element import GapElement, GapElement_Function, _SupportsGapInit
from sage.structure.parent import Parent


class Gap(Parent):
    def eval(self, gap_command: str | _SupportsGapInit) -> GapElement | None: ...
    def function_factory(self, function_name: str) -> GapElement_Function: ...
    def __getattr__(self, name: str) -> GapElement_Function: ...


libgap: Gap
