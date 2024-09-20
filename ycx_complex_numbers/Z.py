from ycx_complex_numbers.complex import Complex, Net
import ycx_complex_numbers as cn


class Z(Complex):
    """Z - Z (Impedance)."""

    _symbol = "Z"

    def __init__(self, c=None):
        super().__init__(c)


class NetZ(Net):
    def __init__(self, z11=None, z12=None, z21=None, z22=None):
        super().__init__(c11=Z(z11), c12=Z(z12), c21=Z(z21), c22=Z(z22))

    @property
    def z11(self):
        return self._c11

    @property
    def z12(self):
        return self._c12

    @property
    def z21(self):
        return self._c21

    @property
    def z22(self):
        return self._c22

    def to_a(self):
        return cn.NetABCD(
            A=self.z11 / self.z21,
            B=self.determinant / self.z21,
            C=1 / self.z21,
            D=self.z22 / self.z21,
        )

    def to_ABCD(self):
        return self.to_a()

    def to_H(self):
        return cn.NetH(
            h11=self.determinant / self.z22,
            h12=self.z12 / self.z22,
            h21=-self.z21 / self.z22,
            h22=1 / self.z22,
        )

    def to_Y(self):
        return cn.NetY(
            y11=self.z22 / self.determinant,
            y12=-self.z12 / self.determinant,
            y21=-self.z21 / self.determinant,
            y22=self.z11 / self.determinant,
        )
