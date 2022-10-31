Neg, Pos, Mult5, Par = 0, 0, 0, 0
for x in range(0, 10):
    valor = int(input("Ingrese el valor: "))
    if valor > 0:
        Pos = Pos+1
    elif valor < 0:
        Neg = Neg+1
    if valor%5 == 0:
        Mult5 = Mult5+1
    if valor%2 == 0:
        Par = Par+valor
print("La cantidad de valores positivos son: ", Pos)
print("La cantidad de valores Negativos son: ", Neg)
print("La cantidad de valores multiplos de 5 son: ", Mult5)
print("El valor acumulado de los numeros par es igual a: ", Par)