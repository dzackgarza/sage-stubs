"""Shared annotation policy constants for stub guardrails."""

OBJECT_RETURN_OK = {"__new__"}

ALLOWED_OBJECT_PARAMETER_SLOTS = {
    ("__contains__", "x"),
    ("__eq__", "other"),
    ("__ne__", "other"),
    ("dumps", "obj"),
    ("save", "obj"),
}


def is_allowed_object_parameter(function_name: str, parameter_name: str) -> bool:
    return (function_name, parameter_name) in ALLOWED_OBJECT_PARAMETER_SLOTS


def is_allowed_object_parameter_surface(name: str) -> bool:
    return any(
        name.endswith(f"{function_name}.{parameter_name}")
        for function_name, parameter_name in ALLOWED_OBJECT_PARAMETER_SLOTS
    )
