import types

def modify_for_nested_pickle(
    cls: type,
    name_prefix: str,
    module: types.ModuleType,
    first_run: bool = ...,
) -> None: ...
def nested_pickle(cls: type) -> type: ...

class NestedClassMetaclass(type):
    def __init__(self, *args: object) -> None: ...

class MainClass(object, metaclass=NestedClassMetaclass):
    class NestedClass:
        class NestedSubClass:
            def dummy(self, x: object, *args: object, r: tuple[int, int, float] = ..., **kwds: object) -> None: ...

class SubClass(MainClass): ...

def _provide_SubClass() -> type[SubClass]: ...

class CopiedClass:
    NestedClass: type[MainClass.NestedClass]
    NestedSubClass: type[MainClass.NestedClass.NestedSubClass]
    SubClass: type[SubClass]

class A1:
    class A2:
        class A3: ...
