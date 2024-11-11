from ycx_complex_numbers.complex import Complex, Net
from ycx_complex_numbers.Y import NetY
import ycx_complex_numbers as cn


class S(Complex):
    """S - An S (Scatter) parameter."""

    _symbol = "S"

    def __init__(self, c=None):
        super().__init__(c)


class NetS(Net):
    """S - Scatter 2-port-node parameters."""

    def __init__(self, s11=None, s12=None, s21=None, s22=None):
        super().__init__(c11=S(s11), c12=S(s12), c21=S(s21), c22=S(s22))

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
        """Convert to Y parameters"""
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

    def to_Z(self, Z0=50 + 0j):
        """Convert to Z parameters"""
        d = (1 - self.s11) * (1 - self.s22) - self.s12 * self.s21
        return cn.NetZ(
            z11=((1 + self.s11) * (1 - self.s22) + self.s12 * self.s21) / d * Z0,
            z12=(2 * self.s12) / d * Z0,
            z21=(2 * self.s21) / d * Z0,
            z22=((1 - self.s11) * (1 + self.s22) + self.s12 * self.s21) / d * Z0,
        )

    def to_a(self):
        """Convert to ABCD parameters"""
        d = 2 * self.s21
        return cn.Neta(
            a11=((1 + self.s11) * (1 - self.s22) + self.s12 * self.s21) / d,
            a12=((1 + self.s11) * (1 + self.s22) - self.s12 * self.s21) / d,
            a21=((1 - self.s11) * (1 - self.s22) - self.s12 * self.s21) / d,
            a22=((1 - self.s11) * (1 + self.s22) + self.s12 * self.s21) / d,
        )

    def to_H(self, Z0=50 + 0j):
        """Convert to H parameters"""
        d = (1 - self.s11) * (1 + self.s22) + self.s12 * self.s21
        return cn.NetH(
            h11=((1 + self.s11) * (1 + self.s22) - self.s12 * self.s21) / d * Z0,
            h12=(2 * self.s12) / d,
            h21=(-2 * self.s21) / d,
            h22=((1 - self.s11) * (1 - self.s22) - self.s12 * self.s21) / d * (1 / Z0),
        )

    def reflcoefin(self, ReflcoefL=cn.ReflCoef(0 + 0j)):
        return cn.ReflCoef(
            self.s11 + (self.s12 * self.s21 * ReflcoefL) / (1 - self.s22 * ReflcoefL)
        )

    def reflcoefout(self, ReflcoefS=cn.ReflCoef(0 + 0j)):
        return cn.ReflCoef(
            self.s22 + (self.s12 * self.s21 * ReflcoefS) / (1 - self.s11 * ReflcoefS)
        )
