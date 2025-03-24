#4) Llenar dos vectores A y B de M elementos cada uno, sumar el elemento uno del vector A con el
#elemento uno del vector B y así sucesivamente hasta M, almacenar el resultado en un vector C, e
#mostrar el vector resultante.

m = int(input("Ingrese la cantidad de elementos en ambos vectores: "))

vectorA = [0]*m
vectorB = [0]*m
vectorC = [0]*m

for i in range(0,m):
    vectorA[i] = int(input(f"Ingrese el elemento en posición {i} del vector A: "))
    vectorB[i] = int(input(f"Ingrese el elemento en posición {i} del vector B: "))

print(vectorA)
print(vectorB)

for i in range(0,m):
    vectorC[i] = vectorA[i] + vectorB[i]

print(vectorC)