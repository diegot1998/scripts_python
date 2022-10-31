Dia = int(input("Ingrese el dia: "))
Mes = int(input("Ingrese el mes: "))
Año = int(input("Ingrese el Año: "))
if Mes == 12:
    print("El mes corresponde a Navidad")
else:
    if Mes > 12:
        print("Dato mal ingresado")
    else:
        print("NO corresponde a Navidad")