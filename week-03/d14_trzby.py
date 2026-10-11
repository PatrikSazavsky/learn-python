def dej_cislo(otazka):
    return float(input(otazka).replace("," , "."))
def prumer(seznam):
    return sum(seznam)/len(seznam)
#Musím zde použít return ne print abych mohl ten výsledek z funkce použít dál   
def hodnoceni(seznam):
    if prumer(seznam) >= 5000:
        return "Výborný týden"
    elif prumer(seznam) >= 2000:
        return "Průměrný týden"
    else:
        return "Špatný týden"

trzby = []
odpoved = "Ano"
while odpoved == "Ano":
        penize = dej_cislo("Jaké jsou Vaše denní tržby? ")
        odpoved = input("Další den? Ano/Ne ")
        trzby.append(penize)

print(trzby) 
#Slovo tržba ve for cyklu bere každou položku postupně ze seznamu tržby.
dny = 0
for trzba in trzby:
    dny = dny + 1
    print(f"Den {dny}: {trzba} Kč")

print(f"Počet dní: {len(trzby)}")
print(f"Součet: {sum(trzby)} Kč")
print(f"Průměrné tržby: {prumer(trzby)} Kč")
print(f"Hodnocení: {hodnoceni(trzby)} ")