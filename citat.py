
"""
Projekt 1: Personlig citatbank
Ett menybaserat program för att hantera citat med filhantering.
"""
import json
import random

class Citat:
    def __init__(self,person,citat):
        self.person = person
        self.citat = citat 

    def to_dict(self):
        return{
        "person": self.person,
        "citat": self.citat
        }

    @classmethod
    def from_dict(cls,citat:dict):
        print(cls)
         
        lista_med_objekt = []

        for x in citat:
            Obj = cls(x["person"], x["citat"])
            lista_med_objekt.append(Obj)

        return lista_med_objekt


def ladda_citat_fran_fil():
    with open("svartin.json", mode = "r", encoding = "utf-8") as read_file:
          data = json.load(read_file)
    return Citat.from_dict(data)


def spara_citat_till_fil(citatlista, filnamn):
    """
    Sparar alla citat till en textfil.
    
    Parametrar:
        citatlista (list): Listan med citat som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """
    # TODO: Implementera funktionen
    # Tips: Använd open() med "w"
    # Tips: Loop'a igenom listan och skriv varje citat + "\n"
    pass


def visa_alla_citat(citatlista):
    """
    Skriver ut alla citat med numrering.
    
    Parametrar:
        citatlista (list): Listan med citat som ska visas
    """
    # TODO: Implementera funktionen
    # Tips: Använd enumerate() för att få index
    # Tips: Använd strip() för att ta bort radbrytningar
    pass


def lagg_till_citat(citatlista):
    """
    Lägger till ett nytt citat i listan.
    Användaren får mata in citat och författare.
    
    Parametrar:
        citatlista (list): Listan som citat ska läggas till i
    
    Returnerar:
        bool: True om citat lades till, False annars
    """
    # TODO: Implementera funktionen
    # Tips: Använd input() för att fråga efter citat och författare
    # Tips: Formatet bör vara "citat - Författare"
    pass


def slumpa_citat(citatlista):
    """
    Visar ett slumpmässigt citat från listan.
    
    Parametrar:
        citatlista (list): Listan att välja citat från
    """
    # TODO: Implementera funktionen
    # Tips: Använd random.randint() eller random.choice()
    # Tips: Kontrollera att listan inte är tom först
    pass


def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # TODO: Implementera huvudprogrammet
    # 1. Ladda befintliga citat med ladda_citat_fran_fil()
    citat = ladda_citat_fran_fil()
    
    print(citat.person)
    # 2. Skapa en while-loop som visar menyn
    # 3. Hantera användarens val med if/elif/else
    # 4. Vid val 2: lägg till citat och spara med spara_citat_till_fil()
    # 5. Vid val 4: avsluta loopen
    alive = True
    while alive:
        running = True
        while running:
            print("""
            Hej, välkommen till citatbanken!!!
            här i banken kan du göra följande:
            1:visa alla citat
            2:Lägg till nytt citat
            3:slumpa fram ett citat
            4:STÄNG PROGRAMMET

""")
            fråga = input("Vad vill du göra?")
            if fråga == "1":
                for i in range (len(citat)):
                    print (f"""{citat[i]["person"]}:  """)
                    print(f"  {{{citat[i]["citat"]}}} ")
            elif fråga == "2":
                pass
            elif fråga == "3":
                pass
            elif fråga == "4":
                quit
            else:
                running=False
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()