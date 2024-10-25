from ycx_complex_numbers.complex import Complex, Net
import ycx_complex_numbers as cn


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

    @property
    def is_passive(self):
        return self.h12 == -self.h21

    @property
    def is_symmetrical(self):
        return self.determinant == 1

    def to_a(self):
        return cn.Neta(
            a11=-self.determinant / self.h21,
            a12=-self.h11 / self.h21,
            a21=-self.h22 / self.h21,
            a22=-1 / self.h21,
        )

    def to_b(self):
        return cn.Netb(
            b11=1 / self.h12,
            b12=self.h11 / self.h12,
            b21=self.h22 / self.h12,
            b22=self.determinant / self.h12,
        )

    def to_ABCD(self):
        return self.to_a()

    def to_Y(self):
        return cn.NetY(
            y11=1 / self.h11,
            y12=-self.h12 / self.h11,
            y21=self.h21 / self.h11,
            y22=self.determinant / self.h11,
        )

    def to_Z(self):
        return cn.NetZ(
            z11=self.determinant / self.h22,
            z12=self.h12 / self.h22,
            z21=-self.h21 / self.h22,
            z22=1 / self.h22,
        )
