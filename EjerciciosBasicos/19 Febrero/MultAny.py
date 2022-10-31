Valor = int(input("Ingrese el valor: "))
if Valor <= 10:
    for x in range(0,12):
        mult = x*Valor
        print("El valor ", x, "Multiplicado por", Valor, "es igual a: ", mult)
else:
    print("El valor no es valido, debe de ser del 1 al 10")