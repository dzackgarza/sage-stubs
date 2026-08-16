from sage.structure.element import Element

def covariant_z0(
    self,
    z0_cov: bool = False,
    prec: int = 53,
    emb: object = None,
    error_limit: float = 1e-06,
) -> tuple[object, ...]: ...
def epsinv(
    self,
    target: object,
    prec: int = 53,
    target_tol: float = 0.001,
    z: object = None,
    emb: object = None,
) -> Element: ...
def get_bound_poly(
    self, prec: int = 53, norm_type: str = "norm", emb: object = None
) -> Element: ...
def smallest_poly(
    self, prec: int = 53, norm_type: str = "norm", emb: object = None
) -> Element: ...
