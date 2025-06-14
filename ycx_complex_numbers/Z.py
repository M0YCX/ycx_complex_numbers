from ycx_complex_numbers.complex import Complex, Net
import ycx_complex_numbers as cn


class Z(Complex):
    """Z - Represents complex Z (Impedance) (R+/-Xj)."""

    _symbol = "Z"

    def __init__(self, c=None):
        super().__init__(c)

    @property
    def R(self):
        return self._c.real

    @property
    def X(self):
        return self._c.imag


class NetZ(Net):
    """Z - Impedance 2-port-node parameters."""

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

    @property
    def is_passive(self):
        return self.z12 == self.z21

    @property
    def is_symmetrical(self):
        return self.z11 == self.z22

    def to_a(self):
        """Convert to ABCD parameters"""
        return cn.Neta(
            a11=self.z11 / self.z21,
            a12=self.determinant / self.z21,
            a21=1 / self.z21,
            a22=self.z22 / self.z21,
        )

    def to_b(self):
        """Convert to ABCD' parameters"""
        return cn.Netb(
            b11=self.z22 / self.z12,
            b12=self.determinant / self.z12,
            b21=1 / self.z12,
            b22=self.z11 / self.z12,
        )

    def to_ABCD(self):
        return self.to_a()

    def to_H(self):
        """Convert to H parameters"""
        return cn.NetH(
            h11=self.determinant / self.z22,
            h12=self.z12 / self.z22,
            h21=-self.z21 / self.z22,
            h22=1 / self.z22,
        )

    def to_Y(self):
        """Convert to Y parameters"""
        return cn.NetY(
            y11=self.z22 / self.determinant,
            y12=-self.z12 / self.determinant,
            y21=-self.z21 / self.determinant,
            y22=self.z11 / self.determinant,
        )

    def to_S(self, Z0=50 + 0j):
        """Convert to S parameters"""
        zi = self.z11 / Z0
        zr = self.z12 / Z0
        zf = self.z21 / Z0
        zo = self.z22 / Z0
        return cn.NetS(
            s11=((zi - 1) * (zo + 1) - zr * zf) / ((zi + 1) * (zo + 1) - zr * zf),
            s12=(2 * zr) / ((zi + 1) * (zo + 1) - zr * zf),
            s21=(2 * zf) / ((zi + 1) * (zo + 1) - zr * zf),
            s22=((zi + 1) * (zo - 1) - zr * zf) / ((zi + 1) * (zo + 1) - zr * zf),
        )

    def zin(self, ZL=50 + 0j):
        return self.z11 - (self.z12 * self.z21) / (self.z22 + ZL)

    def zout(self, ZS=50 + 0j):
        return self.z22 - (self.z12 * self.z21) / (self.z11 + ZS)

    def vswr_in(self, Z0=50 + 0j):
        gamma = (self.zin() - Z0) / (self.zin() + Z0)
        return (1 + abs(gamma)) / (1 - abs(gamma))

    def vswr_out(self, Z0=50 + 0j):
        gamma = (self.zout() - Z0) / (self.zout() + Z0)
        return (1 + abs(gamma)) / (1 - abs(gamma))
