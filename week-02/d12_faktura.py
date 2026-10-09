def zjisti_cislo(otazka):
    return float(input(otazka).replace("," , "."))

def s_dph(castka):
    return castka + castka * 21/100

def stav(dny):
    if dny < 7:
        return "Připomínka"
    elif dny < 30:
        return "Upomínka"
    else: 
        return "Právní spor"

def penale(castka, dny):
    return castka/1000 * dny

def volat_hned(castka, dny):
    return castka >= 10000 and dny >= 14 or dny >= 30

zakaznik = input("Jak se jmenuje klient? ")
bez_dph = zjisti_cislo("Kolik dluží bez daně? ")
po_splatnosti = int(input("Jak dlouho je nazaplacená faktura? "))
dluh_s_dani = s_dph(bez_dph)

print(f"Jméno klienta:  {zakaznik} ")
print(f"Dlužná částka bez daně: {bez_dph} Kč")
print(f"Po přičtení daně: {dluh_s_dani} Kč")
print(f"Dny po spaltnosti: {po_splatnosti} ")
print(f"Stav: {stav(po_splatnosti)} ") 
print(f"Volat hned? {volat_hned(dluh_s_dani, po_splatnosti)} ")

for den in range(1, po_splatnosti + 1):
    print(f"Den {den}, penále: {penale(dluh_s_dani, den)}! ")