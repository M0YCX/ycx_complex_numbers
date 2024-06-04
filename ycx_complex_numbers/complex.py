import numpy as np
import math

# WARNING: file contains utf-8 unicode chars, e.g. ∠


class Complex:
    """Complex - Complex number class."""

    symbol = None
    c = 0 + 0j

    def __init__(self, c=None):
        self.c = c

    def from_polar(self, mag, angle):
        x = mag * np.cos(np.deg2rad(angle))
        y = mag * np.sin(np.deg2rad(angle))
        self.c = complex(x, y)
        return self

    def __str__(self):
        p = self.as_polar()
        return f"{self.symbol+':' if self.symbol else ''}{self.c:.5f} : [mag:{p['mag']:.5f} ∠{p['angle']:.5f}]"

    def __repr__(self):
        return str(self)

    def __abs__(self):
        return abs(self.c)

    def as_complex(self):
        return self.c

    def as_polar(self):
        mag = abs(self.c)
        angle = math.degrees(math.atan2(self.c.imag, self.c.real))
        return {"mag": mag, "angle": angle}

    def as_conjugate(self):
        return Complex((self.c.real - 1j * self.c.imag))

    @property
    def real(self):
        return self.c.real

    @property
    def imag(self):
        return self.c.imag

    def __add__(self, other):
        return Complex(self.c + other.c)

    def __sub__(self, other):
        return Complex(self.c - other.c)

    def __mul__(self, other):
        return Complex(self.c * other.c)

    def __truediv__(self, other):
        return Complex(self.c / other.c)

    def __eq__(self, other):
        return self.c == other.c
