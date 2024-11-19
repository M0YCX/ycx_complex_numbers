import math

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

    def to_a(self, Z0=50 + 0j):
        """Convert to ABCD parameters"""
        d = 2 * self.s21
        Ap = ((1 + self.s11) * (1 - self.s22) + self.s12 * self.s21) / d
        Bp = ((1 + self.s11) * (1 + self.s22) - self.s12 * self.s21) / d
        Cp = ((1 - self.s11) * (1 - self.s22) - self.s12 * self.s21) / d
        Dp = ((1 - self.s11) * (1 + self.s22) + self.s12 * self.s21) / d
        return cn.Neta(
            a11=Ap,
            a12=Bp * Z0,
            a21=Cp / Z0,
            a22=Dp,
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

    @property
    def rollett_stability(self):
        return (
            1 + abs(self.determinant) ** 2 - abs(self.s11) ** 2 - abs(self.s22) ** 2
        ) / (2 * abs(self.s21) * abs(self.s12))

    @property
    def max_available_gain(self):
        Ds = self.determinant
        K = self.rollett_stability
        if K <= 1:
            raise ValueError("K must be greater than 1")

        B1 = 1 + abs(self.s11) ** 2 - abs(self.s22) ** 2 - abs(Ds) ** 2

        if B1 < 0:
            k_calc = K + math.sqrt(K**2 - 1)
        else:
            k_calc = K - math.sqrt(K**2 - 1)

        mag_db = 10 * math.log10(abs(self.s21) / abs(self.s12)) + 10 * math.log10(abs(k_calc))

        return mag_db

    @property
    def insertion_gain(self):
        return 20 * math.log10(abs(self.s21))

    def transducer_gain(self, ReflS=None, ReflL=None):
        Gt = (abs(self.s21)**2 * (1-abs(ReflS)**2) * (1-abs(ReflL)**2)) / (abs((1-self.s11*ReflS)*(1-self.s22*ReflL)-self.s12*self.s21*ReflL*ReflS)**2)
        return 10 * math.log10(Gt)