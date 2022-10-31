Oracion = input("Ingrese su oracion: ")
z = 0
for x in range(len(Oracion)):
    if Oracion[x] == " ":
        z = z+1
print("Existen ", z, "espacion en blanco en la oracion")
