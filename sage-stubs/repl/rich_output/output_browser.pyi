import builtins

from sage.repl.rich_output.buffer import OutputBuffer

class _SageObject: ...

latex_re: _SageObject

class OutputHtml:
    latex: OutputBuffer
    html: OutputBuffer

    def __init__(self, html: builtins.object) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...
    def print_to_stdout(self) -> _SageObject: ...
    def with_html_tag(self) -> _SageObject: ...
