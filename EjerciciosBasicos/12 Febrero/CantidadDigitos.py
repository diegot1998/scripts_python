Num1 = int(input("Inserte el valor numerico: "))

if Num1 < 10:
    print("El numero es de 1 digito")
else:
    if Num1 >= 10 and Num1 < 100:
        print("El valor contiene 2 digitos")
    else:
        if Num1 >= 100 and Num1 < 1000:
            print("El valor contiene 3 digitos")
        else:
            print("El valor contiene mas de 3 digitos")