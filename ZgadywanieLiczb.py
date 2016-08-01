import random

def gra():
    nl = random.randint(1, 10)
    lg = eval(input("O jakiej liczbie pomyślałem?: "))
    while lg in (nl):
        print ("Brawo! Zgadłeś!")
    while not lg in (nl):
        print ("Pomyślałem o liczbie %s. Nie zgadłeś, przykra sprawa" % nl)
        

def menu():
    print ("Menu:")
    print ("1. Start")
    print ("2. Wyjście")
    wybormenu = eval(input("Wybierz opcje 1-2: "))
    if wybormenu == 1:
        gra()
    if wybormenu == 2:
        exit
    while not wybormenu in (1, 2):
        print ("Błąd... Restartowanie.")
        menu()

def logo():
    print ("=============Zgadywanie liczb=============")

logo()
menu()

    
