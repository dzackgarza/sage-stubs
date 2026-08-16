import builtins

class _SageObject: ...

def signal_name(self) -> str: ...

class DocTestReporter:
    error_status: int
    sources_completed: int
    postscript: dict[str, int]

    def __init__(self, controller: builtins.object) -> None: ...
    def were_doctests_with_optional_tag_run(
        self, tag: builtins.object
    ) -> _SageObject: ...
    def report_head(
        self, source: builtins.object, fail_msg: builtins.object = ...
    ) -> _SageObject: ...
    def report(
        self,
        source: builtins.object,
        timeout: builtins.object,
        return_code: builtins.object,
        results: builtins.object,
        output: builtins.object,
        pid: builtins.object = ...,
        *,
        process_tree_before_kill: builtins.object = ...,
    ) -> _SageObject: ...
    def finalize(self) -> _SageObject: ...
