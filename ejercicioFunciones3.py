def isOrdered(lista, n):
    for i in range(n):
        if lista[i] > lista[i+1]:
            return False
    return True

lista = [1,2,3,5,10,9]
n = len(lista)

if isOrdered(lista, n):
    print("SI")
else:
    print("NO")