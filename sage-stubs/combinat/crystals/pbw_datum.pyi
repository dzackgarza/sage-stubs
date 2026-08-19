from collections.abc import Hashable, Iterable, Sequence

from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations
from sage.combinat.root_system.root_system import RootSystem
from sage.combinat.root_system.weyl_group import WeylGroup_gens
from sage.rings.integer import Integer

type CartanIndex = Hashable
type CartanTypeInput = CartanType_abstract | Sequence[object] | str
type LongWord = tuple[CartanIndex, ...]
type LusztigDatum = tuple[int | Integer, ...]
type RootLatticeElement = CombinatorialFreeModule.Element
type BraidInterval = tuple[int, int]
type CartanSubmatrixData = tuple[int, int]
type EnhancedBraidStep = tuple[
    BraidInterval | None,
    CartanSubmatrixData | None,
]
type EnhancedBraidChain = list[EnhancedBraidStep]

class PBWDatum:
    parent: PBWData
    long_word: LongWord
    lusztig_datum: LusztigDatum

    def __init__(
        self,
        parent: PBWData,
        long_word: Iterable[CartanIndex],
        lusztig_datum: Iterable[int | Integer],
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other_PBWDatum: object) -> bool: ...
    def is_equivalent_to(self, other_pbw_datum: PBWDatum) -> bool: ...
    def convert_to_long_word_with_first_letter(
        self,
        i: CartanIndex,
    ) -> PBWDatum: ...
    def convert_to_new_long_word(
        self,
        new_long_word: Iterable[CartanIndex],
    ) -> PBWDatum: ...
    def weight(self) -> RootLatticeElement: ...
    def star(self) -> PBWDatum: ...

class PBWData:
    cartan_type: CartanType_abstract
    root_system: RootSystem
    root_lattice: RootLatticeRealizations.ParentMethods
    weyl_group: WeylGroup_gens

    def __init__(self, cartan_type: CartanTypeInput) -> None: ...
    def convert_to_new_long_word(
        self,
        pbw_datum: PBWDatum,
        new_long_word: Iterable[CartanIndex],
    ) -> PBWDatum: ...
    def _root_list_from(
        self,
        reduced_word: LongWord,
    ) -> list[RootLatticeElement]: ...
    def _long_word_begin_with(self, i: CartanIndex) -> LongWord: ...

def compute_new_lusztig_datum(
    enhanced_braid_chain: EnhancedBraidChain,
    initial_lusztig_datum: Iterable[int | Integer],
) -> LusztigDatum: ...
def tropical_plucker_relation(
    a: CartanSubmatrixData,
    lusztig_datum: Iterable[int | Integer],
) -> LusztigDatum: ...
def enhance_braid_move_chain(
    braid_move_chain: Sequence[Sequence[CartanIndex]],
    cartan_type: CartanType_abstract,
) -> EnhancedBraidChain: ...
