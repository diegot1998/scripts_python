lista=[[1,1,1,1,1], [2,2,2,2,2]]

for k in range(len(lista)):
    suma=0
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
    print(suma)
