from ycx_complex_numbers.complex import Complex


class Y(Complex):
    """Y - A Y (Admittance) parameter."""

    symbol = "Y"
    c = 0 + 0j

    def __init__(self, c=None):
        super().__init__(c)