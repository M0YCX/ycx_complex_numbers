from ycx_complex_numbers.complex import Complex, Net
import ycx_complex_numbers as cn


class a(Complex):
    """ABCD - A ABCD (fwd Chain/Cascade/Transmission) parameter."""

    _symbol = "a"

    def __init__(self, c=None):
        super().__init__(c)


class Neta(Net):
    """ABCD - An ABCD (fwd Chain/Cascade/Transmission) 2-port-node parameters."""
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

    @property
    def is_passive(self):
        return self.A * self.D - self.B * self.C == 1

    @property
    def is_symmetrical(self):
        return self.A == self.D

    def to_b(self):
        """Convert to ABCD' parameters"""
        return cn.Netb(
            b11=self.D / self.determinant,
            b12=self.B / self.determinant,
            b21=self.C / self.determinant,
            b22=self.A / self.determinant,
        )

    def to_H(self):
        """Convert to H parameters"""
        return cn.NetH(
            h11=self.B / self.D,
            h12=self.determinant / self.D,
            h21=-1 / self.D,
            h22=self.C / self.D,
        )

    def to_Y(self):
        """Convert to Y parameters"""
        return cn.NetY(
            y11=self.D / self.B,
            y12=-self.determinant / self.B,
            y21=-1 / self.B,
            y22=self.A / self.B,
        )

    def to_Z(self):
        """Convert to Z parameters"""
        return cn.NetZ(
            z11=self.A / self.C,
            z12=self.determinant / self.C,
            z21=1 / self.C,
            z22=self.D / self.C,
        )

    def to_S(self):
        """Convert to S parameters"""
        d = self.A + self.B + self.C + self.D
        return cn.NetS(
            s11=(self.A + self.B - self.C - self.D) / d,
            s12=(2 * (self.A * self.D - self.B * self.C)) / d,
            s21=2 / d,
            s22=(-self.A + self.B - self.C + self.D) / d,
        )
