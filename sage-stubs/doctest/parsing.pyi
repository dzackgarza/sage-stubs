import builtins
from typing import Self

class _SageObject: ...

ansi_escape_sequence: _SageObject
special_optional_regex_raw: _SageObject
tag_with_explanation_regex_raw: _SageObject
optional_regex: _SageObject
special_optional_regex: _SageObject
tag_with_explanation_regex: _SageObject
no_doctest_regex: _SageObject
optional_tag_regex: _SageObject
optional_file_directive_regex: _SageObject

def parse_optional_tags(
    self,
) -> tuple[dict[str, str | None], str, bool] | dict[str, str | None]: ...
def parse_file_optional_tags(self) -> dict[str, str | None]: ...
def unparse_optional_tags(self, prefix: builtins.str = ...) -> str: ...

optional_tag_columns: _SageObject
standard_tag_columns: _SageObject

def update_optional_tags(
    self,
    tags: builtins.object = ...,
    *,
    add_tags: builtins.object = ...,
    remove_tags: builtins.object = ...,
    force_rewrite: builtins.bool = ...,
) -> _SageObject: ...
def parse_tolerance(self, want: builtins.object) -> _SageObject: ...
def pre_hash(self) -> str: ...
def get_source(self) -> _SageObject: ...
def reduce_hex(self) -> _SageObject: ...

class OriginalSource:
    def __init__(self, example: builtins.object) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: builtins.object) -> builtins.bool | None: ...

class SageDocTestParser:
    long: builtins.bool
    file_optional_tags: _SageObject
    optional_tags: bool
    optional_only: bool
    optionals: _SageObject
    probed_tags: bool

    def __init__(
        self,
        optional_tags: builtins.tuple[_SageObject, ...] = ...,
        long: builtins.bool = ...,
        *,
        probed_tags: builtins.tuple[_SageObject, ...] = ...,
        file_optional_tags: builtins.tuple[_SageObject, ...] = ...,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def parse(
        self, string: builtins.object, *args: builtins.object
    ) -> list[doctest.Example | str]: ...

class SageOutputChecker:
    def human_readable_escape_sequences(
        self, string: builtins.object
    ) -> _SageObject: ...
    def check_output(
        self, want: builtins.object, got: builtins.object, optionflags: builtins.object
    ) -> _SageObject: ...
    def do_fixup(self, want: builtins.object, got: builtins.object) -> _SageObject: ...
    def output_difference(
        self,
        example: builtins.object,
        got: builtins.object,
        optionflags: builtins.object,
    ) -> _SageObject: ...
