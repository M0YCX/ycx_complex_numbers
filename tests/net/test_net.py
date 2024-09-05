from ycx_complex_numbers import *
import re
import pytest


def test_Net():
    n = Net(1 + 0j, 2 + 0j, 3, 4)
    assert n.c11 == (1 + 0j)
    assert n.c12 == (2 + 0j)
    assert n.c21 == (3 + 0j)
    assert n.c22 == (4 + 0j)

    assert n.determinant == (-2 + 0j)


def test_NetY():
    n = NetY(1 + 0j, 2 + 0j, 3, 4)
    assert n.y11 == (1 + 0j)
    assert n.y12 == (2 + 0j)
    assert n.y21 == (3 + 0j)
    assert n.y22 == (4 + 0j)

    assert n.determinant == (-2 + 0j)


def test_NetZ():
    n = NetZ(1 + 0j, 2 + 0j, 3, 4)
    assert n.z11 == (1 + 0j)
    assert n.z12 == (2 + 0j)
    assert n.z21 == (3 + 0j)
    assert n.z22 == (4 + 0j)

    assert n.determinant == (-2 + 0j)


def test_NetS():
    n = NetS(1 + 0j, 2 + 0j, 3, 4)
    assert n.s11 == (1 + 0j)
    assert n.s12 == (2 + 0j)
    assert n.s21 == (3 + 0j)
    assert n.s22 == (4 + 0j)

    assert n.determinant == (-2 + 0j)


def test_NetH():
    n = NetH(1 + 0j, 2 + 0j, 3, 4)
    assert n.h11 == (1 + 0j)
    assert n.h12 == (2 + 0j)
    assert n.h21 == (3 + 0j)
    assert n.h22 == (4 + 0j)

    assert n.determinant == (-2 + 0j)


def test_NetT():
    n = NetT(1 + 0j, 2 + 0j, 3, 4)
    assert n.A == (1 + 0j)
    assert n.B == (2 + 0j)
    assert n.C == (3 + 0j)
    assert n.D == (4 + 0j)

    assert n.determinant == (-2 + 0j)


def test_NetY_to_ZTHS():
    y11 = 13 * 10**-3 + 2j * 10**-3
    y12 = 0 + 0.001j * 10**-3
    y21 = -12 * 10**-3 + 0.1j * 10**-3
    y22 = 1.1 * 10**-3 + 0.15j * 10**-3

    n = NetY(y11=y11, y12=y12, y21=y21, y22=y22)
    z = n.to_Z()
    assert isinstance(z, NetZ)

    t = n.to_T()
    assert isinstance(t, NetT)

    h = n.to_H()
    assert isinstance(h, NetH)

    s = n.to_S()
    assert isinstance(s, NetS)


def test_NetY_in_out():
    y11 = 13 * 10**-3 + 2j * 10**-3
    y12 = 0 + 0.001j * 10**-3
    y21 = -12 * 10**-3 + 0.1j * 10**-3
    y22 = 1.1 * 10**-3 + 0.15j * 10**-3

    n = NetY(y11=y11, y12=y12, y21=y21, y22=y22)
    YS = 1 / (50 + 0j)
    YL = 1 / (1800 + 0j)

    yin_out = n.in_out(ys=YS, yl=YL)

    assert "Yin" in yin_out
    assert "Yout" in yin_out

    assert str(yin_out["Yin"]) == "Y:0.01300+0.00201j : [mag:0.01315 ∠8.77662]"
    assert str(yin_out["Yout"]) == "Y:0.00110+0.00015j : [mag:0.00111 ∠7.78351]"


def test_Net_addition_subtraction():
    for c in (Net, NetZ, NetY, NetH, NetT):
        n = c(1 + 0j, 2 + 0j, 3, 4)
        nres = n + n
        assert nres == c(2 + 0j, 4 + 0j, 6 + 0j, 8 + 0j)

        nres2 = nres - n
        assert nres2 == n
