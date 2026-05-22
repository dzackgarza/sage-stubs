from sage.combinat.abstract_tree import AbstractClonableTree, AbstractLabelledClonableTree
from sage.structure.list_clone import NormalizedClonableList


class RootedTree(AbstractClonableTree, NormalizedClonableList[RootedTree]): ...

class LabelledRootedTree(AbstractLabelledClonableTree, RootedTree): ...
