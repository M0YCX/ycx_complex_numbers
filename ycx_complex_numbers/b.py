from ycx_complex_numbers.complex import Complex, Net
import ycx_complex_numbers as cn


class b(Complex):
    """ABCD' - A ABCD' (rev Chain/Cascade/Transmission) parameters."""

    _symbol = "b"

    def __init__(self, c=None):
        super().__init__(c)


class Netb(Net):
    def __init__(self, b11=None, b12=None, b21=None, b22=None):
        super().__init__(c11=b(b11), c12=b(b12), c21=b(b21), c22=b(b22))

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
    def b11(self):
        return self._c11

    @property
    def b12(self):
        return self._c12

    @property
    def b21(self):
        return self._c21

    @property
    def b22(self):
        return self._c22

    @property
    def is_passive(self):
        return self.A * self.D - self.B * self.C == 1

    @property
    def is_symmetrical(self):
        return self.A == self.D

    def to_a(self):
        return cn.Neta(
            a11=self.D / self.determinant,
            a12=self.B / self.determinant,
            a21=self.C / self.determinant,
            a22=self.A / self.determinant,
        )

    def to_H(self):
        return cn.NetH(
            h11=self.B / self.A,
            h12=1 / self.A,
            h21=-self.determinant / self.A,
            h22=self.C / self.A,
        )

    def to_Y(self):
        return cn.NetY(
            y11=self.A / self.B,
            y12=-1 / self.B,
            y21=-self.determinant / self.B,
            y22=self.D / self.B,
        )

    def to_Z(self):
        return cn.NetZ(
            z11=self.D / self.C,
            z12=1 / self.C,
            z21=self.determinant / self.C,
            z22=self.A / self.C,
        )
