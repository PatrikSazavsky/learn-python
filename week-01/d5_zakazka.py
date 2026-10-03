def material(metry, cena_za_metr):
    return metry * cena_za_metr
    
metry = float(input("Kolik metru? "))
cena_za_metr = float(input("Kolik cena za metr? "))

def prace(hodiny, sazba):
    return hodiny * sazba

hodiny = float(input("Kolik hodin? "))
sazba = float(input("Kolik je vaše sazba? "))

def celkem(metry, cena_za_metr, hodiny, sazba):
    return material(metry, cena_za_metr) + prace(hodiny, sazba)

def s_dph(castka):
    return castka * 1.21

print(f"Celkem za materiál: {material(metry, cena_za_metr)} Kč")
print(f"Kolik stojí práce: {prace(hodiny, sazba)} Kč ")
print(f"Kolik je to celkem Kč: {celkem(metry, cena_za_metr, hodiny, sazba)} Kč" )

