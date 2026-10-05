# Hodnotu materiál dostane funkce celkem a nedostal nic předtím protože print neumí předat hodnotu jiné funkci
def material(metry, cena_za_metr):
    return metry * cena_za_metr

def prace(hodiny, sazba):
    return hodiny * sazba

def celkem(metry, cena_za_metr, hodiny, sazba):
    return material(metry, cena_za_metr) + prace(hodiny, sazba)

def s_dph(castka):
    return castka * 1.21
    
hodiny = float(input("Kolik hodin? ").replace("," , "."))
sazba = float(input("Kolik je vaše sazba? ").replace("," , "."))

metry = float(input("Kolik metru? ").replace("," , "."))
cena_za_metr = float(input("Kolik cena za metr? ").replace("," , "."))

print(f"Celkem za materiál: {material(metry, cena_za_metr)} Kč")
print(f"Kolik stojí práce: {prace(hodiny, sazba)} Kč ")
print(f"Kolik je to celkem Kč: {celkem(metry, cena_za_metr, hodiny, sazba)} Kč" )
print(f"Celkem s dph: {s_dph(celkem(metry, cena_za_metr, hodiny, sazba))} Kč")
