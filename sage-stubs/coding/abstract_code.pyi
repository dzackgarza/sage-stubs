import builtins
from collections.abc import (
    Iterator as _Iterator,
)

class _SageObject: ...

class AbstractCode:
    def __init__(
        self,
        length: builtins.int,
        default_encoder_name: builtins.str = ...,
        default_decoder_name: builtins.str = ...,
        metric: builtins.str = ...,
    ) -> None: ...
    def __getstate__(self) -> _SageObject: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...
    def __contains__(self, c: object) -> bool: ...
    def ambient_space(self) -> _SageObject: ...
    def __call__(self, m: builtins.int) -> _SageObject: ...
    def list(self) -> _SageObject: ...
    def length(self) -> _SageObject: ...
    def metric(self) -> _SageObject: ...
    def add_decoder(
        self, name: builtins.str, decoder: builtins.object
    ) -> _SageObject: ...
    def add_encoder(
        self, name: builtins.str, encoder: builtins.object
    ) -> _SageObject: ...
    def decode_to_code(
        self,
        word: builtins.object,
        decoder_name: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def decode_to_message(
        self,
        word: builtins.object,
        decoder_name: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def decoder(
        self,
        decoder_name: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def decoders_available(self, classes: builtins.bool = ...) -> _SageObject: ...
    def encode(
        self,
        word: builtins.object,
        encoder_name: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def encoder(
        self,
        encoder_name: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def encoders_available(self, classes: builtins.bool = ...) -> _SageObject: ...
    def unencode(
        self,
        c: builtins.object,
        encoder_name: builtins.str = ...,
        nocheck: builtins.bool = ...,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def random_element(
        self, *args: builtins.object, **kwds: builtins.object
    ) -> _SageObject: ...
