lista_liczb = ['1','2','3','4','5','6','7','8','9','0']
lista_znakow = ["+","-","*","/"]
wyraz = input("Podaj wyrażenie: ")
a=0
wynik = None
znaki = []
liczby = []

def dodaj(a,b):
    return a+b
def odejmij(a,b):
    return a-b
def pomnoz(a,b):
    return a*b
def podziel(a,b):
    return a/b

for znak in wyraz:
    if znak == "*" or znak == "/":
        znaki.append(znak)
    else:
        pass
for znak in wyraz:
    if znak == "+" or znak == "-":
        znaki.append(znak)
    else:
        pass

for i, elem in enumerate(wyraz):

    if elem in lista_liczb:
        elem = int(elem)
        if a == 0:
            a = elem
        elif a != 0:
            a = 10 * a + elem
        liczby.append(a)
    elif elem in lista_znakow:
        pass
    else:
        print("Wystąpił bład")
        print("Prawdopodownie wpisałeś literę a nie liczbę")