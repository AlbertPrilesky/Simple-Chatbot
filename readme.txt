# Školní projekt: Jednoduchý Python Chatbot pro sběr kontaktů

Tento projekt představuje jednoduchého interaktivního chatbota běžícího v příkazové řádce (konzoli). Slouží jako školní práce pro demonstraci základních algoritmických struktur v jazyce Python – zejména práce s cykly, podmínkami, validací uživatelských vstupů a ukládáním dat do textových souborů.

 Hlavní funkce projektu
- **Interaktivní textové menu:** Uživatel si volí z nabídky akcí (Zanechat kontakt, O projektu, Konec).
- **Základní validace dat (kontrola vstupů):**
  - **Jméno a zpráva:** Kontrola minimální délky řetězce pomocí funkce `len()`.
  - **E-mail:** Kontrola přítomnosti znaku `@`.
  - **Telefon:** Kontrola, zda vstup obsahuje pouze číslice pomocí metody `.isdigit()`.
- **Očištění vstupů:** Využití metody `.strip()` pro automatické odstranění nechtěných mezer na začátku a konci zadaných textů.
- **Trvalé ukládání dat:** Využití vestavěné knihovny `csv` pro zápis kontaktů do souboru `kontakty.csv`. Data jsou oddělena středníkem (`;`), což umožňuje snadné otevření tabulky v programu Microsoft Excel.
- **Autonomní tvorba souboru:** Pokud soubor `kontakty.csv` na disku ještě neexistuje, program ho díky režimu `mode="a"` (append) automaticky sám vytvoří.

 Struktura projektu
text
├── chatbot.py        # Hlavní zdrojový kód programu v Pythonu
└── README.md         # Dokumentace k projektu (tento soubor)


 Jak program spustit
Uistěte se, že máte nainstalovaný Python 3.

Stáhněte si soubor chatbot.py do libovolné složky.

Otevřete terminál (příkazovou řádku) v této složce.

Spusťte program příkazem:

Bash
python chatbot.py
 Ukázka formátu uložených dat (CSV)
Po úspěšném vyplnění chatbot uloží data do souboru ve struktuře:

Plaintext:
Jan Novák;jan.novak@skola.cz;608987654;Měl bych zájem o konzultaci.
Tento projekt byl vytvořen pro školní účely jako ukázka přehledného a čistého kódu bez externích knihoven.