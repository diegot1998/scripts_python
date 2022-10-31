Password = input("Ingrese la contraseña: ")
if len(Password) >= 10 and len(Password) <= 20:
    print("La contraseña cumple con los requisitos")
else:
    print("La contraseña NO cumple con los requisitos")