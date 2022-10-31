Valor = int(input("Ingrese la cantidad de triangulos: "))
equi, iso, esc = 0, 0, 0
for x in range(0, Valor):
    L1 = int(input("Ingrese el valor del lado 1: "))
    L2 = int(input("Ingrese el valor del lado 2: "))
    L3 = int(input("Ingrese el valor del lado 3: "))
    if L1 == L2 and L2 == L3:
        print("El triangulo ", x, "es un triangulo equilatero")
        equi = equi+1
    elif L1 == L2 and L2 != L3:
        print("El triangulo ", x, "es un triangulo isosceles")
        iso = iso+1
    else:
        print("El triangulo ", x, "es un triangulo escaleno")
        esc = esc+1
print("La cantidad de triangulos equilateros es: ", equi)
print("La cantidad de triangulos isosceles es: ", iso)
print("La cantidad de triangulos escaleno es: ", esc)
