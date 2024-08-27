from ycx_complex_numbers.complex import Complex, Net


class S(Complex):
    """S - An S (Scatter) parameter."""

    _symbol = "S"

    def __init__(self, c=None):
        super().__init__(c)

class NetS(Net):
    def __init__(self, s11=None, s12=None, s21=None, s22=None):
        super().__init__(c11=s11, c12=s12, c21=s21, c22=s22)

    @property
    def s11(self):
        return self._c11
    @property
    def s12(self):
        return self._c12
    @property
    def s21(self):
        return self._c21
    @property
    def s22(self):
        return self._c22