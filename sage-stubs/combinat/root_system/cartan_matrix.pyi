
from sage.matrix.matrix2 import Matrix
from sage.structure.parent import Parent

class CartanMatrix(Matrix):
    def __new__(cls, cartan_type: Parent) -> CartanMatrix: ...
    def __init__(self, cartan_type: Parent) -> None: ...
