#from random import * see variant ei ole kõige parem, koodi optimeerimisel pole see mõistlik
from random import randint
check = randint(0,9)
def loto():#defineerime funktsiooni
    number = input("Sisesta üks täisarv 0-9: ")
    if number.isdigit():
        if int(number)<check:
            print("Sistestatud number on väiksem")
            loto()#pöördume algusesse tagasi
            # Rekursioon on mingi objekti kordamine ennastkopeerival teel
        elif int(number)>check:
            print("Sistestatud number on suurem")
            loto()#pöördume algusesse tagasi
        else:
            print ("Bingo - pihtas, põhjas")
    else:
        print ("Täisarvu taheti. Proovi uuesti")
        loto()#pöördume algusesse tagasi
#kutsume funktsiooni välja
loto()