from ycx_complex_numbers import S, Y, Net, NetY, NetZ, NetH, Neta, Netb, NetS, ReflCoef

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

    def test_equals_with_precision(self):
        y1 = NetY(
            y11=0.00549 + 0.01167j,
            y12=-0.00004 - 0.00030j,
            y21=0.35800 - 0.05655j,
            y22=0.00018 + 0.00144j,
        )
        print(f"y1={y1}")
        y2 = NetY(
            y11=0.00151 + 0.00359j,
            y12=-0.00001 - 0.00031j,
            y21=0.10256 - 0.01436j,
            y22=0.00005 + 0.00064j,
        )
        print(f"y2={y2}")
        assert not y1.equals(y2)
        assert not y1.equals(y2, precision=4)
        assert not y1.equals(y2, precision=5)
        assert y1.equals(y2, precision=0)

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

    @pytest.fixture
    def n3(self):
        return NetY(
            y11=Y(14 + 1j),
            y12=Y(0.2 - 0.2j),
            y21=Y(-14 + 0.8j),
            y22=Y(0.2 + 2j),
        )

    def test_instance(self, n1):
        assert n1.y11 == (1 + 0j)
        assert n1.y12 == (2 + 0j)
        assert n1.y21 == (3 + 0j)
        assert n1.y22 == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)

    def test_linvill_stability(self, n3):
        C = round(n3.linvill_stability, 2)
        assert C == 0.48

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


class TestNetConversions:
    @pytest.fixture
    def n2(self):
        y11 = 13 * 10**-3 + 2j * 10**-3
        y12 = 0 + 0.001j * 10**-3
        y21 = -12 * 10**-3 + 0.1j * 10**-3
        y22 = 1.1 * 10**-3 + 0.15j * 10**-3
        return NetY(y11=y11, y12=y12, y21=y21, y22=y22)

    def test_NetY_to_ZAHS(self, n2):
        y = n2
        z1 = y.to_Z()
        assert isinstance(z1, NetZ)
        assert z1.to_Y().equals(y, precision=16)
        a1 = y.to_a()
        assert isinstance(a1, Neta)
        assert a1.to_Y().equals(y, precision=16)
        b1 = y.to_b()
        assert isinstance(b1, Netb)
        assert b1.to_Y().equals(y, precision=13)
        h1 = y.to_H()
        assert isinstance(h1, NetH)
        assert h1.to_Y().equals(y, precision=16)
        s1 = y.to_S()
        assert isinstance(s1, NetS)
        assert s1.to_Y().equals(y, precision=6)

        z = z1
        aa1 = z.to_a()
        assert isinstance(aa1, Neta)
        assert aa1.to_Z().equals(z, precision=6)
        ab1 = z.to_b()
        assert isinstance(ab1, Netb)
        assert ab1.to_Z().equals(z, precision=10)
        hh = z.to_H()
        assert isinstance(hh, NetH)
        assert hh.to_Z().equals(z, precision=12)
        yy = z.to_Y()
        assert isinstance(yy, NetY)
        assert yy.to_Z().equals(z, precision=10)
        ss = z.to_S()
        assert isinstance(ss, NetS)
        assert ss.to_Z().equals(z, precision=10)

        a = a1
        ab1 = a.to_b()
        assert isinstance(ab1, Netb)
        assert ab1.to_a().equals(a, precision=10)
        hh = a.to_H()
        assert isinstance(hh, NetH)
        assert hh.to_a().equals(a, precision=12)
        yy = a.to_Y()
        assert isinstance(yy, NetY)
        assert yy.to_a().equals(a, precision=14)
        zz = a.to_Z()
        assert isinstance(zz, NetZ)
        assert zz.to_a().equals(a, precision=12)
        ss = a.to_S()
        assert isinstance(ss, NetS)
        assert ss.to_a().equals(a, precision=12)

        b = b1
        aa1 = b.to_a()
        assert isinstance(aa1, Neta)
        assert aa1.to_b().equals(b, precision=6)
        hh = b.to_H()
        assert isinstance(hh, NetH)
        assert hh.to_b().equals(b, precision=9)
        yy = b.to_Y()
        assert isinstance(yy, NetY)
        assert yy.to_b().equals(b, precision=10)
        zz = b.to_Z()
        assert isinstance(zz, NetZ)
        assert zz.to_b().equals(b, precision=8)
        # TODO:
        # ss = b.to_S()
        # assert isinstance(ss, NetS)
        # assert ss.to_b().equals(b, precision=13)

        h = h1
        aa1 = h.to_a()
        assert isinstance(aa1, Neta)
        assert aa1.to_H().equals(h, precision=12)
        ab1 = h.to_b()
        assert isinstance(ab1, Netb)
        assert ab1.to_H().equals(h, precision=10)
        yy = h.to_Y()
        assert isinstance(yy, NetY)
        assert yy.to_H().equals(h, precision=12)
        zz = h.to_Z()
        assert isinstance(zz, NetZ)
        assert zz.to_H().equals(h, precision=12)
        ss = h.to_S()
        assert isinstance(ss, NetS)
        assert ss.to_H().equals(h, precision=12)

        s = s1
        aa1 = s.to_a()
        assert isinstance(aa1, Neta)
        assert aa1.to_S().equals(s, precision=12)
        # TODO:
        # ab1 = s.to_b()
        # assert isinstance(ab1, Netb)
        # assert ab1.to_S().equals(s, precision=10)
        yy = s.to_Y()
        assert isinstance(yy, NetY)
        assert yy.to_S().equals(s, precision=4)
        zz = s.to_Z()
        assert isinstance(zz, NetZ)
        assert zz.to_S().equals(s, precision=12)
        hh = s.to_H()
        assert isinstance(hh, NetH)
        assert hh.to_S().equals(s, precision=9)


class TestNetZ:
    @pytest.fixture
    def n1(self):
        return NetZ(1 + 0j, 2 + 0j, 3, 4)

    @pytest.fixture
    def n2(self):
        return NetZ(50 + 0j, 50 + 0j, 50, 50)

    def test_instance(self, n1):
        assert n1.z11 == (1 + 0j)
        assert n1.z12 == (2 + 0j)
        assert n1.z21 == (3 + 0j)
        assert n1.z22 == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)

    def test_zin(self, n2):
        zin = n2.zin()
        print(f"zin={zin}")
        assert abs(zin) == 25

    def test_zout(self, n2):
        zout = n2.zout()
        print(f"zout={zout}")
        assert abs(zout) == 25

    def test_vswr_in(self, n2):
        vswr_in = round(n2.vswr_in(),2)
        print(f"vswr_in={vswr_in}")
        assert vswr_in == 2.0

    def test_vswr_out(self, n2):
        vswr_out = round(n2.vswr_out(), 2)
        print(f"vswr_out={vswr_out}")
        assert vswr_out == 2.0


class TestNetS:
    @pytest.fixture
    def n1(self):
        return NetS(1 + 0j, 2 + 0j, 3, 4)

    @pytest.fixture
    def n2(self):
        """from RF Circuit Design, Bowick page 143"""
        return NetS(
            s11=S().from_polar(0.4, 162),
            s12=S().from_polar(0.04, 60),
            s21=S().from_polar(5.2, 63),
            s22=S().from_polar(0.35, -39),
        )

    def test_instance(self, n1):
        assert n1.s11 == (1 + 0j)
        assert n1.s12 == (2 + 0j)
        assert n1.s21 == (3 + 0j)
        assert n1.s22 == (4 + 0j)

    def test_determinant(self, n1):
        assert n1.determinant == (-2 + 0j)

    def test_reflcoefin(self, n1):
        rin = n1.reflcoefin()
        assert isinstance(rin, ReflCoef)
        assert rin == 1 + 0j

    def test_reflcoefout(self, n1):
        rout = n1.reflcoefout()
        assert isinstance(rout, ReflCoef)
        assert rout == 4 + 0j

    def test_rollett_stability(self, n2):
        k = round(n2.rollett_stability, 2)
        assert k == 1.74

    def test_max_available_gain_db(self, n2):
        max_available_gain_db = round(n2.max_available_gain_db, 1)
        assert max_available_gain_db == 16.1

    def test_max_stable_gain_db(self, n1):
        max_stable_gain_db = round(n1.max_stable_gain_db, 1)
        print(f"max_stable_gain_db={max_stable_gain_db}")
        assert max_stable_gain_db == 1.8
        # TODO: test valid MSG

    def test_insertion_gain_db(self, n2):
        ins_gain_db = round(n2.insertion_gain_db, 1)
        assert ins_gain_db == 14.3

    def test_transducer_gain_db(self, n2):
        transducer_gain_db = n2.transducer_gain_db(
            ReflS=ReflCoef().from_polar(0.522, -162),
            ReflL=ReflCoef().from_polar(0.487, 39),
        )
        assert round(transducer_gain_db, 1) == 16.1

        transducer_gain_db = n2.transducer_gain_db(
            ReflS=ReflCoef(0),
            ReflL=ReflCoef(0),
        )
        ins_gain_db = round(n2.insertion_gain_db, 1)
        assert round(transducer_gain_db, 1) == ins_gain_db


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
