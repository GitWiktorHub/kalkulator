lista_znakow = ["+", "-", "*", "/", "="]
lista_liczb = ['1','2','3','4','5','6','7','8','9','0']
wyraz = input("Podaj wyrażenie: ")
a=0
działanie = 0
wynik = None
for i, elem in enumerate(wyraz):

    if elem in lista_liczb:
        elem = int(elem)
        if działanie == 0:
            if a == 0:
                a = elem
            elif a != 0:
                a = 10*a + elem
            wynik = a
        elif działanie == 1:
            if a == 0:
                a = elem
            elif a != 0:
                a = 10*a + elem
            try:
                if wyraz[i+1] in lista_znakow:
                    wynik += a
            except IndexError:
                print("Nie wpisałeś znaku =")
        elif działanie == 2:
            if a == 0:
                a = elem
            elif a != 0:
                a = 10*a + elem
            try:
                if wyraz[i+1] in lista_znakow:
                    wynik -= a
            except IndexError:
                print("Nie wpisałeś znaku =")
        elif działanie == 3:
            if a == 0:
                a = elem
            elif a != 0:
                a = 10*a + elem
            try:
                if wyraz[i+1] in lista_znakow:
                    wynik /= a
            except IndexError:
                print("Nie wpisałeś znaku =")
        elif działanie == 4:
            if a == 0:
                a = elem
            elif a != 0:
                a = 10*a + elem
            try:
                if wyraz[i+1] in lista_znakow:
                    wynik *= a
            except IndexError:
                print("Nie wpisałeś znaku =")

    elif elem in lista_znakow:
        if elem == "+":
            działanie = 1
            a=0
        if elem == "-":
            działanie = 2
            a=0
        if elem == "/":
            działanie = 3
            a=0
        if elem == "*":
            działanie = 4
            a=0
        if elem == "=":
            print(wynik)
    else:
        print("Wystąpił bład")
        print("Prawdopodownie wpisałeś literę a nie liczbę")