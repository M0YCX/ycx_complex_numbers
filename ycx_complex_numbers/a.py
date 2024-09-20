from ycx_complex_numbers.complex import Complex, Net
import ycx_complex_numbers as cn


class a(Complex):
    """ABCD - A ABCD (fwd Chain/Cascade/Transmission) parameters."""

    _symbol = "a"

    def __init__(self, c=None):
        super().__init__(c)


class Neta(Net):
    def __init__(self, a11=None, a12=None, a21=None, a22=None):
        super().__init__(c11=a(a11), c12=a(a12), c21=a(a21), c22=a(a22))

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

    @property
    def a11(self):
        return self._c11

    @property
    def a12(self):
        return self._c12

    @property
    def a21(self):
        return self._c21

    @property
    def a22(self):
        return self._c22

    def to_b(self):
        return cn.Netb(
            b11=self.D / self.determinant,
            b12=self.B / self.determinant,
            b21=self.C / self.determinant,
            b22=self.A / self.determinant,
        )

    def to_H(self):
        return cn.NetH(
            h11=self.B / self.D,
            h12=self.determinant / self.D,
            h21=-1 / self.D,
            h22=self.C / self.D,
        )

    def to_Y(self):
        return cn.NetY(
            y11=self.D / self.B,
            y12=-self.determinant / self.B,
            y21=-1 / self.B,
            y22=self.A / self.B,
        )

    def to_Z(self):
        return cn.NetZ(
            z11=self.A / self.C,
            z12=self.determinant / self.C,
            z21=1 / self.C,
            z22=self.D / self.C,
        )