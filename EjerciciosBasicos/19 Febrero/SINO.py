op = "Si"
suma = 0
while op == "Si":
    valor = int(input("Ingrese un valor:"))
    suma = suma+valor
    op = input("Desea cargar otro numero (Si/No):")
print("La suma de valores es igual a: ", suma)