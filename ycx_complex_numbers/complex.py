import numpy as np
import math

# WARNING: file contains utf-8 unicode chars, e.g. ∠


class Complex(object):
    """Complex - Complex number class."""

    _symbol = None

    def __init__(self, c=None):
        if c is None:
            self._c = c
        elif isinstance(c, Complex):
            self._c = c._c
        elif isinstance(c, complex):
            self._c = c
        else:
            self._c = c + 0j

    def from_polar(self, mag, angle):
        x = mag * np.cos(np.deg2rad(angle))
        y = mag * np.sin(np.deg2rad(angle))
        self._c = complex(x, y)
        return self

    def _to_str(self, fmt=""):
        if fmt == "":
            fmt = ".5f"
        p = self.as_polar()
        return (
            f"{self._symbol+':' if self._symbol else ''}"
            + format(self._c, fmt)
            + " : [mag:"
            + format(p["mag"], fmt)
            + " ∠"
            + format(p["angle"], fmt)
            + "]"
        )

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
    def symbol(self):
        return self._symbol if self._symbol is not None else ""

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

    def __neg__(self):
        return self.__class__(-self._c)

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
        if isinstance(other, Complex):
            return self._c == other._c
        else:
            return self._c == other


class Net(object):
    """2-port network of complex numbers"""

    def __init__(self, c11=None, c12=None, c21=None, c22=None):
        self._c11 = c11 if isinstance(c11, Complex) else Complex(c11)
        self._c12 = c12 if isinstance(c12, Complex) else Complex(c12)
        self._c21 = c21 if isinstance(c21, Complex) else Complex(c21)
        self._c22 = c22 if isinstance(c22, Complex) else Complex(c22)

    def _to_str(self, fmt=""):
        return (
            f"[\n  {self._c11.symbol.lower()}11:"
            + format(self._c11, fmt)
            + f",\n  {self._c12.symbol.lower()}12:"
            + format(self._c12, fmt)
            + f",\n  {self._c21.symbol.lower()}21:"
            + format(self._c21, fmt)
            + f",\n  {self._c22.symbol.lower()}22:"
            + format(self._c22, fmt)
            + "\n]"
        )

    def __str__(self):
        return self._to_str()

    def __repr__(self):
        return str(self)

    def __format__(self, fmt):
        return self._to_str(fmt=fmt)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return (
            self.c11 == other.c11
            and self.c12 == other.c12
            and self.c21 == other.c21
            and self.c22 == other.c22
        )

    @property
    def c11(self):
        return self._c11

    @property
    def c12(self):
        return self._c12

    @property
    def c21(self):
        return self._c21

    @property
    def c22(self):
        return self._c22

    @property
    def m(self):
        "as numpy array matrix"
        return np.array([[self.c11, self.c12], [self.c21, self.c22]])

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        res = self.m + other.m
        return self.__class__(
            res[0][0],
            res[0][1],
            res[1][0],
            res[1][1],
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        res = self.m - other.m
        return self.__class__(
            res[0][0],
            res[0][1],
            res[1][0],
            res[1][1],
        )

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        # res = self.m * other.m
        res = np.matmul(self.m, other.m)
        return self.__class__(
            res[0][0],
            res[0][1],
            res[1][0],
            res[1][1],
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        res = self.m / other.m
        return self.__class__(
            res[0][0],
            res[0][1],
            res[1][0],
            res[1][1],
        )

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    @property
    def determinant(self):
        return self._c11 * self._c22 - self._c12 * self._c21
