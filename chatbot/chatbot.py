import csv

# Název souboru, kam ukládáme data
SOUBOR_KONTAKTY = "kontakty.csv"

def uloz_kontakt(jmeno, email, telefon, zprava):
    """Funkce otevře soubor v módu 'a' (append = připisování) a přidá nový řádek."""
    with open(SOUBOR_KONTAKTY, mode="a", encoding="utf-8", newline="") as s:
        zapisovac = csv.writer(s, delimiter=";")
        zapisovac.writerow([jmeno, email, telefon, zprava])

def spust_chatbota():
    print("=== CHATBOT PRO SBĚR KONTAKTŮ ===")
    
    while True:
        # Zobrazení jednoduchého menu
        print("\n[1] Zanechat zprávu a kontakt")
        print("[2] O projektu")
        print("[3] Konec")
        
        volba = input("Vyber možnost (1-3): ").strip()
        
        if volba == "1":
            print("\n--- ZADÁVÁNÍ ÚDAJŮ ---")
            
            # 1. Kontrola jména (nesmí být prázdné a musí mít aspoň 2 znaky)
            jmeno = input("Zadej jméno a příjmení: ").strip()
            if len(jmeno) < 2:
                print("Chyba: Jméno je příliš krátké!")
                continue  # Vrátí nás na začátek cyklu while
                
            # 2. Kontrola e-mailu (jednoduchá kontrola na přítomnost zavináče)
            email = input("Zadej e-mail: ").strip()
            if "@" not in email:
                print("Chyba: Neplatný e-mail (chybí @)!")
                continue
                
            # 3. Kontrola telefonu (musí obsahovat pouze čísla)
            telefon = input("Zadej telefon: ").strip()
            if not telefon.isdigit():
                print("Chyba: Telefon musí obsahovat pouze čísla!")
                continue
                
            # 4. Zpráva (nesmí být prázdná)
            zprava = input("Napiš zprávu: ").strip()
            if len(zprava) < 5:
                print("Chyba: Zpráva je příliš krátká!")
                continue
            
            # Pokud vše projde, data uložíme
            uloz_kontakt(jmeno, email, telefon, zprava)
            print("\nDěkuji! Data byla úspěšně uložena do souboru.")
            
        elif volba == "2":
            print("\n--- O PROJEKTU ---")
            print("Tento chatbot slouží ke sběru a základní validaci kontaktů.")
            print("Data ukládá do lokálního CSV souboru.")
            
        elif volba == "3":
            print("\nKonec programu. Měj se!")
            break  # Ukončí cyklus while a tím i celý program
            
        else:
            print("Neplatná volba, zkus to znovu.")

# Spuštění samotného programu
spust_chatbota()