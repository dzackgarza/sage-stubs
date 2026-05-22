from sage.libs.gap.element import GapElement

class GroupMixinLibGAP:
    def gap(self) -> GapElement: ...
