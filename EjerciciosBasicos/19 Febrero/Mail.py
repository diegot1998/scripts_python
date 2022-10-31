mail = input("Ingrese su correo electronico: ")
z = 0
for x in range(len(mail)):
    if mail[x] == "@":
        z = z+1
print("Existen ", z, "en el mail")
