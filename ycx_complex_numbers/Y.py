from ycx_complex_numbers.complex import Complex


class Y(Complex):
    """Y - A Y (Admittance) parameter."""

    _symbol = "Y"

    def __init__(self, c=None):
        super().__init__(c)
