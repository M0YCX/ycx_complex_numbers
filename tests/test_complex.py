from ycx_complex_numbers import *
import re
import pytest


@pytest.mark.parametrize(
    "test_input", [Complex(50 + 16j), S(50 + 16j), Y(50 + 16j), Z(50 + 16j)]
)
def test_new_complex(test_input):
    c = test_input
    assert c == test_input
    assert c.real == 50.0
    assert c.imag == 16.0

def test_c_protected():
    c = Complex(50 + 16j)
    try:
        c.c = 0+1j
    except AttributeError as e:
        print(str(e))
        assert str(e) == "can't set attribute 'c'"


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
    ],
)
def test_iadd(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c1 += c2
    assert c1.real == 60.0
    assert c1.imag == 21.0


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
    ],
)
def test_add(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c3 = c1 + c2
    assert c3.real == 60.0
    assert c3.imag == 21.0


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
    ],
)
def test_isub(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c1 -= c2
    assert c1.real == 40.0
    assert c1.imag == 11.0


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
    ],
)
def test_sub(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c3 = c1 - c2
    assert c3.real == 40.0
    assert c3.imag == 11.0


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
    ],
)
def test_imul(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c1 *= c2
    assert c1.real == 420.0
    assert c1.imag == 410.0


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
    ],
)
def test_mul(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c3 = c1 * c2
    assert c3.real == 420.0
    assert c3.imag == 410.0


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
    ],
)
def test_idiv(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c1 /= c2
    assert c1.real == 4.64
    assert c1.imag == -0.72


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
    ],
)
def test_div(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c3 = c1 / c2
    assert c3.real == 4.64
    assert c3.imag == -0.72


@pytest.mark.parametrize(
    "test_input1",
    [
        Complex(3 + 4j),
        S(3 + 4j),
        Y(3 + 4j),
        Z(3 + 4j),
    ],
)
def test_abs(test_input1):
    c = test_input1
    assert abs(c) == 5.0


@pytest.mark.parametrize(
    "test_input1, test_re1",
    [
        (Complex(3 + 4j), r"^\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$"),
        (S(3 + 4j), r"^S:\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$"),
        (Y(3 + 4j), r"^Y:\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$"),
        (Z(3 + 4j), r"^Z:\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$"),
    ],
)
def test_str(test_input1, test_re1):
    c = test_input1
    print(type(c).__name__)
    assert re.match(test_re1, str(c))


@pytest.mark.parametrize(
    "test_input1, test_re1",
    [
        (Complex(3 + 4j), r"^\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$"),
        (S(3 + 4j), r"^S:\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$"),
        (Y(3 + 4j), r"^Y:\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$"),
        (Z(3 + 4j), r"^Z:\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$"),
    ],
)
def test_repr(test_input1, test_re1):
    c = test_input1
    assert re.match(test_re1, str(c))


@pytest.mark.parametrize(
    "test_input1",
    [
        Complex(3 + 4j),
        S(3 + 4j),
        Y(3 + 4j),
        Z(3 + 4j),
    ],
)
def test_eq(test_input1):
    c1 = test_input1
    c2 = test_input1
    assert c1 == c2


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(3 + 4j), Complex(3 + 5j)),
        (S(3 + 4j), S(3 + 5j)),
        (Y(3 + 4j), Y(3 + 5j)),
        (Z(3 + 4j), Z(3 + 5j)),
    ],
)
def test_ne(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    assert c1 != c2


@pytest.mark.parametrize(
    "test_input1",
    [
        Complex(3 + 4j),
        S(3 + 4j),
        Y(3 + 4j),
        Z(3 + 4j),
    ],
)
def test_as_polar(test_input1):
    c = test_input1
    p = c.as_polar()
    assert p["mag"] == 5.0
    assert p["angle"] == 53.13010235415598


@pytest.mark.parametrize(
    "test_input1",
    [
        Complex(3 + 4j),
        S(3 + 4j),
        Y(3 + 4j),
        Z(3 + 4j),
    ],
)
def test_as_complex(test_input1):
    c = test_input1
    cpx = c.as_complex()
    assert cpx.real == 3.0
    assert cpx.imag == 4.0
