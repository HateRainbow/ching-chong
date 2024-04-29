import os #os är ett bra filhantering program som nästan funkar exakt som terminalen eller saker som t.ex. linux
from datetime import datetime as dt # datetime låter den kunna få åtkomst till 
"""
class Tid: 
    def __init__(self):
    
        self.tid_nu = dt.now()
        self.månad = angiven_månad
        self.dag = angiven_dag
        self.tid = tid
    
    def time(self):
    
        self.timmar=self.tid[0:2]
        self.min=self.tid[3:5]
    
    def tid_kvar(self, slutdatum):
        return self.tid_nu-dt(slutdatum)"""

fil_packlistor='banana.txt'

#t = Tid()

#Lägger objekt i self.objekt och sedan med addObject funktion kan man sätta in de saker som kommer att läggas.
class Packlistor: 
    def __init__(self):
        self.objekt_list = []

    def addObject(self, objekt):
        self.objekt_list.append(objekt)

p=Packlistor()

#funktion som gör ger vall att 
def main():
    while True:
        main=int(input('För att gå tillbaka till meny tryck 1 och för stänga tryck 0 '))

        if main not in [1,0]:
            print('Fel input')
            continue
        else:
            return main 

#upprepar meny tills lagrad giltig input
while True:
    print(f'Text fil namn:{fil_packlistor}\n')
    print('---> N Ny packlista')
    print('---> I Visa innehål i lista')
    print('---> S lägg till en sak i en lista')
    print('---> X Avsluta.')

    knapp= input('Tryck en av kommando: ').lower() #stora bokstäver blir erkänd som gemen
    
    os.system('cls')
    #os.system skriver in i terminalen och rensa den, så det kommer inte upp två meny i skärm 
    
    if knapp == 'n':
        
        beskrivning=input('Plats och kort beskrivning? ') 
        n=int(input('Hur många objekt?'))

        for i in range(0,n):
            
            föremål=input('Skriv varje enskild föremål och tryck enter: ')        
            p.addObject(föremål)
            
            if i != n-1:
                p.addObject(',')
        
        tid=input('Vilken tid (HH-MM)? ')
        angiven_månad= int(input('Vilken månad (skriv i MM)? '))
        angiven_dag=int(input('Vilken dag (skriv i DD)? '))
        
        with open(fil_packlistor, 'a') as f:
            f.write(f"{beskrivning} {p.tid_nu}/{angiven_månad}/{angiven_dag}\n; {tid}:")
        
        for i in p.objekt_list:
            f.write(f'{i}, ')
            
            if i == len(p.objekt_list):
                
                f.write('\n')
                main=int(input('Tryck 1 om du vill gå tillbaka till meny annars tryck 0 för stänga programmet. '))
                
                if main() == 1:
                    
                    print('skickas tillbaka till meny')
                    os.system('cls')
                    continue
                
                if main () == 0:
                    
                    print('Programmet avslutar ...')
                    f.close()
                    exit()

    if knapp == 'i':
        with open(fil_packlistor, "r") as f:
            r = f.readlines()
            matching_packlists=[rad for rad in r if packlistan in rad]

        if matching_packlists: #om det finns innehål kommer det att gå vidare
            print("Packlistor som matchar:")
            for index, packlist in enumerate(matching_packlists, start=1):
                print(f"{index}. {packlist}")

            val = int(input("Välj en packlista med nummer: "))

            if 0 <= val <= len(r):
                
                valt_pack=matching_packlists[val - 1]
                
                packlista_index=r.index(valt_pack)
                
                item_index=packlista_index + 1
                
                nuvarande_lista=r[item_index].strip()
                
                print(nuvarande_lista)
                
                f.close()

                if main() == 1:
                    print('skickas tillbaka till meny')
                    os.system('cls')
                    continue
                
                if main () == 0:
                    print('Programmet avslutar ...')
                    exit()
        else:
            print('Ingen packlista hittades.')
                
    if knapp == 's':
        sökord=input("Ange ett sökord för att hitta specifika packlistor: ")
        packlistan=f"Packlista; {sökord}"

        with open(fil_packlistor, "r") as f:
            r = f.readlines()

            matching_packlists=[rad for rad in r if packlistan in line]

        if matching_packlists:
            print("Packlistor som matchar:")
            for idx, packlist in enumerate(matching_packlists, start=1):
                print(f"{idx}. {packlist}")

            val = int(input("Välj en packlista med nummer: "))

            if 1 <= val <= len(matching_packlists):
                #(8) 
                
                valt_pack=matching_packlists[val - 1]
                
                packlista_index=r.index(valt_pack)
                
                item_index=packlista_index + 1
                
                if 0<= item_index <= len(r): # Se till att nästa rad finns (där packlistans objekt är listade)
                    
                    nuvarande_lista=r[item_index].strip()  # Befintligt innehåll
                    
                    ny_innehål=input("Vad vill du lägga till i packlistan? ")
                
                    ny_lista=f"{nuvarande_lista}, {ny_innehål}"
                    
                    with open(fil_packlistor, "w") as f:
                        
                        for idx, line in enumerate(r):
                            
                            if idx == item_index: #idx är siffror
                                
                                # Uppdatera raden efter packlista dvs där föremål för packlistan befinner sig
                                f.write(f"{ny_lista}\n")
                                
                                print(f'Det ny objekt {ny_innehål} skrevs in.')
                                print(f'Ny packlistan ser ut så här: {ny_lista}') #lägger ny del av text 
                            
                            else:
                                f.write(line) #Skriver om resten av texten
                                if  line == len(r):
                                    if main() == 1:
                                        print('skickas tillbaka till meny')
                                        os.system('cls')
                                        continue
                                    
                                    if main () == 0:
                                        print('Programmet avslutar ...')
                                        f.close()
                                        exit()
            else:
                print("Ogiltigt knappt.")
        else:
            print("Inga packlistor hittades som matchar sökordet. (Kanske Caps Lock)")
            continue

    if knapp == 'x':
        
        print('Programmet avslutar ... ')
        f.close()  
        exit()
    
    else:
        print('*FEL INPUT*\n')
        continue

#källor:

#(1) https://stackoverflow.com/questions/23319743/find-multiple-instances-of-a-string-in-a-text-file-python

#(2) https://www.w3schools.com/python/python_regex.asp

#(3) https://stackoverflow.com/questions/38489755/python-script-to-type-something-in-terminal

#(4) https://www.analyticsvidhya.com/blog/2023/09/python-enumerate/#:~:text=We%20tell%20enumerate()%20to,start%3D1%20as%20an%20argument.

#(5) https://stackoverflow.com/questions/6806467/rounding-time-in-python

#(7) https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file

#(8) https://stackoverflow.com/questions/176918/how-to-find-the-index-for-a-given-item-in-a-list