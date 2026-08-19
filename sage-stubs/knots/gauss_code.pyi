from collections.abc import Sequence

from sage.graphs.graph import Graph
from sage.rings.integer import Integer


type SignedGaussCode = Sequence[int | Integer]
type DowkerThistlethwaiteCode = Sequence[int | Integer]
type CrossingPair = tuple[int, int]
type CrossingCoordinates = list[CrossingPair]
type RecoveredGaussData = tuple[
    list[int],
    list[CrossingPair],
    list[CrossingPair],
    list[int],
]
type RectangularDiagram = tuple[
    Graph,
    tuple[CrossingCoordinates, CrossingCoordinates],
]


def dowker_to_gauss(
    code: DowkerThistlethwaiteCode,
) -> list[int]: ...


def recover_orientations(
    gauss: SignedGaussCode,
) -> RecoveredGaussData: ...


def rectangular_diagram(
    gauss: SignedGaussCode,
) -> RectangularDiagram: ...
