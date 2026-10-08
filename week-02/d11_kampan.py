def nacti_cislo(otazka):
    return float(input(otazka).replace("," , "."))
#Počítá kolik kliků je za den 
def kliky_za_den(rozpocet, cena_za_klik):
    return rozpocet/cena_za_klik

def typ_kliku(cena_za_klik):
    if cena_za_klik < 5:
        return "Levné"
    elif cena_za_klik < 15:
        return "Přijatelné"
    else:
        return "Drahé"

def je_vyhodna(cena_za_klik, kliky):
    return cena_za_klik < 15 and kliky >= 30 or cena_za_klik < 5

budget = nacti_cislo("Kolik máte rozpočet? ")

nazev = input("Jaký je název kampaně? ")

dni = int(input("Kolik dnů pojede? "))

cena_za_klik = nacti_cislo("Kolik sotjí jeden klik? ")

kliky = kliky_za_den(budget, cena_za_klik)

vyhodne = je_vyhodna(cena_za_klik, kliky)


print(f"Cena za jedno kliknutí: {cena_za_klik} Kč")
print(f"Vyplatí se nebo ne?: {vyhodne}" )
print(f"Je to ok?: {typ_kliku(cena_za_klik)}" )
print(f"Kliků za den: {kliky}" )
print(f"Název kampaně: {nazev}" )
print(f"Kolik máte rozpočet: {budget} Kč")
print(f"Kolik dni pojede kampaň: {dni}" )
#Je zde + 1 aby to pustilo počet dnů který se zaadává v otázce
for dny in range(1, dni + 1):
    print(f" Den číslo {dny}, Rozpočet: {dny * budget}, {kliky * dny} ")