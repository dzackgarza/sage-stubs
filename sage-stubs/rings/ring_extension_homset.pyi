from sage.categories.homset import HomsetCallInput
from sage.rings.homset import RingHomset_generic
from sage.rings.morphism import RingHomomorphism

class RingExtensionHomset(RingHomset_generic):
    # Source returns RingExtensionHomomorphism (ring_extension_homset.py:41);
    # it is a sibling of RingHomomorphism under RingMap, so the base type is
    # the mypy-compatible surface.
    def __call__(self, x: HomsetCallInput = ..., *args: object, **kwds: object) -> RingHomomorphism: ...
