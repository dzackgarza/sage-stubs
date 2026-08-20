type TruthRow = list[bool]
type TruthTableData = list[TruthRow]
type TruthTableList = list[list[str] | TruthRow]


class Truthtable:
    def __init__(
        self,
        t: TruthTableData,
        vo: list[str],
    ) -> None: ...
    def _latex_(self) -> str: ...
    def __repr__(self) -> str: ...
    def get_table_list(self) -> TruthTableList: ...
