"""Shared annotation policy constants for stub guardrails."""

OBJECT_RETURN_OK = {"__new__"}

ALLOWED_OBJECT_PARAMETER_SLOTS = {
    ("__contains__", "x"),
    ("__eq__", "other"),
    ("__ne__", "other"),
}

ALLOWED_OBJECT_PARAMETER_SURFACES = {
    ("sage-stubs/rings/ring.pyi", "__xor__", "n"),
    ("sage-stubs/rings/ring.pyi", "_is_Field", "x"),
    ("sage-stubs/structure/sage_object.pyi", "dumps", "obj"),
    ("sage-stubs/structure/sage_object.pyi", "save", "obj"),
}


def is_allowed_object_parameter(
    function_name: str,
    parameter_name: str,
    path: str | None = None,
) -> bool:
    if (function_name, parameter_name) in ALLOWED_OBJECT_PARAMETER_SLOTS:
        return True
    return (path, function_name, parameter_name) in ALLOWED_OBJECT_PARAMETER_SURFACES


def is_allowed_object_parameter_surface(path: str, name: str) -> bool:
    if any(
        name.endswith(f"{function_name}.{parameter_name}")
        for function_name, parameter_name in ALLOWED_OBJECT_PARAMETER_SLOTS
    ):
        return True
    return any(
        path == allowed_path and name.endswith(f"{function_name}.{parameter_name}")
        for allowed_path, function_name, parameter_name in ALLOWED_OBJECT_PARAMETER_SURFACES
    )
