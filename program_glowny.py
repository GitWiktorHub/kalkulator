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

for i,znak in enumerate(znaki):
    if znak == "+":
        if wynik == None:
            wynik = 0
            print(liczby)
            wynik = liczby[i] + liczby[i+1]
        if wynik != None:
            wynik += liczby[i+1]

print(wynik)