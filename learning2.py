# -*- coding: utf-8 -*-

spis={"Potop" : 8,"Krzyżacy": 9,"Psy": 10,"Karino": 6}
co=input("Czego Pan szuka ? : \n")
print("Wybrany film ", co," posiada ocenę ", spis[co])
nowy=input("Dopisz swój wybrany film ")
ocena=int(input("i jego ocenę : "))
spis[nowy]=ocena
print("\n")
print(spis)
