Manana, tarde, Noche = 0, 0, 0
for x in range(0,5):
    print("Estudiante de la mañana #", x)
    edad = int(input("Ingrese la edad del estudiante del turno de la mañana: "))
    Manana = Manana+edad
for i in range(0,6):
    print("Estudiante de la tarde #", i)
    edad2 = int(input("Ingrese la edad del estudiante del turno de la tarde: "))
    tarde = tarde+edad2
for i in range(0,11):
    print("Estudiante de la noche#", i)
    edad3 = int(input("Ingrese la edad del estudiante del turno de la noche: "))
    Noche = Noche+edad3
Prom1 = Manana/5
Prom2 = tarde/6
Prom3 = Noche/11
print("El promedio de las edades del turno de la mañana es igual a: ", Prom1)
print("El promedio de las edades del turno de la tarde es igual a: ", Prom2)
print("El promedio de las edades del turno de la noche es igual a: ", Prom3)
if Prom1 > Prom2 and Prom1 > Prom3:
    print("Los estudiantes de la mañana tienen un promedio mayor de edad")
elif Prom2 > Prom1 and Prom2 > Prom3:
    print("Los estudiantes de la tarde tienen un promedio mayor de edad")
else:
    print("Los estudiantes de la noche tienen un promedio mayor de edad")