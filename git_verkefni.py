def number1()    :
    tala1 = int(input("sláðu inn tölu: "))
    tala2 = int(input("sláðu inn tölu: "))
    print("Tala1 plús tala2 er", tala1 + tala2)
    print("Tala1 sinnum tala2 er", tala2*tala1)
def number2():
    fnafn = input("Fornafnið þitt?: ")
    enafn = input("Eftirnafnið þitt?: ")
    print("Halló", fnafn, enafn, "hafðu það gott í dag")
def number3():
    texti = input("Texti: ")
    print(texti)
    teljari = 0
    telja = 0
    for stafur in texti:
        if stafur.upper() == stafur:
            teljari += 1
        elif stafur.lower() == stafur:
            telja += 1
    print("Í þessum texta eru", teljari, "hástafir og", telja, "lágstafir.")

while True:
    number1()
    number2()
    number3()