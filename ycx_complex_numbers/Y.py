from ycx_complex_numbers.complex import Complex, Net
import ycx_complex_numbers as cn


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

    def to_ABCD(self):
        return cn.NetABCD(
            A=-self.y22 / self.y21,
            B=-1 / self.y21,
            C=-self.determinant / self.y21,
            D=-self.y11 / self.y21,
        )

    def to_H(self):
        return cn.NetH(
            h11=1 / self.y11,
            h12=-self.y12 / self.y11,
            h21=self.y21 / self.y11,
            h22=self.determinant / self.y11,
        )

    def to_Z(self):
        return cn.NetZ(
            z11=self.y22 / self.determinant,
            z12=-(self.y12 / self.determinant),
            z21=-self.y21 / self.determinant,
            z22=self.y11 / self.determinant,
        )

    def to_S(self, Z0=50+0j):
        yi = self.y11 * Z0
        yr = self.y12 * Z0
        yf = self.y21 * Z0
        yo = self.y22 * Z0
        return cn.NetS(
            s11=((1 - yi) * (1 + yo) + yr * yf)
            / ((1 + yi) * (1 + yo) - yr * yf),
            s12=(-2 * yr)
            / ((1 + yi) * (1 + yo) - yr * yf),
            s21=(-2 * yf) / ((1 + yi) * (1 + yo) - yr * yf),
            s22=((1 + yi) * (1 - yo) + yr * yf)
            / ((1 + yi) * (1 + yo) - yr * yf),
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
