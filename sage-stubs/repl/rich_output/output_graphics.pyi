import builtins

from sage.repl.rich_output.buffer import OutputBuffer

class _SageObject: ...

class OutputImagePng:
    png: OutputBuffer

    def __init__(self, png: builtins.object) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...

class OutputImageGif:
    gif: OutputBuffer

    def __init__(self, gif: builtins.object) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...
    def html_fragment(self) -> _SageObject: ...

class OutputImageJpg:
    jpg: OutputBuffer

    def __init__(self, jpg: builtins.object) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...

class OutputImageSvg:
    svg: OutputBuffer

    def __init__(self, svg: builtins.object) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...

class OutputImagePdf:
    pdf: OutputBuffer

    def __init__(self, pdf: builtins.object) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...

class OutputImageDvi:
    dvi: OutputBuffer

    def __init__(self, dvi: builtins.object) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...
