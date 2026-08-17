from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.element import RingElement


type AngularMomentum = int | Integer | Rational
type WignerValue = Integer | Rational | RealNumber | RingElement


def wigner_3j(
    j_1: AngularMomentum,
    j_2: AngularMomentum,
    j_3: AngularMomentum,
    m_1: AngularMomentum,
    m_2: AngularMomentum,
    m_3: AngularMomentum,
    prec: int | None = None,
) -> WignerValue: ...
def clebsch_gordan(
    j_1: AngularMomentum,
    j_2: AngularMomentum,
    j_3: AngularMomentum,
    m_1: AngularMomentum,
    m_2: AngularMomentum,
    m_3: AngularMomentum,
    prec: int | None = None,
) -> WignerValue: ...
def racah(
    aa: AngularMomentum,
    bb: AngularMomentum,
    cc: AngularMomentum,
    dd: AngularMomentum,
    ee: AngularMomentum,
    ff: AngularMomentum,
    prec: int | None = None,
) -> WignerValue: ...
def wigner_6j(
    j_1: AngularMomentum,
    j_2: AngularMomentum,
    j_3: AngularMomentum,
    j_4: AngularMomentum,
    j_5: AngularMomentum,
    j_6: AngularMomentum,
    prec: int | None = None,
) -> WignerValue: ...
def wigner_9j(
    j_1: AngularMomentum,
    j_2: AngularMomentum,
    j_3: AngularMomentum,
    j_4: AngularMomentum,
    j_5: AngularMomentum,
    j_6: AngularMomentum,
    j_7: AngularMomentum,
    j_8: AngularMomentum,
    j_9: AngularMomentum,
    prec: int | None = None,
) -> WignerValue: ...
def gaunt(
    l_1: AngularMomentum,
    l_2: AngularMomentum,
    l_3: AngularMomentum,
    m_1: AngularMomentum,
    m_2: AngularMomentum,
    m_3: AngularMomentum,
    prec: int | None = None,
) -> WignerValue: ...
