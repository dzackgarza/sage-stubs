import numpy as np
from numpy.typing import NDArray

from sage.matrix.matrix_mod2_dense import Matrix_mod2_dense

type Mod2VectorArray = (
    NDArray[np.int8]
    | NDArray[np.int32]
    | NDArray[np.int64]
    | NDArray[np.bool_]
)
type Mod2MatrixArray = (
    NDArray[np.int8]
    | NDArray[np.int32]
    | NDArray[np.int64]
)

def set_mzd_from_numpy(
    entries_addr: int,
    degree: int,
    x: Mod2VectorArray | object,
) -> int: ...
def _set_matrix_mod2_from_numpy_helper(
    a: Matrix_mod2_dense,
    b: Mod2MatrixArray,
) -> int: ...
def set_matrix_mod2_from_numpy(
    a: Matrix_mod2_dense,
    b: Mod2MatrixArray | object,
) -> int: ...
