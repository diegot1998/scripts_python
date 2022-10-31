ListaS = []
Promedio = 0
for x in range(0,5):
    Sueldo = float(input("Ingrese el valor del sueldo: "))
    ListaS.append(Sueldo)
    Promedio = Promedio+Sueldo
Promedio = Promedio/5
print("El promedio de los sueldos es igual a: ",Promedio)
print("El sueldo de los cinco operarios es: ", ListaS)