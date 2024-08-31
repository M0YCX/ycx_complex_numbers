from ycx_complex_numbers.complex import Complex, Net
# from ycx_complex_numbers.Z import NetZ


class H(Complex):
    """H - A H (hybrid) parameter."""

    _symbol = "H"

    def __init__(self, c=None):
        super().__init__(c)


class NetH(Net):
    def __init__(self, h11=None, h12=None, h21=None, h22=None):
        super().__init__(c11=H(h11), c12=H(h12), c21=H(h21), c22=H(h22))

    @property
    def h11(self):
        return self._c11

    @property
    def h12(self):
        return self._c12

    @property
    def h21(self):
        return self._c21

    @property
    def h22(self):
        return self._c22

    # def to_Z(self):
    #     return NetZ(
    #         z11=self.y22 / self.determinant,
    #         z12=-self.y12 / self.determinant,
    #         z21=-self.y21 / self.determinant,
    #         z22=self.y11 / self.determinant,
    #     )

