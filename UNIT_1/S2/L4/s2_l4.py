figura = int(input("scegli la figura: scrivi 1 per quadrato, 2 per cerchio, 3 per rettangolo: "))

if figura == 1:
    l1= float(input("lunghezza in cm del lato? "))
    p1= l1*4
    print(f"il perimetro equivale a {p1} cm")
elif figura == 2:
    l2 = float(input("lunghezza in cm del raggio? "))
    r1 = (2*3.14)*l2
    print(f"la circonferenza è di {r1} cm")
elif figura == 3:
    l3 = float(input("lunghezza in cm della base? "))
    l4 = float(input("lunghezza in cm dell'altezza? "))
    p2 = (l3*2) + (l4*2)
    print(f"il perimetro equivale a {p2} cm")
else:
    print("scegli una delle tre opzioni")
