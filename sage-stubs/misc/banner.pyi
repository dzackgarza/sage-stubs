import builtins

class _SageObject: ...

class VersionDict:
    major: _SageObject
    minor: _SageObject
    tiny: _SageObject
    prerelease: _SageObject

def version(self) -> str: ...
def banner_text(self=...) -> str: ...
def banner(self) -> None: ...
def version_dict(self) -> VersionDict: ...
def require_version(
    self,
    minor: builtins.int = ...,
    tiny: builtins.float = ...,
    prerelease: builtins.bool = ...,
    print_message: builtins.bool = ...,
) -> bool: ...
