"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Mikulka
email: petr.mikulka@gmail.com
discord: p_mik Mik#7555
"""
import random


print("""
Ahoj
-----------------------------------------------
Zahrajeme si LOGIK
Tvým úkolem je uhodnout čtyřmístné číslo. 
-----------------------------------------------
""")

### FUNKCE ###

# Funkce pro generování tajného čísla
def generuj_tajne_cislo():

    while True:
        cislo = random.randint(1000, 9999)  # aby nezačínalo nulou
        cislo_str = str(cislo)
        
        if len(set(cislo_str)) == 4: # jestli je unikátní
            return cislo_str

# Funkce pro získání vstupu od uživatele
def ziskej_tip_od_uzivatele():
     while True:
        cislo_tip = input("Zadej svůj tip: ")
        
        if cislo_tip.isdigit() and len(cislo_tip) == 4 and len(set(cislo_tip)) == 4 and cislo_tip[0] != '0': # je číslo validní?
            return cislo_tip
        else:
            print("\nČíslo musí být čtyřmístné, nesmí začínat nulou a číslice musí být unikátní. Zkus to znovu\n")

# Funkce pro vyhodnocení tipu
def vyhodnot_tip(tip, tajne_cislo):
    spravne_misto = 0
    spatne_misto = 0
    
    for i in range(4): # porovnání číslic
        if tip[i] == tajne_cislo[i]:
            spravne_misto += 1
        elif tip[i] in tajne_cislo:
            spatne_misto += 1
    
    return spravne_misto, spatne_misto

def hra():
    tajne_cislo = generuj_tajne_cislo() 
    pokusy = 0
    
    while True:
        tip = ziskej_tip_od_uzivatele()
        pokusy += 1
        spravne_misto, spatne_misto = vyhodnot_tip(tip, tajne_cislo)
        
        # Výpis výsledku
        print(f"Správná čísla na správném místě: {spravne_misto}\nSprávná čísla na špatném místě: {spatne_misto}")
        
        # Kontrola výhry
        if spravne_misto == 4:
            print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} po {pokusy} pokusech.")
            break
# print(generuj_tajne_cislo())
# ziskej_tip_od_uzivatele()

hra()