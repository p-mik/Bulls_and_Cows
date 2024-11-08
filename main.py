"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Mikulka
email: petr.mikulka@gmail.com
discord: p_mik Mik#7555
"""
import random
import time

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

### CHEATY ###

def cheat_cheat():
    print("""
        Dostupné cheaty:
        IDDQD - vyzrazení tajného čísla
        stats - zobrazení statistik
        prdím na to - ukončení hry
          """)

def cheat_iddqd(tajne_cislo):
    print(f"Tajné číslo je: {tajne_cislo}\n")

def cheat_stats(pokusy, start_time):
    elapsed_time = time.time() - start_time
    print(f"Počet pokusů: {pokusy}, Uběhlý čas: {int(elapsed_time)} sekund\n")

def cheat_prdim_na_to():
    print("Hra byla ukončena.")

### HRA ###

def hra():
    tajne_cislo = generuj_tajne_cislo() 
    pokusy = 0
    start_time = time.time()
    
    while True:
        tip = input("Zadej svůj tip: ")

        # CHEATY
        if tip == "IDDQD":
            cheat_iddqd(tajne_cislo)
            continue
        elif tip == "stats":
            cheat_stats(pokusy, start_time)
            continue
        elif tip == "prdím na to":
            cheat_prdim_na_to()
            break
        elif tip == "cheat":
            cheat_cheat()
            continue

        pokusy += 1 # přidám počítadlo pokusu

        # je číslo správné?
        if not (tip.isdigit() and len(tip) == 4 and len(set(tip)) == 4 and tip[0] != '0'):
            print("\nČíslo musí být čtyřmístné, nesmí začínat nulou a číslice musí být unikátní. Zkus to znovu\n")
            continue

        spravne_misto, spatne_misto = vyhodnot_tip(tip, tajne_cislo)
        
        # Kontrola výhry
        if spravne_misto == 4:
            print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} po {pokusy} pokusech.")
            break

        # Výpis výsledku
        print(f"\nSprávná čísla na správném místě: {spravne_misto}\nSprávná čísla na špatném místě: {spatne_misto}\n")

# print(generuj_tajne_cislo())
# ziskej_tip_od_uzivatele()

hra()