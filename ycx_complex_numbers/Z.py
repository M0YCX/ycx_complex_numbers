from ycx_complex_numbers.complex import Complex


class Z(Complex):
    """Z - Z (Impedance)."""

    symbol = "Z"
    c = 0 + 0j

    def __init__(self, c=None):
        super().__init__(c)
