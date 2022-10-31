y = 1
x=0
z= 0
h = 0
while y <= 10:
    INP = int(input("Ingrese la nota: "))
    if INP >= 7 and INP<=10:
        z = z+1
    else:
        h = h+1
    y = y+1
print("La cantidad de notas mayores es igual a: ", z)
print("La cantidad de notas menores es igual a: ", h)