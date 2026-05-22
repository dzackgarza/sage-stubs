from sage.matrix.matrix import Matrix

class VectorSpaceMorphism:
    def __init__(
        self,
        homspace: object,
        A: Matrix,
        side: str = ...,
    ) -> None: ...
    def is_invertible(self) -> bool: ...

def linear_transformation(
    arg0: object,
    arg1: object = ...,
    arg2: object = ...,
    side: str = ...,
) -> VectorSpaceMorphism: ...
