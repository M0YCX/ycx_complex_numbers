import numpy as np
import math

# WARNING: file contains utf-8 unicode chars, e.g. ∠

class Complex(object):
    """Complex - Complex number class."""

    _symbol = None

    def __init__(self, c=None):
        if isinstance(c, Complex):
            self._c = c._c
        else:
            self._c = c

    def from_polar(self, mag, angle):
        x = mag * np.cos(np.deg2rad(angle))
        y = mag * np.sin(np.deg2rad(angle))
        self._c = complex(x, y)
        return self

    def _to_str(self, fmt=""):
        if fmt == "":
            fmt = ".5f"
        p = self.as_polar()
        return f"{self._symbol+':' if self._symbol else ''}" + format(self._c, fmt) + " : [mag:" + format(p['mag'], fmt) + "} ∠" + format(p['angle'], fmt) + "]"

    def __str__(self):
        return self._to_str()

    def __repr__(self):
        return str(self)

    def __format__(self, fmt):
        return self._to_str(fmt=fmt)

    def __abs__(self):
        return abs(self._c)

    def as_complex(self):
        return self._c

    def as_polar(self):
        mag = abs(self._c)
        angle = math.degrees(math.atan2(self._c.imag, self._c.real))
        return {"mag": mag, "angle": angle}

    def as_conjugate(self):
        return self.__class__((self._c.real - 1j * self._c.imag))

    @property
    def c(self):
        return self._c

    @property
    def real(self):
        return self._c.real

    @property
    def imag(self):
        return self._c.imag

    @property
    def conjugate(self):
        return self.__class__(np.conjugate(self._c))

    def __add__(self, other):
        if isinstance(other, Complex):
            return self.__class__(self._c + other._c)
        else:
            return self.__class__(self._c + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return self.__class__(self._c - other._c)
        else:
            return self.__class__(self._c - other)

    def __rsub__(self, other):
        if isinstance(other, Complex):
            return self.__class__(other._c - self._c)
        else:
            return self.__class__(other - self._c)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return self.__class__(self._c * other._c)
        else:
            return self.__class__(self._c * other)

    def __rmul__(self, other):
        return self.__class__(other * self._c)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return self.__class__(self._c / other._c)
        else:
            return self.__class__(self._c / other)

    def __rtruediv__(self, other):
        if isinstance(other, Complex):
            return self.__class__(other / self._c)
        else:
            return self.__class__(other / self._c)

    def __eq__(self, other):
        return self._c == other._c
