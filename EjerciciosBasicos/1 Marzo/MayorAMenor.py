A = [2,5,6,7]
aux1 = []
for k in range(4):
    for x in range(3-k):
        if A[x]>A[x+1]:
            aux1=A[x]
            A[x]=A[x+1]
            A[x+1]=aux1
print(A)





