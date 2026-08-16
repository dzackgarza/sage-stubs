import builtins

class _SageObject: ...

class Rule:
    def to_pairs(
        self,
        obj1: builtins.object = ...,
        obj2: builtins.object = ...,
        check: builtins.bool = ...,
    ) -> _SageObject: ...
    def forward_rule(
        self,
        obj1: builtins.object,
        obj2: builtins.object,
        check_standard: builtins.bool = ...,
        check: builtins.bool = ...,
    ) -> _SageObject: ...
    def backward_rule(
        self, p: builtins.int, q: builtins.int, output: builtins.object
    ) -> _SageObject: ...

class RuleRSK:
    def insertion(self, j: builtins.int, r: builtins.int) -> _SageObject: ...
    def reverse_insertion(
        self, x: builtins.object, row: builtins.object
    ) -> _SageObject: ...

class RuleEG:
    def insertion(self, j: builtins.int, r: builtins.int) -> _SageObject: ...
    def reverse_insertion(
        self, x: builtins.object, row: builtins.object
    ) -> _SageObject: ...

class RuleHecke:
    def forward_rule(
        self,
        obj1: builtins.object,
        obj2: builtins.object,
        check_standard: builtins.bool = ...,
    ) -> _SageObject: ...
    def backward_rule(
        self, p: builtins.int, q: builtins.int, output: builtins.object
    ) -> _SageObject: ...
    def insertion(
        self, j: builtins.int, ir: builtins.object, r: builtins.int, p: builtins.int
    ) -> _SageObject: ...
    def reverse_insertion(
        self, i: builtins.int, x: builtins.object, row: builtins.object, p: builtins.int
    ) -> _SageObject: ...

class RuleDualRSK:
    def to_pairs(
        self,
        obj1: builtins.object = ...,
        obj2: builtins.object = ...,
        check: builtins.bool = ...,
    ) -> _SageObject: ...
    def insertion(self, j: builtins.int, r: builtins.int) -> _SageObject: ...
    def reverse_insertion(
        self, x: builtins.object, row: builtins.object
    ) -> _SageObject: ...

class RuleCoRSK:
    def to_pairs(
        self,
        obj1: builtins.object = ...,
        obj2: builtins.object = ...,
        check: builtins.bool = ...,
    ) -> _SageObject: ...
    def backward_rule(
        self, p: builtins.int, q: builtins.int, output: builtins.object
    ) -> _SageObject: ...

class RuleSuperRSK:
    def to_pairs(
        self,
        obj1: builtins.object = ...,
        obj2: builtins.object = ...,
        check: builtins.bool = ...,
    ) -> _SageObject: ...
    def forward_rule(
        self,
        obj1: builtins.object,
        obj2: builtins.object,
        check_standard: builtins.bool = ...,
        check: builtins.bool = ...,
    ) -> _SageObject: ...
    def insertion(
        self, j: builtins.int, r: builtins.int, epsilon: builtins.int = ...
    ) -> _SageObject: ...
    def backward_rule(
        self, p: builtins.int, q: builtins.int, output: builtins.str = ...
    ) -> _SageObject: ...
    def reverse_insertion(
        self, x: builtins.object, row: builtins.object, epsilon: builtins.int = ...
    ) -> _SageObject: ...

class RuleStar:
    def forward_rule(
        self,
        obj1: builtins.object,
        obj2: builtins.object = ...,
        check_braid: builtins.bool = ...,
    ) -> _SageObject: ...
    def backward_rule(
        self, p: builtins.int, q: builtins.int, output: builtins.str = ...
    ) -> _SageObject: ...
    def insertion(self, b: builtins.object, r: builtins.int) -> _SageObject: ...
    def reverse_insertion(self, x: builtins.object, r: builtins.int) -> _SageObject: ...

class InsertionRules:
    RSK: _SageObject
    EG: _SageObject
    Hecke: _SageObject
    dualRSK: _SageObject
    coRSK: _SageObject
    superRSK: _SageObject
    Star: _SageObject

def RSK(
    self=...,
    obj2: builtins.object = ...,
    insertion: builtins.object = ...,
    check_standard: builtins.bool = ...,
    **options: builtins.object,
) -> _SageObject: ...

robinson_schensted_knuth: _SageObject

def RSK_inverse(
    self, q: builtins.int, output: builtins.str = ..., insertion: builtins.object = ...
) -> _SageObject: ...

robinson_schensted_knuth_inverse: _SageObject

def to_matrix(self, b: builtins.object) -> _SageObject: ...
