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

    def to_Y(self, Z0=50 + 0j):
        return NetY(
            y11=((1 + self.s22) * (1 - self.s11) + self.s12 * self.s21)
            / ((1 + self.s11) * (1 + self.s22) + self.s12 * self.s21)
            * (1 / Z0),
            y12=(-2 * self.s12)
            / ((1 + self.s11) * (1 + self.s22) - self.s12 * self.s21)
            * (1 / Z0),
            y21=(-2 * self.s21)
            / ((1 + self.s11) * (1 + self.s22) - self.s12 * self.s21)
            * (1 / Z0),
            y22=((1 + self.s11) * (1 - self.s22) + self.s12 * self.s21)
            / ((1 + self.s22) * (1 + self.s11) - self.s12 * self.s21)
            * (1 / Z0),
        )
