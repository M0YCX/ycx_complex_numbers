from ycx_complex_numbers.complex import Complex, Net


class Z(Complex):
    """Z - Z (Impedance)."""

    _symbol = "Z"

    def __init__(self, c=None):
        super().__init__(c)

class NetZ(Net):
    def __init__(self, z11=None, z12=None, z21=None, z22=None):
        super().__init__(c11=z11, c12=z12, c21=z21, c22=z22)

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