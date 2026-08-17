from typing import Self

from sage.rings.integer import Integer
from sage.rings.padics.padic_generic import pAdicGeneric
from sage.rings.padics.padic_generic_element import pAdicGenericElement
from sage.structure.parent import ElementConstructorInput

class pAdicExtElement(pAdicGenericElement):
    def ext_p_list(self, pos: ElementConstructorInput) -> Self: ...
    def ext_p_list_precs(
        self, pos: ElementConstructorInput, prec: int | Integer
    ) -> Self: ...
    def frobenius(self, arithmetic: ElementConstructorInput = ...) -> Self: ...
    def residue(
        self,
        absprec: int | Integer = ...,
        field: pAdicGeneric = ...,
        check_prec: ElementConstructorInput = ...,
    ) -> Self: ...
    def _const_term_test(self) -> Self: ...
    def _ext_p_list(self, pos: ElementConstructorInput) -> Self: ...
