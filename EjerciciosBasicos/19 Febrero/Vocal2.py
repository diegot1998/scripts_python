Nombre = input("Ingrese su nombre: ")
Nombre1=Nombre.lower()
z = 0
for x in range(len(Nombre1)):
    print(Nombre1[x])
    if Nombre1[x] == "a" or Nombre[x] == "e" or Nombre[x] == "i" or Nombre[x] == "o" or Nombre[x] == "u":
        z = z+1
        print(z)
print("El nombre tiene ", z, "Vocales")