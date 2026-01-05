import math
from math import sqrt

# from mpmath import mp

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
        """Convert this matrix to Y-Parameters.
        Parameters:
            - Z0: Normalised complex impedance. Can be specified as:
                + a real value. e.g. 50
                + a complex value, e.g. 50+0j
                + a 2-element array of real or complex values, representing the
                normalised impedances of each ports' termination (aka ZS and
                ZL respectively)
        """
        Z01 = Complex(50 + 0j)
        Z02 = Complex(50 + 0j)

        if isinstance(Z0, int) or isinstance(Z0, complex):
            Z01 = Complex(Z0)
            Z02 = Complex(Z0)
        elif isinstance(Z0, tuple) or isinstance(Z0, list):
            Z01 = Complex(Z0[0])
            Z02 = Complex(Z0[1])

        return NetY(
            y11=(
                (1 - self.s11) * (Z02.conjugate + self.s22 * Z02)
                + self.s12 * self.s21 * Z02
            )
            / (
                (Z01.conjugate + self.s11 * Z01) * (Z02.conjugate + self.s22 * Z02)
                - self.s12 * self.s21 * Z01 * Z02
            ),
            y12=(-2 * self.s12 * sqrt(Z01.real * Z02.real))
            / (
                (Z01.conjugate + self.s11 * Z01) * (Z02.conjugate + self.s22 * Z02)
                - self.s12 * self.s21 * Z01 * Z02
            ),
            y21=(-2 * self.s21 * sqrt(Z01.real * Z02.real))
            / (
                (Z01.conjugate + self.s11 * Z01) * (Z02.conjugate + self.s22 * Z02)
                - self.s12 * self.s21 * Z01 * Z02
            ),
            y22=(
                (Z01.conjugate + self.s11 * Z01) * (1 - self.s22)
                + self.s12 * self.s21 * Z01
            )
            / (
                (Z01.conjugate + self.s11 * Z01) * (Z02.conjugate + self.s22 * Z02)
                - self.s12 * self.s21 * Z01 * Z02
            ),
        )

    def to_Z(self, Z0=50 + 0j):
        """Convert this matrix to Z-Parameters.
        Parameters:
            - Z0: Normalised complex impedance. Can be specified as:
                + a real value. e.g. 50
                + a complex value, e.g. 50+0j
                + a 2-element array of real or complex values, representing the
                normalised impedances of each ports' termination (aka ZS and
                ZL respectively)
        """
        Z01 = Complex(50 + 0j)
        Z02 = Complex(50 + 0j)

        if isinstance(Z0, int) or isinstance(Z0, complex):
            Z01 = Complex(Z0)
            Z02 = Complex(Z0)
        elif isinstance(Z0, tuple) or isinstance(Z0, list):
            Z01 = Complex(Z0[0])
            Z02 = Complex(Z0[1])

        d = (1 - self.s11) * (1 - self.s22) - self.s12 * self.s21

        # return cn.NetZ(
        #     z11=((1 + self.s11) * (1 - self.s22) + self.s12 * self.s21) / d * Z0,
        #     z12=(2 * self.s12) / d * Z0,
        #     z21=(2 * self.s21) / d * Z0,
        #     z22=((1 - self.s11) * (1 + self.s22) + self.s12 * self.s21) / d * Z0,
        # )
        return cn.NetZ(
            z11=(
                (Z01.conjugate + self.s11 * Z01) * (1 - self.s22)
                + self.s12 * self.s21 * Z01
            )
            / d,
            z12=(2 * self.s12 * sqrt(Z01.real * Z02.real)) / d,
            z21=(2 * self.s21 * sqrt(Z01.real * Z02.real)) / d,
            z22=(
                (1 - self.s11) * (Z02.conjugate + self.s22 * Z02)
                + self.s12 * self.s21 * Z02
            )
            / d,
        )

    def to_a(self, Z0=50 + 0j):
        """Convert this matrix to ABCD-Parameters.
        Parameters:
            - Z0: Normalised complex impedance. Can be specified as:
                + a real value. e.g. 50
                + a complex value, e.g. 50+0j
                + a 2-element array of real or complex values, representing the
                normalised impedances of each ports' termination (aka ZS and
                ZL respectively)
        """
        Z01 = Complex(50 + 0j)
        Z02 = Complex(50 + 0j)

        if isinstance(Z0, int) or isinstance(Z0, complex):
            Z01 = Complex(Z0)
            Z02 = Complex(Z0)
        elif isinstance(Z0, tuple) or isinstance(Z0, list):
            Z01 = Complex(Z0[0])
            Z02 = Complex(Z0[1])

        d = 2 * self.s21 * sqrt(Z01.real * Z02.real)
        return cn.Neta(
            # A
            a11=(
                (Z01.conjugate + self.s11 * Z02) * (1 - self.s22)
                + self.s12 * self.s21 * Z01
            )
            / d,
            # B
            a12=(
                (Z01.conjugate + self.s11 * Z01) * (Z02.conjugate + self.s22 * Z02)
                - self.s12 * self.s21 * Z01 * Z02
            )
            / d,
            # C
            a21=((1 - self.s11) * (1 - self.s22) - self.s12 * self.s21) / d,
            # D
            a22=(
                (1 - self.s11) * (Z02.conjugate + self.s22 * Z02)
                + self.s12 * self.s21 * Z02
            )
            / d,
        )

    def to_H(self, Z0=50 + 0j):
        """Convert this matrix to H-Parameters.
        Parameters:
            - Z0: Normalised complex impedance. Can be specified as:
                + a real value. e.g. 50
                + a complex value, e.g. 50+0j
                + a 2-element array of real or complex values, representing the
                normalised impedances of each ports' termination (aka ZS and
                ZL respectively)
        """
        Z01 = Complex(50 + 0j)
        Z02 = Complex(50 + 0j)

        if isinstance(Z0, int) or isinstance(Z0, complex):
            Z01 = Complex(Z0)
            Z02 = Complex(Z0)
        elif isinstance(Z0, tuple) or isinstance(Z0, list):
            Z01 = Complex(Z0[0])
            Z02 = Complex(Z0[1])

        d = (1 - self.s11) * (
            Z02.conjugate + self.s22 * Z02
        ) + self.s12 * self.s21 * Z02
        return cn.NetH(
            h11=(
                (Z01.conjugate + self.s11 * Z01) * (Z02.conjugate + self.s22 * Z02)
                - self.s12 * self.s21 * Z01 * Z02
            )
            / d,
            h12=(2 * self.s12 * sqrt(Z01.real * Z02.real)) / d,
            h21=(-2 * self.s21 * sqrt(Z01.real * Z02.real)) / d,
            h22=((1 - self.s11) * (1 - self.s22) - self.s12 * self.s21) / d,
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
    def max_available_gain_db(self):
        K = self.rollett_stability
        if K <= 1:
            return None

        Ds = self.determinant
        B1 = 1 + abs(self.s11) ** 2 - abs(self.s22) ** 2 - abs(Ds) ** 2

        if B1 < 0:
            k_calc = K + math.sqrt(K**2 - 1)
        else:
            k_calc = K - math.sqrt(K**2 - 1)

        mag_db = 10 * math.log10(abs(self.s21) / abs(self.s12)) + 10 * math.log10(
            abs(k_calc)
        )

        return mag_db

    @property
    def max_stable_gain_db(self):
        K = self.rollett_stability
        if K > 1:
            return None
        return 10 * math.log10(abs(self.s21) / abs(self.s12))

    @property
    def insertion_gain_db(self):
        return 20 * math.log10(abs(self.s21))

    def transducer_gain_db(self, ReflS=None, ReflL=None):
        Gt = (abs(self.s21) ** 2 * (1 - abs(ReflS) ** 2) * (1 - abs(ReflL) ** 2)) / (
            abs(
                (1 - self.s11 * ReflS) * (1 - self.s22 * ReflL)
                - self.s12 * self.s21 * ReflL * ReflS
            )
            ** 2
        )
        return 10 * math.log10(Gt)
