def nacti_cislo(otazka):
    return float(input(otazka).replace("," , "."))
def sleva(castka):
    if castka < 15000:
        return 0
    elif castka < 40000:
        return 5
    else:
        return 10
def soucet(ceny):
    dohromady = 0
    for castky in ceny:
        dohromady = dohromady + castky
    return dohromady
ceny = []
odpoved = "Ano"
#While cyklus potřebuje start (cena přes načti číslo), podmínku (odpoved je ano) a posun (ceny.append)
while odpoved == "Ano":
    cena = nacti_cislo("Cena položky: ")
    ceny.append(cena)
    odpoved  = input("Další položka? Ano/Ne ")

polozka = 0
for castka in ceny:
    polozka = polozka + 1
    print(f"Položka: {polozka}, částka: {castka} ")
celkem = soucet(ceny)
print(f"Součet: {celkem} Kč, Sleva: {sleva(celkem)} %, Po slevě: {celkem - (celkem * sleva(celkem)/100)} Kč")
