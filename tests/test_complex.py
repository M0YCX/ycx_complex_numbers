from ycx_complex_numbers import *
import re
import pytest




def test_new_complex():
    c = Complex(50+16j)
    assert c.real == 50.0
    assert c.imag == 16.0

def test_iadd():
    c1 = Complex(50+16j)
    c2 = Complex(10+5j)
    c1 += c2
    assert c1.real == 60.0
    assert c1.imag == 21.0

def test_add():
    c1 = Complex(50+16j)
    c2 = Complex(10+5j)
    c3 = c1 + c2
    assert c3.real == 60.0
    assert c3.imag == 21.0

def test_isub():
    c1 = Complex(50+16j)
    c2 = Complex(10+5j)
    c1 -= c2
    assert c1.real == 40.0
    assert c1.imag == 11.0

def test_sub():
    c1 = Complex(50+16j)
    c2 = Complex(10+5j)
    c3 = c1 - c2
    assert c3.real == 40.0
    assert c3.imag == 11.0

def test_imul():
    c1 = Complex(50+16j)
    c2 = Complex(10+5j)
    c1 *= c2
    assert c1.real == 420.0
    assert c1.imag == 410.0

def test_mul():
    c1 = Complex(50+16j)
    c2 = Complex(10+5j)
    c3 = c1 * c2
    assert c3.real == 420.0
    assert c3.imag == 410.0

def test_idiv():
    c1 = Complex(50+16j)
    c2 = Complex(10+5j)
    c1 /= c2
    assert c1.real == 4.64
    assert c1.imag == -0.72

def test_div():
    c1 = Complex(50+16j)
    c2 = Complex(10+5j)
    c3 = c1 / c2
    assert c3.real == 4.64
    assert c3.imag == -0.72

def test_abs():
    c = Complex(3+4j)
    assert abs(c) == 5.0

def test_str():
    c = Complex(3+4j)
    assert re.match(r'^\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$', str(c))

def test_repr():
    c = Complex(3+4j)
    assert re.match(r'^\d+\.?\d+\+\d+\.?\d+j : \[mag:.*\]$', str(c))

def test_eq():
    c1 = Complex(3+4j)
    c2 = Complex(3+4j)
    assert c1 == c2

def test_ne():
    c1 = Complex(3+4j)
    c2 = Complex(3+5j)
    assert c1 != c2

# Test as polar
def test_as_polar():
    c = Complex(3+4j)
    p = c.as_polar()
    assert p["mag"] == 5.0
    assert p["angle"] == 53.13010235415598

def test_as_complex():
    c = Complex(3+4j)
    cpx = c.as_complex()
    assert cpx.real == 3.0
    assert cpx.imag == 4.0
