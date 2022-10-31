Num1 = int(input("Ingrese numero 1: "))
Num2 = int(input("Ingrese numero 2: "))
Num3 = int(input("Ingrese numero 3: "))
if (Num1 == Num2) and (Num2 == Num3):
    SUM = Num1 + Num2
    Mult = SUM * Num3
    print("La suma y la multiplicacion de estos valores es igual a: ", Mult)
else:
    print("Los tres valores no son iguales")