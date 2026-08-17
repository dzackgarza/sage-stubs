from sage.rings.integer import Integer
from sage.rings.padics.padic_generic_element import pAdicGenericElement
from sage.structure.parent import ElementConstructorInput

def get_ordp(
    x: pAdicGenericElement | ElementConstructorInput, prime_pow: ElementConstructorInput
) -> pAdicGenericElement: ...
def get_preccap(
    x: pAdicGenericElement | ElementConstructorInput, prime_pow: ElementConstructorInput
) -> pAdicGenericElement: ...
def comb_prec(
    iprec: ElementConstructorInput, prec: int | Integer
) -> pAdicGenericElement: ...
def cconv_mpq_t_shared(
    out: ElementConstructorInput,
    x: pAdicGenericElement | ElementConstructorInput,
    prec: int | Integer,
    absolute: ElementConstructorInput,
    prime_pow: ElementConstructorInput,
) -> pAdicGenericElement: ...
def cconv_mpq_t_out_shared(
    out: ElementConstructorInput,
    x: pAdicGenericElement | ElementConstructorInput,
    valshift: ElementConstructorInput,
    prec: int | Integer,
    prime_pow: ElementConstructorInput,
) -> pAdicGenericElement: ...
def cconv_shared(
    out: ElementConstructorInput,
    x: pAdicGenericElement | ElementConstructorInput,
    prec: int | Integer,
    valshift: ElementConstructorInput,
    prime_pow: ElementConstructorInput,
) -> pAdicGenericElement: ...
def cconv_mpz_t_shared(
    out: ElementConstructorInput,
    x: pAdicGenericElement | ElementConstructorInput,
    prec: int | Integer,
    absolute: ElementConstructorInput,
    prime_pow: ElementConstructorInput,
) -> pAdicGenericElement: ...
def cconv_mpz_t_out_shared(
    out: ElementConstructorInput,
    x: pAdicGenericElement | ElementConstructorInput,
    valshift: ElementConstructorInput,
    prec: int | Integer,
    prime_pow: ElementConstructorInput,
) -> pAdicGenericElement: ...
