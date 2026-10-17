def pocet_horkych(roky):
    pocet = 0
    for horky in roky:
        if typ_leadu(horky) == "Horký":
            pocet = pocet + 1
    return pocet

def typ_leadu(rok):
    if rok < 2016:
        return "Horký"
    elif rok < 2021:
        return "Vlažný"
    else:
        return "Studený"

prehled = []
roky = []
odpoved = "Ano"
while odpoved == "Ano":
    firma = input("Jaký je název firmy? ")
    rok = int(input("Jaký je rok firmy? "))
    if rok < 1990 or rok > 2026:
        print("Neplatný rok, firmu přeskakuju ")
    else:
        prehled.append(f"{firma}: {typ_leadu(rok)} ")
        roky.append(rok)
    odpoved = input("Další firma? Ano/Ne ")

poradi = 0
for jmeno in prehled:
    poradi = poradi + 1
    print(f"{poradi}. {jmeno} ")

print(f"Horkých leadů: {pocet_horkych(roky)} ze {len(roky)}" )