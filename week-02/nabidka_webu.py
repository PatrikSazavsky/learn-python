def cena_webu(stranky, cena_za_stranku):
    return stranky * cena_za_stranku

def sleva(castka):
    if castka < 15000:
        return 0

    elif castka < 40000:
        return 5

    else:
        return 10
#Jestli to spadne tak kvůli tomu že nevolám funkci (bez závorky) ale pouze ji jmenuje ve výpočtu
def po_sleve(castka):
    return castka - castka * sleva(castka)/100

def nacti_cislo(otazka):
    return float(input(otazka).replace("," , "."))


jmeno_firmy = input("Jmeno vasi firmy? ")

stranky = nacti_cislo("Kolik stránek? ")

cena_za_stranku = nacti_cislo("Cena za stranku? ")

za_web = cena_webu(stranky, cena_za_stranku)

print(f" Jméno: {jmeno_firmy} : {za_web} Kč" )

print(f"Sleva : {sleva(za_web)} Kč" )

print(f"Po sleve : {po_sleve(za_web)} Kč" )