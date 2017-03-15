from math import ceil #võtame kõik
print ("Ehitame küpsisetorti.")
pikkus = input("Kui pikka torti tahad?")
laius= input("Kui laia torti tahad? ")
korgus = input("Kui kõrget torti tahad? ")
tk_pakis = input("Mitu küpsist on ühes pakis? ")

def pakke ():
    tk_arv = int(pikkus)*int(laius)*int(korgus)
    pakkide_arv = tk_arv/int(tk_pakis)
    print (round(pakkide_arv+0.49))
    print (ceil(pakkide_arv))
pakke()
