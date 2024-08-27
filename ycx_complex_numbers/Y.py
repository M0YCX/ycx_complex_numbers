from ycx_complex_numbers.complex import Complex, Net
from ycx_complex_numbers.Z import NetZ


class Y(Complex):
    """Y - A Y (Admittance) parameter."""

    _symbol = "Y"

    def __init__(self, c=None):
        super().__init__(c)


class NetY(Net):
    def __init__(self, y11=None, y12=None, y21=None, y22=None):
        super().__init__(c11=Y(y11), c12=Y(y12), c21=Y(y21), c22=Y(y22))

    @property
    def y11(self):
        return self._c11

    @property
    def y12(self):
        return self._c12

    @property
    def y21(self):
        return self._c21

    @property
    def y22(self):
        return self._c22

    def to_Z(self):
        return NetZ(
            z11=self.y22 / self.determinant,
            z12=-self.y12 / self.determinant,
            z21=-self.y21 / self.determinant,
            z22=self.y11 / self.determinant,
        )

    def in_out(self, ys=None, yl=None):
        """return the input and output admittance for this Y matrix and given source and load admittances"""
        ys = Y(ys)
        yl = Y(yl)
        return {
            "Yin": self.y11 - (self.y12 * self.y21) / (yl + self.y22),
            "Yout": self.y22 - (self.y12 * self.y21) / (ys + self.y11),
            "Y": self,
            "ys": ys,
            "yl": yl,
        }
