Num1 = int(input("Ingrese numero 1: "))
Num2 = int(input("Ingrese numero 2: "))
Num3 = int(input("Ingrese numero 3: "))
if Num1 > Num2:
    if Num1 > Num3:
        print("El numero mas alto es: ",Num1)
    else:
        print("El numero mas alto es: ", Num3)
else:
    if Num2 > Num3:
        print("El numero mas alto es: ",Num2)
    else:
        print("El numero mas alto es: ",Num3)
