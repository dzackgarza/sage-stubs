# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class OutputVideoBase:
    def __init__(self, video: builtins.object, loop: builtins.bool = ...) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...
    def html_fragment(self, url: builtins.object, link_attrs: builtins.str = ...) -> _SageObject: ...

class OutputVideoOgg:
    ext: _SageObject
    mimetype: _SageObject

class OutputVideoWebM:
    ext: _SageObject
    mimetype: _SageObject

class OutputVideoMp4:
    ext: _SageObject
    mimetype: _SageObject

class OutputVideoFlash:
    ext: _SageObject
    mimetype: _SageObject

class OutputVideoMatroska:
    ext: _SageObject
    mimetype: _SageObject

class OutputVideoAvi:
    ext: _SageObject
    mimetype: _SageObject

class OutputVideoWmv:
    ext: _SageObject
    mimetype: _SageObject

class OutputVideoQuicktime:
    ext: _SageObject
    mimetype: _SageObject
