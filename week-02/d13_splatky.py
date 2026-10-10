#Funkce od uživatele zjištůje číselný údaj a přepisuje jej automaticky na desetinné číslo, voláme ji v proměných přes které zoodpovídáme otázky
def dodej_cislo(otazka):
    return float(input(otazka).replace("," , "."))
#Funkce počítá jaký horizont je pro klienta který splácí, volá ji poslední print. 
def delka_splaceni(mesic):
    if mesic <= 3:
        return "Krátké"
    elif mesic <= 12:
        return "Středobbý horizont"
    else:
        return "Dlouho"

klient = input("Jméno klienta? ")
cena = dodej_cislo("Jaká je cena? ")
splatka = dodej_cislo("Kolik budete splácet měsíčně? ")
print(f" {klient}: {cena}Kč, {splatka} Kč")
mesic = 0
dluh = cena
while dluh > 0:
    dluh = dluh - splatka
    if dluh < 0:
       dluh = 0
    mesic = mesic + 1
    print(f"Měsíc {mesic}, zbývá uhradit: {dluh} Kč")  
print(f"Splaceno za {mesic} měsíců ")
print(f"Jaký je horizont pro splátku: {(delka_splaceni(mesic))} ")