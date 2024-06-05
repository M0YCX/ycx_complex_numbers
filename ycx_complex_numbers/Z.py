from ycx_complex_numbers.complex import Complex


class Z(Complex):
    """Z - Z (Impedance)."""

    _symbol = "Z"

    def __init__(self, c=None):
        super().__init__(c)
