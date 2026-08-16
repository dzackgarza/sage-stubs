import builtins

class _SageObject: ...

class OutputVideoBase:
    loop: builtins.bool

    def __init__(self, video: builtins.object, loop: builtins.bool = ...) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...
    def html_fragment(
        self, url: builtins.object, link_attrs: builtins.str = ...
    ) -> _SageObject: ...

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
