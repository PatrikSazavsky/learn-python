def nacti_cislo(otazka):
    return float(input(otazka).replace(",", "."))

def cena_webu(stranky, cena_za_stranku):
    return stranky * cena_za_stranku

def sleva(castka):
    if castka < 15000:
        return 0
    elif castka < 40000:
        return 5
    else: 
        return 10

def po_sleve(castka):
    return castka - castka * sleva(castka)/100
#return vrací hodnotu funkce ceník a nesmí být uvnitř cyklu protože vrátí pouze jednu cenu a cyklus ukončí, dále ji pak voláme
def cenik(max_stranek, cena_za_stranku):
    ceny = []
    for stranky in range(1, max_stranek + 1):
        ceny.append(cena_webu(stranky, cena_za_stranku))
    return ceny

cena_za_stranku = nacti_cislo("Kolik stojí stránku: ")
max_stranek = int(nacti_cislo("Kolik maximálně stránek? "))
ceny = cenik(max_stranek, cena_za_stranku)
pocet_stranek = 0
for cena in ceny:
    pocet_stranek = pocet_stranek + 1
    print(f"{pocet_stranek} str, sleva {sleva(cena)} %, po slevě {po_sleve(cena)} Kč")
