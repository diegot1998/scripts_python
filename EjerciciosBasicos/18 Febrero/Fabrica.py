n = int(input("Ingrese la cantidad de piezas: "))
x = 1
y= 0
while x <= n:
    Medida = float(input("Ingrese las medidas de la pieza: "))
    if Medida>= 1.20 and Medida<= 1.30:
        y = y+1
    x = x+1
print("La cantidad de piezas aptas es igual a: ", y)
