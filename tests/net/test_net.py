from ycx_complex_numbers import Net, NetY, NetZ, NetH, Neta, Netb, NetS

# import re
import pytest


class TestNet:
    @pytest.fixture
    def n1(self):
        return Net(1 + 0j, 2 + 0j, 3, 4)

    @pytest.fixture
    def n2(self):
        return Net(1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j)

    @pytest.fixture
    def n3(self):
        return Net(10 + 0j, 20 + 0j, 30, 40)

    def test_instance(self, n1):
        assert n1.c11 == (1 + 0j)
        assert n1.c12 == (2 + 0j)
        assert n1.c21 == (3 + 0j)
        assert n1.c22 == (4 + 0j)

    def test_str(self, n1):
        assert (
            str(n1)
            == "[\n  11:1.00000+0.00000j : [mag:1.00000 ∠0.00000],\n  12:2.00000+0.00000j : [mag:2.00000 ∠0.00000],\n  21:3.00000+0.00000j : [mag:3.00000 ∠0.00000],\n  22:4.00000+0.00000j : [mag:4.00000 ∠0.00000]\n]"
        )
        assert (
            f"{n1}"
            == "[\n  11:1.00000+0.00000j : [mag:1.00000 ∠0.00000],\n  12:2.00000+0.00000j : [mag:2.00000 ∠0.00000],\n  21:3.00000+0.00000j : [mag:3.00000 ∠0.00000],\n  22:4.00000+0.00000j : [mag:4.00000 ∠0.00000]\n]"
        )

    def test_str_formats(self, n1):
        assert (
            f"{n1:~S}"
            == "[\n  11:1.00000+0.00000j :\n[mag:1.00000 ∠0.00000],\n  12:2.00000+0.00000j :\n[mag:2.00000 ∠0.00000],\n  21:3.00000+0.00000j :\n[mag:3.00000 ∠0.00000],\n  22:4.00000+0.00000j :\n[mag:4.00000 ∠0.00000]\n]"
        )
        assert (
            f"{n1:.9f}"
            == "[\n  11:1.000000000+0.000000000j : [mag:1.000000000 ∠0.000000000],\n  12:2.000000000+0.000000000j : [mag:2.000000000 ∠0.000000000],\n  21:3.000000000+0.000000000j : [mag:3.000000000 ∠0.000000000],\n  22:4.000000000+0.000000000j : [mag:4.000000000 ∠0.000000000]\n]"
        )

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)

    def test_equals(self, n1, n2):
        assert n1 == n1
        assert n1 != n2

    def test_add(self, n1, n2):
        n1sum = n1 + n1
        assert n1sum.c11 == 2 + 0j
        assert n1sum.c12 == 4 + 0j
        assert n1sum.c21 == 6 + 0j
        assert n1sum.c22 == 8 + 0j

        n2sum = n1 + n2
        assert n2sum.c11 == 2 + 1j
        assert n2sum.c12 == 4 + 2j
        assert n2sum.c21 == 6 + 3j
        assert n2sum.c22 == 8 + 4j

        rn2sum = n2 + n1
        assert rn2sum.c11 == 2 + 1j
        assert rn2sum.c12 == 4 + 2j
        assert rn2sum.c21 == 6 + 3j
        assert rn2sum.c22 == 8 + 4j

    def test_sub(self, n1, n2, n3):
        n3subn1 = n3 - n1
        assert n3subn1.c11 == 9
        assert n3subn1.c12 == 18 + 0j
        assert n3subn1.c21 == 27
        assert n3subn1.c22 == 36 - 0j

    def test_matmul(self, n1, n2):
        n1matmuln2 = n1 @ n2
        assert n1matmuln2.c11 == 7 + 7j
        assert n1matmuln2.c12 == 10 + 10j
        assert n1matmuln2.c21 == 15 + 15j
        assert n1matmuln2.c22 == 22 + 22j

    def test_mul(self, n1):
        res = n1 * 2
        assert res.c11 == 2
        assert res.c12 == 4
        assert res.c21 == 6
        assert res.c22 == 8

        rres = 2 * n1
        assert rres.c11 == 2
        assert rres.c12 == 4
        assert rres.c21 == 6
        assert rres.c22 == 8


class TestNetY:
    @pytest.fixture
    def n1(self):
        return NetY(1 + 0j, 2 + 0j, 3, 4)

    @pytest.fixture
    def n2(self):
        y11 = 13 * 10**-3 + 2j * 10**-3
        y12 = 0 + 0.001j * 10**-3
        y21 = -12 * 10**-3 + 0.1j * 10**-3
        y22 = 1.1 * 10**-3 + 0.15j * 10**-3
        return NetY(y11=y11, y12=y12, y21=y21, y22=y22)

    def test_instance(self, n1):
        assert n1.y11 == (1 + 0j)
        assert n1.y12 == (2 + 0j)
        assert n1.y21 == (3 + 0j)
        assert n1.y22 == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)

    def test_NetY_to_ZAHS(self, n2):
        z = n2.to_Z()
        assert isinstance(z, NetZ)
        aa1 = z.to_a()
        assert isinstance(aa1, Neta)
        # aa2 = z.to_ABCD()
        # assert isinstance(aa2, Neta)
        hh = z.to_H()
        assert isinstance(hh, NetH)
        yy = z.to_Y()
        assert isinstance(yy, NetY)

        a = n2.to_a()
        assert isinstance(a, Neta)
        # a2 = n.to_ABCD()
        # assert isinstance(a2, Neta)
        hh = a.to_H()
        assert isinstance(hh, NetH)
        yy = a.to_Y()
        assert isinstance(yy, NetY)
        zz = a.to_Z()
        assert isinstance(zz, NetZ)

        h = n2.to_H()
        assert isinstance(h, NetH)
        aa1 = h.to_a()
        assert isinstance(aa1, Neta)
        # aa2 = h.to_ABCD()
        # assert isinstance(aa2, Neta)
        yy = h.to_Y()
        assert isinstance(yy, NetY)
        zz = h.to_Z()
        assert isinstance(zz, NetZ)

        s = n2.to_S()
        assert isinstance(s, NetS)

    def test_NetY_in_out(self, n2):
        YS = 1 / (50 + 0j)
        YL = 1 / (1800 + 0j)

        yin_out = n2.in_out(ys=YS, yl=YL)

        assert "Yin" in yin_out
        assert "Yout" in yin_out

        assert str(yin_out["Yin"]) == "Y:0.01300+0.00201j : [mag:0.01315 ∠8.77662]"
        assert str(yin_out["Yout"]) == "Y:0.00110+0.00015j : [mag:0.00111 ∠7.78351]"

    def test_NetY_exchanges(self, n2):
        # assume start as ce
        nce = n2
        nce_cb = nce.exchange_to_cb(from_config="ce")
        nce_cc = nce.exchange_to_cc(from_config="ce")

        nce_cb_ce = nce_cb.exchange_to_ce(from_config="cb")
        assert nce_cb_ce.equals(nce, precision=9)

        nce_cb_cc = nce_cb.exchange_to_cc(from_config="cb")
        assert nce_cb_cc.equals(nce_cc, precision=9)

        nce_cc_ce = nce_cb_cc.exchange_to_ce(from_config="cc")
        assert nce.equals(nce_cc_ce, precision=9)

        nce_cc_cb = nce_cb_cc.exchange_to_cb(from_config="cc")
        assert nce_cb.equals(nce_cc_cb, precision=9)


class TestNetZ:
    @pytest.fixture
    def n1(self):
        return NetZ(1 + 0j, 2 + 0j, 3, 4)

    def test_instance(self, n1):
        assert n1.z11 == (1 + 0j)
        assert n1.z12 == (2 + 0j)
        assert n1.z21 == (3 + 0j)
        assert n1.z22 == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)


class TestNetS:
    @pytest.fixture
    def n1(self):
        return NetS(1 + 0j, 2 + 0j, 3, 4)

    def test_instance(self, n1):
        assert n1.s11 == (1 + 0j)
        assert n1.s12 == (2 + 0j)
        assert n1.s21 == (3 + 0j)
        assert n1.s22 == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)


class TestNetH:
    @pytest.fixture
    def n1(self):
        return NetH(1 + 0j, 2 + 0j, 3, 4)

    def test_instance(self, n1):
        assert n1.h11 == (1 + 0j)
        assert n1.h12 == (2 + 0j)
        assert n1.h21 == (3 + 0j)
        assert n1.h22 == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)


class TestNeta:
    @pytest.fixture
    def n1(self):
        return Neta(1 + 0j, 2 + 0j, 3, 4)

    def test_instance(self, n1):
        assert n1.A == (1 + 0j)
        assert n1.B == (2 + 0j)
        assert n1.C == (3 + 0j)
        assert n1.D == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)


class TestNetb:
    @pytest.fixture
    def n1(self):
        return Netb(1 + 0j, 2 + 0j, 3, 4)

    def test_instance(self, n1):
        assert n1.A == (1 + 0j)
        assert n1.B == (2 + 0j)
        assert n1.C == (3 + 0j)
        assert n1.D == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)


def test_Net_addition_subtraction():
    for c in (Net, NetZ, NetY, NetH, Neta):
        n = c(1 + 0j, 2 + 0j, 3, 4)
        nres = n + n
        assert nres == c(2 + 0j, 4 + 0j, 6 + 0j, 8 + 0j)

        nres2 = nres - n
        assert nres2 == n


def test_Net_matrix_product():
    c1 = Net(1, 2, 3, 4)
    c2 = Net(2, 3, 4, 5)
    res = c1 @ c2
    assert res == Net(10, 13, 22, 29)


def test_Net_a_b():
    a1 = Neta(1 + 0j, 2 + 0j, 3, 4)
    assert isinstance(a1, Neta)

    b1 = a1.to_b()
    assert isinstance(b1, Netb)

    assert a1 != b1

    a2 = b1.to_a()
    assert isinstance(a2, Neta)
    assert a2 == a1

    b2 = a2.to_b()
    assert isinstance(b2, Netb)
    assert b2 == b1
