from pojisteny import Pojisteny

class Evidence:
    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self):
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        vek = int(input("Zadejte věk:\n"))
        telefon = input("Zadejte telefonní číslo:\n")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)
        print(f"Pojištěný {jmeno} {prijmeni} byl přidán.")

    def vypis_pojisteneho(self):
        print("Seznam všech pojištěných:")
        for pojisteny in self.pojisteni:
            print(pojisteny)

    def vyhledat_pojisteneho(self):
        jmeno = input("Zadejte jméno:\n")
        prijmeni = input("Zadejte příjmení:\n")
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(pojisteny)
                break
        else:
            print(f"Pojištěný {jmeno} {prijmeni} nebyl nalezen.")