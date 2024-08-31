from ycx_complex_numbers.complex import Complex, Net
# from ycx_complex_numbers.Z import NetZ


class T(Complex):
    """T - A ABCD (Transmission) parameter."""

    _symbol = "T"

    def __init__(self, c=None):
        super().__init__(c)


class NetT(Net):
    def __init__(self, A=None, B=None, C=None, D=None):
        super().__init__(c11=T(A), c12=T(B), c21=T(C), c22=T(D))

    @property
    def A(self):
        return self._c11

    @property
    def B(self):
        return self._c12

    @property
    def C(self):
        return self._c21

    @property
    def D(self):
        return self._c22

    # def to_Z(self):
    #     return NetZ(
    #         z11=self.y22 / self.determinant,
    #         z12=-self.y12 / self.determinant,
    #         z21=-self.y21 / self.determinant,
    #         z22=self.y11 / self.determinant,
    #     )

