from tkinter import *
okno = Tk()

lista_liczb = ['1','2','3','4','5','6','7','8','9','0']
lista_znakow = ["+","-","*","/","="]
print("PAMIĘTAJ O ZNAKU =")
wyraz = input("Podaj wyrażenie: ")
a=0
wynik = None
znaki = []
liczby = []

for i, elem in enumerate(wyraz):

    if elem in lista_liczb:
        elem = int(elem)
        if a == 0:
            a = elem
        elif a != 0:
            a = 10 * a + elem
    elif elem in lista_znakow:
        liczby.append(a)
        a = 0
        znaki.append(elem)
    else:
        print("Wystąpił bład")
        print("Prawdopodownie wpisałeś literę a nie liczbę")
        break
if wyraz[-1] != "=":
    print("Program nie zadziałał, ponieważ NIE WPISAŁEŚ ZNAKU =")
print(znaki)
print(liczby)
for i,znak in enumerate(znaki):
    if znak == "*":
        if wynik is None:
            wynik = liczby[i] * liczby[i+1]

        elif wynik is not None:
            wynik *= liczby[i+1]


    elif znak == "/":
        if wynik is None:
            wynik = liczby[i] / liczby[i+1]

        elif wynik is not None:
            wynik /= liczby[i+1]


for i,znak in enumerate(znaki):
    if znak == "+":
        if wynik is None:
            wynik = liczby[i] + liczby[i+1]
        elif wynik is not None:
            wynik += liczby[i]

    elif znak == "-":
        if wynik is None:
            wynik = liczby[i] - liczby[i+1]
        elif wynik is not None:
            wynik -= liczby[i]

print("Wynik: ",wynik)
okno.mainloop()