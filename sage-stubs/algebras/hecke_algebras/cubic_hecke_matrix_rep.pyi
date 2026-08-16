import builtins

class _SageObject: ...

class GenSign:
    pos: _SageObject
    neg: _SageObject

class RepresentationType:
    def is_split(self) -> bool: ...
    def is_regular(self) -> bool: ...
    def data_section(self) -> _SageObject: ...
    def number_of_representations(self, nstrands: builtins.object) -> _SageObject: ...
    RegularLeft: _SageObject
    RegularRight: _SageObject
    SplitIrredMarin: _SageObject
    SplitIrredChevie: _SageObject

class AbsIrreducibeRep:
    def alternative_name(self) -> _SageObject: ...
    def dimension(self) -> _SageObject: ...
    def number_gens(self) -> _SageObject: ...
    def length_orbit(self) -> _SageObject: ...
    def gap_index(self) -> _SageObject: ...
    def internal_index(self) -> _SageObject: ...
    W2_100: _SageObject
    W2_001: _SageObject
    W2_010: _SageObject
    W3_100: _SageObject
    W3_001: _SageObject
    W3_010: _SageObject
    W3_011: _SageObject
    W3_110: _SageObject
    W3_101: _SageObject
    W3_111: _SageObject
    W4_100: _SageObject
    W4_001: _SageObject
    W4_010: _SageObject
    W4_011: _SageObject
    W4_110: _SageObject
    W4_101: _SageObject
    W4_111: _SageObject
    W4_120: _SageObject
    W4_201: _SageObject
    W4_012: _SageObject
    W4_102: _SageObject
    W4_210: _SageObject
    W4_021: _SageObject
    W4_213: _SageObject
    W4_132: _SageObject
    W4_321: _SageObject
    W4_231: _SageObject
    W4_123: _SageObject
    W4_312: _SageObject
    W4_422: _SageObject
    W4_224: _SageObject
    W4_242: _SageObject
    W4_333: _SageObject
    W4_333bar: _SageObject
    W5_100: _SageObject
    W5_001: _SageObject
    W5_010: _SageObject
    W5_013: _SageObject
    W5_130: _SageObject
    W5_301: _SageObject
    W5_031: _SageObject
    W5_103: _SageObject
    W5_310: _SageObject
    W5_203: _SageObject
    W5_032: _SageObject
    W5_320: _SageObject
    W5_230: _SageObject
    W5_023: _SageObject
    W5_302: _SageObject
    W5_033: _SageObject
    W5_330: _SageObject
    W5_303: _SageObject
    W5_163: _SageObject
    W5_631: _SageObject
    W5_316: _SageObject
    W5_136: _SageObject
    W5_613: _SageObject
    W5_361: _SageObject
    W5_366: _SageObject
    W5_663: _SageObject
    W5_636: _SageObject
    W5_933: _SageObject
    W5_339: _SageObject
    W5_393: _SageObject

class CubicHeckeMatrixRep:
    def __getitem__(self, item: builtins.object) -> _SageObject: ...
    def block_diagonal_list(self) -> _SageObject: ...
    def reduce_to_irr_block(self, irr: builtins.object) -> _SageObject: ...

class CubicHeckeMatrixSpace:
    @staticmethod
    def __classcall_private__(
        cls: builtins.object,
        cubic_hecke_algebra: builtins.object,
        representation_type: builtins.object = ...,
        subdivide: builtins.bool = ...,
        original: builtins.bool = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        base_ring: builtins.object,
        dimension: builtins.int,
        cubic_hecke_algebra: builtins.object,
        representation_type: builtins.object,
        subdivide: builtins.object,
    ) -> None: ...
    def construction(self) -> _SageObject: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...
    def __call__(
        self,
        entries: builtins.object = ...,
        coerce: builtins.bool = ...,
        copy: builtins.bool = ...,
    ) -> _SageObject: ...
    def zero(self) -> _SageObject: ...
    def one(self) -> _SageObject: ...
    def some_elements(self) -> _SageObject: ...
