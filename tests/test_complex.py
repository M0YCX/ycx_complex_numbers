from ycx_complex_numbers import *
import re
import pytest

CX_RE = r"\d+\.?\d+[\+\-]\d+\.?\d+j : \[mag:.*\]$"

@pytest.mark.parametrize(
    "test_input", [Complex(50 + 16j), S(50 + 16j), Y(50 + 16j), Z(50 + 16j), ReflCoef(50 + 16j)]
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
        assert str(e) in ["can't set attribute 'c'", "property 'c' of 'Complex' object has no setter"]


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
        (ReflCoef(50 + 16j), ReflCoef(10 + 5j)),
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
        (ReflCoef(50 + 16j), ReflCoef(10 + 5j)),
    ],
)
def test_add(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c3 = c1 + c2
    assert c3.real == 60.0
    assert c3.imag == 21.0

def test_int_radd():
    res = 1 + Complex(50 + 16j)
    print(res)
    assert res.real == 51.0
    assert res.imag == 16.0

def test_float_radd():
    res = 1.0 + Complex(50 + 16j)
    print(res)
    assert res.real == 51.0
    assert res.imag == 16.0

@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
        (ReflCoef(50 + 16j), ReflCoef(10 + 5j)),
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
        (ReflCoef(50 + 16j), ReflCoef(10 + 5j)),
    ],
)
def test_sub(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c3 = c1 - c2
    assert c3.real == 40.0
    assert c3.imag == 11.0

def test_int_rsub():
    res = 1 - Complex(50 + 16j)
    print(res)
    assert res.real == -49.0
    assert res.imag == -16.0

@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
        (ReflCoef(50 + 16j), ReflCoef(10 + 5j)),
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
        (ReflCoef(50 + 16j), ReflCoef(10 + 5j)),
    ],
)
def test_mul(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c3 = c1 * c2
    assert c3.real == 420.0
    assert c3.imag == 410.0

def test_int_rmul():
    res = 2 * Complex(50 + 16j)
    print(res)
    assert res.real == 100.0
    assert res.imag == 32.0

@pytest.mark.parametrize(
    "test_input1, test_input2",
    [
        (Complex(50 + 16j), Complex(10 + 5j)),
        (S(50 + 16j), S(10 + 5j)),
        (Y(50 + 16j), Y(10 + 5j)),
        (Z(50 + 16j), Z(10 + 5j)),
        (ReflCoef(50 + 16j), ReflCoef(10 + 5j)),
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
        (ReflCoef(50 + 16j), ReflCoef(10 + 5j)),
    ],
)
def test_div(test_input1, test_input2):
    c1 = test_input1
    c2 = test_input2
    c3 = c1 / c2
    assert c3.real == 4.64
    assert c3.imag == -0.72

def test_int_rdiv():
    res = 1 / Complex(50 + 16j)
    print(res)
    assert res.real == 0.018142235123367198
    assert res.imag == -0.005805515239477504

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
        (Complex(3 + 4j), rf"^{CX_RE}"),
        (S(3 + 4j), rf"^S:{CX_RE}"),
        (Y(3 + 4j), rf"^Y:{CX_RE}"),
        (Z(3 + 4j), rf"^Z:{CX_RE}"),
        (ReflCoef(3 + 4j), rf"^𝚪:{CX_RE}")
    ],
)
def test_str(test_input1, test_re1):
    c = test_input1
    print(type(c).__name__)
    assert re.match(test_re1, str(c))


@pytest.mark.parametrize(
    "test_input1, test_re1",
    [
        (Complex(3 + 4j), rf"^{CX_RE}"),
        (S(3 + 4j), rf"^S:{CX_RE}"),
        (Y(3 + 4j), rf"^Y:{CX_RE}"),
        (Z(3 + 4j), rf"^Z:{CX_RE}"),
        (ReflCoef(3 + 4j), rf"^𝚪:{CX_RE}")
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
        ReflCoef(3 + 4j)
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
        (ReflCoef(3 + 4j), ReflCoef(3 + 5j))
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
        ReflCoef(3 + 4j)
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
        ReflCoef(3 + 4j)
    ],
)
def test_as_complex(test_input1):
    c = test_input1
    cpx = c.as_complex()
    assert cpx.real == 3.0
    assert cpx.imag == 4.0

def test_Z_case_from_gamma():
    test_re1 = rf"^Z:{CX_RE}"
    print(test_re1)
    Z0 = Z(50+0j)
    GS = Complex(0.672-17j)

    ZS = Z0 * (1+GS)

    print(ZS)
    assert re.match(test_re1, str(ZS))

def test_from_class():
    cin = S(0.123+2.3j)
    cout = ReflCoef(cin)
    print(cout)
    assert isinstance(cout, ReflCoef)

def test_format():
    cin = S(0.123456+2.333333j)
    cin_f = f"{cin:.9f}"
    assert cin_f == "S:0.123456000+2.333333000j : [mag:2.336596729} ∠86.971320337]"

    cin_f_def = f"{cin}"
    print(cin_f_def)
    assert cin_f_def == "S:0.12346+2.33333j : [mag:2.33660} ∠86.97132]"
