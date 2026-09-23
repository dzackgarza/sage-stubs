"""Source-backed return shapes and ordered substitution in asymptotic helpers."""

from sage.rings.asymptotic.asymptotics_multivariate_generating_functions import (
    FractionWithFactoredDenominatorRing,
    FractionWithFactoredDenominatorSum,
    diff_seq,
    subs_all,
)

x, y = var("x y")
expressions = (x + y, x**2)
substituted = subs_all(expressions, {x: 1})
assert isinstance(substituted, list)
assert substituted == [y + 1, 1]
assert all(value.parent() is SR for value in substituted)

named = {"sum": x + y, "square": x**2}
assert subs_all(named, {x: 1}) == {"sum": y + 1, "square": 1}
assert subs_all((named,), {x: 1}) == [{"sum": y + 1, "square": 1}]
assert subs_all((x + y, named), {x: 1}) == [
    y + 1, {"sum": y + 1, "square": 1}
]

# Substitutions are successive, not simultaneous; changing their order changes
# the result. A tuple of substitutions has the same order as a list.
ordered = [{x: y}, {y: 3}]
assert subs_all(x, ordered) == 3
assert subs_all(x, tuple(ordered)) == 3
assert subs_all(x, list(reversed(ordered))) == y
assert subs_all(x, None) == x
assert subs_all(ZZ.zero(), None) == 0
assert diff_seq((x, y), ((1, 0), (0,))) == (x, x, y)

# Element.subs can change the concrete type: evaluating a polynomial need not
# return a polynomial. This is why the general helper cannot promise T -> T.
univariate = PolynomialRing(ZZ, "t")
t = univariate.gen()
evaluated = subs_all(t**2, {t: 2})
assert evaluated == 4
assert evaluated.parent() is ZZ

polynomials = PolynomialRing(ZZ, names=("u", "v"))
u, v = polynomials.gens()
fractions = FractionWithFactoredDenominatorRing(polynomials)
fraction = fractions(u + v, [(v, 1), (u, 1)])
assert fractions.base_ring() is ZZ
assert fraction.parent() is fractions
assert repr(FractionWithFactoredDenominatorSum([fraction])) == repr(fraction)
