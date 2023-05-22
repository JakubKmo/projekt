from evidence import Evidence

if __name__ == "__main__":
    evidencer = Evidence()

    while True:
        print("--------------------\nEvidence pojištěných\n--------------------")
       
        print("Vyberte akci:")
        print("1. Přidat nového pojištěného")
        print("2. Vypsat všechny pojištěné")
        print("3. Vyhledat pojištěného")
        print("4. Konec")

        volba = input("> ")

        if volba == "1":
            evidencer.pridej_pojisteneho()
        elif volba == "2":
            evidencer.vypis_pojisteneho()
        elif volba == "3":
            evidencer.vyhledat_pojisteneho()
        elif volba == "4":
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")
        
        input("Stiskněte enter pro návrat do menu...")