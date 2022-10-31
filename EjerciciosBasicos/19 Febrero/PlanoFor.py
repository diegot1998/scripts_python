Valor = int(input("Ingrese la cantidad de puntos: "))
cua1, cua2, cua3, cua4 = 0, 0, 0 ,0
for x in range(0, Valor):
    print("Punto #", x)
    P1 = int(input("Ingrese el valor del punto en x: "))
    P2 = int(input("Ingrese el valor del punto en y: "))
    if P1 > 0 and P2 > 0:
        cua1 = cua1+1
    elif P1 < 0 and P2 > 0:
        cua2 = cua2+1
    elif P1 < 0 and P2 < 0:
        cua3 = cua3+1
    else:
        cua4 = cua4+1
print("La cantidad de puntos en el primer cuadrante es: ", cua1)
print("La cantidad de puntos en el segundo cuadrante es: ", cua2)
print("La cantidad de puntos en el tercer cuadrante es: ", cua3)
print("La cantidad de puntos en el cuarto cuadrante es: ", cua4)