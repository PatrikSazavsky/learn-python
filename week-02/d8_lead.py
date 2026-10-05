firma = input("Jaké je jméno firmy? ")
#Funkce vrátí horky, vlazny, studeny podle inputu uživatele
def typ_leadu(rok):
    if rok < 2016:
        return "horky"  

    elif rok < 2021:
        return "vlažný"
    
    else:
        return "studený"

rok = int(input("Jaký je rok webu? "))
#Tady to spadlo, protože nemůžu přes volat string jako funkci - dal jsem ji jako funkci s nějakým argumentem v závorce (BLBOST)
print(f"Jak se jmenuje firma: {firma} : {(typ_leadu(rok))}" )