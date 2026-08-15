from sage.modules.free_module import FreeModule_generic
from sage.matrix.matrix2 import Matrix

class FreeQuadraticModule_generic_pid(FreeModule_generic):
    def gram_matrix(self) -> Matrix: ...
