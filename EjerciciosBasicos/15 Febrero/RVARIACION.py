Num1 = int(input("Ingrese numero 1: "))
Num2 = int(input("Ingrese numero 2: "))
Num3 = int(input("Ingrese numero 3: "))
if (Num1 != Num2 and Num1 != Num3) and (Num2 !=Num3):
    if Num1 > Num2 and Num2 < Num3:
        if Num1 > Num3:
            RVariacion = Num1 - Num2
            print(RVariacion)
        else:
            RVariacion = Num3 - Num2
            print(RVariacion)
    else:
        if Num1 > Num2 and Num2 > Num3:
            RVariacion = Num1 - Num3
            print(RVariacion)
        else:  
            if Num2 > Num1 and Num1 > Num3:
                RVariacion = Num2 - Num3
                print(RVariacion)
            else:
                if Num2 > Num1 and Num1 < Num3:
                    RVariacion = Num2 - Num1
                    print(RVariacion) 
                else:
                    if Num3 > Num2 and Num2 > Num1:
                        RVariacion = Num3 - Num1
                        print(RVariacion)
                    else:
                        if Num3 > Num2 and Num2 < Num1:
                            RVariacion = Num3 - Num2
                            print(RVariacion) 
else:
    print("Los numeros no son distintos")