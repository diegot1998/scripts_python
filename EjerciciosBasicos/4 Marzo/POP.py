lista=[]
for x in range(10):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1


print(lista)
