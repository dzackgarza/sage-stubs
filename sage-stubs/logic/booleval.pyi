from collections.abc import Mapping

from sage.logic.logicparser import BooleanBranch, BooleanParseTree, BooleanOperator


def eval_formula(
    tree: BooleanParseTree,
    vdict: Mapping[str, bool],
) -> bool: ...
def eval_f(tree: BooleanBranch) -> bool: ...
def eval_op(
    op: BooleanOperator | str,
    lv: str | bool | None,
    rv: str | bool | None,
) -> bool: ...
