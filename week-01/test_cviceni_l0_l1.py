"""Testy k cviceni_l0_l1.py. Tenhle soubor neupravuj, jen ho spouštěj."""

from cviceni_l0_l1 import (
    dvakrat, pozdrav, ucesat, na_cislo, je_sude,
    s_dph, je_dospely, typ_cisla, znamka, muze_ridit, vizitka,
)


# Úroveň 1
def test_dvakrat():
    assert dvakrat(5) == 10
    assert dvakrat(0) == 0
    assert dvakrat(-3) == -6


def test_pozdrav():
    assert pozdrav("Patrik") == "Ahoj, Patrik!"


def test_ucesat():
    assert ucesat("  patrik ") == "Patrik"
    assert ucesat("eva") == "Eva"


def test_na_cislo():
    assert na_cislo("42") == 42


def test_je_sude():
    assert je_sude(4) is True
    assert je_sude(7) is False
    assert je_sude(0) is True


# Úroveň 2
def test_s_dph():
    assert s_dph(100) == 121.0
    assert s_dph(9.99) == 12.09


def test_je_dospely():
    assert je_dospely(18) is True
    assert je_dospely(17) is False


def test_typ_cisla():
    assert typ_cisla(5) == "kladné"
    assert typ_cisla(-2) == "záporné"
    assert typ_cisla(0) == "nula"


def test_znamka():
    assert znamka(95) == "A"
    assert znamka(90) == "A"
    assert znamka(75) == "B"
    assert znamka(60) == "C"
    assert znamka(10) == "F"


def test_muze_ridit():
    assert muze_ridit(20, True) is True
    assert muze_ridit(20, False) is False
    assert muze_ridit(16, True) is False


# Úroveň 3
def test_vizitka():
    assert vizitka("  patrik ", 20) == "Patrik (dospělý)"
    assert vizitka("eva", 12) == "Eva (dítě)"
