from ycx_complex_numbers.a import a, Neta
import ycx_complex_numbers as cn
from warnings import warn


class ABCD(a):
    def __init__(self, c=None):
        warn("ABCD is deprecated, please use 'a'")
        super().__init__(c)


class NetABCD(Neta):
    def __init__(self, A=None, B=None, C=None, D=None):
        warn("NetABCD is deprecated, please use 'Neta'")
        super().__init__(a11=a(A), a12=a(B), a21=a(C), a22=a(D))
