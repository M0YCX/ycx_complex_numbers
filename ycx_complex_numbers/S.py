from ycx_complex_numbers.complex import Complex

class S(Complex):
    """S - An S (Scatter) parameter."""

    symbol = "S"
    c = 0 + 0j

    def __init__(self, c=None):
        super().__init__(c)