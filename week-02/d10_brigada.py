def nacti_cislo(otazka):
    return float(input(otazka).replace("," , "."))

def hruba_mzda(hodiny, sazba):
    return hodiny * sazba

def dan(castka):
    if castka < 10000:
        return 0
    elif castka < 30000:
        return 15
    else:
        return 23

def cista_mzda(castka):
    return castka - castka * dan(castka)/100

def dojezd(minuty):
    if minuty < 20:
        return "Blízko"
    elif minuty < 45:
        return "OK"
    else:
        return "Daleko"

def je_vyhodna(minuty, sazba): 
         return minuty < 45 and sazba >= 180 or sazba >= 250
         

pocet_hodin = nacti_cislo("Kolik hodin? ")

sazba = nacti_cislo("Kolik je Vaše mzda na hodinu? ")

minuty = nacti_cislo("Kolik je dojezd do práce? ")

hruba = hruba_mzda(pocet_hodin, sazba)

cesta = dojezd(minuty)

kolik_dan = dan(hruba)

vyhodny = je_vyhodna(minuty, sazba)

nazev = input("Nazev brigady? ")

print(f"Pozice: {nazev}" )

print(f"Čistá mzda: {cista_mzda(hruba)} Kč ") 

print(f"Dojezd {cesta} Kč ") 

print(f"Vyplatí se?: {vyhodny} Kč ") 

print(f"Hrubá mzda: {hruba} Kč ") 

