def sage_eval(
    source: str | tuple[str, str] | tuple[str, str, dict[str, object]],
    locals: dict[str, object] | None = None,
    cmds: str = '',
    preparse: bool = True
) -> object: ...

def sageobj(x: object, vars: dict[str, object] | None = None) -> object: ...
