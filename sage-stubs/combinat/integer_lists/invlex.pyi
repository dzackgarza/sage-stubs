from typing import Any
from collections.abc import Iterator, Iterable
from sage.combinat.integer_lists.lists import IntegerLists

class IntegerListsLex(IntegerLists):
    @classmethod
    def __classcall_private__(cls, n: int | None = None, **kwargs: object) -> IntegerListsLex: ...
