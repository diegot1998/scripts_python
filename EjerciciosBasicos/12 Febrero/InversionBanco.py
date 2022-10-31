Inversion = int(input("Ingrese el valor de la inversion:  "))
Interes = int(input("Ingrese el valor de los intereses: "))
TotalI = (Inversion*Interes)/100
if (TotalI >=7000):
    Inversion = Inversion + TotalI
    print("El capital mas el interes a invertir de nuevo es: ")
    print(Inversion)
else:
    print("El capital a invertir es: ")
    print(Inversion)