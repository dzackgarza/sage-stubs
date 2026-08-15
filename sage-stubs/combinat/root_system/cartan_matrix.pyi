from sage.matrix.matrix2 import Matrix
from sage.structure.parent import Parent
from typing import Self

class CartanMatrix(Matrix):
    def __new__(cls, cartan_type: Parent) -> Self: ...
    def __init__(self, cartan_type: Parent) -> None: ...
