import builtins

class _SageObject: ...

ext_table: _SageObject

def get_key_base(
    self,
    prec: builtins.int,
    type: builtins.object,
    print_mode: builtins.object,
    names: builtins.object,
    ram_name: builtins.str,
    print_pos: builtins.object,
    print_sep: builtins.object,
    print_alphabet: builtins.object,
    print_max_terms: builtins.object,
    show_prec: builtins.object,
    check: builtins.bool,
    valid_types: builtins.object,
    label: builtins.str = ...,
) -> _SageObject: ...

padic_field_cache: _SageObject
DEFAULT_PREC: _SageObject

class Qp_class:
    def create_key(
        self,
        p: builtins.int,
        prec: builtins.int = ...,
        type: builtins.str = ...,
        print_mode: builtins.object = ...,
        names: builtins.object = ...,
        ram_name: builtins.str = ...,
        print_pos: builtins.object = ...,
        print_sep: builtins.object = ...,
        print_alphabet: builtins.object = ...,
        print_max_terms: builtins.object = ...,
        show_prec: builtins.object = ...,
        check: builtins.bool = ...,
        label: builtins.str = ...,
    ) -> _SageObject: ...
    def create_object(
        self, version: builtins.object, key: builtins.object
    ) -> _SageObject: ...

Qp: _SageObject

def Qq(
    self,
    prec: builtins.int = ...,
    type: builtins.str = ...,
    modulus: builtins.object = ...,
    names: builtins.object = ...,
    print_mode: builtins.object = ...,
    ram_name: builtins.str = ...,
    res_name: builtins.str = ...,
    print_pos: builtins.object = ...,
    print_sep: builtins.object = ...,
    print_max_ram_terms: builtins.object = ...,
    print_max_unram_terms: builtins.object = ...,
    print_max_terse_terms: builtins.object = ...,
    show_prec: builtins.object = ...,
    check: builtins.bool = ...,
    implementation: builtins.str = ...,
) -> _SageObject: ...
def QpCR(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def QpFP(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def QqCR(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def QqFP(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def QpLC(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def QpLF(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def QpER(
    self,
    prec: builtins.int = ...,
    halt: builtins.object = ...,
    secure: builtins.bool = ...,
    *args: builtins.object,
    **kwds: builtins.object,
) -> _SageObject: ...

class Zp_class:
    def create_key(
        self,
        p: builtins.int,
        prec: builtins.int = ...,
        type: builtins.str = ...,
        print_mode: builtins.object = ...,
        names: builtins.object = ...,
        ram_name: builtins.str = ...,
        print_pos: builtins.object = ...,
        print_sep: builtins.object = ...,
        print_alphabet: builtins.object = ...,
        print_max_terms: builtins.object = ...,
        show_prec: builtins.object = ...,
        check: builtins.bool = ...,
        label: builtins.str = ...,
    ) -> _SageObject: ...
    def create_object(
        self, version: builtins.object, key: builtins.object
    ) -> _SageObject: ...

Zp: _SageObject

def Zq(
    self,
    prec: builtins.int = ...,
    type: builtins.str = ...,
    modulus: builtins.object = ...,
    names: builtins.object = ...,
    print_mode: builtins.object = ...,
    ram_name: builtins.str = ...,
    res_name: builtins.str = ...,
    print_pos: builtins.object = ...,
    print_sep: builtins.object = ...,
    print_max_ram_terms: builtins.object = ...,
    print_max_unram_terms: builtins.object = ...,
    print_max_terse_terms: builtins.object = ...,
    show_prec: builtins.object = ...,
    check: builtins.bool = ...,
    implementation: builtins.str = ...,
) -> _SageObject: ...
def ZpCR(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZpCA(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZpFM(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZpFP(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZqCR(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZqCA(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZqFM(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZqFP(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZpLC(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZpLF(
    self, prec: builtins.int = ..., *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def ZpER(
    self,
    prec: builtins.int = ...,
    halt: builtins.object = ...,
    secure: builtins.bool = ...,
    *args: builtins.object,
    **kwds: builtins.object,
) -> _SageObject: ...

class pAdicExtension_class:
    def create_key_and_extra_args(
        self,
        base: builtins.object,
        modulus: builtins.object,
        prec: builtins.int = ...,
        print_mode: builtins.object = ...,
        names: builtins.object = ...,
        var_name: builtins.str = ...,
        res_name: builtins.str = ...,
        unram_name: builtins.str = ...,
        ram_name: builtins.str = ...,
        print_pos: builtins.object = ...,
        print_sep: builtins.object = ...,
        print_alphabet: builtins.object = ...,
        print_max_ram_terms: builtins.object = ...,
        print_max_unram_terms: builtins.object = ...,
        print_max_terse_terms: builtins.object = ...,
        show_prec: builtins.object = ...,
        check: builtins.bool = ...,
        unram: builtins.bool = ...,
        implementation: builtins.str = ...,
    ) -> _SageObject: ...
    def create_object(
        self,
        version: builtins.object,
        key: builtins.object,
        approx_modulus: builtins.object = ...,
        shift_seed: builtins.object = ...,
    ) -> _SageObject: ...

ExtensionFactory: _SageObject
pAdicExtension: _SageObject

def split(self, prec: builtins.int) -> _SageObject: ...
def truncate_to_prec(
    self, R: builtins.int, absprec: builtins.object
) -> _SageObject: ...
def krasner_check(self, prec: builtins.int) -> _SageObject: ...
def is_eisenstein(self) -> bool: ...
def is_unramified(self) -> bool: ...
