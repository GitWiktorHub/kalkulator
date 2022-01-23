lista_znakow = ["+", "-", "*", "/", "="]
lista_liczb = ['1','2','3','4','5','6','7','8','9','0']
wyraz = input("Podaj wyrażenie: ")
a=0
działanie = 0
wynik = None
znaki = []

def dodaj(a,b):
    return a+b
def odejmij(a,b):
    return a-b
def pomnoz(a,b):
    return a*b
def podziel(a,b):
    return a/b

for znak in wyraz:
    if znak in lista_znakow:
        znaki.append(znak)
    else:
        pass

for i, elem in enumerate(wyraz):

    if elem in lista_liczb:
        elem = int(elem)
        if działanie == 0:
            if a == 0:
                a = elem
            elif a != 0:
                a = 10*a + elem
            plik = open("liczby","a+")
            a = str(a)
            plik.write(a)
            plik.close()
            a = int(a)
            wynik = a
        
    else:
        print("Wystąpił bład")
        print("Prawdopodownie wpisałeś literę a nie liczbę")