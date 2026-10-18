def typ_leadu(rok):
    if rok < 2016:
        return "Horký"
    elif rok < 2021:
        return "Vlažný"
    else:
        return "Studený"

def je_duplicita(firma, firmy):
    return firma in firmy

def prvni_horky(firmy, roky):
    vysledek = "zadny"
    for nazvy in range(len(firmy)):
        if typ_leadu(roky[nazvy]) == "Horký":
            vysledek = firmy[nazvy]
            break
    return vysledek

firmy = []
roky = []
odpoved = "Ano"
while odpoved == "Ano":
    firma = input("Jaký je název firmy? ")


    if je_duplicita(firma, firmy):
        print(f"Firma {firma} už v seznamu je")

    else:
        rok = int(input("Jaký je rok firmy? "))
        firmy.append(firma)
        roky.append(rok)
    odpoved = input("Další firma? Ano/Ne ")

print(f"Počet firem: {len(firmy)}")
print(f"První horký lead: {prvni_horky(firmy, roky)}")
