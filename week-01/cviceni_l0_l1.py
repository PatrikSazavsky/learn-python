"""Procvičování L0 + L1: syntax, logika, kombinace.

Jak na to:
1. Přečti zadání funkce a spočítej si příklad v hlavě nebo na papíře.
2. Smaž `pass` a napiš tělo funkce (odsazené o 4 mezery).
3. Spusť testy:  uv run pytest week-01/test_cviceni_l0_l1.py
4. Červený test = čti poslední řádek chyby. Zelený = jdi na další.

`pass` znamená „zatím tu nic není“. Funkce s `pass` vrací None,
proto na začátku všechny testy padají. To je v pořádku.
"""


# ---------- ÚROVEŇ 1: jeden pojem, jeden řádek ----------

def dvakrat(x):
    """Vrať x krát 2.  dvakrat(5) -> 10"""
    pass


def pozdrav(jmeno):
    """Vrať text s pozdravem (f-string).  pozdrav("Patrik") -> "Ahoj, Patrik!" """
    pass


def ucesat(text):
    """Ořízni mezery a dej velké první písmeno (metody str).
    ucesat("  patrik ") -> "Patrik"
    """
    pass


def na_cislo(text):
    """Převeď text na celé číslo.  na_cislo("42") -> 42"""
    pass


def je_sude(n):
    """Vrať True, když je n sudé, jinak False (použij %).
    je_sude(4) -> True,  je_sude(7) -> False
    """
    pass


# ---------- ÚROVEŇ 2: kombinace pojmů ----------

def s_dph(castka):
    """Vrať částku s DPH 21 %, zaokrouhlenou na 2 desetinná místa.
    s_dph(100) -> 121.0,  s_dph(9.99) -> 12.09
    """
    pass


def je_dospely(vek):
    """Vrať True, když je vek 18 nebo víc.  je_dospely(18) -> True"""
    pass


def typ_cisla(n):
    """Vrať "kladné", "záporné" nebo "nula" (if / elif / else).
    typ_cisla(5) -> "kladné",  typ_cisla(-2) -> "záporné",  typ_cisla(0) -> "nula"
    """
    pass


def znamka(body):
    """Body 0–100 -> známka (pozor na pořadí podmínek!):
    90 a víc "A", 75 a víc "B", 50 a víc "C", jinak "F".
    znamka(95) -> "A",  znamka(75) -> "B",  znamka(10) -> "F"
    """
    pass


def muze_ridit(vek, ma_papiry):
    """Vrať True, jen když je vek 18+ A ZÁROVEŇ ma_papiry je True (and).
    muze_ridit(20, True) -> True,  muze_ridit(20, False) -> False
    """
    pass


# ---------- ÚROVEŇ 3: funkce volá funkci ----------

def vizitka(jmeno, vek):
    """Použij ucesat() a je_dospely(). Vrať:
    vizitka("  patrik ", 20) -> "Patrik (dospělý)"
    vizitka("eva", 12)       -> "Eva (dítě)"
    """
    pass
