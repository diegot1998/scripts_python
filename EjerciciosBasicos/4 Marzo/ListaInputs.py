lista=[]
elementos=int(input("Cuantos elementos tendra la lista:"))
sub=int(input("Cuantos elementos tendran las listas internas:"))
for k in range(elementos):
    lista.append([])
    for x in range(sub):
        valor=int(input("Ingrese valor:"))
        lista[k].append(valor)

print(lista)