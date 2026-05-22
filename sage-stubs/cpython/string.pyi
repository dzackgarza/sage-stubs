FS_ENCODING: str

def bytes_to_str(
    b: bytes | str,
    encoding: str | None = None,
    errors: str | None = None,
) -> str: ...
def str_to_bytes(
    s: str | bytes,
    encoding: str | None = None,
    errors: str | None = None,
) -> bytes: ...
