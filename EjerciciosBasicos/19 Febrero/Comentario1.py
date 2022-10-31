x = 0
suma = 0
while x == 0:
    Valor = int(input("Ingrese un valor: "))
    if Valor == -1:
        break
    else:
        suma = suma+Valor
print("El valor final es igual a: ", suma)

#Realizar un programa que solicite la carga de valores enteros por teclado y
#los sume. Finalizar la carga al ingresar el valor -1.