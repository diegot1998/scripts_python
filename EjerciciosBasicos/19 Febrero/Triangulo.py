v = int(input("Ingrese la cantidad de veces que quiere repetir el proceso: "))
y=0
for x in range(0, v):
    b = int(input("Ingrese la base del triangulo: "))
    h = int(input("Ingrese la altura del triangulo: "))
    Superficie = (h*b)/2
    print("La base del triangulo ", x, "es igual a: ", b)
    print("La altura del triangulo ", x, "es igual a: ", h)
    print("La superficie del triangulo ", x, "es igual a: ", Superficie)
    if Superficie >= 12:
        y = y+1
print("La cantidad de triangulos con superficie mayor a 12 es: ", y)