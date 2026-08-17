from collections.abc import Mapping

from sage.symbolic.expression import Expression
from sage.symbolic.function import Function


type SymbolConversions = Mapping[str, str]
type SymbolTable = dict[str, dict[str, Expression | Function]]

symbol_table: SymbolTable

def register_symbol(
    obj: Expression | Function,
    conversions: SymbolConversions,
    nargs: int | None = None,
) -> None: ...
